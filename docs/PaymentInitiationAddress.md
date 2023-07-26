# PaymentInitiationAddress

The optional address of the payment recipient's bank account. Required by most institutions outside of the UK.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **[str]** | An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters. | 
**city** | **str** | The city where the recipient is located. Maximum of 35 characters. | 
**postal_code** | **str** | The postal code where the recipient is located. Maximum of 16 characters. | 
**country** | **str** | The ISO 3166-1 alpha-2 country code where the recipient is located. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


