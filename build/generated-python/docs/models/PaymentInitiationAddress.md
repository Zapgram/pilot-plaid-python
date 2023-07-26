# plaid.model.payment_initiation_address.PaymentInitiationAddress

The optional address of the payment recipient's bank account. Required by most institutions outside of the UK.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The optional address of the payment recipient&#x27;s bank account. Required by most institutions outside of the UK. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | The ISO 3166-1 alpha-2 country code where the recipient is located. | 
**city** | str,  | str,  | The city where the recipient is located. Maximum of 35 characters. | 
**[street](#street)** | list, tuple,  | tuple,  | An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters. | 
**postal_code** | str,  | str,  | The postal code where the recipient is located. Maximum of 16 characters. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# street

An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

