# py3_requests

The Python3 Requests Package Developed By Guolei

# Installation

```shell
pip install py3_requests
```

# Documentation

# [Requests Document](https://requests.readthedocs.io/en/latest/)

# Example

```python
import py3_requests
from requests import Response


# response handler 
def normal_response_handler(response: Response):
    if isinstance(response, Response) and response.status_code == 200:
        return response.text
    return None


# response handler usage 
result = py3_requests.request(
    response_handler=normal_response_handler,
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
