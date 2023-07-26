# plaid.model.fdx_party.FDXParty

FDX Participant - an entity or person that is a part of a FDX API transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | FDX Participant - an entity or person that is a part of a FDX API transaction | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human recognizable common name | 
**type** | [**FDXPartyType**](FDXPartyType.md) | [**FDXPartyType**](FDXPartyType.md) |  | 
**homeUri** | str,  | str,  | URI for party, where an end user could learn more about the company or application involved in the data sharing chain | [optional] 
**logoUri** | str,  | str,  | URI for a logo asset to be displayed to the end user | [optional] 
**registry** | [**FDXPartyRegistry**](FDXPartyRegistry.md) | [**FDXPartyRegistry**](FDXPartyRegistry.md) |  | [optional] 
**registeredEntityName** | str,  | str,  | Registered name of party | [optional] 
**registeredEntityId** | str,  | str,  | Registered id of party | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

