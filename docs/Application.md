# Application

Metadata about the application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | 
**name** | **str** | The name of the application | 
**display_name** | **str, none_type** | A human-readable name of the application for display purposes | 
**join_date** | **date** | The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | 
**logo_url** | **str, none_type** | A URL that links to the application logo image. | 
**application_url** | **str, none_type** | The URL for the application&#39;s website | 
**reason_for_access** | **str, none_type** | A string provided by the connected app stating why they use their respective enabled products. | 
**use_case** | **str, none_type** | A string representing client’s broad use case as assessed by Plaid. | 
**company_legal_name** | **str, none_type** | A string representing the name of client’s legal entity. | 
**city** | **str, none_type** | A string representing the city of the client’s headquarters. | 
**region** | **str, none_type** | A string representing the region of the client’s headquarters. | 
**postal_code** | **str, none_type** | A string representing the postal code of the client’s headquarters. | 
**country_code** | **str, none_type** | A string representing the country code of the client’s headquarters. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


