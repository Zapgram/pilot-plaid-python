# SignalWarning

Conveys information about the errors causing missing or stale bank data used to construct the /signal/evaluate scores and response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning_type** | **str** | A broad categorization of the warning. Safe for programmatic use. | [optional] 
**warning_code** | **str** | The warning code identifies a specific kind of warning that pertains to the error causing bank data to be missing. Safe for programmatic use. For more details on warning codes, please refer to Plaid standard error codes documentation. In case you receive the &#x60;ITEM_LOGIN_REQUIRED&#x60; warning, we recommend re-authenticating your user by implementing Link&#39;s update mode. This will guide your user to fix their credentials, allowing Plaid to start fetching data again for future Signal requests. | [optional] 
**warning_message** | **str** | A developer-friendly representation of the warning type. This may change over time and is not safe for programmatic use. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


