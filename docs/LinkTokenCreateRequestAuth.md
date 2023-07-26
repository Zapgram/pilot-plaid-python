# LinkTokenCreateRequestAuth

Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type_select_enabled** | **bool** | Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between linking instantly or manually prior to selecting their financial institution. Note that this can only be true if &#x60;same_day_microdeposits_enabled&#x60; is set to true. | [optional]  if omitted the server will use the default value of False
**automated_microdeposits_enabled** | **bool** | Specifies whether the Link session is enabled for the Automated Micro-deposits flow. | [optional] 
**instant_match_enabled** | **bool** | Specifies whether the Link session is enabled for the Instant Match flow. As of November 2022, Instant Match will be enabled by default. Instant Match can be disabled by setting this field to &#x60;false&#x60;. | [optional] 
**same_day_microdeposits_enabled** | **bool** | Specifies whether the Link session is enabled for the Same Day Micro-deposits flow. | [optional] 
**reroute_to_credentials** | **str** | Specifies what type of Reroute to Credentials pane should be used in the Link session for the Same Day Micro-deposits flow. | [optional] 
**flow_type** | **str** | This field has been deprecated in favor of &#x60;auth_type_select_enabled&#x60;. | [optional]  if omitted the server will use the default value of "FLEXIBLE_AUTH"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


