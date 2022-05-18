# cbrain_api.UserfilesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userfiles_change_provider_post**](UserfilesApi.md#userfiles_change_provider_post) | **POST** /userfiles/change_provider | Moves the Userfiles from their current Data Provider to a new one.
[**userfiles_compress_post**](UserfilesApi.md#userfiles_compress_post) | **POST** /userfiles/compress | Compresses many Userfiles each into their own GZIP archive.
[**userfiles_delete_files_delete**](UserfilesApi.md#userfiles_delete_files_delete) | **DELETE** /userfiles/delete_files | Delete several files that have been registered as Userfiles
[**userfiles_download_post**](UserfilesApi.md#userfiles_download_post) | **POST** /userfiles/download | Download several files
[**userfiles_get**](UserfilesApi.md#userfiles_get) | **GET** /userfiles | List of the Userfiles accessible to the current user.
[**userfiles_id_content_get**](UserfilesApi.md#userfiles_id_content_get) | **GET** /userfiles/{id}/content | Get the content of a Userfile
[**userfiles_id_get**](UserfilesApi.md#userfiles_id_get) | **GET** /userfiles/{id} | Get information on a Userfile.
[**userfiles_id_put**](UserfilesApi.md#userfiles_id_put) | **PUT** /userfiles/{id} | Update information on a Userfile.
[**userfiles_post**](UserfilesApi.md#userfiles_post) | **POST** /userfiles | Creates a new Userfile and upload its content.
[**userfiles_sync_multiple_post**](UserfilesApi.md#userfiles_sync_multiple_post) | **POST** /userfiles/sync_multiple | Syncs Userfiles to the local Data Providers cache.
[**userfiles_uncompress_post**](UserfilesApi.md#userfiles_uncompress_post) | **POST** /userfiles/uncompress | Uncompresses many Userfiles.


# **userfiles_change_provider_post**
> userfiles_change_provider_post(multi_userfile_mod_req)

Moves the Userfiles from their current Data Provider to a new one.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to move.

try:
    # Moves the Userfiles from their current Data Provider to a new one.
    api_instance.userfiles_change_provider_post(multi_userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_change_provider_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to move. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_compress_post**
> userfiles_compress_post(multi_userfile_mod_req)

Compresses many Userfiles each into their own GZIP archive.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to compress.

try:
    # Compresses many Userfiles each into their own GZIP archive.
    api_instance.userfiles_compress_post(multi_userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_compress_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to compress. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_delete_files_delete**
> userfiles_delete_files_delete(multi_userfile_mod_req)

Delete several files that have been registered as Userfiles

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to destroy.

try:
    # Delete several files that have been registered as Userfiles
    api_instance.userfiles_delete_files_delete(multi_userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_delete_files_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to destroy. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_download_post**
> file userfiles_download_post(multi_userfile_mod_req)

Download several files

This method compresses several Userfiles in .gz format and prepares them to be downloaded.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to be downloaded. If more than one file is specified, they will be zipped into a gzip archive.

try:
    # Download several files
    api_response = api_instance.userfiles_download_post(multi_userfile_mod_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_download_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to be downloaded. If more than one file is specified, they will be zipped into a gzip archive. | 

### Return type

[**file**](file.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/*, text/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_get**
> list[Userfile] userfiles_get(page=page, per_page=per_page)

List of the Userfiles accessible to the current user.

This method returns a list of Userfiles that are available to the current User. 

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
page = 56 # int | Page number when paginating. See also the per_page parameter (optional)
per_page = 56 # int | Size of each page when paginating. See also the page parameter (optional)

try:
    # List of the Userfiles accessible to the current user.
    api_response = api_instance.userfiles_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number when paginating. See also the per_page parameter | [optional] 
 **per_page** | **int**| Size of each page when paginating. See also the page parameter | [optional] 

### Return type

[**list[Userfile]**](Userfile.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_id_content_get**
> file userfiles_id_content_get(id)

Get the content of a Userfile

This method allows you to download the content of a userfile.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID number of the Userfile to download

try:
    # Get the content of a Userfile
    api_response = api_instance.userfiles_id_content_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_id_content_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID number of the Userfile to download | 

### Return type

[**file**](file.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/*, text/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_id_get**
> Userfile userfiles_id_get(id)

Get information on a Userfile.

This method returns information about a single Userfile, specified by its ID. Information returned includes the ID of the owner, the Group (project) it is a part of, a description, information about where the acutal copy of the file currently is, and what the status is of any synhronization operations that may have been requested. 

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
id = 56 # int | The ID number of the Userfile to get information on.

try:
    # Get information on a Userfile.
    api_response = api_instance.userfiles_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID number of the Userfile to get information on. | 

### Return type

[**Userfile**](Userfile.md)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_id_put**
> userfiles_id_put(id, userfile_mod_req)

Update information on a Userfile.

This method allows a User to update information on a userfile. 

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
id = 789 # int | The ID number of the Userfile to update.
userfile_mod_req = cbrain_api.UserfileModReq() # UserfileModReq | 

try:
    # Update information on a Userfile.
    api_instance.userfiles_id_put(id, userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID number of the Userfile to update. | 
 **userfile_mod_req** | [**UserfileModReq**](UserfileModReq.md)|  | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_post**
> object userfiles_post(upload_file, data_provider_id, userfile_group_id, file_type, do_extract=do_extract, up_ex_mode=up_ex_mode)

Creates a new Userfile and upload its content.

This method creates a new Userfile in CBRAIN, with the current user as the owner of the file. 

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
upload_file = '/path/to/file.txt' # file | File content to upload to CBRAIN
data_provider_id = 56 # int | The ID of the Data Provider to upload the file to.
userfile_group_id = 56 # int | ID of the group that will have access to the Userfile
file_type = 'SingleFile' # str | The type of the file (default to SingleFile)
do_extract = 'do_extract_example' # str | set to the string 'on' to indicate that the uploaded content is a tar.gz or .zip archive that need to be extracted. See also the parameter _up_ex_mode (optional)
up_ex_mode = 'up_ex_mode_example' # str | if '_do_extract' is set to 'on', set this to 'collection' to create a single collection, or 'multiple' to create one file per entry in the uploaded content (optional)

try:
    # Creates a new Userfile and upload its content.
    api_response = api_instance.userfiles_post(upload_file, data_provider_id, userfile_group_id, file_type, do_extract=do_extract, up_ex_mode=up_ex_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_file** | **file**| File content to upload to CBRAIN | 
 **data_provider_id** | **int**| The ID of the Data Provider to upload the file to. | 
 **userfile_group_id** | **int**| ID of the group that will have access to the Userfile | 
 **file_type** | **str**| The type of the file | [default to SingleFile]
 **do_extract** | **str**| set to the string &#39;on&#39; to indicate that the uploaded content is a tar.gz or .zip archive that need to be extracted. See also the parameter _up_ex_mode | [optional] 
 **up_ex_mode** | **str**| if &#39;_do_extract&#39; is set to &#39;on&#39;, set this to &#39;collection&#39; to create a single collection, or &#39;multiple&#39; to create one file per entry in the uploaded content | [optional] 

### Return type

**object**

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_sync_multiple_post**
> userfiles_sync_multiple_post(multi_userfile_mod_req)

Syncs Userfiles to the local Data Providers cache.

Synchronizing files to their the local cache allows you to download, visualize and do processing on them that is not available if not synced. CBRAIN operations will sync files automatically, and this is only necessary if a file is changed on its host Data Provdier by an external process.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to synchronize.

try:
    # Syncs Userfiles to the local Data Providers cache.
    api_instance.userfiles_sync_multiple_post(multi_userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_sync_multiple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to synchronize. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfiles_uncompress_post**
> userfiles_uncompress_post(multi_userfile_mod_req)

Uncompresses many Userfiles.

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
api_instance = cbrain_api.UserfilesApi(cbrain_api.ApiClient(configuration))
multi_userfile_mod_req = cbrain_api.MultiUserfilesModReq() # MultiUserfilesModReq | The IDs of the files to uncompress.

try:
    # Uncompresses many Userfiles.
    api_instance.userfiles_uncompress_post(multi_userfile_mod_req)
except ApiException as e:
    print("Exception when calling UserfilesApi->userfiles_uncompress_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_userfile_mod_req** | [**MultiUserfilesModReq**](MultiUserfilesModReq.md)| The IDs of the files to uncompress. | 

### Return type

void (empty response body)

### Authorization

[BrainPortalSession](../README.md#BrainPortalSession)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

