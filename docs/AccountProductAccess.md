# AccountProductAccess

Allow the application to access specific products on this account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_data** | **bool, none_type** | Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**statements** | **bool, none_type** | Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**tax_documents** | **bool, none_type** | Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


