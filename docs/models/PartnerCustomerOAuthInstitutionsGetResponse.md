# plaid.model.partner_customer_o_auth_institutions_get_response.PartnerCustomerOAuthInstitutionsGetResponse

Response schema for `/partner/customer/oauth_institutions/get`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response schema for &#x60;/partner/customer/oauth_institutions/get&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**flowdown_status** | [**PartnerEndCustomerFlowdownStatus**](PartnerEndCustomerFlowdownStatus.md) | [**PartnerEndCustomerFlowdownStatus**](PartnerEndCustomerFlowdownStatus.md) |  | [optional] 
**questionnaire_status** | [**PartnerEndCustomerQuestionnaireStatus**](PartnerEndCustomerQuestionnaireStatus.md) | [**PartnerEndCustomerQuestionnaireStatus**](PartnerEndCustomerQuestionnaireStatus.md) |  | [optional] 
**[institutions](#institutions)** | list, tuple,  | tuple,  | The OAuth institutions with which the end customer&#x27;s application is being registered. | [optional] 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# institutions

The OAuth institutions with which the end customer's application is being registered.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The OAuth institutions with which the end customer&#x27;s application is being registered. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PartnerEndCustomerOAuthInstitution**](PartnerEndCustomerOAuthInstitution.md) | [**PartnerEndCustomerOAuthInstitution**](PartnerEndCustomerOAuthInstitution.md) | [**PartnerEndCustomerOAuthInstitution**](PartnerEndCustomerOAuthInstitution.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

