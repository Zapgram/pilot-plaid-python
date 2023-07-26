# plaid.model.enhancements.Enhancements

A grouping of the Plaid produced transaction enhancement fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A grouping of the Plaid produced transaction enhancement fields. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**category_id** | None, str,  | NoneClass, str,  | The ID of the category to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**payment_channel** | [**PaymentChannel**](PaymentChannel.md) | [**PaymentChannel**](PaymentChannel.md) |  | 
**location** | [**Location**](Location.md) | [**Location**](Location.md) |  | 
**[category](#category)** | list, tuple,  | tuple,  | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**merchant_name** | None, str,  | NoneClass, str,  | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | [optional] 
**website** | None, str,  | NoneClass, str,  | The website associated with this transaction, if available. | [optional] 
**logo_url** | None, str,  | NoneClass, str,  | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file. | [optional] 
**check_number** | None, str,  | NoneClass, str,  | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**personal_finance_category_icon_url** | str,  | str,  | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | [optional] 
**[counterparties](#counterparties)** | list, tuple,  | tuple,  | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# category

A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

