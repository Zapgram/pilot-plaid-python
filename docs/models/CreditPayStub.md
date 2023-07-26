# plaid.model.credit_pay_stub.CreditPayStub

An object representing an end user's pay stub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing an end user&#x27;s pay stub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**net_pay** | [**CreditPayStubNetPay**](CreditPayStubNetPay.md) | [**CreditPayStubNetPay**](CreditPayStubNetPay.md) |  | 
**earnings** | [**CreditPayStubEarnings**](CreditPayStubEarnings.md) | [**CreditPayStubEarnings**](CreditPayStubEarnings.md) |  | 
**pay_period_details** | [**PayStubPayPeriodDetails**](PayStubPayPeriodDetails.md) | [**PayStubPayPeriodDetails**](PayStubPayPeriodDetails.md) |  | 
**employer** | [**CreditPayStubEmployer**](CreditPayStubEmployer.md) | [**CreditPayStubEmployer**](CreditPayStubEmployer.md) |  | 
**deductions** | [**CreditPayStubDeductions**](CreditPayStubDeductions.md) | [**CreditPayStubDeductions**](CreditPayStubDeductions.md) |  | 
**document_id** | None, str,  | NoneClass, str,  | An identifier of the document referenced by the document metadata. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | 
**employee** | [**CreditPayStubEmployee**](CreditPayStubEmployee.md) | [**CreditPayStubEmployee**](CreditPayStubEmployee.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

