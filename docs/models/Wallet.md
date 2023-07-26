# plaid.model.wallet.Wallet

An object representing the e-wallet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the e-wallet | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wallet_id** | str,  | str,  | A unique ID identifying the e-wallet | 
**balance** | [**WalletBalance**](WalletBalance.md) | [**WalletBalance**](WalletBalance.md) |  | 
**numbers** | [**WalletNumbers**](WalletNumbers.md) | [**WalletNumbers**](WalletNumbers.md) |  | 
**status** | [**WalletStatus**](WalletStatus.md) | [**WalletStatus**](WalletStatus.md) |  | 
**recipient_id** | str,  | str,  | The ID of the recipient that corresponds to the e-wallet account numbers | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

