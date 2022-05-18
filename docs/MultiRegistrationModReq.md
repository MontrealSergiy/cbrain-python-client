# MultiRegistrationModReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basenames** | **list[str]** |  | [optional] 
**filetypes** | **list[str]** | An array containing the filetypes associated with the files to register; each element must be a string containing the cbrain file type, a single dash, and then a repeat of the basename found in the basenames parameters. For example, \&quot;TextFile-abc.txt\&quot; | [optional] 
**as_user_id** | **int** | The ID of the user to register files as. | [optional] 
**browse_path** | **str** | A relative path such as \&quot;abcd/efgh\&quot; that can be provided when registering basenames deeper under the root of the DataProvider. This parameter only works for DataProvider types that have a &#39;multi-level&#39; capability. Otherwise the string is ignored. The relative path will be used for all basenames in the current request. | [optional] 
**other_group_id** | **int** | The ID of the project controlling access to the registered files. | [optional] 
**delete** | **bool** | Specifies to delete the file contents. This is only used during an \&quot;unregister\&quot; action. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


