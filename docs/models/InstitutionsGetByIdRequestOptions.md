# plaid.model.institutions_get_by_id_request_options.InstitutionsGetByIdRequestOptions

Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies optional parameters for &#x60;/institutions/get_by_id&#x60;. If provided, must not be &#x60;null&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**include_optional_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, return an institution&#x27;s logo, brand color, and URL. When available, the bank&#x27;s logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is &#x60;false&#x60;.  Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos. | [optional] if omitted the server will use the default value of False
**include_status** | bool,  | BoolClass,  | If &#x60;true&#x60;, the response will include status information about the institution. Default value is &#x60;false&#x60;. | [optional] if omitted the server will use the default value of False
**include_auth_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional] if omitted the server will use the default value of False
**include_payment_initiation_metadata** | bool,  | BoolClass,  | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

