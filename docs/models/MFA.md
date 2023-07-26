# plaid.model.mfa.MFA

Specifies the multi-factor authentication settings to use with this test account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies the multi-factor authentication settings to use with this test account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**question_rounds** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of rounds of questions. Required if value of &#x60;type&#x60; is &#x60;questions&#x60;.  | 
**selections_per_question** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of available answers per question, used if &#x60;type&#x60; is &#x60;selection&#x60;. Defaults to 2.  | 
**type** | str,  | str,  | Possible values are &#x60;device&#x60;, &#x60;selections&#x60;, or &#x60;questions&#x60;.  If value is &#x60;device&#x60;, the MFA answer is &#x60;1234&#x60;.  If value is &#x60;selections&#x60;, the MFA answer is always the first option.  If value is &#x60;questions&#x60;, the MFA answer is  &#x60;answer_&lt;i&gt;_&lt;j&gt;&#x60; for the j-th question in the i-th round, starting from 0. For example, the answer to the first question in the second round is &#x60;answer_1_0&#x60;. | 
**questions_per_round** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of questions per round. Required if value of &#x60;type&#x60; is &#x60;questions&#x60;. If value of type is &#x60;selections&#x60;, default value is 2. | 
**selection_rounds** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of rounds of selections, used if &#x60;type&#x60; is &#x60;selections&#x60;. Defaults to 1. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

