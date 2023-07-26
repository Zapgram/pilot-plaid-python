# plaid.model.payment_initiation_recipient.PaymentInitiationRecipient

PaymentInitiationRecipient defines a payment initiation recipient

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationRecipient defines a payment initiation recipient | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the recipient. | 
**recipient_id** | str,  | str,  | The ID of the recipient. | 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**iban** | None, str,  | NoneClass, str,  | The International Bank Account Number (IBAN) for the recipient. | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

