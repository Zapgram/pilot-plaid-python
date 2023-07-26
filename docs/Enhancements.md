# Enhancements

A grouping of the Plaid produced transaction enhancement fields.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_channel** | [**PaymentChannel**](PaymentChannel.md) |  | 
**category_id** | **str, none_type** | The ID of the category to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**category** | **[str]** | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**location** | [**Location**](Location.md) |  | 
**merchant_name** | **str, none_type** | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | [optional] 
**website** | **str, none_type** | The website associated with this transaction, if available. | [optional] 
**logo_url** | **str, none_type** | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file. | [optional] 
**check_number** | **str, none_type** | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**personal_finance_category_icon_url** | **str** | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | [optional] 
**counterparties** | [**[Counterparty]**](Counterparty.md) | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


