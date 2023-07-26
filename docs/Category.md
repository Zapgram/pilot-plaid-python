# Category

Information describing a transaction category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | An identifying number for the category. &#x60;category_id&#x60; is a Plaid-specific identifier and does not necessarily correspond to merchant category codes. | 
**group** | **str** | &#x60;place&#x60; for physical transactions or &#x60;special&#x60; for other transactions such as bank charges. | 
**hierarchy** | **[str]** | A hierarchical array of the categories to which this &#x60;category_id&#x60; belongs. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


