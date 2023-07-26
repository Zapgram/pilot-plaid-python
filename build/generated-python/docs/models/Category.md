# plaid.model.category.Category

Information describing a transaction category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information describing a transaction category | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**category_id** | str,  | str,  | An identifying number for the category. &#x60;category_id&#x60; is a Plaid-specific identifier and does not necessarily correspond to merchant category codes. | 
**[hierarchy](#hierarchy)** | list, tuple,  | tuple,  | A hierarchical array of the categories to which this &#x60;category_id&#x60; belongs. | 
**group** | str,  | str,  | &#x60;place&#x60; for physical transactions or &#x60;special&#x60; for other transactions such as bank charges. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hierarchy

A hierarchical array of the categories to which this `category_id` belongs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A hierarchical array of the categories to which this &#x60;category_id&#x60; belongs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

