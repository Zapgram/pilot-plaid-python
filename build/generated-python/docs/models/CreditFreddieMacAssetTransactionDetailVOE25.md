# plaid.model.credit_freddie_mac_asset_transaction_detail_voe25.CreditFreddieMacAssetTransactionDetailVOE25

Documentation not found in the MISMO model viewer and not provided by Freddie Mac.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Documentation not found in the MISMO model viewer and not provided by Freddie Mac. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AssetTransactionCategoryType** | [**AssetTransactionCategoryType**](AssetTransactionCategoryType.md) | [**AssetTransactionCategoryType**](AssetTransactionCategoryType.md) |  | 
**AssetTransactionPaidByName** | None, str,  | NoneClass, str,  | Populate with who did the transaction. | 
**AssetTransactionTypeAdditionalDescription** | None, str,  | NoneClass, str,  | FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee, interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer. | 
**AssetTransactionDate** | str, date,  | str,  | Asset Transaction Date. | value must conform to RFC-3339 full-date YYYY-MM-DD
**AssetTransactionPostDate** | str, date,  | str,  | Asset Transaction Post Date. | value must conform to RFC-3339 full-date YYYY-MM-DD
**AssetTransactionPaidToName** | None, str,  | NoneClass, str,  | Populate with for whom the transaction is done. | 
**AssetTransactionType** | [**AssetTransactionType**](AssetTransactionType.md) | [**AssetTransactionType**](AssetTransactionType.md) |  | 
**AssetTransactionUniqueIdentifier** | str,  | str,  | A vendor created unique Identifier. | 
**FinancialInstitutionTransactionIdentifier** | None, str,  | NoneClass, str,  | FI provided Transaction Identifier. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

