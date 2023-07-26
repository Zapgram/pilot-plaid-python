# LinkTokenGetMetadataResponse

An object specifying the arguments originally provided to the `/link/token/create` call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_products** | [**[Products]**](Products.md) | The &#x60;products&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**webhook** | **str, none_type** | The &#x60;webhook&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**country_codes** | [**[CountryCode]**](CountryCode.md) | The &#x60;country_codes&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**language** | **str, none_type** | The &#x60;language&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**redirect_uri** | **str, none_type** | The &#x60;redirect_uri&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**client_name** | **str, none_type** | The &#x60;client_name&#x60; specified in the &#x60;/link/token/create&#x60; call. | 
**institution_data** | [**LinkTokenCreateInstitutionData**](LinkTokenCreateInstitutionData.md) |  | [optional] 
**account_filters** | [**AccountFiltersResponse**](AccountFiltersResponse.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


