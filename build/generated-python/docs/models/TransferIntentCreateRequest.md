# plaid.model.transfer_intent_create_request.TransferIntentCreateRequest

Defines the request schema for `/transfer/intent/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/intent/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**description** | str,  | str,  | A description for the underlying transfer. Maximum of 8 characters. | 
**user** | [**TransferUserInRequest**](TransferUserInRequest.md) | [**TransferUserInRequest**](TransferUserInRequest.md) |  | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**account_id** | None, str,  | NoneClass, str,  | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | [optional] 
**funding_account_id** | [**TransferFundingAccountIDRequest**](TransferFundingAccountIDRequest.md) | [**TransferFundingAccountIDRequest**](TransferFundingAccountIDRequest.md) |  | [optional] 
**network** | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) |  | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**origination_account_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used. | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount, e.g. \&quot;USD\&quot; | [optional] 
**require_guarantee** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, the transfer requires a &#x60;GUARANTEED&#x60; decision by Plaid to proceed (Guarantee customers only). | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

