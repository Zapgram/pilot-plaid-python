# NumbersACATS

Identifying information for transferring holdings to an investments account via ACATS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Plaid account ID associated with the account numbers | 
**account** | **str** | The full account number for the account | 
**dtc_numbers** | **[str]** | Identifiers for the clearinghouses that are assocciated with the account in order of relevance. This array will be empty if we can&#39;t provide any account level data. Institution level data can be retrieved from the institutions/get endpoints. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


