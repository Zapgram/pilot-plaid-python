# plaid.model.credit_w2.CreditW2

W2 is an object that represents income data taken from a W2 tax document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | W2 is an object that represents income data taken from a W2 tax document. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statutory_employee** | None, str,  | NoneClass, str,  | Statutory employee. | 
**other** | None, str,  | NoneClass, str,  | Other. | 
**allocated_tips** | None, str,  | NoneClass, str,  | Allocated tips. | 
**retirement_plan** | None, str,  | NoneClass, str,  | Retirement plan. | 
**wages_tips_other_comp** | None, str,  | NoneClass, str,  | Wages from tips and other compensation. | 
**nonqualified_plans** | None, str,  | NoneClass, str,  | Nonqualified plans. | 
**document_id** | str,  | str,  | An identifier of the document referenced by the document metadata. | 
**employee** | [**CreditPayStubEmployee**](CreditPayStubEmployee.md) | [**CreditPayStubEmployee**](CreditPayStubEmployee.md) |  | 
**tax_year** | None, str,  | NoneClass, str,  | The tax year of the W2 document. | 
**social_security_tax_withheld** | None, str,  | NoneClass, str,  | Social security tax withheld for the tax year. | 
**social_security_wages** | None, str,  | NoneClass, str,  | Wages from social security. | 
**social_security_tips** | None, str,  | NoneClass, str,  | Tips from social security. | 
**medicare_wages_and_tips** | None, str,  | NoneClass, str,  | Wages and tips from medicare. | 
**third_party_sick_pay** | None, str,  | NoneClass, str,  | Third party sick pay. | 
**employer_id_number** | None, str,  | NoneClass, str,  | An employee identification number or EIN. | 
**federal_income_tax_withheld** | None, str,  | NoneClass, str,  | Federal income tax withheld for the tax year. | 
**medicare_tax_withheld** | None, str,  | NoneClass, str,  | Medicare tax withheld for the tax year. | 
**employer** | [**CreditPayStubEmployer**](CreditPayStubEmployer.md) | [**CreditPayStubEmployer**](CreditPayStubEmployer.md) |  | 
**[box_12](#box_12)** | list, tuple,  | tuple,  |  | 
**[state_and_local_wages](#state_and_local_wages)** | list, tuple,  | tuple,  |  | 
**box_9** | None, str,  | NoneClass, str,  | Contents from box 9 on the W2. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | 
**dependent_care_benefits** | None, str,  | NoneClass, str,  | Dependent care benefits. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# box_12

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**W2Box12**](W2Box12.md) | [**W2Box12**](W2Box12.md) | [**W2Box12**](W2Box12.md) |  | 

# state_and_local_wages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**W2StateAndLocalWages**](W2StateAndLocalWages.md) | [**W2StateAndLocalWages**](W2StateAndLocalWages.md) | [**W2StateAndLocalWages**](W2StateAndLocalWages.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

