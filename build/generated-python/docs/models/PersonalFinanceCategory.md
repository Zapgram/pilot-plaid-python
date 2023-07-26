# plaid.model.personal_finance_category.PersonalFinanceCategory

Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.  See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detailed** | str,  | str,  | A granular category conveying the transaction&#x27;s intent. This field can also be used as a unique identifier for the category. | 
**primary** | str,  | str,  | A high level category that communicates the broad category of the transaction. | 
**confidence_level** | None, str,  | NoneClass, str,  | A description of how confident we are that the provided categories accurately describe the transaction intent.  &#x60;very_high&#x60;: We are more than 98% confident that this category reflects the intent of the transaction. &#x60;high&#x60;: We are more than 90% confident that this category reflects the intent of the transaction. &#x60;medium&#x60;: We are moderately confident that this category reflects the intent of the transaction. &#x60;low&#x60;: This category may reflect the intent, but there may be other categories that are more accurate. &#x60;unknown&#x60;: Error | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

