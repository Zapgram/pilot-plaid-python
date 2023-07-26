# plaid.model.investments_holdings_get_response.InvestmentsHoldingsGetResponse

InvestmentsHoldingsGetResponse defines the response schema for `/investments/holdings/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | InvestmentsHoldingsGetResponse defines the response schema for &#x60;/investments/holdings/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) | [**Item**](Item.md) |  | 
**[accounts](#accounts)** | list, tuple,  | tuple,  | The accounts associated with the Item | 
**[holdings](#holdings)** | list, tuple,  | tuple,  | The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the &#x60;securities&#x60; field.  | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**[securities](#securities)** | list, tuple,  | tuple,  | Objects describing the securities held in the accounts associated with the Item.  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

The accounts associated with the Item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The accounts associated with the Item | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) |  | 

# holdings

The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the &#x60;securities&#x60; field.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Holding**](Holding.md) | [**Holding**](Holding.md) | [**Holding**](Holding.md) |  | 

# securities

Objects describing the securities held in the accounts associated with the Item. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Objects describing the securities held in the accounts associated with the Item.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Security**](Security.md) | [**Security**](Security.md) | [**Security**](Security.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

