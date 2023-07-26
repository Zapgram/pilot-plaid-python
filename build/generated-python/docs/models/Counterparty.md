# plaid.model.counterparty.Counterparty

The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**website** | None, str,  | NoneClass, str,  | The website associated with the counterparty. | 
**logo_url** | None, str,  | NoneClass, str,  | The URL of a logo associated with the counterparty, if available. The logo is formatted as a 100x100 pixel PNG file. | 
**name** | str,  | str,  | The name of the counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | 
**type** | [**CounterpartyType**](CounterpartyType.md) | [**CounterpartyType**](CounterpartyType.md) |  | 
**entity_id** | None, str,  | NoneClass, str,  | A unique, stable, Plaid-generated id that maps to the counterparty. | [optional] 
**confidence_level** | None, str,  | NoneClass, str,  | A description of how confident we are that the provided counterparty is involved in the transaction.  &#x60;very_high&#x60;: We recognize this counterparty and we are more than 98% confident that it is involved in this transaction. &#x60;high&#x60;: We recognize this counterparty and we are more than 90% confident that it is involved in this transaction. &#x60;medium&#x60;: We are moderately confident that this counterparty was involved in this transaction, but some details may differ from our records. &#x60;low&#x60;: We didn’t find a matching counterparty in our records, so we are returning a cleansed name parsed out of the request description. &#x60;unknown&#x60;: Error | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

