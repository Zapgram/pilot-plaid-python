# IncomeVerificationPrecheckRequest

IncomeVerificationPrecheckRequest defines the request schema for `/income/verification/precheck`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**user** | [**IncomeVerificationPrecheckUser**](IncomeVerificationPrecheckUser.md) |  | [optional] 
**employer** | [**IncomeVerificationPrecheckEmployer**](IncomeVerificationPrecheckEmployer.md) |  | [optional] 
**payroll_institution** | [**IncomeVerificationPrecheckPayrollInstitution**](IncomeVerificationPrecheckPayrollInstitution.md) |  | [optional] 
**transactions_access_token** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**transactions_access_tokens** | **[str]** | An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with &#x60;transactions&#x60;, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product. | [optional] 
**us_military_info** | [**IncomeVerificationPrecheckMilitaryInfo**](IncomeVerificationPrecheckMilitaryInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


