# WalletPaymentScheme

The payment scheme used to execute this transaction. This is present only for transaction types `PAYOUT` and `REFUND`.  `FASTER_PAYMENTS`: The standard payment scheme within the UK.  `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.  `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment to a beneficiary within the SEPA area.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The payment scheme used to execute this transaction. This is present only for transaction types &#x60;PAYOUT&#x60; and &#x60;REFUND&#x60;.  &#x60;FASTER_PAYMENTS&#x60;: The standard payment scheme within the UK.  &#x60;SEPA_CREDIT_TRANSFER&#x60;: The standard payment to a beneficiary within the SEPA area.  &#x60;SEPA_CREDIT_TRANSFER_INSTANT&#x60;: Instant payment to a beneficiary within the SEPA area. |  must be one of ["null", "FASTER_PAYMENTS", "SEPA_CREDIT_TRANSFER", "SEPA_CREDIT_TRANSFER_INSTANT", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


