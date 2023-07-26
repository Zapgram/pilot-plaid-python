# plaid.model.transaction_counterparty.TransactionCounterparty

The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**website** | None, str,  | NoneClass, str,  | The website associated with the counterparty. | 
**logo_url** | None, str,  | NoneClass, str,  | The URL of a logo associated with the counterparty, if available. The logo is formatted as a 100x100 pixel PNG filepath. | 
**name** | str,  | str,  | The name of the counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | 
**type** | [**CounterpartyType**](CounterpartyType.md) | [**CounterpartyType**](CounterpartyType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

