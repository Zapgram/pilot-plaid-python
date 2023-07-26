# plaid.model.fdx_hateoas_link.FDXHateoasLink

REST application constraint (Hypermedia As The Engine Of Application State)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | REST application constraint (Hypermedia As The Engine Of Application State) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | str,  | str,  | URL to invoke the action on the resource | 
**action** | [**FDXHateoasLinkAction**](FDXHateoasLinkAction.md) | [**FDXHateoasLinkAction**](FDXHateoasLinkAction.md) |  | [optional] 
**rel** | str,  | str,  | Relation of this link to its containing entity, as defined by and with many example relation values at [IETF RFC5988](https://datatracker.ietf.org/doc/html/rfc5988) | [optional] 
**[types](#types)** | list, tuple,  | tuple,  | Content-types that can be used in the Accept header | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# types

Content-types that can be used in the Accept header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Content-types that can be used in the Accept header | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FDXContentTypes**](FDXContentTypes.md) | [**FDXContentTypes**](FDXContentTypes.md) | [**FDXContentTypes**](FDXContentTypes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

