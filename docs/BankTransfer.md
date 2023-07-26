# BankTransfer

Represents a bank transfer within the Bank Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid’s unique identifier for a bank transfer. | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**account_id** | **str** | The account ID that should be credited/debited for this bank transfer. | 
**type** | [**BankTransferType**](BankTransferType.md) |  | 
**user** | [**BankTransferUser**](BankTransferUser.md) |  | 
**amount** | **str** | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**description** | **str** | The description of the transfer. | 
**created** | **datetime** | The datetime when this bank transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**status** | [**BankTransferStatus**](BankTransferStatus.md) |  | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**cancellable** | **bool** | When &#x60;true&#x60;, you can still cancel this bank transfer. | 
**failure_reason** | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**custom_tag** | **str, none_type** | A string containing the custom tag provided by the client in the create request. Will be null if not provided. | 
**metadata** | [**BankTransferMetadata**](BankTransferMetadata.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


