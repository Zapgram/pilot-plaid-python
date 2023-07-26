# PSLFStatus

Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_eligibility_date** | **date, none_type** | The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 
**payments_made** | **int, none_type** | The number of qualifying payments that have been made. | 
**payments_remaining** | **int, none_type** | The number of qualifying payments remaining. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


