# plaid.model.paystub_deduction.PaystubDeduction

Deduction on the paystub

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Deduction on the paystub | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_pretax** | None, bool,  | NoneClass, BoolClass,  | &#x60;true&#x60; if the deduction is pre-tax; &#x60;false&#x60; otherwise. | 
**total** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the deduction. | value must be a 64 bit float
**type** | None, str,  | NoneClass, str,  | The description of the deduction, as provided on the paystub. For example: &#x60;\&quot;401(k)\&quot;&#x60;, &#x60;\&quot;FICA MED TAX\&quot;&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

