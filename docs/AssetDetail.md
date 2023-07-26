# AssetDetail

Details about an asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_unique_identifier** | **str** | A vendor created unique Identifier. | 
**asset_account_identifier** | **str** | A unique alphanumeric string identifying an asset. | 
**asset_as_of_date** | **str** | Account Report As of Date / Create Date. Format YYYY-MM-DD | 
**asset_description** | **str, none_type** | A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset. | 
**asset_available_balance_amount** | **float** | Asset Account Available Balance. | 
**asset_current_balance_amount** | **float** | A vendor created unique Identifier | 
**asset_type** | [**AssetType**](AssetType.md) |  | 
**asset_type_additional_description** | **str, none_type** | Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit. | 
**asset_days_requested_count** | **int** | The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days. | 
**asset_ownership_type** | **str, none_type** | Ownership type of the asset account. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


