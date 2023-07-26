# plaid.model.transfer_expected_sweep_settlement_schedule_item.TransferExpectedSweepSettlementScheduleItem

Defines an expected sweep date and amount.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines an expected sweep date and amount. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sweep_settlement_date** | str, date,  | str,  | The settlement date of a sweep for this transfer. | value must conform to RFC-3339 full-date YYYY-MM-DD
**swept_settled_amount** | str,  | str,  | The accumulated amount that has been swept by &#x60;sweep_settlement_date&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

