# plaid.model.transfer_originator_diligence.TransferOriginatorDiligence

The diligence information for the originator.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The diligence information for the originator. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**naics_code** | str,  | str,  | The NAICS code of the originator. | 
**dba** | str,  | str,  | The business name of the originator. | 
**website** | str,  | str,  | The website of the originator. | 
**address** | [**TransferOriginatorAddress**](TransferOriginatorAddress.md) | [**TransferOriginatorAddress**](TransferOriginatorAddress.md) |  | 
**tax_id** | str,  | str,  | The tax ID of the originator. | 
**credit_usage_configuration** | [**TransferCreditUsageConfiguration**](TransferCreditUsageConfiguration.md) | [**TransferCreditUsageConfiguration**](TransferCreditUsageConfiguration.md) |  | [optional] 
**debit_usage_configuration** | [**TransferDebitUsageConfiguration**](TransferDebitUsageConfiguration.md) | [**TransferDebitUsageConfiguration**](TransferDebitUsageConfiguration.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

