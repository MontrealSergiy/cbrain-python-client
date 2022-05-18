# cbrain_api.GroupsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get**](GroupsApi.md#groups_get) | **GET** /groups | Get a list of the Groups (projects) available to the current user.
[**groups_id_delete**](GroupsApi.md#groups_id_delete) | **DELETE** /groups/{id} | Deletes a Group (project).
[**groups_id_get**](GroupsApi.md#groups_id_get) | **GET** /groups/{id} | Get information on a Group (project).
[**groups_id_put**](GroupsApi.md#groups_id_put) | **PUT** /groups/{id} | Update the properties of a Group (project).
[**groups_post**](GroupsApi.md#groups_post) | **POST** /groups | Creates a new Group.


# **groups_get**
> list[Group] groups_get(page=page, per_page=per_page)

Get a list of the Groups (projects) available to the current user.

This method returns a list of all of the groups that the current user has access to. 

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
api_instance = cbrain_api.GroupsApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # Get a list of the Groups (projects) available to the current user.
    api_response = api_instance.groups_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_delete**
> groups_id_delete(id)

Deletes a Group (project).

This method allows the removal of Groups (projects) that are no longer necessary. Groups that have Userfiles associated with them may not be deleted. 

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
api_instance = cbrain_api.GroupsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the Group to delete.

try:
    # Deletes a Group (project).
    api_instance.groups_id_delete(id)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the Group to delete. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_get**
> Group groups_id_get(id)

Get information on a Group (project).

This method returns information on a single Group (project), specified by the ID parameter. Information returned includes the list of Users who are members of the group, the ID of the Site the Group is part of, and whether or not the group is visible to Regular Users. 

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
api_instance = cbrain_api.GroupsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the Group to get information on.

try:
    # Get information on a Group (project).
    api_response = api_instance.groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the Group to get information on. | 

### Return type

[**Group**](Group.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_put**
> groups_id_put(id, group_mod_req)

Update the properties of a Group (project).

This method allows the properties of a Group (project) to be updated. This includes the User membership, the ID of the site the Group belongs to, and the visibility status of the group to Regular Users. 

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
api_instance = cbrain_api.GroupsApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the Group
group_mod_req = cbrain_api.GroupModReq() # GroupModReq | An object with the group information to update

try:
    # Update the properties of a Group (project).
    api_instance.groups_id_put(id, group_mod_req)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the Group | 
 **group_mod_req** | [**GroupModReq**](GroupModReq.md)| An object with the group information to update | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> Group groups_post(group_mod_req)

Creates a new Group.

This method creates a new Group, which allows users to organize their files and tasks. 

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
api_instance = cbrain_api.GroupsApi(cbrain_api.ApiClient(configuration))
group_mod_req = cbrain_api.GroupModReq() # GroupModReq | An object describing the group to create

try:
    # Creates a new Group.
    api_response = api_instance.groups_post(group_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mod_req** | [**GroupModReq**](GroupModReq.md)| An object describing the group to create | 

### Return type

[**Group**](Group.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

