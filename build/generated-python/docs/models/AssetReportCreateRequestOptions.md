# plaid.model.asset_report_create_request_options.AssetReportCreateRequestOptions

An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/asset_report/create&#x60; results. If provided, must be non-&#x60;null&#x60;. The optional &#x60;user&#x60; object is required for the report to be eligible for Fannie Mae&#x27;s Day 1 Certainty program. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_report_id** | None, str,  | NoneClass, str,  | Client-generated identifier, which can be used by lenders to track loan applications. | [optional] 
**webhook** | None, str,  | NoneClass, str,  | URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready. | [optional] 
**include_fast_report** | None, bool,  | NoneClass, BoolClass,  | true to return balance and identity earlier as a fast report. Defaults to false if omitted. | [optional] 
**[products](#products)** | list, tuple,  | tuple,  | Additional information that can be included in the asset report. Possible values: &#x60;\&quot;investments\&quot;&#x60; | [optional] 
**[add_ons](#add_ons)** | list, tuple,  | tuple,  | Use this field to request a &#x60;fast_asset&#x60; report. When Fast Assets is requested, Plaid will create two versions of the Asset Report: first, the Fast Asset Report, which will contain only current identity and balance information, and later, the Full Asset Report, which will also contain historical balance information and transaction data. A &#x60;PRODUCT_READY&#x60; webhook will be fired for each Asset Report when it is ready, and the &#x60;report_type&#x60; field will indicate whether the webhook is firing for the &#x60;full&#x60; or &#x60;fast&#x60; Asset Report. To retrieve the Fast Asset Report, call &#x60;/asset_report/get&#x60; with &#x60;fast_report&#x60; set to &#x60;true&#x60;. There is no additional charge for using Fast Assets. | [optional] 
**user** | [**AssetReportUser**](AssetReportUser.md) | [**AssetReportUser**](AssetReportUser.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

Additional information that can be included in the asset report. Possible values: `\"investments\"`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional information that can be included in the asset report. Possible values: &#x60;\&quot;investments\&quot;&#x60; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# add_ons

Use this field to request a `fast_asset` report. When Fast Assets is requested, Plaid will create two versions of the Asset Report: first, the Fast Asset Report, which will contain only current identity and balance information, and later, the Full Asset Report, which will also contain historical balance information and transaction data. A `PRODUCT_READY` webhook will be fired for each Asset Report when it is ready, and the `report_type` field will indicate whether the webhook is firing for the `full` or `fast` Asset Report. To retrieve the Fast Asset Report, call `/asset_report/get` with `fast_report` set to `true`. There is no additional charge for using Fast Assets.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Use this field to request a &#x60;fast_asset&#x60; report. When Fast Assets is requested, Plaid will create two versions of the Asset Report: first, the Fast Asset Report, which will contain only current identity and balance information, and later, the Full Asset Report, which will also contain historical balance information and transaction data. A &#x60;PRODUCT_READY&#x60; webhook will be fired for each Asset Report when it is ready, and the &#x60;report_type&#x60; field will indicate whether the webhook is firing for the &#x60;full&#x60; or &#x60;fast&#x60; Asset Report. To retrieve the Fast Asset Report, call &#x60;/asset_report/get&#x60; with &#x60;fast_report&#x60; set to &#x60;true&#x60;. There is no additional charge for using Fast Assets. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetReportAddOns**](AssetReportAddOns.md) | [**AssetReportAddOns**](AssetReportAddOns.md) | [**AssetReportAddOns**](AssetReportAddOns.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

