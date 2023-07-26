# CreditEmploymentVerification

The object containing proof of employment data for an individual.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | ID of the payroll provider account. | 
**status** | **str, none_type** | Current employment status. | 
**start_date** | **date, none_type** | Start of employment in ISO 8601 format (YYYY-MM-DD). | 
**end_date** | **date, none_type** | End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD). | 
**employer** | [**CreditEmployerVerification**](CreditEmployerVerification.md) |  | 
**title** | **str, none_type** | Current title of employee. | 
**platform_ids** | [**CreditPlatformIds**](CreditPlatformIds.md) |  | 
**employee_type** | **str, none_type** | The type of employment for the individual. &#x60;\&quot;FULL_TIME\&quot;&#x60;: A full-time employee. &#x60;\&quot;PART_TIME\&quot;&#x60;: A part-time employee. &#x60;\&quot;CONTRACTOR\&quot;&#x60;: An employee typically hired externally through a contracting group. &#x60;\&quot;TEMPORARY\&quot;&#x60;: A temporary employee. &#x60;\&quot;OTHER\&quot;&#x60;: The employee type is not one of the above defined types. | 
**last_paystub_date** | **date, none_type** | The date of the employee&#39;s most recent paystub in ISO 8601 format (YYYY-MM-DD). | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


