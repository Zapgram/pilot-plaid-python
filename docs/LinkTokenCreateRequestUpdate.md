# LinkTokenCreateRequestUpdate

Specifies options for initializing Link for [update mode](https://plaid.com/docs/link/update-mode).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_selection_enabled** | **bool** | If &#x60;true&#x60;, enables [update mode with Account Select](https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts) for institutions that do not use OAuth, or that use OAuth but do not have their own account selection flow. For institutions that have an OAuth account selection flow (i.e. most OAuth-enabled institutions), update mode with Account Select will always be enabled, regardless of the value of this field. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


