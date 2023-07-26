# plaid.model.kyc_check_details.KYCCheckDetails

Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Additional information for the &#x60;kyc_check&#x60; step. This field will be &#x60;null&#x60; unless &#x60;steps.kyc_check&#x60; has reached a terminal state of either &#x60;success&#x60; or &#x60;failed&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_number** | [**KYCCheckIDNumberSummary**](KYCCheckIDNumberSummary.md) | [**KYCCheckIDNumberSummary**](KYCCheckIDNumberSummary.md) |  | 
**address** | [**KYCCheckAddressSummary**](KYCCheckAddressSummary.md) | [**KYCCheckAddressSummary**](KYCCheckAddressSummary.md) |  | 
**date_of_birth** | [**KYCCheckDateOfBirthSummary**](KYCCheckDateOfBirthSummary.md) | [**KYCCheckDateOfBirthSummary**](KYCCheckDateOfBirthSummary.md) |  | 
**name** | [**KYCCheckNameSummary**](KYCCheckNameSummary.md) | [**KYCCheckNameSummary**](KYCCheckNameSummary.md) |  | 
**phone_number** | [**KYCCheckPhoneSummary**](KYCCheckPhoneSummary.md) | [**KYCCheckPhoneSummary**](KYCCheckPhoneSummary.md) |  | 
**status** | str,  | str,  | The outcome status for the associated Identity Verification attempt&#x27;s &#x60;kyc_check&#x60; step. This field will always have the same value as &#x60;steps.kyc_check&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

