# PayrollItemStatus

Details about the status of the payroll item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_status** | **str, none_type** | Denotes the processing status for the verification.  &#x60;UNKNOWN&#x60;: The processing status could not be determined.  &#x60;PROCESSING_COMPLETE&#x60;: The processing has completed and the user has approved for sharing. The data is available to be retrieved.  &#x60;PROCESSING&#x60;: The verification is still processing. The data is not available yet.  &#x60;FAILED&#x60;: The processing failed to complete successfully.  &#x60;APPROVAL_STATUS_PENDING&#x60;: The processing has completed but the user has not yet approved the sharing of the data. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


