# plaid.model.partner_customer_create_request.PartnerCustomerCreateRequest

Request schema for `/partner/customer/create`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Request schema for &#x60;/partner/customer/create&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_diligence_attested** | bool,  | BoolClass,  | Denotes whether or not the partner has completed attestation of diligence for the end customer to be created. | 
**website** | str,  | str,  | The end customer&#x27;s website. | 
**address** | [**PartnerEndCustomerAddress**](PartnerEndCustomerAddress.md) | [**PartnerEndCustomerAddress**](PartnerEndCustomerAddress.md) |  | 
**application_name** | str,  | str,  | The name of the end customer&#x27;s application. This will be shown to end users when they go through the Plaid Link flow. | 
**company_name** | str,  | str,  | The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users. | 
**is_bank_addendum_completed** | bool,  | BoolClass,  | Denotes whether the partner has forwarded the Plaid bank addendum to the end customer. | 
**legal_entity_name** | str,  | str,  | The end customer&#x27;s legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users. | 
**[products](#products)** | list, tuple,  | tuple,  | The products to be enabled for the end customer. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**create_link_customization** | bool,  | BoolClass,  | If &#x60;true&#x60;, the end customer&#x27;s default Link customization will be set to match the partner&#x27;s. You can always change the end customer&#x27;s Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information. | [optional] 
**logo** | str,  | str,  | Base64-encoded representation of the end customer&#x27;s logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if &#x60;create_link_customization&#x60; is &#x60;true&#x60;. If &#x60;create_link_customization&#x60; is &#x60;false&#x60; and the logo is omitted, a stock logo will be used. | [optional] 
**technical_contact** | [**PartnerEndCustomerTechnicalContact**](PartnerEndCustomerTechnicalContact.md) | [**PartnerEndCustomerTechnicalContact**](PartnerEndCustomerTechnicalContact.md) |  | [optional] 
**billing_contact** | [**PartnerEndCustomerBillingContact**](PartnerEndCustomerBillingContact.md) | [**PartnerEndCustomerBillingContact**](PartnerEndCustomerBillingContact.md) |  | [optional] 
**customer_support_info** | [**PartnerEndCustomerCustomerSupportInfo**](PartnerEndCustomerCustomerSupportInfo.md) | [**PartnerEndCustomerCustomerSupportInfo**](PartnerEndCustomerCustomerSupportInfo.md) |  | [optional] 
**assets_under_management** | [**PartnerEndCustomerAssetsUnderManagement**](PartnerEndCustomerAssetsUnderManagement.md) | [**PartnerEndCustomerAssetsUnderManagement**](PartnerEndCustomerAssetsUnderManagement.md) |  | [optional] 
**[redirect_uris](#redirect_uris)** | list, tuple,  | tuple,  | A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use &#x60;*&#x60; as a wildcard character, e.g. &#x60;https://*.example.com/oauth.html&#x60;. To modify redirect URIs for an end customer after creating them, go to the end customer&#x27;s [API page](https://dashboard.plaid.com/team/api) in the Dashboard. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

The products to be enabled for the end customer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The products to be enabled for the end customer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Products**](Products.md) | [**Products**](Products.md) | [**Products**](Products.md) |  | 

# redirect_uris

A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use &#x60;*&#x60; as a wildcard character, e.g. &#x60;https://*.example.com/oauth.html&#x60;. To modify redirect URIs for an end customer after creating them, go to the end customer&#x27;s [API page](https://dashboard.plaid.com/team/api) in the Dashboard. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

