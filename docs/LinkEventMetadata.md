# LinkEventMetadata

Metadata about an event that occured while the user was going through Link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation. Emitted by: all events. | 
**error_code** | **str** | The error code that the user encountered. Emitted by &#x60;ERROR&#x60;, &#x60;EXIT&#x60;. | [optional] 
**error_message** | **str** | The error message that the user encountered. Emitted by: &#x60;ERROR&#x60;, &#x60;EXIT&#x60;. | [optional] 
**error_type** | **str** | The error type that the user encountered. Emitted by: &#x60;ERROR&#x60;, &#x60;EXIT&#x60;. | [optional] 
**exit_status** | **str** | The status key indicates the point at which the user exited the Link flow. Emitted by: &#x60;EXIT&#x60;. | [optional] 
**institution_id** | **str** | The ID of the selected institution. Emitted by: all events. | [optional] 
**institution_name** | **str** | The name of the selected institution. Emitted by: all events. | [optional] 
**institution_search_query** | **str** | The query used to search for institutions. Emitted by: &#x60;SEARCH_INSTITUTION&#x60;. | [optional] 
**mfa_type** | **str** | If set, the user has encountered one of the following MFA types: code, device, questions, selections. Emitted by: &#x60;SUBMIT_MFA&#x60; and &#x60;TRANSITION_VIEW&#x60; when view_name is &#x60;MFA&#x60;. | [optional] 
**view_name** | **str** | The name of the view that is being transitioned to. Emitted by: &#x60;TRANSITION_VIEW&#x60;. | [optional] 
**selection** | **str** | Either the verification method for a matched institution selected by the user or the Auth Type Select flow type selected by the user. If selection is used to describe selected verification method, then possible values are &#x60;phoneotp&#x60; or &#x60;password&#x60;;  if selection is used to describe the selected Auth Type Select flow, then possible values are &#x60;flow_type_manual&#x60; or &#x60;flow_type_instant&#x60;. Emitted by: &#x60;MATCHED_SELECT_VERIFY_METHOD&#x60; and &#x60;SELECT_AUTH_TYPE&#x60;. | [optional] 
**brand_name** | **str** | The name of the selected brand. | [optional] 
**match_reason** | **str** | The reason this institution was matched, which will be either &#x60;returning_user&#x60; or &#x60;routing_number&#x60;. Emitted by: &#x60;MATCHED_SELECT_INSTITUTION&#x60;. | [optional] 
**routing_number** | **str** | The routing number submitted by user at the micro-deposits routing number pane. Emitted by &#x60;SUBMIT_ROUTING_NUMBER&#x60;. | [optional] 
**account_number_mask** | **str** | The account number mask extracted from the user-provided account number. If the user-inputted account number is four digits long, &#x60;account_number_mask&#x60; is empty. Emitted by &#x60;SUBMIT_ACCOUNT_NUMBER&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


