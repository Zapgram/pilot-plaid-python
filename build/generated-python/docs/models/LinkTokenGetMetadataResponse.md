# plaid.model.link_token_get_metadata_response.LinkTokenGetMetadataResponse

An object specifying the arguments originally provided to the `/link/token/create` call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying the arguments originally provided to the &#x60;/link/token/create&#x60; call. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhook** | None, str,  | NoneClass, str,  | The &#x60;webhook&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | The &#x60;country_codes&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**language** | None, str,  | NoneClass, str,  | The &#x60;language&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**redirect_uri** | None, str,  | NoneClass, str,  | The &#x60;redirect_uri&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**[initial_products](#initial_products)** | list, tuple,  | tuple,  | The &#x60;products&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**client_name** | None, str,  | NoneClass, str,  | The &#x60;client_name&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**institution_data** | [**LinkTokenCreateInstitutionData**](LinkTokenCreateInstitutionData.md) | [**LinkTokenCreateInstitutionData**](LinkTokenCreateInstitutionData.md) |  | [optional] 
**account_filters** | [**AccountFiltersResponse**](AccountFiltersResponse.md) | [**AccountFiltersResponse**](AccountFiltersResponse.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# initial_products

The `products` specified in the `/link/token/create` call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The &#x60;products&#x60; specified in the &#x60;/link/token/create&#x60; call. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Products**](Products.md) | [**Products**](Products.md) | [**Products**](Products.md) |  | 

# country_codes

The `country_codes` specified in the `/link/token/create` call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The &#x60;country_codes&#x60; specified in the &#x60;/link/token/create&#x60; call. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

