# cbrain_api.SessionsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_delete**](SessionsApi.md#session_delete) | **DELETE** /session | Destroy the current session
[**session_get**](SessionsApi.md#session_get) | **GET** /session | Get session information
[**session_post**](SessionsApi.md#session_post) | **POST** /session | Create a new session


# **session_delete**
> session_delete()

Destroy the current session

This destroys the current session, effectively terminating the access to the service. 

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
api_instance = cbrain_api.SessionsApi(cbrain_api.ApiClient(configuration))

try:
    # Destroy the current session
    api_instance.session_delete()
except ApiException as e:
    print("Exception when calling SessionsApi->session_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_get**
> SessionInfo session_get()

Get session information

This returns information about the current session. 

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
api_instance = cbrain_api.SessionsApi(cbrain_api.ApiClient(configuration))

try:
    # Get session information
    api_response = api_instance.session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionInfo**](SessionInfo.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_post**
> SessionInfo session_post(login, password)

Create a new session

This is the main entry point to create a CBRAIN session. Note that if a user is currently logged in, a new session will not be created, and the current session will be re-used. 

### Example
```python
from __future__ import print_function
import time
import cbrain_api
from cbrain_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cbrain_api.SessionsApi()
login = 'login_example' # str | The username of the user trying to connect.
password = 'password_example' # str | The password of the user

try:
    # Create a new session
    api_response = api_instance.session_post(login, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| The username of the user trying to connect. | 
 **password** | **str**| The password of the user | 

### Return type

[**SessionInfo**](SessionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

