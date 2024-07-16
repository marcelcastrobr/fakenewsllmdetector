# CSR Results

## Review:

Guardian Review

Summary: **update langchain to 0.0.317 (or later)**

Overview:
1:Many blog post. No deployable architecture, sample code to be run by user on a machine (local or AWS). AWS readonly dependencies: Bedrock, STS. 3rd-Party libraries: Langchain, Wikipedia.

Threat Model
Summary: Not an application, a set of sample scripts. No architectural artifacts are created. Code is readonly, does not create artifacts or write data. No deployable application.

Data in Transit: Not sensitive data, N/A
Authentication/Authorization: No application. Test scripts use AWS credentials from notebook/CLI.
Data at rest: No rested data, N/A
Logging and Auditing: No application, script logging not needed.
Operational Patching: No application, N/A.
Runtime Exception Handling: No application, N/A
Denial of Service: No application, N/A

Other notes:
**Not noted in content, but setup requires activation of Claude2 model in Bedrock.** 

Security/Scan Analyze:

Bandit, pip-audit and Python code analyzer results. (Bandit same as previous note)
Must use langchain 0.0.317 before approval. (tested: sample code works with 0.0.317, to my knowledge).
Primarily, -162 allows for arbitrary code to be run within langchain, and at least some content is coming from wikipedia, though numexpr() not being used here, Unless there's a reason to not upgrade to 0.0.317?

PIp-audit vulnerabilities in 0.0.304 ::

Name Version ID Fix Versions
---------- ------- ------------------- ------------
langchain 0.0.304 PYSEC-2023-162 0.0.308 https://vulners.com/osv/OSV:PYSEC-2023-162
langchain 0.0.304 PYSEC-2023-205 0.0.317 https://vulners.com/osv/OSV:PYSEC-2023-205
langchain 0.0.304 GHSA-7gfq-f96f-g85j 0.0.312 https://nvd.nist.gov/vuln/detail/CVE-2023-36281



## Changes:

```bash
(blog) ➜  3-github pip install langchain --upgrade

(blog) ➜  3-github pip show langchain           
Name: langchain
Version: 0.0.320
Summary: Building applications with LLMs through composability
Home-page: https://github.com/langchain-ai/langchain
Author: 
Author-email: 
License: MIT
Location: /Users/marcasbr/miniconda3/envs/blog/lib/python3.10/site-packages
Requires: aiohttp, anyio, async-timeout, dataclasses-json, jsonpatch, langsmith, numpy, pydantic, PyYAML, requests, SQLAlchemy, tenacity
Required-by: 
```

