# plaid.model.link_delivery_communication_method.LinkDeliveryCommunicationMethod

The communication method containing both the type and address to send the URL.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The communication method containing both the type and address to send the URL. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**method** | [**LinkDeliveryDeliveryMethod**](LinkDeliveryDeliveryMethod.md) | [**LinkDeliveryDeliveryMethod**](LinkDeliveryDeliveryMethod.md) |  | [optional] 
**address** | str,  | str,  | The phone number / email address that Hosted Link sessions are delivered to. Phone numbers must be in E.164 format. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

