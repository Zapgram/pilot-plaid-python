# SignalPaymentMethod

The payment method to complete the transaction after the risk assessment. It may be different from the default payment method.  `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day  `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors  `STANDARD_ACH`: standard ACH by NACHA  `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow  `DEBIT_CARD`: if the default payment is over debit card networks  `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods  Possible values: `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The payment method to complete the transaction after the risk assessment. It may be different from the default payment method.  &#x60;SAME_DAY_ACH&#x60;: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day  &#x60;NEXT_DAY_ACH&#x60;: Next Day ACH settlement for debit transactions, offered by some payment processors  &#x60;STANDARD_ACH&#x60;: standard ACH by NACHA  &#x60;REAL_TIME_PAYMENTS&#x60;: real-time payments such as RTP and FedNow  &#x60;DEBIT_CARD&#x60;: if the default payment is over debit card networks  &#x60;MULTIPLE_PAYMENT_METHODS&#x60;: if there is no default debit rail or there are multiple payment methods  Possible values: &#x60;SAME_DAY_ACH&#x60;, &#x60;NEXT_DAY_ACH&#x60;, &#x60;STANDARD_ACH&#x60;, &#x60;REAL_TIME_PAYMENTS&#x60;, &#x60;DEBIT_CARD&#x60;, &#x60;MULTIPLE_PAYMENT_METHODS&#x60;  |  must be one of ["SAME_DAY_ACH", "NEXT_DAY_ACH", "STANDARD_ACH", "REAL_TIME_PAYMENTS", "DEBIT_CARD", "MULTIPLE_PAYMENT_METHODS", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


