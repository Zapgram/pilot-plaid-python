# plaid.model.deposit_switch_token_create_response.DepositSwitchTokenCreateResponse

DepositSwitchTokenCreateResponse defines the response schema for `/deposit_switch/token/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DepositSwitchTokenCreateResponse defines the response schema for &#x60;/deposit_switch/token/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deposit_switch_token** | str,  | str,  | Deposit switch token, used to initialize Link for the Deposit Switch product | 
**deposit_switch_token_expiration_time** | str,  | str,  | Expiration time of the token, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

