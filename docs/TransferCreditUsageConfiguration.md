# TransferCreditUsageConfiguration

Specifies the originator's expected usage of credits. For all dollar amounts, use a decimal string with two digits of precision e.g. \"10.00\". This field is required if the originator is expected to process credit transfers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_frequency** | [**OriginatorExpectedTransferFrequency**](OriginatorExpectedTransferFrequency.md) |  | 
**expected_highest_amount** | **str** | The originator’s expected highest amount for a single credit transfer. | 
**expected_average_amount** | **str** | The originator’s expected average amount per credit. | 
**expected_monthly_amount** | **str** | The originator’s monthly expected ACH credit processing amount for the next 6-12 months. | 
**sec_codes** | [**[CreditACHClass]**](CreditACHClass.md) | Specifies the expected use cases for the originator’s credit transfers. This should be a list that contains one or more of the following codes:  &#x60;\&quot;ccd\&quot;&#x60; - Corporate Credit or Debit - fund transfer between two corporate bank accounts  &#x60;\&quot;ppd\&quot;&#x60; - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  &#x60;\&quot;web\&quot;&#x60; - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


