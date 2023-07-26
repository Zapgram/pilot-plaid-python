# CreditPayrollIncomeRefreshResponse

CreditPayrollIncomeRefreshResponse defines the response schema for `/credit/payroll_income/refresh`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**verification_refresh_status** | **str** | The verification refresh status. One of the following:  &#x60;\&quot;USER_PRESENCE_REQUIRED\&quot;&#x60; User presence is required to refresh an income verification. &#x60;\&quot;SUCCESSFUL\&quot;&#x60; The income verification refresh was successful. &#x60;\&quot;NOT_FOUND\&quot;&#x60; No new data was found after the income verification refresh. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


