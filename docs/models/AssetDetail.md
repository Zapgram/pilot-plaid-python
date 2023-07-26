# plaid.model.asset_detail.AssetDetail

Details about an asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about an asset. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AssetDaysRequestedCount** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days. | 
**AssetOwnershipType** | None, str,  | NoneClass, str,  | Ownership type of the asset account. | 
**AssetType** | [**AssetType**](AssetType.md) | [**AssetType**](AssetType.md) |  | 
**AssetAccountIdentifier** | str,  | str,  | A unique alphanumeric string identifying an asset. | 
**AssetDescription** | None, str,  | NoneClass, str,  | A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset. | 
**AssetAsOfDate** | str,  | str,  | Account Report As of Date / Create Date. Format YYYY-MM-DD | 
**AssetUniqueIdentifier** | str,  | str,  | A vendor created unique Identifier. | 
**AssetAvailableBalanceAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Asset Account Available Balance. | value must be a 64 bit float
**AssetCurrentBalanceAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | A vendor created unique Identifier | value must be a 64 bit float
**AssetTypeAdditionalDescription** | None, str,  | NoneClass, str,  | Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

