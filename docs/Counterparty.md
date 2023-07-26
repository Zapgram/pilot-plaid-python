# Counterparty

The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | 
**type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**website** | **str, none_type** | The website associated with the counterparty. | 
**logo_url** | **str, none_type** | The URL of a logo associated with the counterparty, if available. The logo is formatted as a 100x100 pixel PNG file. | 
**entity_id** | **str, none_type** | A unique, stable, Plaid-generated id that maps to the counterparty. | [optional] 
**confidence_level** | **str, none_type** | A description of how confident we are that the provided counterparty is involved in the transaction.  &#x60;very_high&#x60;: We recognize this counterparty and we are more than 98% confident that it is involved in this transaction. &#x60;high&#x60;: We recognize this counterparty and we are more than 90% confident that it is involved in this transaction. &#x60;medium&#x60;: We are moderately confident that this counterparty was involved in this transaction, but some details may differ from our records. &#x60;low&#x60;: We didn’t find a matching counterparty in our records, so we are returning a cleansed name parsed out of the request description. &#x60;unknown&#x60;: Error | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


