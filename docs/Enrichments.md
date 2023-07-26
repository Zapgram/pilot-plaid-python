# Enrichments

A grouping of the Plaid produced transaction enrichment fields.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparties** | [**[Counterparty]**](Counterparty.md) | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | 
**location** | [**Location**](Location.md) |  | 
**logo_url** | **str, none_type** | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file. | 
**merchant_name** | **str, none_type** | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | 
**payment_channel** | [**PaymentChannel**](PaymentChannel.md) |  | 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | 
**personal_finance_category_icon_url** | **str** | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | 
**website** | **str, none_type** | The website associated with this transaction. | 
**check_number** | **str, none_type** | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**entity_id** | **str, none_type** | A unique, stable, Plaid-generated id that maps to the primary counterparty. | [optional] 
**legacy_category_id** | **str, none_type** | The ID of the legacy category to which this transaction belongs. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the &#x60;personal_finance_category&#x60; for transaction categorization to obtain the best results. | [optional] 
**legacy_category** | **[str]** | A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the &#x60;personal_finance_category&#x60; for transaction categorization to obtain the best results. | [optional] 
**recurrence** | [**Recurrence**](Recurrence.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


