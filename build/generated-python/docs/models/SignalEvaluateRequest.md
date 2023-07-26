# plaid.model.signal_evaluate_request.SignalEvaluateRequest

SignalEvaluateRequest defines the request schema for `/signal/evaluate`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SignalEvaluateRequest defines the request schema for &#x60;/signal/evaluate&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The access token associated with the Item data is being requested for. | 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The transaction amount, in USD (e.g. &#x60;102.05&#x60;) | value must be a 64 bit float
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; of the account that is the funding source for the proposed transaction. The &#x60;account_id&#x60; is returned in the &#x60;/accounts/get&#x60; endpoint as well as the [&#x60;onSuccess&#x60;](/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id) callback metadata.  This will return an [&#x60;INVALID_ACCOUNT_ID&#x60;](/docs/errors/invalid-input/#invalid_account_id) error if the account has been removed at the bank or if the &#x60;account_id&#x60; is no longer valid. | 
**client_transaction_id** | str,  | str,  | The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**user_present** | None, bool,  | NoneClass, BoolClass,  | &#x60;true&#x60; if the end user is present while initiating the ACH transfer and the endpoint is being called; &#x60;false&#x60; otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing). | [optional] 
**client_user_id** | str,  | str,  | A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. Personally identifiable information, such as an email address or phone number, should not be used in the &#x60;client_user_id&#x60;. | [optional] 
**is_recurring** | None, bool,  | NoneClass, BoolClass,  | &#x60;true&#x60; if the ACH transaction is a recurring transaction; &#x60;false&#x60; otherwise  | [optional] 
**default_payment_method** | None, str,  | NoneClass, str,  | The default ACH or non-ACH payment method to complete the transaction. &#x60;SAME_DAY_ACH&#x60;: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day &#x60;NEXT_DAY_ACH&#x60;: Next Day ACH settlement for debit transactions, offered by some payment processors &#x60;STANDARD_ACH&#x60;: standard ACH by NACHA &#x60;REAL_TIME_PAYMENTS&#x60;: real-time payments such as RTP and FedNow &#x60;DEBIT_CARD&#x60;: if the default payment is over debit card networks &#x60;MULTIPLE_PAYMENT_METHODS&#x60;: if there is no default debit rail or there are multiple payment methods Possible values:  &#x60;SAME_DAY_ACH&#x60;, &#x60;NEXT_DAY_ACH&#x60;, &#x60;STANDARD_ACH&#x60;, &#x60;REAL_TIME_PAYMENTS&#x60;, &#x60;DEBIT_CARD&#x60;, &#x60;MULTIPLE_PAYMENT_METHODS&#x60; | [optional] 
**user** | [**SignalUser**](SignalUser.md) | [**SignalUser**](SignalUser.md) |  | [optional] 
**device** | [**SignalDevice**](SignalDevice.md) | [**SignalDevice**](SignalDevice.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
