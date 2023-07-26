# plaid.model.institutions_search_request_options.InstitutionsSearchRequestOptions

An optional object to filter `/institutions/search` results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/institutions/search&#x60; results. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oauth** | None, bool,  | NoneClass, BoolClass,  | Limit results to institutions with or without OAuth login flows. Note that institutions will have &#x60;oauth&#x60; set to &#x60;true&#x60; if some Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth will have the &#x60;oauth&#x60; attribute set to &#x60;true&#x60;. | [optional] 
**include_optional_metadata** | bool,  | BoolClass,  | When true, return the institution&#x27;s homepage URL, logo and primary brand color. | [optional] 
**include_auth_metadata** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional] if omitted the server will use the default value of False
**include_payment_initiation_metadata** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional] if omitted the server will use the default value of False
**payment_initiation** | [**InstitutionsSearchPaymentInitiationOptions**](InstitutionsSearchPaymentInitiationOptions.md) | [**InstitutionsSearchPaymentInitiationOptions**](InstitutionsSearchPaymentInitiationOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

