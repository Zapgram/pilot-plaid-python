# ItemGetResponse

ItemGetResponse defines the response schema for `/item/get` and `/item/webhook/update`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**ItemStatusNullable**](ItemStatusNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


