# ProcessorSignalDecisionReportRequest

ProcessorSignalDecisionReportRequest defines the request schema for `/processor/signal/decision/report`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_token** | **str** | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**client_transaction_id** | **str** | Must be the same as the &#x60;client_transaction_id&#x60; supplied when calling &#x60;/signal/evaluate&#x60; | 
**initiated** | **bool** | &#x60;true&#x60; if the ACH transaction was initiated, &#x60;false&#x60; otherwise.  This field must be returned as a boolean. If formatted incorrectly, this will result in an [&#x60;INVALID_FIELD&#x60;](/docs/errors/invalid-request/#invalid_field) error. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**days_funds_on_hold** | **int, none_type** | The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.  For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization. | [optional] 
**decision_outcome** | [**SignalDecisionOutcome**](SignalDecisionOutcome.md) |  | [optional] 
**payment_method** | [**SignalPaymentMethod**](SignalPaymentMethod.md) |  | [optional] 
**amount_instantly_available** | **float, none_type** | The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


