# plaid.model.kyc_check_address_summary.KYCCheckAddressSummary

Result summary object specifying how the `address` field matched.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Result summary object specifying how the &#x60;address&#x60; field matched. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**summary** | [**MatchSummaryCode**](MatchSummaryCode.md) | [**MatchSummaryCode**](MatchSummaryCode.md) |  | 
**po_box** | [**POBoxStatus**](POBoxStatus.md) | [**POBoxStatus**](POBoxStatus.md) |  | 
**type** | [**AddressPurposeLabel**](AddressPurposeLabel.md) | [**AddressPurposeLabel**](AddressPurposeLabel.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

