# RiskCheckEmail

Result summary object specifying values for `email` attributes of risk check.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deliverable** | [**RiskCheckEmailIsDeliverableStatus**](RiskCheckEmailIsDeliverableStatus.md) |  | 
**breach_count** | **int, none_type** | Count of all known breaches of this email address if known. | 
**first_breached_at** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**last_breached_at** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**domain_registered_at** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**domain_is_free_provider** | [**RiskCheckEmailDomainIsFreeProvider**](RiskCheckEmailDomainIsFreeProvider.md) |  | 
**domain_is_custom** | [**RiskCheckEmailDomainIsCustom**](RiskCheckEmailDomainIsCustom.md) |  | 
**domain_is_disposable** | [**RiskCheckEmailDomainIsDisposable**](RiskCheckEmailDomainIsDisposable.md) |  | 
**top_level_domain_is_suspicious** | [**RiskCheckEmailTopLevelDomainIsSuspicious**](RiskCheckEmailTopLevelDomainIsSuspicious.md) |  | 
**linked_services** | [**[RiskCheckLinkedService]**](RiskCheckLinkedService.md) | A list of online services where this email address has been detected to have accounts or other activity. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


