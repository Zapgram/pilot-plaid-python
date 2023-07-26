# plaid.model.standalone_account_type.StandaloneAccountType

The schema below describes the various `types` and corresponding `subtypes` that Plaid recognizes and reports for financial institution accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The schema below describes the various &#x60;types&#x60; and corresponding &#x60;subtypes&#x60; that Plaid recognizes and reports for financial institution accounts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**loan** | str,  | str,  | A loan type account. Supported products for &#x60;loan&#x60; accounts are: Balance, Liabilities, and Transactions. | 
**other** | str,  | str,  | Other or unknown account type. Supported products for &#x60;other&#x60; accounts are: Balance, Transactions, Identity, and Assets. | 
**investment** | str,  | str,  | An investment account. Supported products for &#x60;investment&#x60; accounts are: Balance and Investments. In API versions 2018-05-22 and earlier, this type is called &#x60;brokerage&#x60;. | 
**depository** | str,  | str,  | An account type holding cash, in which funds are deposited. Supported products for &#x60;depository&#x60; accounts are: Auth (&#x60;checking&#x60; and &#x60;savings&#x60; types only), Balance, Transactions, Identity, Payment Initiation, and Assets. | 
**credit** | str,  | str,  | A credit card type account. Supported products for &#x60;credit&#x60; accounts are: Balance, Transactions, Identity, and Liabilities. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

