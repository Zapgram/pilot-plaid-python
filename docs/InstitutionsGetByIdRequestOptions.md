# InstitutionsGetByIdRequestOptions

Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_optional_metadata** | **bool** | When &#x60;true&#x60;, return an institution&#39;s logo, brand color, and URL. When available, the bank&#39;s logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is &#x60;false&#x60;.  Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos. | [optional]  if omitted the server will use the default value of False
**include_status** | **bool** | If &#x60;true&#x60;, the response will include status information about the institution. Default value is &#x60;false&#x60;. | [optional]  if omitted the server will use the default value of False
**include_auth_metadata** | **bool** | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional]  if omitted the server will use the default value of False
**include_payment_initiation_metadata** | **bool** | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


