# Item

Metadata about the Item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The Plaid Item ID. The &#x60;item_id&#x60; is always unique; linking the same account at the same institution twice will result in two Items with different &#x60;item_id&#x60; values. Like all Plaid identifiers, the &#x60;item_id&#x60; is case-sensitive. | 
**webhook** | **str, none_type** | The URL registered to receive webhooks for the Item. | 
**error** | [**PlaidError**](PlaidError.md) |  | 
**available_products** | [**[Products]**](Products.md) | A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with &#x60;billed_products&#x60;. | 
**billed_products** | [**[Products]**](Products.md) | A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with &#x60;available_products&#x60;. Note - &#x60;billed_products&#x60; is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as &#x60;balance&#x60;, will not appear here.  | 
**consent_expiration_time** | **datetime, none_type** | The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the &#x60;ITEM_LOGIN_REQUIRED&#x60; error state. To circumvent the &#x60;ITEM_LOGIN_REQUIRED&#x60; error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.  Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be null.  | 
**update_type** | **str** | Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.  &#x60;background&#x60; - Item can be updated in the background  &#x60;user_present_required&#x60; - Item requires user interaction to be updated | 
**institution_id** | **str, none_type** | The Plaid Institution ID associated with the Item. Field is &#x60;null&#x60; for Items created via Same Day Micro-deposits. | [optional] 
**products** | [**[Products]**](Products.md) | A list of initialized products for the Item. In almost all cases, this will be the same as the &#x60;billed_products&#x60; field. For some products, it is possible for the product to be initialized on an Item but not yet billed (e.g. Assets, before &#x60;/asset_report/create&#x60; has been called), in which case the product may appear in &#x60;products&#x60; but not in &#x60;billed_products&#x60;.  | [optional] 
**consented_products** | [**[Products]**](Products.md) | A list of products that have gone through consent collection for the Item. Only present for those enabled in the [Data Transparency](https://plaid.com/docs/link/data-transparency-messaging-migration-guide) beta. If you are not enrolled in Data Transparency, this field is not used.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


