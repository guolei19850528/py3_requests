# py3_requests

#### 介绍

针对requests库的封装

#### 安装

```shell
pip install py3_requests
```

#### 依赖库

* ~python 3.0
* [requests](https://pypi.org/project/requests/)
* [addict](https://pypi.org/project/addict/)
* [jsonschema](https://pypi.org/project/jsonschema/)
* [retrying](https://pypi.org/project/retrying/)
* [xmltodict](https://pypi.org/project/xmltodict/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [lxml](https://pypi.org/project/lxml/)
* [html5lib](https://pypi.org/project/html5lib/)


#### 使用说明

```python
import requests
import py3_requests

# requests.request args
args = ()

# requests.request kwargs
kwargs = {}

# response = py3_requests.ResponseHandler.status_code_200_json_addict(requests.Response)
response = py3_requests.request(
    response_handler=py3_requests.ResponseHandler.status_code_200_json_addict,
    *args,
    **kwargs
)


# 定制使用
class RequestUrl(py3_requests.RequestUrl):
    """
    your request url
    """
    pass


class ValidatorJsonSchema(py3_requests.ValidatorJsonSchema):
    """
    your validator schema
    """
    pass


class ResponseHandler(py3_requests.ResponseHandler):
    """
    your response handler
    """
    pass


# your request
response = py3_requests.request(
    response_handler=ResponseHandler.status_code_200_json,
    *args,
    **kwargs
)
```
