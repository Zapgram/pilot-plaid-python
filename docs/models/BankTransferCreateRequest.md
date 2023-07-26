# plaid.model.bank_transfer_create_request.BankTransferCreateRequest

Defines the request schema for `/bank_transfer/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/bank_transfer/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. | 
**amount** | str,  | str,  | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount – should be set to \&quot;USD\&quot;. | 
**description** | str,  | str,  | The transfer description. Maximum of 10 characters. | 
**idempotency_key** | [**BankTransferIdempotencyKey**](BankTransferIdempotencyKey.md) | [**BankTransferIdempotencyKey**](BankTransferIdempotencyKey.md) |  | 
**type** | [**BankTransferType**](BankTransferType.md) | [**BankTransferType**](BankTransferType.md) |  | 
**user** | [**BankTransferUser**](BankTransferUser.md) | [**BankTransferUser**](BankTransferUser.md) |  | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**custom_tag** | None, str,  | NoneClass, str,  | An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters. | [optional] 
**metadata** | [**BankTransferMetadata**](BankTransferMetadata.md) | [**BankTransferMetadata**](BankTransferMetadata.md) |  | [optional] 
**origination_account_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
