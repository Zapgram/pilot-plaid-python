# PaymentScheme

Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.  `LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.  `LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.  `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.  `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Payment scheme. If not specified - the default in the region will be used (e.g. &#x60;SEPA_CREDIT_TRANSFER&#x60; for EU). Using unsupported values will result in a failed payment.  &#x60;LOCAL_DEFAULT&#x60;: The default payment scheme for the selected market and currency will be used.  &#x60;LOCAL_INSTANT&#x60;: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.  &#x60;SEPA_CREDIT_TRANSFER&#x60;: The standard payment to a beneficiary within the SEPA area.  &#x60;SEPA_CREDIT_TRANSFER_INSTANT&#x60;: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks. |  must be one of ["null", "LOCAL_DEFAULT", "LOCAL_INSTANT", "SEPA_CREDIT_TRANSFER", "SEPA_CREDIT_TRANSFER_INSTANT", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


