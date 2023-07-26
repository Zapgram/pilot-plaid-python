# CreditCategory

Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such use cases. Please reach out to your account manager or sales representative if you would like to receive this field.  See the [`taxonomy csv file`](https://plaid.com/documents/credit-category-taxonomy.csv) for a full list of credit categories.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | A high level category that communicates the broad category of the transaction. | 
**detailed** | **str** | A granular category conveying the transaction&#39;s intent. This field can also be used as a unique identifier for the category. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


