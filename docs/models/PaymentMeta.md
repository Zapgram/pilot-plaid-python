# plaid.model.payment_meta.PaymentMeta

Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.  If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync or `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be &#x60;null&#x60;.  If the &#x60;transactions&#x60; object was returned by a Transactions endpoint such as &#x60;/transactions/sync or &#x60;/transactions/get&#x60;, the &#x60;payment_meta&#x60; key will always appear, but no data elements are guaranteed. If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payee** | None, str,  | NoneClass, str,  | For transfers, the party that is receiving the transaction. | 
**ppd_id** | None, str,  | NoneClass, str,  | The ACH PPD ID for the payer. | 
**reason** | None, str,  | NoneClass, str,  | The payer-supplied description of the transfer. | 
**by_order_of** | None, str,  | NoneClass, str,  | The party initiating a wire transfer. Will be &#x60;null&#x60; if the transaction is not a wire transfer. | 
**payment_processor** | None, str,  | NoneClass, str,  | The name of the payment processor | 
**payer** | None, str,  | NoneClass, str,  | For transfers, the party that is paying the transaction. | 
**reference_number** | None, str,  | NoneClass, str,  | The transaction reference number supplied by the financial institution. | 
**payment_method** | None, str,  | NoneClass, str,  | The type of transfer, e.g. &#x27;ACH&#x27; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

