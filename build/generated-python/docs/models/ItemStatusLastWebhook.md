# plaid.model.item_status_last_webhook.ItemStatusLastWebhook

Information about the last webhook fired for the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Information about the last webhook fired for the Item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent_at** | None, str, datetime,  | NoneClass, str,  | [ISO 8601](https://wikipedia.org/wiki/ISO_8601) timestamp of when the webhook was fired.  | [optional] value must conform to RFC-3339 date-time
**code_sent** | None, str,  | NoneClass, str,  | The last webhook code sent. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

