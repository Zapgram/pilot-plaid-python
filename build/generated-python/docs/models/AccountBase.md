# plaid.model.account_base.AccountBase

A single account at a financial institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A single account at a financial institution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**official_name** | None, str,  | NoneClass, str,  | The official name of the account as given by the financial institution | 
**balances** | [**AccountBalance**](AccountBalance.md) | [**AccountBalance**](AccountBalance.md) |  | 
**account_id** | str,  | str,  | Plaid’s unique identifier for the account. This value will not change unless Plaid can&#x27;t reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new &#x60;account_id&#x60; will be assigned to the account.  The &#x60;account_id&#x60; can also change if the &#x60;access_token&#x60; is deleted and the same credentials that were used to generate that &#x60;access_token&#x60; are used to generate a new &#x60;access_token&#x60; on a later date. In that case, the new &#x60;account_id&#x60; will be different from the old &#x60;account_id&#x60;.  If an account with a specific &#x60;account_id&#x60; disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.  Like all Plaid identifiers, the &#x60;account_id&#x60; is case sensitive. | 
**subtype** | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | 
**name** | str,  | str,  | The name of the account, either assigned by the user or by the financial institution itself | 
**type** | [**AccountType**](AccountType.md) | [**AccountType**](AccountType.md) |  | 
**mask** | None, str,  | NoneClass, str,  | The last 2-4 alphanumeric characters of an account&#x27;s official account number. Note that the mask may be non-unique between an Item&#x27;s accounts, and it may also not match the mask that the bank displays to the user. | 
**verification_status** | str,  | str,  | The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.  &#x60;pending_automatic_verification&#x60;: The Item is pending automatic verification  &#x60;pending_manual_verification&#x60;: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the micro-deposit.  &#x60;automatically_verified&#x60;: The Item has successfully been automatically verified   &#x60;manually_verified&#x60;: The Item has successfully been manually verified  &#x60;verification_expired&#x60;: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.  &#x60;verification_failed&#x60;: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.    | [optional] must be one of ["automatically_verified", "pending_automatic_verification", "pending_manual_verification", "manually_verified", "verification_expired", "verification_failed", ] 
**persistent_account_id** | str,  | str,  | A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account across different Items for depository accounts. This is currently an opt-in field and only supported for Chase Items. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

