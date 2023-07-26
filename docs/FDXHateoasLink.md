# FDXHateoasLink

REST application constraint (Hypermedia As The Engine Of Application State)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to invoke the action on the resource | 
**action** | [**FDXHateoasLinkAction**](FDXHateoasLinkAction.md) |  | [optional] 
**rel** | **str** | Relation of this link to its containing entity, as defined by and with many example relation values at [IETF RFC5988](https://datatracker.ietf.org/doc/html/rfc5988) | [optional] 
**types** | [**[FDXContentTypes]**](FDXContentTypes.md) | Content-types that can be used in the Accept header | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


