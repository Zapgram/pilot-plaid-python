# plaid.model.deposit_switch_address_data.DepositSwitchAddressData

The user's address.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The user&#x27;s address. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | The ISO 3166-1 alpha-2 country code | 
**city** | str,  | str,  | The full city name | 
**street** | str,  | str,  | The full street address Example: &#x60;\&quot;564 Main Street, APT 15\&quot;&#x60; | 
**postal_code** | str,  | str,  | The postal code | 
**region** | str,  | str,  | The region or state Example: &#x60;\&quot;NC\&quot;&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

