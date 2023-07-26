# plaid.model.link_delivery_recipient.LinkDeliveryRecipient

Metadata related to the recipient. If the information required to populate this field is not available, leave it blank.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata related to the recipient. If the information required to populate this field is not available, leave it blank. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[communication_methods](#communication_methods)** | list, tuple,  | tuple,  | The list of communication methods to send the Hosted Link session URL to. If delivery is not required, leave this field blank. | [optional] 
**first_name** | str,  | str,  | First name of the recipient. Will be used in the body of the email / text (if configured). If this information is not available, leave this field blank. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# communication_methods

The list of communication methods to send the Hosted Link session URL to. If delivery is not required, leave this field blank.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of communication methods to send the Hosted Link session URL to. If delivery is not required, leave this field blank. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkDeliveryCommunicationMethod**](LinkDeliveryCommunicationMethod.md) | [**LinkDeliveryCommunicationMethod**](LinkDeliveryCommunicationMethod.md) | [**LinkDeliveryCommunicationMethod**](LinkDeliveryCommunicationMethod.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

