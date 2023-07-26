# AssetReportGetRequest

AssetReportGetRequest defines the request schema for `/asset_report/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**asset_report_token** | **str** | A token that can be provided to endpoints such as &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60; to fetch or update an Asset Report. | [optional] 
**user_token** | **str** | The user token associated with the User for which to create an asset report for. The latest asset report associated with the User will be returned | [optional] 
**include_insights** | **bool** | &#x60;true&#x60; if you would like to retrieve the Asset Report with Insights, &#x60;false&#x60; otherwise. This field defaults to &#x60;false&#x60; if omitted. | [optional]  if omitted the server will use the default value of False
**fast_report** | **bool** | &#x60;true&#x60; to fetch \&quot;fast\&quot; version of asset report. Defaults to false if omitted. Can only be used if &#x60;/asset_report/create&#x60; was called with &#x60;options.add_ons&#x60; set to &#x60;[\&quot;fast_assets\&quot;]&#x60;. | [optional]  if omitted the server will use the default value of False
**options** | [**AssetReportGetRequestOptions**](AssetReportGetRequestOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


