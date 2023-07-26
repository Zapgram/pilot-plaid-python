# plaid.model.product_status_breakdown.ProductStatusBreakdown

A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1. The time range used for calculating the breakdown may range from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period assessed may be 24 hours or more. For more details, see [Institution status details](https://plaid.com/docs/account/activity/#institution-status-details).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A detailed breakdown of the institution&#x27;s performance for a request type. The values for &#x60;success&#x60;, &#x60;error_plaid&#x60;, and &#x60;error_institution&#x60; sum to 1. The time range used for calculating the breakdown may range from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period assessed may be 24 hours or more. For more details, see [Institution status details](https://plaid.com/docs/account/activity/#institution-status-details). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error_plaid** | decimal.Decimal, int, float,  | decimal.Decimal,  | The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal.  | value must be a 64 bit float
**success** | decimal.Decimal, int, float,  | decimal.Decimal,  | The percentage of login attempts that are successful, expressed as a decimal. | value must be a 64 bit float
**error_institution** | decimal.Decimal, int, float,  | decimal.Decimal,  | The percentage of logins that are failing due to an issue in the institution&#x27;s system, expressed as a decimal. | value must be a 64 bit float
**refresh_interval** | str,  | str,  | The &#x60;refresh_interval&#x60; may be &#x60;DELAYED&#x60; or &#x60;STOPPED&#x60; even when the success rate is high. This value is only returned for Transactions status breakdowns. | [optional] must be one of ["NORMAL", "DELAYED", "STOPPED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

