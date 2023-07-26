# plaid.model.link_token_create_request_user_stated_income_source.LinkTokenCreateRequestUserStatedIncomeSource

Specifies user stated income sources for the Income product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies user stated income sources for the Income product | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**employer** | str,  | str,  | The employer corresponding to an income source specified by the user | [optional] 
**category** | [**UserStatedIncomeSourceCategory**](UserStatedIncomeSourceCategory.md) | [**UserStatedIncomeSourceCategory**](UserStatedIncomeSourceCategory.md) |  | [optional] 
**pay_per_cycle** | decimal.Decimal, int, float,  | decimal.Decimal,  | The income amount paid per cycle for a specified income source | [optional] value must be a 64 bit float
**pay_annual** | decimal.Decimal, int, float,  | decimal.Decimal,  | The income amount paid annually for a specified income source | [optional] value must be a 64 bit float
**pay_type** | [**UserStatedIncomeSourcePayType**](UserStatedIncomeSourcePayType.md) | [**UserStatedIncomeSourcePayType**](UserStatedIncomeSourcePayType.md) |  | [optional] 
**pay_frequency** | [**UserStatedIncomeSourceFrequency**](UserStatedIncomeSourceFrequency.md) | [**UserStatedIncomeSourceFrequency**](UserStatedIncomeSourceFrequency.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

