# plaid.model.asset_report.AssetReport

An object representing an Asset Report

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing an Asset Report | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date_generated** | str, datetime,  | str,  | The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | value must conform to RFC-3339 date-time
**client_report_id** | None, str,  | NoneClass, str,  | An identifier you determine and submit for the Asset Report. | 
**[items](#items)** | list, tuple,  | tuple,  | Data returned by Plaid about each of the Items included in the Asset Report. | 
**user** | [**AssetReportUser**](AssetReportUser.md) | [**AssetReportUser**](AssetReportUser.md) |  | 
**asset_report_id** | str,  | str,  | A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive. | 
**days_requested** | decimal.Decimal, int, float,  | decimal.Decimal,  | The duration of transaction history you requested | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Data returned by Plaid about each of the Items included in the Asset Report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data returned by Plaid about each of the Items included in the Asset Report. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetReportItem**](AssetReportItem.md) | [**AssetReportItem**](AssetReportItem.md) | [**AssetReportItem**](AssetReportItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

