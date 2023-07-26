# plaid.model.payment_initiation_recipient_create_request.PaymentInitiationRecipientCreateRequest

PaymentInitiationRecipientCreateRequest defines the request schema for `/payment_initiation/recipient/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationRecipientCreateRequest defines the request schema for &#x60;/payment_initiation/recipient/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**iban** | None, str,  | NoneClass, str,  | The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required. | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

