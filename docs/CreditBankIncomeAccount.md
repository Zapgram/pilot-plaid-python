# CreditBankIncomeAccount

The Item's bank accounts that have the selected data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Plaid&#39;s unique identifier for the account. | 
**mask** | **str, none_type** | The last 2-4 alphanumeric characters of an account&#39;s official account number. Note that the mask may be non-unique between an Item&#39;s accounts, and it may also not match the mask that the bank displays to the user. | 
**name** | **str** | The name of the bank account. | 
**official_name** | **str, none_type** | The official name of the bank account. | 
**subtype** | [**DepositoryAccountSubtype**](DepositoryAccountSubtype.md) |  | 
**type** | [**CreditBankIncomeAccountType**](CreditBankIncomeAccountType.md) |  | 
**owners** | [**[Owner]**](Owner.md) | Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


