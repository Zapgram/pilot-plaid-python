# plaid.model.payment_consent_valid_date_time.PaymentConsentValidDateTime

Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Life span for the payment consent. After the &#x60;to&#x60; date the payment consent expires and can no longer be used for payment initiation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | None, str, datetime,  | NoneClass, str,  | The date and time from which the consent should be active, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | [optional] value must conform to RFC-3339 date-time
**to** | None, str, datetime,  | NoneClass, str,  | The date and time at which the consent expires, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

