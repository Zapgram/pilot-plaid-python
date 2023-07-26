# plaid.model.asset_report_freddie_get_response.AssetReportFreddieGetResponse

AssetReportFreddieGetResponse defines the response schema for `/asset_report/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AssetReportFreddieGetResponse defines the response schema for &#x60;/asset_report/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DEAL** | [**AssetReportFreddie**](AssetReportFreddie.md) | [**AssetReportFreddie**](AssetReportFreddie.md) |  | 
**SchemaVersion** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Verification Of Assets (aka VOA or Freddie Mac Schema) schema version. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

