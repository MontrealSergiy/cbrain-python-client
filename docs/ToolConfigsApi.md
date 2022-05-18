# cbrain_api.ToolConfigsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_configs_get**](ToolConfigsApi.md#tool_configs_get) | **GET** /tool_configs | Get a list of tool versions installed.
[**tool_configs_id_get**](ToolConfigsApi.md#tool_configs_id_get) | **GET** /tool_configs/{id} | Get information about a particular tool configuration


# **tool_configs_get**
> list[ToolConfig] tool_configs_get(page=page, per_page=per_page)

Get a list of tool versions installed.

This method returns a list of tool config objects. 

### Example
```python
from __future__ import print_function
import time
import cbrain_api
from cbrain_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: BrainPortalSession
configuration = cbrain_api.Configuration()
configuration.api_key['cbrain_api_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cbrain_api_token'] = 'Bearer'

# create an instance of the API class
api_instance = cbrain_api.ToolConfigsApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # Get a list of tool versions installed.
    api_response = api_instance.tool_configs_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigsApi->tool_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[ToolConfig]**](ToolConfig.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configs_id_get**
> ToolConfig tool_configs_id_get(id)

Get information about a particular tool configuration

Returns the information about how a particular configuration of a tool on an execution server. 

### Example
```python
from __future__ import print_function
import time
import cbrain_api
from cbrain_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: BrainPortalSession
configuration = cbrain_api.Configuration()
configuration.api_key['cbrain_api_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cbrain_api_token'] = 'Bearer'

# create an instance of the API class
api_instance = cbrain_api.ToolConfigsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | the ID of the configuration

try:
    # Get information about a particular tool configuration
    api_response = api_instance.tool_configs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigsApi->tool_configs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the ID of the configuration | 

### Return type

[**ToolConfig**](ToolConfig.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

