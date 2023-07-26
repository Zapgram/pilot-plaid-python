# plaid.model.bank_transfer.BankTransfer

Represents a bank transfer within the Bank Transfers API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a bank transfer within the Bank Transfers API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**metadata** | [**BankTransferMetadata**](BankTransferMetadata.md) | [**BankTransferMetadata**](BankTransferMetadata.md) |  | 
**created** | str, datetime,  | str,  | The datetime when this bank transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | value must conform to RFC-3339 date-time
**description** | str,  | str,  | The description of the transfer. | 
**failure_reason** | [**BankTransferFailure**](BankTransferFailure.md) | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**type** | [**BankTransferType**](BankTransferType.md) | [**BankTransferType**](BankTransferType.md) |  | 
**cancellable** | bool,  | BoolClass,  | When &#x60;true&#x60;, you can still cancel this bank transfer. | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**custom_tag** | None, str,  | NoneClass, str,  | A string containing the custom tag provided by the client in the create request. Will be null if not provided. | 
**account_id** | str,  | str,  | The account ID that should be credited/debited for this bank transfer. | 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**origination_account_id** | str,  | str,  | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**id** | str,  | str,  | Plaid’s unique identifier for a bank transfer. | 
**user** | [**BankTransferUser**](BankTransferUser.md) | [**BankTransferUser**](BankTransferUser.md) |  | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**status** | [**BankTransferStatus**](BankTransferStatus.md) | [**BankTransferStatus**](BankTransferStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

