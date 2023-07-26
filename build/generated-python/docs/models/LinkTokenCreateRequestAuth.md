# plaid.model.link_token_create_request_auth.LinkTokenCreateRequestAuth

Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**auth_type_select_enabled** | bool,  | BoolClass,  | Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between linking instantly or manually prior to selecting their financial institution. Note that this can only be true if &#x60;same_day_microdeposits_enabled&#x60; is set to true. | [optional] if omitted the server will use the default value of False
**automated_microdeposits_enabled** | bool,  | BoolClass,  | Specifies whether the Link session is enabled for the Automated Micro-deposits flow. | [optional] 
**instant_match_enabled** | bool,  | BoolClass,  | Specifies whether the Link session is enabled for the Instant Match flow. As of November 2022, Instant Match will be enabled by default. Instant Match can be disabled by setting this field to &#x60;false&#x60;. | [optional] 
**same_day_microdeposits_enabled** | bool,  | BoolClass,  | Specifies whether the Link session is enabled for the Same Day Micro-deposits flow. | [optional] 
**reroute_to_credentials** | str,  | str,  | Specifies what type of Reroute to Credentials pane should be used in the Link session for the Same Day Micro-deposits flow. | [optional] must be one of ["OFF", "OPTIONAL", "FORCED", ] 
**flow_type** | str,  | str,  | This field has been deprecated in favor of &#x60;auth_type_select_enabled&#x60;. | [optional] must be one of ["FLEXIBLE_AUTH", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

