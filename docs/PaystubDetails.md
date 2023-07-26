# PaystubDetails

An object representing details that can be found on the paystub.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_period_start_date** | **date, none_type** | Beginning date of the pay period on the paystub in the &#39;YYYY-MM-DD&#39; format. | [optional] 
**pay_period_end_date** | **date, none_type** | Ending date of the pay period on the paystub in the &#39;YYYY-MM-DD&#39; format. | [optional] 
**pay_date** | **date, none_type** | Pay date on the paystub in the &#39;YYYY-MM-DD&#39; format. | [optional] 
**paystub_provider** | **str, none_type** | The name of the payroll provider that generated the paystub, e.g. ADP | [optional] 
**pay_frequency** | [**PaystubPayFrequency**](PaystubPayFrequency.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


