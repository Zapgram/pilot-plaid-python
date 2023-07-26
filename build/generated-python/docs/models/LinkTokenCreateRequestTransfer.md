# plaid.model.link_token_create_request_transfer.LinkTokenCreateRequestTransfer

Specifies options for initializing Link for use with the Transfer product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with the Transfer product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**intent_id** | str,  | str,  | The &#x60;id&#x60; returned by the &#x60;/transfer/intent/create&#x60; endpoint. | [optional] 
**payment_profile_token** | str,  | str,  | The &#x60;payment_profile_token&#x60; returned by the &#x60;/payment_profile/create&#x60; endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

