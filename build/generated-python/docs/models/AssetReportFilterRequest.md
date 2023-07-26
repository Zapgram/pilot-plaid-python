# plaid.model.asset_report_filter_request.AssetReportFilterRequest

AssetReportFilterRequest defines the request schema for `/asset_report/filter`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AssetReportFilterRequest defines the request schema for &#x60;/asset_report/filter&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[account_ids_to_exclude](#account_ids_to_exclude)** | list, tuple,  | tuple,  | The accounts to exclude from the Asset Report, identified by &#x60;account_id&#x60;. | 
**asset_report_token** | str,  | str,  | A token that can be provided to endpoints such as &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60; to fetch or update an Asset Report. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids_to_exclude

The accounts to exclude from the Asset Report, identified by `account_id`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The accounts to exclude from the Asset Report, identified by &#x60;account_id&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
