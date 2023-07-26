# plaid.model.signal_address_data.SignalAddressData

Data about the components comprising an address.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Data about the components comprising an address. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**city** | str,  | str,  | The full city name | [optional] 
**region** | None, str,  | NoneClass, str,  | The region or state Example: &#x60;\&quot;NC\&quot;&#x60; | [optional] 
**street** | str,  | str,  | The full street address Example: &#x60;\&quot;564 Main Street, APT 15\&quot;&#x60; | [optional] 
**postal_code** | None, str,  | NoneClass, str,  | The postal code | [optional] 
**country** | None, str,  | NoneClass, str,  | The ISO 3166-1 alpha-2 country code | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

