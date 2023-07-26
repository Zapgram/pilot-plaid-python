# plaid.model.transfer_authorization_device.TransferAuthorizationDevice

Information about the device being used to initiate the authorization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the device being used to initiate the authorization. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip_address** | str,  | str,  | The IP address of the device being used to initiate the authorization. Required when the end-user is present at authorization create time. | [optional] 
**user_agent** | str,  | str,  | The user agent of the device being used to initiate the authorization. Required when the end-user is present at authorization create time. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

