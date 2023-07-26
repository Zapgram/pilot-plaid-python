# plaid.model.income_breakdown.IncomeBreakdown

An object representing a breakdown of the different income types on the paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing a breakdown of the different income types on the paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hours** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The number of hours logged for this income for this pay period. | 
**total** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The total pay for this pay period. | value must be a 64 bit float
**rate** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The hourly rate at which the income is paid. | value must be a 64 bit float
**type** | [**IncomeBreakdownType**](IncomeBreakdownType.md) | [**IncomeBreakdownType**](IncomeBreakdownType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

