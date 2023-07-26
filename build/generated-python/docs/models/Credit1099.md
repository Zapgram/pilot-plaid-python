# plaid.model.credit1099.Credit1099

An object representing an end user's 1099 tax form

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing an end user&#x27;s 1099 tax form | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**document_id** | None, str,  | NoneClass, str,  | An identifier of the document referenced by the document metadata. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | [optional] 
**form_1099_type** | [**Form1099Type**](Form1099Type.md) | [**Form1099Type**](Form1099Type.md) |  | [optional] 
**recipient** | [**Credit1099Recipient**](Credit1099Recipient.md) | [**Credit1099Recipient**](Credit1099Recipient.md) |  | [optional] 
**payer** | [**Credit1099Payer**](Credit1099Payer.md) | [**Credit1099Payer**](Credit1099Payer.md) |  | [optional] 
**filer** | [**Credit1099Filer**](Credit1099Filer.md) | [**Credit1099Filer**](Credit1099Filer.md) |  | [optional] 
**tax_year** | None, str,  | NoneClass, str,  | Tax year of the tax form. | [optional] 
**rents** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in rent by payer. | [optional] value must be a 64 bit float
**royalties** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in royalties by payer. | [optional] value must be a 64 bit float
**other_income** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in other income by payer. | [optional] value must be a 64 bit float
**federal_income_tax_withheld** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of federal income tax withheld from payer. | [optional] value must be a 64 bit float
**fishing_boat_proceeds** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of fishing boat proceeds from payer. | [optional] value must be a 64 bit float
**medical_and_healthcare_payments** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of medical and healthcare payments from payer. | [optional] value must be a 64 bit float
**nonemployee_compensation** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of nonemployee compensation from payer. | [optional] value must be a 64 bit float
**substitute_payments_in_lieu_of_dividends_or_interest** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of substitute payments made by payer. | [optional] value must be a 64 bit float
**payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer** | None, str,  | NoneClass, str,  | Whether or not payer made direct sales over $5000 of consumer products. | [optional] 
**crop_insurance_proceeds** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of crop insurance proceeds. | [optional] value must be a 64 bit float
**excess_golden_parachute_payments** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of golden parachute payments made by payer. | [optional] value must be a 64 bit float
**gross_proceeds_paid_to_an_attorney** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of gross proceeds paid to an attorney by payer. | [optional] value must be a 64 bit float
**section_409a_deferrals** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of 409A deferrals earned by payer. | [optional] value must be a 64 bit float
**section_409a_income** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of 409A income earned by payer. | [optional] value must be a 64 bit float
**state_tax_withheld** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of state tax withheld of payer for primary state. | [optional] value must be a 64 bit float
**state_tax_withheld_lower** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of state tax withheld of payer for secondary state. | [optional] value must be a 64 bit float
**payer_state_number** | None, str,  | NoneClass, str,  | Primary state ID. | [optional] 
**payer_state_number_lower** | None, str,  | NoneClass, str,  | Secondary state ID. | [optional] 
**state_income** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | State income reported for primary state. | [optional] value must be a 64 bit float
**state_income_lower** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | State income reported for secondary state. | [optional] value must be a 64 bit float
**transactions_reported** | None, str,  | NoneClass, str,  | One of the values will be provided Payment card Third party network | [optional] 
**pse_name** | None, str,  | NoneClass, str,  | Name of the PSE (Payment Settlement Entity). | [optional] 
**pse_telephone_number** | None, str,  | NoneClass, str,  | Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity). | [optional] 
**gross_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Gross amount reported. | [optional] value must be a 64 bit float
**card_not_present_transaction** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in card not present transactions. | [optional] value must be a 64 bit float
**merchant_category_code** | None, str,  | NoneClass, str,  | Merchant category of filer. | [optional] 
**number_of_payment_transactions** | None, str,  | NoneClass, str,  | Number of payment transactions made. | [optional] 
**january_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for January. | [optional] value must be a 64 bit float
**february_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for February. | [optional] value must be a 64 bit float
**march_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for March. | [optional] value must be a 64 bit float
**april_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for April. | [optional] value must be a 64 bit float
**may_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for May. | [optional] value must be a 64 bit float
**june_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for June. | [optional] value must be a 64 bit float
**july_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for July. | [optional] value must be a 64 bit float
**august_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for August. | [optional] value must be a 64 bit float
**september_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for September. | [optional] value must be a 64 bit float
**october_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for October. | [optional] value must be a 64 bit float
**november_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for November. | [optional] value must be a 64 bit float
**december_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount reported for December. | [optional] value must be a 64 bit float
**primary_state** | None, str,  | NoneClass, str,  | Primary state of business. | [optional] 
**secondary_state** | None, str,  | NoneClass, str,  | Secondary state of business. | [optional] 
**primary_state_id** | None, str,  | NoneClass, str,  | Primary state ID. | [optional] 
**secondary_state_id** | None, str,  | NoneClass, str,  | Secondary state ID. | [optional] 
**primary_state_income_tax** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | State income tax reported for primary state. | [optional] value must be a 64 bit float
**secondary_state_income_tax** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | State income tax reported for secondary state. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

