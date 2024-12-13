# py3_requests

The Python3 Requests Package Developed By Guolei

# Installation

```shell
pip install py3_requests
```

# Documentation

## [requests](https://requests.readthedocs.io/en/latest/)

## [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

## [addict document](https://pypi.org/project/addict/)

## [xmltodict document](https://pypi.org/project/xmltodict/)

# Example

```python
import py3_requests
from requests import Response

# response handler usage 
result = py3_requests.request(
    response_handler=py3_requests.ResponseHandler.status_code_200_text,
    url="https://www.baidu.com",
    method="GET"
)
# result is normal_response_handler return value
print(result)

# not response handler usage return requests.Response instance
response = py3_requests.request(
    url="https://www.baidu.com",
    method="GET"
)
# response is requests.Response instance
print(response)
```
