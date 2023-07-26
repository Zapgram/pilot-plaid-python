# plaid.model.processor_token_create_request.ProcessorTokenCreateRequest

ProcessorTokenCreateRequest defines the request schema for `/processor/token/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ProcessorTokenCreateRequest defines the request schema for &#x60;/processor/token/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The access token associated with the Item data is being requested for. | 
**account_id** | str,  | str,  | The &#x60;account_id&#x60; value obtained from the &#x60;onSuccess&#x60; callback in Link | 
**processor** | str,  | str,  | The processor you are integrating with. | must be one of ["dwolla", "galileo", "modern_treasury", "ocrolus", "prime_trust", "vesta", "drivewealth", "vopay", "achq", "check", "checkbook", "circle", "sila_money", "rize", "svb_api", "unit", "wyre", "lithic", "alpaca", "astra", "moov", "treasury_prime", "marqeta", "checkout", "solid", "highnote", "gemini", "apex_clearing", "gusto", "adyen", "atomic", "i2c", "wepay", "riskified", "utb", "adp_roll", "fortress_trust", "bond", ] 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

