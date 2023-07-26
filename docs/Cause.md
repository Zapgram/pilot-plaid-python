# Cause

An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | [**PlaidErrorType**](PlaidErrorType.md) |  | 
**error_code** | **str** | The particular error code. Safe for programmatic use. | 
**error_message** | **str** | A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use. | 
**display_message** | **str, none_type** | A user-friendly representation of the error code. &#x60;null&#x60; if the error is not related to user action.  This may change over time and is not safe for programmatic use. | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**request_id** | **str** | A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks. | [optional] 
**causes** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, &#x60;causes&#x60; will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.  &#x60;causes&#x60; will only be provided for the &#x60;error_type&#x60; &#x60;ASSET_REPORT_ERROR&#x60;. &#x60;causes&#x60; will also not be populated inside an error nested within a &#x60;warning&#x60; object. | [optional] 
**status** | **int, none_type** | The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook. | [optional] 
**documentation_url** | **str** | The URL of a Plaid documentation page with more information about the error | [optional] 
**suggested_action** | **str, none_type** | Suggested steps for resolving the error | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


