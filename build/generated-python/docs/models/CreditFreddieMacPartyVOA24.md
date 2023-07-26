# plaid.model.credit_freddie_mac_party_voa24.CreditFreddieMacPartyVOA24

A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TAXPAYER_IDENTIFIERS** | [**TaxpayerIdentifiers**](TaxpayerIdentifiers.md) | [**TaxpayerIdentifiers**](TaxpayerIdentifiers.md) |  | 
**ROLES** | [**Roles**](Roles.md) | [**Roles**](Roles.md) |  | 
**INDIVIDUAL** | [**CreditFreddieMacPartyIndividualVOA24**](CreditFreddieMacPartyIndividualVOA24.md) | [**CreditFreddieMacPartyIndividualVOA24**](CreditFreddieMacPartyIndividualVOA24.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

