# plaid.model.credit_bank_income_account.CreditBankIncomeAccount

The Item's bank accounts that have the selected data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Item&#x27;s bank accounts that have the selected data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**official_name** | None, str,  | NoneClass, str,  | The official name of the bank account. | 
**account_id** | str,  | str,  | Plaid&#x27;s unique identifier for the account. | 
**subtype** | [**DepositoryAccountSubtype**](DepositoryAccountSubtype.md) | [**DepositoryAccountSubtype**](DepositoryAccountSubtype.md) |  | 
**name** | str,  | str,  | The name of the bank account. | 
**[owners](#owners)** | list, tuple,  | tuple,  | Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array. | 
**type** | [**CreditBankIncomeAccountType**](CreditBankIncomeAccountType.md) | [**CreditBankIncomeAccountType**](CreditBankIncomeAccountType.md) |  | 
**mask** | None, str,  | NoneClass, str,  | The last 2-4 alphanumeric characters of an account&#x27;s official account number. Note that the mask may be non-unique between an Item&#x27;s accounts, and it may also not match the mask that the bank displays to the user. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# owners

Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Owner**](Owner.md) | [**Owner**](Owner.md) | [**Owner**](Owner.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

