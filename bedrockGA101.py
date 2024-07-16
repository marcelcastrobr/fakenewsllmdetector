import boto3
import json
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from IPython.display import display, Markdown, display_json

REGION = 'us-west-2' #replace this with your own region

bedrock = boto3.client(
    'bedrock', 
    region_name=REGION)

# Define Amazon Bedrock
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name=REGION,
)


#print(bedrock.list_foundation_models())
display(display_json(bedrock.list_foundation_models()))

model_kwargs={
        "max_tokens_to_sample": 8191,
    }
llm = Bedrock(model_id="anthropic.claude-v2", client=bedrock_runtime, model_kwargs=model_kwargs)

print(llm)
#display(display_json(llm))

def generate_and_print(llm, q):
    total_prompt = """"""

    template = """Here is a statement:
    {statement}
    Make a bullet point list of the assumptions you made when given the above statement.\n\n"""
    prompt_template = PromptTemplate(input_variables=["statement"], template=template)
    assumptions_chain = LLMChain(llm=llm, prompt=prompt_template)
    total_prompt = total_prompt + template

    template = """Here is a bullet point list of assertions:
    {assertions}
    For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
    prompt_template = PromptTemplate(input_variables=["assertions"], template=template)
    fact_checker_chain = LLMChain(llm=llm, prompt=prompt_template)
    total_prompt = total_prompt + template

    template = """Based on the above assertions, the final response is FALSE if one of the assertions is FALSE. Otherwise, TRUE. You should only respond with TRUE or FALSE.'{}'""".format(q)
    template = """{facts}\n""" + template
    prompt_template = PromptTemplate(input_variables=["facts"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    total_prompt = total_prompt + template

    overall_chain = SimpleSequentialChain(chains=[assumptions_chain, fact_checker_chain, answer_chain], verbose=True)
    answer = overall_chain.run(q)

    return answer

q="The first woman to receive a Ph.D. in computer science was Dr. Barbara Liskov, who earned her degree from Stanford University in 1968."
print(f'The statement is: {q}')
display(Markdown(generate_and_print(llm, q)))






