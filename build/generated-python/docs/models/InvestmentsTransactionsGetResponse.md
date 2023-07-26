# plaid.model.investments_transactions_get_response.InvestmentsTransactionsGetResponse

InvestmentsTransactionsGetResponse defines the response schema for `/investments/transactions/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | InvestmentsTransactionsGetResponse defines the response schema for &#x60;/investments/transactions/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) | [**Item**](Item.md) |  | 
**[accounts](#accounts)** | list, tuple,  | tuple,  | The accounts for which transaction history is being fetched. | 
**[investment_transactions](#investment_transactions)** | list, tuple,  | tuple,  | The transactions being fetched | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**total_investment_transactions** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of transactions available within the date range specified. If &#x60;total_investment_transactions&#x60; is larger than the size of the &#x60;transactions&#x60; array, more transactions are available and can be fetched via manipulating the &#x60;offset&#x60; parameter. | 
**[securities](#securities)** | list, tuple,  | tuple,  | All securities for which there is a corresponding transaction being fetched. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

The accounts for which transaction history is being fetched.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The accounts for which transaction history is being fetched. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) |  | 

# securities

All securities for which there is a corresponding transaction being fetched.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | All securities for which there is a corresponding transaction being fetched. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Security**](Security.md) | [**Security**](Security.md) | [**Security**](Security.md) |  | 

# investment_transactions

The transactions being fetched

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The transactions being fetched | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InvestmentTransaction**](InvestmentTransaction.md) | [**InvestmentTransaction**](InvestmentTransaction.md) | [**InvestmentTransaction**](InvestmentTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

