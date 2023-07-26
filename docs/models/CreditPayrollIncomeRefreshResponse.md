# plaid.model.credit_payroll_income_refresh_response.CreditPayrollIncomeRefreshResponse

CreditPayrollIncomeRefreshResponse defines the response schema for `/credit/payroll_income/refresh`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreditPayrollIncomeRefreshResponse defines the response schema for &#x60;/credit/payroll_income/refresh&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**verification_refresh_status** | str,  | str,  | The verification refresh status. One of the following:  &#x60;\&quot;USER_PRESENCE_REQUIRED\&quot;&#x60; User presence is required to refresh an income verification. &#x60;\&quot;SUCCESSFUL\&quot;&#x60; The income verification refresh was successful. &#x60;\&quot;NOT_FOUND\&quot;&#x60; No new data was found after the income verification refresh. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

