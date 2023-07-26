# plaid.model.override_accounts.OverrideAccounts

Data to use to set values of test accounts. Some values cannot be specified in the schema and will instead will be calculated from other test data in order to achieve more consistent, realistic test data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data to use to set values of test accounts. Some values cannot be specified in the schema and will instead will be calculated from other test data in order to achieve more consistent, realistic test data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subtype** | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 
**identity** | [**OwnerOverride**](OwnerOverride.md) | [**OwnerOverride**](OwnerOverride.md) |  | 
**inflow_model** | [**InflowModel**](InflowModel.md) | [**InflowModel**](InflowModel.md) |  | 
**liability** | [**LiabilityOverride**](LiabilityOverride.md) | [**LiabilityOverride**](LiabilityOverride.md) |  | 
**meta** | [**Meta**](Meta.md) | [**Meta**](Meta.md) |  | 
**numbers** | [**Numbers**](Numbers.md) | [**Numbers**](Numbers.md) |  | 
**currency** | str,  | str,  | ISO-4217 currency code. If provided, the account will be denominated in the given currency. Transactions will also be in this currency by default. | 
**force_available_balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | If provided, the account will always have this amount as its  available balance, regardless of current balance or changes in transactions over time. | value must be a 64 bit float
**[transactions](#transactions)** | list, tuple,  | tuple,  | Specify the list of transactions on the account. | 
**type** | [**OverrideAccountType**](OverrideAccountType.md) | [**OverrideAccountType**](OverrideAccountType.md) |  | 
**starting_balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | If provided, the account will start with this amount as the current balance.  | value must be a 64 bit float
**holdings** | [**HoldingsOverride**](HoldingsOverride.md) | [**HoldingsOverride**](HoldingsOverride.md) |  | [optional] 
**investment_transactions** | [**InvestmentsTransactionsOverride**](InvestmentsTransactionsOverride.md) | [**InvestmentsTransactionsOverride**](InvestmentsTransactionsOverride.md) |  | [optional] 
**income** | [**IncomeOverride**](IncomeOverride.md) | [**IncomeOverride**](IncomeOverride.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

Specify the list of transactions on the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specify the list of transactions on the account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionOverride**](TransactionOverride.md) | [**TransactionOverride**](TransactionOverride.md) | [**TransactionOverride**](TransactionOverride.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

