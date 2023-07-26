# AssetReport

An object representing an Asset Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_report_id** | **str** | A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive. | 
**client_report_id** | **str, none_type** | An identifier you determine and submit for the Asset Report. | 
**date_generated** | **datetime** | The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | 
**days_requested** | **float** | The duration of transaction history you requested | 
**user** | [**AssetReportUser**](AssetReportUser.md) |  | 
**items** | [**[AssetReportItem]**](AssetReportItem.md) | Data returned by Plaid about each of the Items included in the Asset Report. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


