# PartnerCustomerOAuthInstitutionsGetResponse

Response schema for `/partner/customer/oauth_institutions/get`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flowdown_status** | [**PartnerEndCustomerFlowdownStatus**](PartnerEndCustomerFlowdownStatus.md) |  | [optional] 
**questionnaire_status** | [**PartnerEndCustomerQuestionnaireStatus**](PartnerEndCustomerQuestionnaireStatus.md) |  | [optional] 
**institutions** | [**[PartnerEndCustomerOAuthInstitution]**](PartnerEndCustomerOAuthInstitution.md) | The OAuth institutions with which the end customer&#39;s application is being registered. | [optional] 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


