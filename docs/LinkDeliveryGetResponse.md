# LinkDeliveryGetResponse

LinkDeliveryGetRequest defines the response schema for `/link_delivery/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LinkDeliverySessionStatus**](LinkDeliverySessionStatus.md) |  | 
**created_at** | **datetime** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Hosted Link session was created at. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**completed_at** | **datetime, none_type** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Hosted Link session was completed at. | [optional] 
**access_tokens** | **[str], none_type** | An array of access tokens associated with the Hosted Link session. | [optional] 
**item_ids** | **[str], none_type** | An array of &#x60;item_id&#x60;s associated with the Hosted Link session. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


