# ProcessorBankTransferCreateRequest

Defines the request schema for `/processor/bank_transfer/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | [**BankTransferIdempotencyKey**](BankTransferIdempotencyKey.md) |  | 
**processor_token** | **str** | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**type** | [**BankTransferType**](BankTransferType.md) |  | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**amount** | **str** | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**iso_currency_code** | **str** | The currency of the transfer amount – should be set to \&quot;USD\&quot;. | 
**description** | **str** | The transfer description. Maximum of 10 characters. | 
**user** | [**BankTransferUser**](BankTransferUser.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**custom_tag** | **str, none_type** | An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters. | [optional] 
**metadata** | [**BankTransferMetadata**](BankTransferMetadata.md) |  | [optional] 
**origination_account_id** | **str, none_type** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


