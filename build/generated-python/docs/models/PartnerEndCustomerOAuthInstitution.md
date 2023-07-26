# plaid.model.partner_end_customer_o_auth_institution.PartnerEndCustomerOAuthInstitution

The OAuth registration information for an institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The OAuth registration information for an institution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**institution_id** | str,  | str,  |  | [optional] 
**environments** | [**PartnerEndCustomerOAuthInstitutionEnvironments**](PartnerEndCustomerOAuthInstitutionEnvironments.md) | [**PartnerEndCustomerOAuthInstitutionEnvironments**](PartnerEndCustomerOAuthInstitutionEnvironments.md) |  | [optional] 
**production_enablement_date** | None, str,  | NoneClass, str,  | The date on which the end customer&#x27;s application was approved by the institution, or an empty string if their application has not yet been approved. | [optional] 
**classic_disablement_date** | None, str,  | NoneClass, str,  | The date on which non-OAuth Item adds will no longer be supported for this institution, or an empty string if no such date has been set by the institution. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

