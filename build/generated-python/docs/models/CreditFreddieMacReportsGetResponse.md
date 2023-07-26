# plaid.model.credit_freddie_mac_reports_get_response.CreditFreddieMacReportsGetResponse

CreditFreddieMacReportsGetResponse defines the response schema for `/credit/freddie_mac/reports/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreditFreddieMacReportsGetResponse defines the response schema for &#x60;/credit/freddie_mac/reports/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**VOA** | [**CreditFreddieMacVerificationOfAssetsVOA24**](CreditFreddieMacVerificationOfAssetsVOA24.md) | [**CreditFreddieMacVerificationOfAssetsVOA24**](CreditFreddieMacVerificationOfAssetsVOA24.md) |  | [optional] 
**VOE** | [**CreditFreddieVerificationOfEmploymentVOE25**](CreditFreddieVerificationOfEmploymentVOE25.md) | [**CreditFreddieVerificationOfEmploymentVOE25**](CreditFreddieVerificationOfEmploymentVOE25.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

