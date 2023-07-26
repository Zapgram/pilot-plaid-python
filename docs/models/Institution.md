# plaid.model.institution.Institution

Details relating to a specific financial institution

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details relating to a specific financial institution | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[routing_numbers](#routing_numbers)** | list, tuple,  | tuple,  | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. | 
**name** | str,  | str,  | The official name of the institution. | 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | A list of the country codes supported by the institution. | 
**oauth** | bool,  | BoolClass,  | Indicates that the institution has an OAuth login flow. This will be &#x60;true&#x60; if OAuth is supported for any Items associated with the institution, even if the institution also supports non-OAuth connections. | 
**institution_id** | str,  | str,  | Unique identifier for the institution. Note that the same institution may have multiple records, each with different institution IDs; for example, if the institution has migrated to OAuth, there may be separate &#x60;institution_id&#x60;s for the OAuth and non-OAuth versions of the institution. Institutions that operate in different countries or with multiple login portals may also have separate &#x60;institution_id&#x60;s for each country or portal. | 
**[products](#products)** | list, tuple,  | tuple,  | A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return &#x60;auth&#x60; in the product array; institutions that do not list &#x60;auth&#x60; may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the &#x60;auth_metadata&#x60; object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/). | 
**url** | None, str,  | NoneClass, str,  | The URL for the institution&#x27;s website | [optional] 
**primary_color** | None, str,  | NoneClass, str,  | Hexadecimal representation of the primary color used by the institution | [optional] 
**logo** | None, str,  | NoneClass, str,  | Base64 encoded representation of the institution&#x27;s logo, returned as a base64 encoded 152x152 PNG. Not all institutions&#x27; logos are available. | [optional] 
**[dtc_numbers](#dtc_numbers)** | list, tuple,  | tuple,  | A partial list of DTC numbers associated with the institution. | [optional] 
**status** | [**InstitutionStatus**](InstitutionStatus.md) | [**InstitutionStatus**](InstitutionStatus.md) |  | [optional] 
**payment_initiation_metadata** | [**PaymentInitiationMetadata**](PaymentInitiationMetadata.md) | [**PaymentInitiationMetadata**](PaymentInitiationMetadata.md) |  | [optional] 
**auth_metadata** | [**AuthMetadata**](AuthMetadata.md) | [**AuthMetadata**](AuthMetadata.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return `auth` in the product array; institutions that do not list `auth` may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the `auth_metadata` object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return &#x60;auth&#x60; in the product array; institutions that do not list &#x60;auth&#x60; may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the &#x60;auth_metadata&#x60; object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Products**](Products.md) | [**Products**](Products.md) | [**Products**](Products.md) |  | 

# country_codes

A list of the country codes supported by the institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of the country codes supported by the institution. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) |  | 

# routing_numbers

A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# dtc_numbers

A partial list of DTC numbers associated with the institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A partial list of DTC numbers associated with the institution. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

