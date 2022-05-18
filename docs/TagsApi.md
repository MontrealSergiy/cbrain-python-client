# cbrain_api.TagsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | Get a list of the tags currently in CBRAIN.
[**tags_id_delete**](TagsApi.md#tags_id_delete) | **DELETE** /tags/{id} | Delete a tag.
[**tags_id_get**](TagsApi.md#tags_id_get) | **GET** /tags/{id} | Get one tag.
[**tags_id_put**](TagsApi.md#tags_id_put) | **PUT** /tags/{id} | Update a tag.
[**tags_post**](TagsApi.md#tags_post) | **POST** /tags | Create a new tag.


# **tags_get**
> list[Tag] tags_get()

Get a list of the tags currently in CBRAIN.

This method returns a list of tag objects. 

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
api_instance = cbrain_api.TagsApi(cbrain_api.ApiClient(configuration))

try:
    # Get a list of the tags currently in CBRAIN.
    api_response = api_instance.tags_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_delete**
> tags_id_delete(id)

Delete a tag.

Delete the tag specified by the ID parameter.

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
api_instance = cbrain_api.TagsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the tag to delete.

try:
    # Delete a tag.
    api_instance.tags_id_delete(id)
except ApiException as e:
    print("Exception when calling TagsApi->tags_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the tag to delete. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_get**
> Tag tags_id_get(id)

Get one tag.

Returns a single tag with the ID specified. 

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
api_instance = cbrain_api.TagsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID of the tag to get.

try:
    # Get one tag.
    api_response = api_instance.tags_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the tag to get. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_put**
> tags_id_put(id, tag_mod_req)

Update a tag.

Update the tag specified by the ID parameter.

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
api_instance = cbrain_api.TagsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the tag to update.
tag_mod_req = cbrain_api.TagModReq() # TagModReq | 

try:
    # Update a tag.
    api_instance.tags_id_put(id, tag_mod_req)
except ApiException as e:
    print("Exception when calling TagsApi->tags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the tag to update. | 
 **tag_mod_req** | [**TagModReq**](TagModReq.md)|  | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_post**
> Tag tags_post(tag_mod_req)

Create a new tag.

Create a new tag in CBRAIN. 

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
api_instance = cbrain_api.TagsApi(cbrain_api.ApiClient(configuration))
tag_mod_req = cbrain_api.TagModReq() # TagModReq | 

try:
    # Create a new tag.
    api_response = api_instance.tags_post(tag_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_mod_req** | [**TagModReq**](TagModReq.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

