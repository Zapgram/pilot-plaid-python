# plaid.model.application.Application

Metadata about the application

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata about the application | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**city** | None, str,  | NoneClass, str,  | A string representing the city of the client’s headquarters. | 
**logo_url** | None, str,  | NoneClass, str,  | A URL that links to the application logo image. | 
**join_date** | str, date,  | str,  | The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | value must conform to RFC-3339 full-date YYYY-MM-DD
**display_name** | None, str,  | NoneClass, str,  | A human-readable name of the application for display purposes | 
**application_id** | str,  | str,  | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | 
**application_url** | None, str,  | NoneClass, str,  | The URL for the application&#x27;s website | 
**use_case** | None, str,  | NoneClass, str,  | A string representing client’s broad use case as assessed by Plaid. | 
**country_code** | None, str,  | NoneClass, str,  | A string representing the country code of the client’s headquarters. | 
**company_legal_name** | None, str,  | NoneClass, str,  | A string representing the name of client’s legal entity. | 
**reason_for_access** | None, str,  | NoneClass, str,  | A string provided by the connected app stating why they use their respective enabled products. | 
**name** | str,  | str,  | The name of the application | 
**postal_code** | None, str,  | NoneClass, str,  | A string representing the postal code of the client’s headquarters. | 
**region** | None, str,  | NoneClass, str,  | A string representing the region of the client’s headquarters. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

