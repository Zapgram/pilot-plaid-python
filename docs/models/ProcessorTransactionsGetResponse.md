# plaid.model.processor_transactions_get_response.ProcessorTransactionsGetResponse

ProcessorTransactionsGetResponse defines the response schema for `/processor/transactions/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ProcessorTransactionsGetResponse defines the response schema for &#x60;/processor/transactions/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) | [**Item**](Item.md) |  | 
**total_transactions** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of transactions available within the date range specified. If &#x60;total_transactions&#x60; is larger than the size of the &#x60;transactions&#x60; array, more transactions are available and can be fetched via manipulating the &#x60;offset&#x60; parameter. | 
**[accounts](#accounts)** | list, tuple,  | tuple,  | An array containing the &#x60;accounts&#x60; associated with the Item for which transactions are being returned. Each transaction can be mapped to its corresponding account via the &#x60;account_id&#x60; field. | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array containing transactions from the account. Transactions are returned in reverse chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned is determined by the &#x60;count&#x60; parameter. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

An array containing the `accounts` associated with the Item for which transactions are being returned. Each transaction can be mapped to its corresponding account via the `account_id` field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array containing the &#x60;accounts&#x60; associated with the Item for which transactions are being returned. Each transaction can be mapped to its corresponding account via the &#x60;account_id&#x60; field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) |  | 

# transactions

An array containing transactions from the account. Transactions are returned in reverse chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned is determined by the `count` parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array containing transactions from the account. Transactions are returned in reverse chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned is determined by the &#x60;count&#x60; parameter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

