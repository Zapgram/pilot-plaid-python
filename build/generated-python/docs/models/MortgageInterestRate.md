# plaid.model.mortgage_interest_rate.MortgageInterestRate

Object containing metadata about the interest rate for the mortgage.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing metadata about the interest rate for the mortgage. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**percentage** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan. | value must be a 64 bit float
**type** | None, str,  | NoneClass, str,  | The type of interest charged (fixed or variable). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

