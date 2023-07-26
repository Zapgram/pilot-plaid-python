# plaid.model.apr.APR

Information about the APR on the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the APR on the account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apr_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Annual Percentage Rate applied.  | value must be a 64 bit float
**apr_type** | str,  | str,  | The type of balance to which the APR applies. | must be one of ["balance_transfer_apr", "cash_apr", "purchase_apr", "special", ] 
**interest_charge_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of money charged due to interest from last statement. | value must be a 64 bit float
**balance_subject_to_apr** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of money that is subjected to the APR if a balance was carried beyond payment due date. How it is calculated can vary by card issuer. It is often calculated as an average daily balance. | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

