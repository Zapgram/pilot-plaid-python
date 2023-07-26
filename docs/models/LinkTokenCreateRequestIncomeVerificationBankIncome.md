# plaid.model.link_token_create_request_income_verification_bank_income.LinkTokenCreateRequestIncomeVerificationBankIncome

Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with Bank Income. This field is required if &#x60;income_verification&#x60; is included in the &#x60;products&#x60; array and &#x60;bank&#x60; is specified in &#x60;income_source_types&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | The number of days of data to request for the Bank Income product | 
**enable_multiple_items** | None, bool,  | NoneClass, BoolClass,  | Whether to enable multiple Items to be added in the Link session | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

