# plaid.model.earnings.Earnings

An object representing both a breakdown of earnings on a paystub and the total earnings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing both a breakdown of earnings on a paystub and the total earnings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[subtotals](#subtotals)** | list, tuple,  | tuple,  |  | [optional] 
**[totals](#totals)** | list, tuple,  | tuple,  |  | [optional] 
**[breakdown](#breakdown)** | list, tuple,  | tuple,  |  | [optional] 
**total** | [**EarningsTotal**](EarningsTotal.md) | [**EarningsTotal**](EarningsTotal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subtotals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EarningsTotal**](EarningsTotal.md) | [**EarningsTotal**](EarningsTotal.md) | [**EarningsTotal**](EarningsTotal.md) |  | 

# totals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EarningsTotal**](EarningsTotal.md) | [**EarningsTotal**](EarningsTotal.md) | [**EarningsTotal**](EarningsTotal.md) |  | 

# breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EarningsBreakdown**](EarningsBreakdown.md) | [**EarningsBreakdown**](EarningsBreakdown.md) | [**EarningsBreakdown**](EarningsBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

