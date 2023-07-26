# Institution

Details relating to a specific financial institution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Unique identifier for the institution. Note that the same institution may have multiple records, each with different institution IDs; for example, if the institution has migrated to OAuth, there may be separate &#x60;institution_id&#x60;s for the OAuth and non-OAuth versions of the institution. Institutions that operate in different countries or with multiple login portals may also have separate &#x60;institution_id&#x60;s for each country or portal. | 
**name** | **str** | The official name of the institution. | 
**products** | [**[Products]**](Products.md) | A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return &#x60;auth&#x60; in the product array; institutions that do not list &#x60;auth&#x60; may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the &#x60;auth_metadata&#x60; object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/). | 
**country_codes** | [**[CountryCode]**](CountryCode.md) | A list of the country codes supported by the institution. | 
**routing_numbers** | **[str]** | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. | 
**oauth** | **bool** | Indicates that the institution has an OAuth login flow. This will be &#x60;true&#x60; if OAuth is supported for any Items associated with the institution, even if the institution also supports non-OAuth connections. | 
**url** | **str, none_type** | The URL for the institution&#39;s website | [optional] 
**primary_color** | **str, none_type** | Hexadecimal representation of the primary color used by the institution | [optional] 
**logo** | **str, none_type** | Base64 encoded representation of the institution&#39;s logo, returned as a base64 encoded 152x152 PNG. Not all institutions&#39; logos are available. | [optional] 
**dtc_numbers** | **[str]** | A partial list of DTC numbers associated with the institution. | [optional] 
**status** | [**InstitutionStatus**](InstitutionStatus.md) |  | [optional] 
**payment_initiation_metadata** | [**PaymentInitiationMetadata**](PaymentInitiationMetadata.md) |  | [optional] 
**auth_metadata** | [**AuthMetadata**](AuthMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


