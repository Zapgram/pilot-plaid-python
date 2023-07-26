# Credit1099

An object representing an end user's 1099 tax form

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str, none_type** | An identifier of the document referenced by the document metadata. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | [optional] 
**form_1099_type** | [**Form1099Type**](Form1099Type.md) |  | [optional] 
**recipient** | [**Credit1099Recipient**](Credit1099Recipient.md) |  | [optional] 
**payer** | [**Credit1099Payer**](Credit1099Payer.md) |  | [optional] 
**filer** | [**Credit1099Filer**](Credit1099Filer.md) |  | [optional] 
**tax_year** | **str, none_type** | Tax year of the tax form. | [optional] 
**rents** | **float, none_type** | Amount in rent by payer. | [optional] 
**royalties** | **float, none_type** | Amount in royalties by payer. | [optional] 
**other_income** | **float, none_type** | Amount in other income by payer. | [optional] 
**federal_income_tax_withheld** | **float, none_type** | Amount of federal income tax withheld from payer. | [optional] 
**fishing_boat_proceeds** | **float, none_type** | Amount of fishing boat proceeds from payer. | [optional] 
**medical_and_healthcare_payments** | **float, none_type** | Amount of medical and healthcare payments from payer. | [optional] 
**nonemployee_compensation** | **float, none_type** | Amount of nonemployee compensation from payer. | [optional] 
**substitute_payments_in_lieu_of_dividends_or_interest** | **float, none_type** | Amount of substitute payments made by payer. | [optional] 
**payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer** | **str, none_type** | Whether or not payer made direct sales over $5000 of consumer products. | [optional] 
**crop_insurance_proceeds** | **float, none_type** | Amount of crop insurance proceeds. | [optional] 
**excess_golden_parachute_payments** | **float, none_type** | Amount of golden parachute payments made by payer. | [optional] 
**gross_proceeds_paid_to_an_attorney** | **float, none_type** | Amount of gross proceeds paid to an attorney by payer. | [optional] 
**section_409a_deferrals** | **float, none_type** | Amount of 409A deferrals earned by payer. | [optional] 
**section_409a_income** | **float, none_type** | Amount of 409A income earned by payer. | [optional] 
**state_tax_withheld** | **float, none_type** | Amount of state tax withheld of payer for primary state. | [optional] 
**state_tax_withheld_lower** | **float, none_type** | Amount of state tax withheld of payer for secondary state. | [optional] 
**payer_state_number** | **str, none_type** | Primary state ID. | [optional] 
**payer_state_number_lower** | **str, none_type** | Secondary state ID. | [optional] 
**state_income** | **float, none_type** | State income reported for primary state. | [optional] 
**state_income_lower** | **float, none_type** | State income reported for secondary state. | [optional] 
**transactions_reported** | **str, none_type** | One of the values will be provided Payment card Third party network | [optional] 
**pse_name** | **str, none_type** | Name of the PSE (Payment Settlement Entity). | [optional] 
**pse_telephone_number** | **str, none_type** | Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity). | [optional] 
**gross_amount** | **float, none_type** | Gross amount reported. | [optional] 
**card_not_present_transaction** | **float, none_type** | Amount in card not present transactions. | [optional] 
**merchant_category_code** | **str, none_type** | Merchant category of filer. | [optional] 
**number_of_payment_transactions** | **str, none_type** | Number of payment transactions made. | [optional] 
**january_amount** | **float, none_type** | Amount reported for January. | [optional] 
**february_amount** | **float, none_type** | Amount reported for February. | [optional] 
**march_amount** | **float, none_type** | Amount reported for March. | [optional] 
**april_amount** | **float, none_type** | Amount reported for April. | [optional] 
**may_amount** | **float, none_type** | Amount reported for May. | [optional] 
**june_amount** | **float, none_type** | Amount reported for June. | [optional] 
**july_amount** | **float, none_type** | Amount reported for July. | [optional] 
**august_amount** | **float, none_type** | Amount reported for August. | [optional] 
**september_amount** | **float, none_type** | Amount reported for September. | [optional] 
**october_amount** | **float, none_type** | Amount reported for October. | [optional] 
**november_amount** | **float, none_type** | Amount reported for November. | [optional] 
**december_amount** | **float, none_type** | Amount reported for December. | [optional] 
**primary_state** | **str, none_type** | Primary state of business. | [optional] 
**secondary_state** | **str, none_type** | Secondary state of business. | [optional] 
**primary_state_id** | **str, none_type** | Primary state ID. | [optional] 
**secondary_state_id** | **str, none_type** | Secondary state ID. | [optional] 
**primary_state_income_tax** | **float, none_type** | State income tax reported for primary state. | [optional] 
**secondary_state_income_tax** | **float, none_type** | State income tax reported for secondary state. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


