# plaid.model.asset_report_item.AssetReportItem

A representation of an Item within an Asset Report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A representation of an Item within an Asset Report. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**[accounts](#accounts)** | list, tuple,  | tuple,  | Data about each of the accounts open on the Item. | 
**institution_name** | str,  | str,  | The full financial institution name associated with the Item. | 
**date_last_updated** | str, datetime,  | str,  | The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | value must conform to RFC-3339 date-time
**institution_id** | str,  | str,  | The id of the financial institution associated with the Item. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

Data about each of the accounts open on the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data about each of the accounts open on the Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountAssets**](AccountAssets.md) | [**AccountAssets**](AccountAssets.md) | [**AccountAssets**](AccountAssets.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

