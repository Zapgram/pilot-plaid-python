# SignalUser

Details about the end user initiating the transaction (i.e., the account holder).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**SignalPersonName**](SignalPersonName.md) |  | [optional] 
**phone_number** | **str, none_type** | The user&#39;s phone number, in E.164 format: +{countrycode}{number}. For example: \&quot;+14151234567\&quot; | [optional] 
**email_address** | **str, none_type** | The user&#39;s email address. | [optional] 
**address** | [**SignalAddressData**](SignalAddressData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


