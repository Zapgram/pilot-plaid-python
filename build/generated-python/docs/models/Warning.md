# plaid.model.warning.Warning

It is possible for an Asset Report to be returned with missing account owner information. In such cases, the Asset Report will contain warning data in the response, indicating why obtaining the owner information failed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | It is possible for an Asset Report to be returned with missing account owner information. In such cases, the Asset Report will contain warning data in the response, indicating why obtaining the owner information failed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cause** | [**Cause**](Cause.md) | [**Cause**](Cause.md) |  | 
**warning_type** | str,  | str,  | The warning type, which will always be &#x60;ASSET_REPORT_WARNING&#x60; | 
**warning_code** | str,  | str,  | The warning code identifies a specific kind of warning. &#x60;OWNERS_UNAVAILABLE&#x60; indicates that account-owner information is not available.&#x60;INVESTMENTS_UNAVAILABLE&#x60; indicates that Investments specific information is not available. &#x60;TRANSACTIONS_UNAVAILABLE&#x60; indicates that transactions information associated with Credit and Depository accounts are unavailable. | must be one of ["OWNERS_UNAVAILABLE", "INVESTMENTS_UNAVAILABLE", "TRANSACTIONS_UNAVAILABLE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

