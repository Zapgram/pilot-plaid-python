# AssetReportGetResponse

AssetReportGetResponse defines the response schema for `/asset_report/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**AssetReport**](AssetReport.md) |  | 
**warnings** | [**[Warning]**](Warning.md) | If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


