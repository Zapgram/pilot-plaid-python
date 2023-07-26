# plaid.model.transfer_sweep_list_request.TransferSweepListRequest

Defines the request schema for `/transfer/sweep/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/sweep/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_date** | None, str, datetime,  | NoneClass, str,  | The start datetime of sweeps to return (RFC 3339 format). | [optional] value must conform to RFC-3339 date-time
**end_date** | None, str, datetime,  | NoneClass, str,  | The end datetime of sweeps to return (RFC 3339 format). | [optional] value must conform to RFC-3339 date-time
**count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum number of sweeps to return. | [optional] if omitted the server will use the default value of 25
**offset** | decimal.Decimal, int,  | decimal.Decimal,  | The number of sweeps to skip before returning results. | [optional] if omitted the server will use the default value of 0
**amount** | None, str,  | NoneClass, str,  | Filter sweeps to only those with the specified amount. | [optional] 
**status** | [**SweepStatus**](SweepStatus.md) | [**SweepStatus**](SweepStatus.md) |  | [optional] 
**originator_client_id** | None, str,  | NoneClass, str,  | Filter sweeps to only those with the specified originator client. | [optional] 
**funding_account_id** | None, str,  | NoneClass, str,  | Filter sweeps to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**transfer_id** | None, str,  | NoneClass, str,  | Filter sweeps to only those with the included &#x60;transfer_id&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

