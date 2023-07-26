# plaid.model.signal_decision_report_request.SignalDecisionReportRequest

SignalDecisionReportRequest defines the request schema for `/signal/decision/report`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SignalDecisionReportRequest defines the request schema for &#x60;/signal/decision/report&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**initiated** | bool,  | BoolClass,  | &#x60;true&#x60; if the ACH transaction was initiated, &#x60;false&#x60; otherwise.  This field must be returned as a boolean. If formatted incorrectly, this will result in an [&#x60;INVALID_FIELD&#x60;](/docs/errors/invalid-request/#invalid_field) error. | 
**client_transaction_id** | str,  | str,  | Must be the same as the &#x60;client_transaction_id&#x60; supplied when calling &#x60;/signal/evaluate&#x60; | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**days_funds_on_hold** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.  For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization. | [optional] 
**decision_outcome** | [**SignalDecisionOutcome**](SignalDecisionOutcome.md) | [**SignalDecisionOutcome**](SignalDecisionOutcome.md) |  | [optional] 
**payment_method** | [**SignalPaymentMethod**](SignalPaymentMethod.md) | [**SignalPaymentMethod**](SignalPaymentMethod.md) |  | [optional] 
**amount_instantly_available** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05). | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

