# plaid.model.payment_initiation_standing_order_metadata.PaymentInitiationStandingOrderMetadata

Metadata specifically related to valid Payment Initiation standing order configurations for the institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata specifically related to valid Payment Initiation standing order configurations for the institution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**supports_standing_order_negative_execution_days** | bool,  | BoolClass,  | This is only applicable to &#x60;MONTHLY&#x60; standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a &#x60;MONTHLY&#x60; standing order relative to the end of the month. | 
**supports_standing_order_end_date** | bool,  | BoolClass,  | Indicates whether the institution supports closed-ended standing orders by providing an end date. | 
**[valid_standing_order_intervals](#valid_standing_order_intervals)** | list, tuple,  | tuple,  | A list of the valid standing order intervals supported by the institution. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# valid_standing_order_intervals

A list of the valid standing order intervals supported by the institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of the valid standing order intervals supported by the institution. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentScheduleInterval**](PaymentScheduleInterval.md) | [**PaymentScheduleInterval**](PaymentScheduleInterval.md) | [**PaymentScheduleInterval**](PaymentScheduleInterval.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

