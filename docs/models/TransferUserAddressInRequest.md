# plaid.model.transfer_user_address_in_request.TransferUserAddressInRequest

The address associated with the account holder. Providing this data will improve the likelihood that Plaid will be able to guarantee the transfer, if applicable.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The address associated with the account holder. Providing this data will improve the likelihood that Plaid will be able to guarantee the transfer, if applicable. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**street** | str,  | str,  | The street number and name (i.e., \&quot;100 Market St.\&quot;). | [optional] 
**city** | str,  | str,  | Ex. \&quot;San Francisco\&quot; | [optional] 
**region** | str,  | str,  | The state or province (e.g., \&quot;CA\&quot;). | [optional] 
**postal_code** | str,  | str,  | The postal code (e.g., \&quot;94103\&quot;). | [optional] 
**country** | str,  | str,  | A two-letter country code (e.g., \&quot;US\&quot;). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

