# plaid.model.credit_ach_class.CreditACHClass

Specifies the use case of the transfer. Required for transfers on an ACH network.  `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts  `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  `\"web\"` - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Specifies the use case of the transfer. Required for transfers on an ACH network.  &#x60;\&quot;ccd\&quot;&#x60; - Corporate Credit or Debit - fund transfer between two corporate bank accounts  &#x60;\&quot;ppd\&quot;&#x60; - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  &#x60;\&quot;web\&quot;&#x60; - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver | must be one of ["ccd", "ppd", "web", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

