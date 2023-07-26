# plaid.model.external_payment_refund_details.ExternalPaymentRefundDetails

Details about external payment refund

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Details about external payment refund | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | 
**iban** | None, str,  | NoneClass, str,  | The International Bank Account Number (IBAN) for the account. | 
**name** | str,  | str,  | The name of the account holder. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

