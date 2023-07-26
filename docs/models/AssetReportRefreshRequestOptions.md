# plaid.model.asset_report_refresh_request_options.AssetReportRefreshRequestOptions

An optional object to filter `/asset_report/refresh` results. If provided, cannot be `null`. If not specified, the `options` from the original call to `/asset_report/create` will be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/asset_report/refresh&#x60; results. If provided, cannot be &#x60;null&#x60;. If not specified, the &#x60;options&#x60; from the original call to &#x60;/asset_report/create&#x60; will be used. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_report_id** | None, str,  | NoneClass, str,  | Client-generated identifier, which can be used by lenders to track loan applications. | [optional] 
**webhook** | None, str,  | NoneClass, str,  | URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready. | [optional] 
**user** | [**AssetReportUser**](AssetReportUser.md) | [**AssetReportUser**](AssetReportUser.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

