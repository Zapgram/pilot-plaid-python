# ConnectedApplication

Describes the connected application for a particular end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | 
**name** | **str** | The name of the application | 
**created_at** | **date** | The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | 
**display_name** | **str, none_type** | A human-readable name of the application for display purposes | [optional] 
**logo_url** | **str, none_type** | A URL that links to the application logo image. | [optional] 
**application_url** | **str, none_type** | The URL for the application&#39;s website | [optional] 
**reason_for_access** | **str, none_type** | A string provided by the connected app stating why they use their respective enabled products. | [optional] 
**scopes** | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


