# plaid.model.credit_session_bank_income_status.CreditSessionBankIncomeStatus

Status of the Bank Income Link session.  `APPROVED`: User has approved and verified their income  `NO_DEPOSITS_FOUND`: We attempted, but were unable to find any income in the connected account.  `USER_REPORTED_NO_INCOME`: The user explicitly indicated that they don't receive income in the connected account.  `STARTED`: The user began the bank income portion of the link flow.  `INTERNAL_ERROR`: The user encountered an internal error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Status of the Bank Income Link session.  &#x60;APPROVED&#x60;: User has approved and verified their income  &#x60;NO_DEPOSITS_FOUND&#x60;: We attempted, but were unable to find any income in the connected account.  &#x60;USER_REPORTED_NO_INCOME&#x60;: The user explicitly indicated that they don&#x27;t receive income in the connected account.  &#x60;STARTED&#x60;: The user began the bank income portion of the link flow.  &#x60;INTERNAL_ERROR&#x60;: The user encountered an internal error. | must be one of ["APPROVED", "NO_DEPOSITS_FOUND", "USER_REPORTED_NO_INCOME", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

