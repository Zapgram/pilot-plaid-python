# TransferAuthorizationProposedTransfer

Details regarding the proposed transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_account_id** | **str, none_type** | The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited. | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**network** | **str** | The network or rails used for the transfer. | 
**origination_account_id** | **str** | Plaid&#39;s unique identifier for the origination account that was used for this transfer. | 
**iso_currency_code** | **str** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | 
**originator_client_id** | **str, none_type** | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**credit_funds_source** | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) |  | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


