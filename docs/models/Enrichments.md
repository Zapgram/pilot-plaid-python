# plaid.model.enrichments.Enrichments

A grouping of the Plaid produced transaction enrichment fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A grouping of the Plaid produced transaction enrichment fields. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**personal_finance_category_icon_url** | str,  | str,  | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | 
**website** | None, str,  | NoneClass, str,  | The website associated with this transaction. | 
**logo_url** | None, str,  | NoneClass, str,  | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file. | 
**payment_channel** | [**PaymentChannel**](PaymentChannel.md) | [**PaymentChannel**](PaymentChannel.md) |  | 
**merchant_name** | None, str,  | NoneClass, str,  | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | 
**location** | [**Location**](Location.md) | [**Location**](Location.md) |  | 
**[counterparties](#counterparties)** | list, tuple,  | tuple,  | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | 
**check_number** | None, str,  | NoneClass, str,  | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**entity_id** | None, str,  | NoneClass, str,  | A unique, stable, Plaid-generated id that maps to the primary counterparty. | [optional] 
**legacy_category_id** | None, str,  | NoneClass, str,  | The ID of the legacy category to which this transaction belongs. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the &#x60;personal_finance_category&#x60; for transaction categorization to obtain the best results. | [optional] 
**[legacy_category](#legacy_category)** | list, tuple,  | tuple,  | A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the &#x60;personal_finance_category&#x60; for transaction categorization to obtain the best results. | [optional] 
**recurrence** | [**Recurrence**](Recurrence.md) | [**Recurrence**](Recurrence.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# counterparties

The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Counterparty**](Counterparty.md) | [**Counterparty**](Counterparty.md) | [**Counterparty**](Counterparty.md) |  | 

# legacy_category

A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the `personal_finance_category` for transaction categorization to obtain the best results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the &#x60;personal_finance_category&#x60; for transaction categorization to obtain the best results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

