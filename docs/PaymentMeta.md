# PaymentMeta

Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.  If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync or `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str, none_type** | The transaction reference number supplied by the financial institution. | 
**ppd_id** | **str, none_type** | The ACH PPD ID for the payer. | 
**payee** | **str, none_type** | For transfers, the party that is receiving the transaction. | 
**by_order_of** | **str, none_type** | The party initiating a wire transfer. Will be &#x60;null&#x60; if the transaction is not a wire transfer. | 
**payer** | **str, none_type** | For transfers, the party that is paying the transaction. | 
**payment_method** | **str, none_type** | The type of transfer, e.g. &#39;ACH&#39; | 
**payment_processor** | **str, none_type** | The name of the payment processor | 
**reason** | **str, none_type** | The payer-supplied description of the transfer. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


