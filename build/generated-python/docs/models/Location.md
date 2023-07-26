# plaid.model.location.Location

A representation of where a transaction took place

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A representation of where a transaction took place | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | None, str,  | NoneClass, str,  | The ISO 3166-1 alpha-2 country code where the transaction occurred. | 
**address** | None, str,  | NoneClass, str,  | The street address where the transaction occurred. | 
**city** | None, str,  | NoneClass, str,  | The city where the transaction occurred. | 
**store_number** | None, str,  | NoneClass, str,  | The merchant defined store number where the transaction occurred. | 
**lon** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The longitude where the transaction occurred. | value must be a 64 bit float
**postal_code** | None, str,  | NoneClass, str,  | The postal code where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called &#x60;zip&#x60;. | 
**region** | None, str,  | NoneClass, str,  | The region or state where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called &#x60;state&#x60;. | 
**lat** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The latitude where the transaction occurred. | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

