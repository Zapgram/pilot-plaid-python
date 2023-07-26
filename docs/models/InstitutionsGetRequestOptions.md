# plaid.model.institutions_get_request_options.InstitutionsGetRequestOptions

An optional object to filter `/institutions/get` results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/institutions/get&#x60; results. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[products](#products)** | list, tuple, None,  | tuple, NoneClass,  | Filter the Institutions based on which products they support.  | [optional] 
**[routing_numbers](#routing_numbers)** | list, tuple, None,  | tuple, NoneClass,  | Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid. | [optional] 
**oauth** | None, bool,  | NoneClass, BoolClass,  | Limit results to institutions with or without OAuth login flows. Note that institutions will have &#x60;oauth&#x60; set to &#x60;true&#x60; if some Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth will have the &#x60;oauth&#x60; attribute set to &#x60;true&#x60;. | [optional] 
**include_optional_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, return the institution&#x27;s homepage URL, logo and primary brand color.  Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos. | [optional] 
**include_auth_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional] if omitted the server will use the default value of False
**include_payment_initiation_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

Filter the Institutions based on which products they support. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Filter the Institutions based on which products they support.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Products**](Products.md) | [**Products**](Products.md) | [**Products**](Products.md) |  | 

# routing_numbers

Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

