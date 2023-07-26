# TransferCreditFundsSource

Specifies the source of funds for the transfer. Only valid for `credit` transfers, and defaults to `sweep` if not specified. This field is not specified for `debit` transfers.  `sweep` - Sweep funds from your funding account `prefunded_rtp_credits` - Use your prefunded RTP credit balance with Plaid `prefunded_ach_credits` - Use your prefunded ACH credit balance with Plaid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Specifies the source of funds for the transfer. Only valid for &#x60;credit&#x60; transfers, and defaults to &#x60;sweep&#x60; if not specified. This field is not specified for &#x60;debit&#x60; transfers.  &#x60;sweep&#x60; - Sweep funds from your funding account &#x60;prefunded_rtp_credits&#x60; - Use your prefunded RTP credit balance with Plaid &#x60;prefunded_ach_credits&#x60; - Use your prefunded ACH credit balance with Plaid |  must be one of ["sweep", "prefunded_rtp_credits", "prefunded_ach_credits", "null", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


