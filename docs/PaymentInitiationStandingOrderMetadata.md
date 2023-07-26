# PaymentInitiationStandingOrderMetadata

Metadata specifically related to valid Payment Initiation standing order configurations for the institution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_standing_order_end_date** | **bool** | Indicates whether the institution supports closed-ended standing orders by providing an end date. | 
**supports_standing_order_negative_execution_days** | **bool** | This is only applicable to &#x60;MONTHLY&#x60; standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a &#x60;MONTHLY&#x60; standing order relative to the end of the month. | 
**valid_standing_order_intervals** | [**[PaymentScheduleInterval]**](PaymentScheduleInterval.md) | A list of the valid standing order intervals supported by the institution. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


