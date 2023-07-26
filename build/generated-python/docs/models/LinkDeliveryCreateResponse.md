# plaid.model.link_delivery_create_response.LinkDeliveryCreateResponse

LinkDeliveryCreateResponse defines the response schema for `/link_delivery/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LinkDeliveryCreateResponse defines the response schema for &#x60;/link_delivery/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**link_delivery_session_id** | str,  | str,  | The ID for the Hosted Link session. Same as the &#x60;link_token&#x60; string excluding the \&quot;link-{env}-\&quot; prefix. | 
**link_delivery_url** | str,  | str,  | The URL to the Hosted Link session, which will be delivered by the specified delivery method. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

