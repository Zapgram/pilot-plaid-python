# plaid.model.client_provided_transaction_location.ClientProvidedTransactionLocation

A representation of where a transaction took place.  Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the `description` field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A representation of where a transaction took place.  Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the &#x60;description&#x60; field. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | The country where the transaction occurred. | [optional] 
**region** | str,  | str,  | The region or state where the transaction occurred. | [optional] 
**city** | str,  | str,  | The city where the transaction occurred. | [optional] 
**address** | str,  | str,  | The street address where the transaction occurred. | [optional] 
**postal_code** | str,  | str,  | The postal code where the transaction occurred. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

