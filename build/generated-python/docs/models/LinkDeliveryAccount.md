# plaid.model.link_delivery_account.LinkDeliveryAccount

Information related to account attached to the connected Item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information related to account attached to the connected Item | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The Plaid &#x60;account_id&#x60; | [optional] 
**name** | str,  | str,  | The official account name | [optional] 
**mask** | str,  | str,  | The last 2-4 alphanumeric characters of an account&#x27;s official account number. Note that the mask may be non-unique between an Item&#x27;s accounts. It may also not match the mask that the bank displays to the user. | [optional] 
**type** | str,  | str,  | The account type. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values | [optional] 
**subtype** | str,  | str,  | The account subtype. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values | [optional] 
**verification_status** | [**LinkDeliveryVerificationStatus**](LinkDeliveryVerificationStatus.md) | [**LinkDeliveryVerificationStatus**](LinkDeliveryVerificationStatus.md) |  | [optional] 
**class_type** | str,  | str,  | If micro-deposit verification is being used, indicates whether the account being verified is a &#x60;business&#x60; or &#x60;personal&#x60; account. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

