# ExternalPaymentInitiationConsentOptions

Additional payment consent options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_refund_details** | **bool, none_type** | When &#x60;true&#x60;, Plaid will attempt to request refund details from the payee&#39;s financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the &#x60;/payment_initiation/payment/get&#x60; response. | [optional] 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the payer&#39;s account. Where possible, the end user will be able to set up payment consent using only the specified bank account if provided. | [optional] 
**bacs** | [**PaymentInitiationOptionalRestrictionBacs**](PaymentInitiationOptionalRestrictionBacs.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


