# TransactionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_date** | **date, none_type** | The date that the transaction was authorized. For posted transactions, the &#x60;date&#x60; field will indicate the posted date, but &#x60;authorized_date&#x60; will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the &#x60;authorized_date&#x60;, when available, is generally preferable to use over the &#x60;date&#x60; field for posted transactions, as it will generally represent the date the user actually made the transaction. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DD&#x60; ). | 
**authorized_datetime** | **datetime, none_type** | Date and time when a transaction was authorized in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DDTHH:mm:ssZ&#x60; ). For posted transactions, the &#x60;datetime&#x60; field will indicate the posted date, but &#x60;authorized_datetime&#x60; will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the &#x60;authorized_datetime&#x60;, when available, is generally preferable to use over the &#x60;datetime&#x60; field for posted transactions, as it will generally represent the date the user actually made the transaction.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later. | 
**datetime** | **datetime, none_type** | Date and time when a transaction was posted in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DDTHH:mm:ssZ&#x60; ). For the date that the transaction was initiated, rather than posted, see the &#x60;authorized_datetime&#x60; field.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later. | 
**payment_channel** | **str** | The channel used to make a payment. &#x60;online:&#x60; transactions that took place online.  &#x60;in store:&#x60; transactions that were made at a physical location.  &#x60;other:&#x60; transactions that relate to banks, e.g. fees or deposits.  This field replaces the &#x60;transaction_type&#x60; field.  | 
**transaction_code** | [**TransactionCode**](TransactionCode.md) |  | 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**personal_finance_category_icon_url** | **str** | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | [optional] 
**counterparties** | [**[TransactionCounterparty]**](TransactionCounterparty.md) | The counterparties present in the transaction. Counterparties, such as the financial institutions, are extracted by Plaid from the raw description. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


