# cbrain_api.DataProvidersApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_providers_get**](DataProvidersApi.md#data_providers_get) | **GET** /data_providers | Get a list of the Data Providers available to the current user.
[**data_providers_id_browse_get**](DataProvidersApi.md#data_providers_id_browse_get) | **GET** /data_providers/{id}/browse | List the files on a Data Provider.
[**data_providers_id_delete_post**](DataProvidersApi.md#data_providers_id_delete_post) | **POST** /data_providers/{id}/delete | Deletes unregistered files from a CBRAIN Data provider.
[**data_providers_id_get**](DataProvidersApi.md#data_providers_id_get) | **GET** /data_providers/{id} | Get information on a particular Data Provider.
[**data_providers_id_is_alive_get**](DataProvidersApi.md#data_providers_id_is_alive_get) | **GET** /data_providers/{id}/is_alive | Pings a Data Provider to check if it is running.
[**data_providers_id_register_post**](DataProvidersApi.md#data_providers_id_register_post) | **POST** /data_providers/{id}/register | Registers a file as a Userfile in CBRAIN.
[**data_providers_id_unregister_post**](DataProvidersApi.md#data_providers_id_unregister_post) | **POST** /data_providers/{id}/unregister | Unregisters files as Userfile in CBRAIN.


# **data_providers_get**
> list[DataProvider] data_providers_get(page=page, per_page=per_page)

Get a list of the Data Providers available to the current user.

This method returns a list of Data Provider objects that represent servers with disk space accessible for storing Userfiles. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # Get a list of the Data Providers available to the current user.
    api_response = api_instance.data_providers_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[DataProvider]**](DataProvider.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_browse_get**
> list[FileInfo] data_providers_id_browse_get(id)

List the files on a Data Provider.

This method allows the inspection of what files are present on a Data Provider specified by the ID parameter. Files that are not yet registered as Userfiles are visible using this method, as well as regularly accessible Userfiles. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID of the Data Provider to browse.

try:
    # List the files on a Data Provider.
    api_response = api_instance.data_providers_id_browse_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_browse_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Provider to browse. | 

### Return type

[**list[FileInfo]**](FileInfo.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_delete_post**
> RegistrationInfo data_providers_id_delete_post(id, multi_registration_mod_req)

Deletes unregistered files from a CBRAIN Data provider.

This method allows files that have not been registered from CBRAIN to be deleted. This may be necessary if files were uploaded in error, or if they were unregistered but not immediately deleted. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID of the Data Provider to delete files from.
multi_registration_mod_req = cbrain_api.MultiRegistrationModReq() # MultiRegistrationModReq | Arrays containing the files to delete.

try:
    # Deletes unregistered files from a CBRAIN Data provider.
    api_response = api_instance.data_providers_id_delete_post(id, multi_registration_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Provider to delete files from. | 
 **multi_registration_mod_req** | [**MultiRegistrationModReq**](MultiRegistrationModReq.md)| Arrays containing the files to delete. | 

### Return type

[**RegistrationInfo**](RegistrationInfo.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_get**
> DataProvider data_providers_id_get(id)

Get information on a particular Data Provider.

This method returns a single Data Provider specified by the ID parameter 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | ID of the Data Provider to get information on.

try:
    # Get information on a particular Data Provider.
    api_response = api_instance.data_providers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the Data Provider to get information on. | 

### Return type

[**DataProvider**](DataProvider.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_is_alive_get**
> str data_providers_id_is_alive_get(id)

Pings a Data Provider to check if it is running.

This method allows the querying of a Data Provider specified by the ID parameter to see if it is running or not. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 789 # int | The ID of the Data Provider to query.

try:
    # Pings a Data Provider to check if it is running.
    api_response = api_instance.data_providers_id_is_alive_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_is_alive_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Provider to query. | 

### Return type

**str**

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_register_post**
> RegistrationInfo data_providers_id_register_post(id, multi_registration_mod_req)

Registers a file as a Userfile in CBRAIN.

This method allows new files to be added to CBRAIN. The files must first be transfered to the Data Provider via SFTP. For more information on SFTP file transfers, consult the CBRAIN Wiki documentation. Once files are present on the Data Provider, this method registers them in CBRAIN by specifying the file type. You can also specify to copy/move the files to another Data Provider after file registration. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID of the Data Provider to register files on.
multi_registration_mod_req = cbrain_api.MultiRegistrationModReq() # MultiRegistrationModReq | Arrays containing the filenames and types to register.

try:
    # Registers a file as a Userfile in CBRAIN.
    api_response = api_instance.data_providers_id_register_post(id, multi_registration_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Provider to register files on. | 
 **multi_registration_mod_req** | [**MultiRegistrationModReq**](MultiRegistrationModReq.md)| Arrays containing the filenames and types to register. | 

### Return type

[**RegistrationInfo**](RegistrationInfo.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_providers_id_unregister_post**
> RegistrationInfo data_providers_id_unregister_post(id, multi_registration_mod_req)

Unregisters files as Userfile in CBRAIN.

This method allows files to be unregistered from CBRAIN. This will not delete the files, but removes them from the CBRAIN database, so Tools may no longer be run on them. 

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
api_instance = cbrain_api.DataProvidersApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID of the Data Provider to unregister files from.
multi_registration_mod_req = cbrain_api.MultiRegistrationModReq() # MultiRegistrationModReq | Arrays containing the filenames to unregister.

try:
    # Unregisters files as Userfile in CBRAIN.
    api_response = api_instance.data_providers_id_unregister_post(id, multi_registration_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProvidersApi->data_providers_id_unregister_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Provider to unregister files from. | 
 **multi_registration_mod_req** | [**MultiRegistrationModReq**](MultiRegistrationModReq.md)| Arrays containing the filenames to unregister. | 

### Return type

[**RegistrationInfo**](RegistrationInfo.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

