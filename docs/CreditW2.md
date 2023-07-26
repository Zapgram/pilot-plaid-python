# CreditW2

W2 is an object that represents income data taken from a W2 tax document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | 
**document_id** | **str** | An identifier of the document referenced by the document metadata. | 
**employer** | [**CreditPayStubEmployer**](CreditPayStubEmployer.md) |  | 
**employee** | [**CreditPayStubEmployee**](CreditPayStubEmployee.md) |  | 
**tax_year** | **str, none_type** | The tax year of the W2 document. | 
**employer_id_number** | **str, none_type** | An employee identification number or EIN. | 
**wages_tips_other_comp** | **str, none_type** | Wages from tips and other compensation. | 
**federal_income_tax_withheld** | **str, none_type** | Federal income tax withheld for the tax year. | 
**social_security_wages** | **str, none_type** | Wages from social security. | 
**social_security_tax_withheld** | **str, none_type** | Social security tax withheld for the tax year. | 
**medicare_wages_and_tips** | **str, none_type** | Wages and tips from medicare. | 
**medicare_tax_withheld** | **str, none_type** | Medicare tax withheld for the tax year. | 
**social_security_tips** | **str, none_type** | Tips from social security. | 
**allocated_tips** | **str, none_type** | Allocated tips. | 
**box_9** | **str, none_type** | Contents from box 9 on the W2. | 
**dependent_care_benefits** | **str, none_type** | Dependent care benefits. | 
**nonqualified_plans** | **str, none_type** | Nonqualified plans. | 
**box_12** | [**[W2Box12]**](W2Box12.md) |  | 
**statutory_employee** | **str, none_type** | Statutory employee. | 
**retirement_plan** | **str, none_type** | Retirement plan. | 
**third_party_sick_pay** | **str, none_type** | Third party sick pay. | 
**other** | **str, none_type** | Other. | 
**state_and_local_wages** | [**[W2StateAndLocalWages]**](W2StateAndLocalWages.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


