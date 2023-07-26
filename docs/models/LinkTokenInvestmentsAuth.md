# plaid.model.link_token_investments_auth.LinkTokenInvestmentsAuth

Configuration parameters for the Investments Auth Product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration parameters for the Investments Auth Product | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**manual_entry_enabled** | None, bool,  | NoneClass, BoolClass,  | If &#x60;true&#x60;, show institutions that use the manual entry fallback flow. | [optional] if omitted the server will use the default value of False
**masked_number_match_enabled** | None, bool,  | NoneClass, BoolClass,  | If &#x60;true&#x60;, show institutions that use the masked number match fallback flow. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

