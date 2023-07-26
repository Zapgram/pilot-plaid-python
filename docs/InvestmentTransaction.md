# InvestmentTransaction

A transaction within an investment account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investment_transaction_id** | **str** | The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the &#x60;investment_transaction_id&#x60; is case sensitive. | 
**account_id** | **str** | The &#x60;account_id&#x60; of the account against which this transaction posted. | 
**security_id** | **str, none_type** | The &#x60;security_id&#x60; to which this transaction is related. | 
**date** | **date** | The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction. | 
**name** | **str** | The institution’s description of the transaction. | 
**quantity** | **float** | The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions. | 
**amount** | **float** | The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities. | 
**price** | **float** | The price of the security at which this transaction occurred. | 
**fees** | **float, none_type** | The combined value of all fees applied to this transaction | 
**type** | [**InvestmentTransactionType**](InvestmentTransactionType.md) |  | 
**subtype** | [**InvestmentTransactionSubtype**](InvestmentTransactionSubtype.md) |  | 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**cancel_transaction_id** | **str, none_type** | A legacy field formerly used internally by Plaid to identify certain canceled transactions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


