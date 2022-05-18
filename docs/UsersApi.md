# cbrain_api.UsersApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UsersApi.md#users_get) | **GET** /users | Returns all of the users in CBRAIN. Only available to admins.
[**users_id_delete**](UsersApi.md#users_id_delete) | **DELETE** /users/{id} | Deletes a CBRAIN user
[**users_id_get**](UsersApi.md#users_id_get) | **GET** /users/{id} | Returns information about a user
[**users_id_patch**](UsersApi.md#users_id_patch) | **PATCH** /users/{id} | Update information about a user
[**users_post**](UsersApi.md#users_post) | **POST** /users | Create a new user in CBRAIN. Only available to admins.


# **users_get**
> list[User] users_get(page=page, per_page=per_page)

Returns all of the users in CBRAIN. Only available to admins.

Returns all of the users registered in CBRAIN, as well as information on their permissions and group/site memberships.

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
api_instance = cbrain_api.UsersApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # Returns all of the users in CBRAIN. Only available to admins.
    api_response = api_instance.users_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> users_id_delete(id)

Deletes a CBRAIN user

Deletes a CBRAIN User from the database 

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
api_instance = cbrain_api.UsersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of user to update

try:
    # Deletes a CBRAIN user
    api_instance.users_id_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of user to update | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> User users_id_get(id)

Returns information about a user

Returns the information about the user associated with the ID given in argument. A normal user only has access to her own information, while an administrator or site manager can have access to a larger set of users. 

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
api_instance = cbrain_api.UsersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the user

try:
    # Returns information about a user
    api_response = api_instance.users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the user | 

### Return type

[**User**](User.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_patch**
> User users_id_patch(id, user_mod_req)

Update information about a user

Updates the information about a user 

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
api_instance = cbrain_api.UsersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of user to update
user_mod_req = cbrain_api.UserModReq() # UserModReq | An object representing a request for a new User

try:
    # Update information about a user
    api_response = api_instance.users_id_patch(id, user_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of user to update | 
 **user_mod_req** | [**UserModReq**](UserModReq.md)| An object representing a request for a new User | 

### Return type

[**User**](User.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(user_mod_req)

Create a new user in CBRAIN. Only available to admins.

Creates a new user in CBRAIN. Only admins can create new users. 

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
api_instance = cbrain_api.UsersApi(cbrain_api.ApiClient(configuration))
user_mod_req = cbrain_api.UserModReq() # UserModReq | An object representing a request for a new User

try:
    # Create a new user in CBRAIN. Only available to admins.
    api_response = api_instance.users_post(user_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_mod_req** | [**UserModReq**](UserModReq.md)| An object representing a request for a new User | 

### Return type

[**User**](User.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

