# plaid.model.institutions_search_request.InstitutionsSearchRequest

InstitutionsSearchRequest defines the request schema for `/institutions/search`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | InstitutionsSearchRequest defines the request schema for &#x60;/institutions/search&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**query** | str,  | str,  | The search query. Institutions with names matching the query are returned | 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the &#x60;country_codes&#x60; parameter is an optional parameter within the &#x60;options&#x60; object and will default to &#x60;[US]&#x60; if it is not supplied.  | 
**[products](#products)** | list, tuple, None,  | tuple, NoneClass,  | Filter the Institutions based on whether they support all products listed in &#x60;products&#x60;. Provide &#x60;null&#x60; to get institutions regardless of supported products. Note that when &#x60;auth&#x60; is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if &#x60;auth&#x60; is not present in their product array. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**InstitutionsSearchRequestOptions**](InstitutionsSearchRequestOptions.md) | [**InstitutionsSearchRequestOptions**](InstitutionsSearchRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

Filter the Institutions based on whether they support all products listed in `products`. Provide `null` to get institutions regardless of supported products. Note that when `auth` is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if `auth` is not present in their product array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Filter the Institutions based on whether they support all products listed in &#x60;products&#x60;. Provide &#x60;null&#x60; to get institutions regardless of supported products. Note that when &#x60;auth&#x60; is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if &#x60;auth&#x60; is not present in their product array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Products**](Products.md) | [**Products**](Products.md) | [**Products**](Products.md) |  | 

# country_codes

Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the &#x60;country_codes&#x60; parameter is an optional parameter within the &#x60;options&#x60; object and will default to &#x60;[US]&#x60; if it is not supplied.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

