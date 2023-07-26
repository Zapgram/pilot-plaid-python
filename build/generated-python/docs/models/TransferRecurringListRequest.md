# plaid.model.transfer_recurring_list_request.TransferRecurringListRequest

Defines the request schema for `/transfer/recurring/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/recurring/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_time** | None, str, datetime,  | NoneClass, str,  | The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**end_time** | None, str, datetime,  | NoneClass, str,  | The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of recurring transfers to return. | [optional] if omitted the server will use the default value of 25
**offset** | decimal.Decimal, int,  | decimal.Decimal,  | The number of recurring transfers to skip before returning results. | [optional] if omitted the server will use the default value of 0
**funding_account_id** | None, str,  | NoneClass, str,  | Filter recurring transfers to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

