# plaid.model.total.Total

An object representing both the current pay period and year to date amount for a category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing both the current pay period and year to date amount for a category. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**canonical_description** | [**TotalCanonicalDescription**](TotalCanonicalDescription.md) | [**TotalCanonicalDescription**](TotalCanonicalDescription.md) |  | [optional] 
**description** | None, str,  | NoneClass, str,  | Text of the line item as printed on the paystub. | [optional] 
**current_pay** | [**Pay**](Pay.md) | [**Pay**](Pay.md) |  | [optional] 
**ytd_pay** | [**Pay**](Pay.md) | [**Pay**](Pay.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

