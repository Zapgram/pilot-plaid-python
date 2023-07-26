# IdentityVerificationUserAddress

Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str, none_type** | The primary street portion of an address. If the user has submitted their address, this field will always be filled. | 
**street2** | **str, none_type** | Extra street information, like an apartment or suite number. | 
**city** | **str, none_type** | City from the end user&#39;s address | 
**region** | **str, none_type** | An ISO 3166-2 subdivision code. Related terms would be \&quot;state\&quot;, \&quot;province\&quot;, \&quot;prefecture\&quot;, \&quot;zone\&quot;, \&quot;subdivision\&quot;, etc. | 
**postal_code** | **str, none_type** | The postal code for the associated address. Between 2 and 10 alphanumeric characters. For US-based addresses this must be 5 numeric digits. | 
**country** | [**GenericCountryCode**](GenericCountryCode.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


