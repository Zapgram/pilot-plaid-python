# PartnerEndCustomerStatus

The status of the given end customer.  `UNDER_REVIEW`: The end customer has been created and enabled in the non-Production environments. The end customer must be manually reviewed by the Plaid team before it can be enabled in production, at which point its status will automatically transition to `PENDING_ENABLEMENT` or `DENIED`.  `PENDING_ENABLEMENT`: The end customer is ready to be enabled in the Production environment. Call the `/partner/customer/enable` endpoint to enable the end customer in Production.  `ACTIVE`: The end customer has been enabled in all environments.  `DENIED`: The end customer has been created and enabled in the non-Production environments, but it did not pass review by the Plaid team and therefore cannot be enabled in the Production environment. Talk to your Account Manager for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the given end customer.  &#x60;UNDER_REVIEW&#x60;: The end customer has been created and enabled in the non-Production environments. The end customer must be manually reviewed by the Plaid team before it can be enabled in production, at which point its status will automatically transition to &#x60;PENDING_ENABLEMENT&#x60; or &#x60;DENIED&#x60;.  &#x60;PENDING_ENABLEMENT&#x60;: The end customer is ready to be enabled in the Production environment. Call the &#x60;/partner/customer/enable&#x60; endpoint to enable the end customer in Production.  &#x60;ACTIVE&#x60;: The end customer has been enabled in all environments.  &#x60;DENIED&#x60;: The end customer has been created and enabled in the non-Production environments, but it did not pass review by the Plaid team and therefore cannot be enabled in the Production environment. Talk to your Account Manager for more information. |  must be one of ["UNDER_REVIEW", "PENDING_ENABLEMENT", "ACTIVE", "DENIED", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


