# TransactionOverride

Data to populate as test transaction data. If not specified, random transactions will be generated instead.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_transacted** | **date** | The date of the transaction, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Transactions in Sandbox will move from pending to posted once their transaction date has been reached. If a &#x60;date_transacted&#x60; is not provided by the institution, a transaction date may be available in the [&#x60;authorized_date&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-authorized-date) field. | 
**date_posted** | **date** | The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Posted dates in the past or present will result in posted transactions; posted dates in the future will result in pending transactions. | 
**amount** | **float** | The transaction amount. Can be negative. | 
**description** | **str** | The transaction description. | 
**currency** | **str** | The ISO-4217 format currency code for the transaction. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


