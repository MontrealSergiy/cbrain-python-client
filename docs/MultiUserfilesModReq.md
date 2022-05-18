# MultiUserfilesModReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **list[str]** |  | [optional] 
**data_provider_id_for_mv_cp** | **int** |  | [optional] 
**specified_filename** | **str** | The name of the archive file that the Userfiles will be compressed into when downloading. | [optional] 
**operation** | **str** | Used when affecting the synchronization status of files. Either \&quot;sync_local\&quot; or \&quot;all_newer\&quot;. \&quot;sync_local\&quot; will ensure that the version of the file in the CBRAIN portal cache is the most recent version that exists on the Data Provider. \&quot;all_newer\&quot; will ensure that ALL caches known to CBRAIN are updated with the most recent version of the files in the host Data Provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


