# plaid.model.payment_initiation_consent_constraints.PaymentInitiationConsentConstraints

Limitations that will be applied to payments initiated using the payment consent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limitations that will be applied to payments initiated using the payment consent. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[periodic_amounts](#periodic_amounts)** | list, tuple,  | tuple,  | A list of amount limitations per period of time. | 
**max_payment_amount** | [**PaymentConsentMaxPaymentAmount**](PaymentConsentMaxPaymentAmount.md) | [**PaymentConsentMaxPaymentAmount**](PaymentConsentMaxPaymentAmount.md) |  | 
**valid_date_time** | [**PaymentConsentValidDateTime**](PaymentConsentValidDateTime.md) | [**PaymentConsentValidDateTime**](PaymentConsentValidDateTime.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# periodic_amounts

A list of amount limitations per period of time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of amount limitations per period of time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentConsentPeriodicAmount**](PaymentConsentPeriodicAmount.md) | [**PaymentConsentPeriodicAmount**](PaymentConsentPeriodicAmount.md) | [**PaymentConsentPeriodicAmount**](PaymentConsentPeriodicAmount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

