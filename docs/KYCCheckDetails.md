# KYCCheckDetails

Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The outcome status for the associated Identity Verification attempt&#39;s &#x60;kyc_check&#x60; step. This field will always have the same value as &#x60;steps.kyc_check&#x60;. | 
**address** | [**KYCCheckAddressSummary**](KYCCheckAddressSummary.md) |  | 
**name** | [**KYCCheckNameSummary**](KYCCheckNameSummary.md) |  | 
**date_of_birth** | [**KYCCheckDateOfBirthSummary**](KYCCheckDateOfBirthSummary.md) |  | 
**id_number** | [**KYCCheckIDNumberSummary**](KYCCheckIDNumberSummary.md) |  | 
**phone_number** | [**KYCCheckPhoneSummary**](KYCCheckPhoneSummary.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


