# plaid.model.payment_initiation_consent_status.PaymentInitiationConsentStatus

The status of the payment consent.  `UNAUTHORISED`: Consent created, but requires user authorisation.  `REJECTED`: Consent authorisation was rejected by the user and/or the bank.  `AUTHORISED`: Consent is active and ready to be used.  `REVOKED`: Consent has been revoked and can no longer be used.  `EXPIRED`: Consent is no longer valid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The status of the payment consent.  &#x60;UNAUTHORISED&#x60;: Consent created, but requires user authorisation.  &#x60;REJECTED&#x60;: Consent authorisation was rejected by the user and/or the bank.  &#x60;AUTHORISED&#x60;: Consent is active and ready to be used.  &#x60;REVOKED&#x60;: Consent has been revoked and can no longer be used.  &#x60;EXPIRED&#x60;: Consent is no longer valid. | must be one of ["UNAUTHORISED", "AUTHORISED", "REVOKED", "REJECTED", "EXPIRED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

