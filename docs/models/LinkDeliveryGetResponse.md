# plaid.model.link_delivery_get_response.LinkDeliveryGetResponse

LinkDeliveryGetRequest defines the response schema for `/link_delivery/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LinkDeliveryGetRequest defines the response schema for &#x60;/link_delivery/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Hosted Link session was created at. | value must conform to RFC-3339 date-time
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**LinkDeliverySessionStatus**](LinkDeliverySessionStatus.md) | [**LinkDeliverySessionStatus**](LinkDeliverySessionStatus.md) |  | 
**completed_at** | None, str, datetime,  | NoneClass, str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Hosted Link session was completed at. | [optional] value must conform to RFC-3339 date-time
**[access_tokens](#access_tokens)** | list, tuple, None,  | tuple, NoneClass,  | An array of access tokens associated with the Hosted Link session. | [optional] 
**[item_ids](#item_ids)** | list, tuple, None,  | tuple, NoneClass,  | An array of &#x60;item_id&#x60;s associated with the Hosted Link session. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# access_tokens

An array of access tokens associated with the Hosted Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | An array of access tokens associated with the Hosted Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The access token associated with the Item data is being requested for. | 

# item_ids

An array of `item_id`s associated with the Hosted Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | An array of &#x60;item_id&#x60;s associated with the Hosted Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

