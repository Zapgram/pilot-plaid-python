# plaid.model.institutions_search_account_filter.InstitutionsSearchAccountFilter

An account filter to apply to institutions search requests

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An account filter to apply to institutions search requests | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[loan](#loan)** | list, tuple,  | tuple,  |  | [optional] 
**[depository](#depository)** | list, tuple,  | tuple,  |  | [optional] 
**[credit](#credit)** | list, tuple,  | tuple,  |  | [optional] 
**[investment](#investment)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# loan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 

# depository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 

# credit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 

# investment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

