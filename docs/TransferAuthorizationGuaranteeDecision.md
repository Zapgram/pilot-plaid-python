# TransferAuthorizationGuaranteeDecision

Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either &#x60;GUARANTEED&#x60; or &#x60;NOT_GUARANTEED&#x60; indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the &#x60;guarantee_decision_rationale&#x60; field. Refer to the &#x60;code&#x60; field in &#x60;guarantee_decision_rationale&#x60; for details. |  must be one of ["GUARANTEED", "NOT_GUARANTEED", "null", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


