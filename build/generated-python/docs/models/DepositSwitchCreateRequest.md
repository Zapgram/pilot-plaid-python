# plaid.model.deposit_switch_create_request.DepositSwitchCreateRequest

DepositSwitchCreateRequest defines the request schema for `/deposit_switch/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DepositSwitchCreateRequest defines the request schema for &#x60;/deposit_switch/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**target_access_token** | str,  | str,  | Access token for the target Item, typically provided in the Import Item response.  | 
**target_account_id** | str,  | str,  | Plaid Account ID that specifies the target bank account. This account will become the recipient for a user&#x27;s direct deposit. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**country_code** | None, str,  | NoneClass, str,  | ISO-3166-1 alpha-2 country code standard. | [optional] must be one of ["US", "CA", ] 
**options** | [**DepositSwitchCreateRequestOptions**](DepositSwitchCreateRequestOptions.md) | [**DepositSwitchCreateRequestOptions**](DepositSwitchCreateRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

