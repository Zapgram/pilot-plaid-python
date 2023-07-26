# plaid.model.transfer_intent_create.TransferIntentCreate

Represents a transfer intent within Transfer UI.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a transfer intent within Transfer UI. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**funding_account_id** | str,  | str,  | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**created** | str, datetime,  | str,  | The datetime the transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**iso_currency_code** | str,  | str,  | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**description** | str,  | str,  | A description for the underlying transfer. Maximum of 8 characters. | 
**origination_account_id** | str,  | str,  | Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used. | 
**id** | str,  | str,  | Plaid&#x27;s unique identifier for the transfer intent object. | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**status** | [**TransferIntentStatus**](TransferIntentStatus.md) | [**TransferIntentStatus**](TransferIntentStatus.md) |  | 
**account_id** | None, str,  | NoneClass, str,  | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**network** | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) |  | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**require_guarantee** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, the transfer requires a &#x60;GUARANTEED&#x60; decision by Plaid to proceed (Guarantee customers only). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

