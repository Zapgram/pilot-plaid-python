# plaid.model.address_data.AddressData

Data about the components comprising an address.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about the components comprising an address. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | None, str,  | NoneClass, str,  | The ISO 3166-1 alpha-2 country code | 
**city** | None, str,  | NoneClass, str,  | The full city name | 
**street** | str,  | str,  | The full street address Example: &#x60;\&quot;564 Main Street, APT 15\&quot;&#x60; | 
**postal_code** | None, str,  | NoneClass, str,  | The postal code. In API versions 2018-05-22 and earlier, this field is called &#x60;zip&#x60;. | 
**region** | None, str,  | NoneClass, str,  | The region or state. In API versions 2018-05-22 and earlier, this field is called &#x60;state&#x60;. Example: &#x60;\&quot;NC\&quot;&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

