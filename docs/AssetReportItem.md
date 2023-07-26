# AssetReportItem

A representation of an Item within an Asset Report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**institution_name** | **str** | The full financial institution name associated with the Item. | 
**institution_id** | **str** | The id of the financial institution associated with the Item. | 
**date_last_updated** | **datetime** | The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**accounts** | [**[AccountAssets]**](AccountAssets.md) | Data about each of the accounts open on the Item. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


