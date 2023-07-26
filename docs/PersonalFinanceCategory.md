# PersonalFinanceCategory

Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.  See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | A high level category that communicates the broad category of the transaction. | 
**detailed** | **str** | A granular category conveying the transaction&#39;s intent. This field can also be used as a unique identifier for the category. | 
**confidence_level** | **str, none_type** | A description of how confident we are that the provided categories accurately describe the transaction intent.  &#x60;very_high&#x60;: We are more than 98% confident that this category reflects the intent of the transaction. &#x60;high&#x60;: We are more than 90% confident that this category reflects the intent of the transaction. &#x60;medium&#x60;: We are moderately confident that this category reflects the intent of the transaction. &#x60;low&#x60;: This category may reflect the intent, but there may be other categories that are more accurate. &#x60;unknown&#x60;: Error | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


