# plaid.model.recaptcha_required_error.RecaptchaRequiredError

The request was flagged by Plaid's fraud system, and requires additional verification to ensure they are not a bot.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request was flagged by Plaid&#x27;s fraud system, and requires additional verification to ensure they are not a bot. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**http_code** | str,  | str,  | 400 | 
**error_type** | str,  | str,  | RECAPTCHA_ERROR | 
**display_message** | str,  | str,  |  | 
**error_code** | str,  | str,  | RECAPTCHA_REQUIRED | 
**link_user_experience** | str,  | str,  | Your user will be prompted to solve a Google reCAPTCHA challenge in the Link Recaptcha pane. If they solve the challenge successfully, the user&#x27;s request is resubmitted and they are directed to the next Item creation step. | 
**common_causes** | str,  | str,  | Plaid&#x27;s fraud system detects abusive traffic and considers a variety of parameters throughout Item creation requests. When a request is considered risky or possibly fraudulent, Link presents a reCAPTCHA for the user to solve. | 
**troubleshooting_steps** | str,  | str,  | Link will automatically guide your user through reCAPTCHA verification. As a general rule, we recommend instrumenting basic fraud monitoring to detect and protect your website from spam and abuse.  If your user cannot verify their session, please submit a Support ticket with the following identifiers: &#x60;link_session_id&#x60; or &#x60;request_id&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

