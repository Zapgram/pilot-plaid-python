# plaid.model.payment_initiation_recipient_list_response.PaymentInitiationRecipientListResponse

PaymentInitiationRecipientListResponse defines the response schema for `/payment_initiation/recipient/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationRecipientListResponse defines the response schema for &#x60;/payment_initiation/recipient/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[recipients](#recipients)** | list, tuple,  | tuple,  | An array of payment recipients created for Payment Initiation | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# recipients

An array of payment recipients created for Payment Initiation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of payment recipients created for Payment Initiation | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentInitiationRecipient**](PaymentInitiationRecipient.md) | [**PaymentInitiationRecipient**](PaymentInitiationRecipient.md) | [**PaymentInitiationRecipient**](PaymentInitiationRecipient.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

