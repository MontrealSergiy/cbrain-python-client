# cbrain_api.TasksApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_get**](TasksApi.md#tasks_get) | **GET** /tasks | Get the list of Tasks.
[**tasks_id_get**](TasksApi.md#tasks_id_get) | **GET** /tasks/{id} | Get information on a Task.
[**tasks_post**](TasksApi.md#tasks_post) | **POST** /tasks | Create a new Task.


# **tasks_get**
> list[CbrainTask] tasks_get(page=page, per_page=per_page)

Get the list of Tasks.

This method returns the list of Tasks accessible to the current user. 

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
api_instance = cbrain_api.TasksApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # Get the list of Tasks.
    api_response = api_instance.tasks_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[CbrainTask]**](CbrainTask.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_get**
> CbrainTask tasks_id_get(id)

Get information on a Task.

This method returns information on a Task, including its status, Task restartability and information on where the results are kept. 

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
api_instance = cbrain_api.TasksApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID number of the Task to delete.

try:
    # Get information on a Task.
    api_response = api_instance.tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID number of the Task to delete. | 

### Return type

[**CbrainTask**](CbrainTask.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_post**
> list[CbrainTask] tasks_post(cbrain_task)

Create a new Task.

This method allows the creation of a new Task. 

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
api_instance = cbrain_api.TasksApi(cbrain_api.ApiClient(configuration))
cbrain_task = cbrain_api.CbrainTaskModReq() # CbrainTaskModReq | The task to create.

try:
    # Create a new Task.
    api_response = api_instance.tasks_post(cbrain_task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cbrain_task** | [**CbrainTaskModReq**](CbrainTaskModReq.md)| The task to create. | 

### Return type

[**list[CbrainTask]**](CbrainTask.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

