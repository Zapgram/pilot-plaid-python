# plaid.model.asset_report_create_request.AssetReportCreateRequest

AssetReportCreateRequest defines the request schema for `/asset_report/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AssetReportCreateRequest defines the request schema for &#x60;/asset_report/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, &#x60;days_requested&#x60; must be at least 61 for new originations or at least 31 for refinancings.  An Asset Report requested with \&quot;Additional History\&quot; (that is, with more than 61 days of transaction history) will incur an Additional History fee. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**[access_tokens](#access_tokens)** | list, tuple,  | tuple,  | An array of access tokens corresponding to the Items that will be included in the report. The &#x60;assets&#x60; product must have been initialized for the Items during link; the Assets product cannot be added after initialization. | [optional] 
**user_token** | str,  | str,  | The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report. | [optional] 
**options** | [**AssetReportCreateRequestOptions**](AssetReportCreateRequestOptions.md) | [**AssetReportCreateRequestOptions**](AssetReportCreateRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# access_tokens

An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of access tokens corresponding to the Items that will be included in the report. The &#x60;assets&#x60; product must have been initialized for the Items during link; the Assets product cannot be added after initialization. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The access token associated with the Item data is being requested for. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

