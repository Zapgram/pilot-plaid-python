# plaid.model.link_token_create_request_account_subtypes.LinkTokenCreateRequestAccountSubtypes

By default, Link will only display account types that are compatible with all products supplied in the `products` parameter of `/link/token/create`. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\"all\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link.  For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).  For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in the OAuth window. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | By default, Link will only display account types that are compatible with all products supplied in the &#x60;products&#x60; parameter of &#x60;/link/token/create&#x60;. You can further limit the accounts shown in Link by using &#x60;account_filters&#x60; to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value &#x60;\&quot;all\&quot;&#x60;. If the &#x60;account_filters&#x60; filter is used, any account type for which a filter is not specified will be entirely omitted from Link.  For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).  For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in the OAuth window.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**depository** | [**LinkTokenCreateDepositoryFilter**](LinkTokenCreateDepositoryFilter.md) | [**LinkTokenCreateDepositoryFilter**](LinkTokenCreateDepositoryFilter.md) |  | [optional] 
**credit** | [**LinkTokenCreateCreditFilter**](LinkTokenCreateCreditFilter.md) | [**LinkTokenCreateCreditFilter**](LinkTokenCreateCreditFilter.md) |  | [optional] 
**loan** | [**LinkTokenCreateLoanFilter**](LinkTokenCreateLoanFilter.md) | [**LinkTokenCreateLoanFilter**](LinkTokenCreateLoanFilter.md) |  | [optional] 
**investment** | [**LinkTokenCreateInvestmentFilter**](LinkTokenCreateInvestmentFilter.md) | [**LinkTokenCreateInvestmentFilter**](LinkTokenCreateInvestmentFilter.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

