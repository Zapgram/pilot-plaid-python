# StandaloneInvestmentTransactionType

Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash will appear as negative amounts, outflow of cash will appear as positive amounts.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy** | **str** | Buying an investment | 
**sell** | **str** | Selling an investment | 
**cancel** | **str** | A cancellation of a pending transaction | 
**cash** | **str** | Activity that modifies a cash position | 
**fee** | **str** | Fees on the account, e.g. commission, bookkeeping, options-related. | 
**transfer** | **str** | Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


