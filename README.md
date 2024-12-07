# py3_requests

The Python3 Requests Library Developed By Guolei

# Installation

```shell
pip install py3_requests
```

# Official Documentation

# [Requests Document](https://requests.readthedocs.io/en/latest/)

# Example

```python
import requests
import py3_requests

# normal usages
response = py3_requests.request(
    method='GET',
    url='https://www.baidu.com',
)


def response_handler(response: requests.Response = None):
    """
    your business code
    """
    pass


# customer usages
result = py3_requests.request(
    response_handler=response_handler,
    method='GET',
    url='https://www.baidu.com',
)
```
