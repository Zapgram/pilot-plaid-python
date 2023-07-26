# TransferAuthorizationGuaranteeDecisionRationaleCode

A code representing the reason Plaid declined to guarantee this transfer:  `RETURN_BANK`: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this transfer.  `RETURN_CUSTOMER`: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to guarantee this transfer.  `GUARANTEE_LIMIT_REACHED`: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number or rate of guarantees that applies to this transfer.  `RISK_ESTIMATE_UNAVAILABLE`: A risk estimate is unavailable for this Item.  `REQUIRED_PARAM_MISSING`: Required fields are missing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A code representing the reason Plaid declined to guarantee this transfer:  &#x60;RETURN_BANK&#x60;: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this transfer.  &#x60;RETURN_CUSTOMER&#x60;: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to guarantee this transfer.  &#x60;GUARANTEE_LIMIT_REACHED&#x60;: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number or rate of guarantees that applies to this transfer.  &#x60;RISK_ESTIMATE_UNAVAILABLE&#x60;: A risk estimate is unavailable for this Item.  &#x60;REQUIRED_PARAM_MISSING&#x60;: Required fields are missing. |  must be one of ["RETURN_BANK", "RETURN_CUSTOMER", "GUARANTEE_LIMIT_REACHED", "RISK_ESTIMATE_UNAVAILABLE", "REQUIRED_PARAM_MISSING", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


