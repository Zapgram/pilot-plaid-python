# ClientProvidedTransactionLocation

A representation of where a transaction took place.  Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the `description` field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The country where the transaction occurred. | [optional] 
**region** | **str** | The region or state where the transaction occurred. | [optional] 
**city** | **str** | The city where the transaction occurred. | [optional] 
**address** | **str** | The street address where the transaction occurred. | [optional] 
**postal_code** | **str** | The postal code where the transaction occurred. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


