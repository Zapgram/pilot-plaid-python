# plaid.model.institutions_get_request.InstitutionsGetRequest

InstitutionsGetRequest defines the request schema for `/institutions/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | InstitutionsGetRequest defines the request schema for &#x60;/institutions/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**offset** | decimal.Decimal, int,  | decimal.Decimal,  | The number of Institutions to skip. | 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of Institutions to return. | 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard.  In API versions 2019-05-29 and earlier, the &#x60;country_codes&#x60; parameter is an optional parameter within the &#x60;options&#x60; object and will default to &#x60;[US]&#x60; if it is not supplied.  | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**InstitutionsGetRequestOptions**](InstitutionsGetRequestOptions.md) | [**InstitutionsGetRequestOptions**](InstitutionsGetRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# country_codes

Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard.  In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard.  In API versions 2019-05-29 and earlier, the &#x60;country_codes&#x60; parameter is an optional parameter within the &#x60;options&#x60; object and will default to &#x60;[US]&#x60; if it is not supplied.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

