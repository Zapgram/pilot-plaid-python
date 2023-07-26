# plaid.model.link_token_create_request_payment_initiation.LinkTokenCreateRequestPaymentInitiation

Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. Either `payment_id` or `consent_id` must be provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if &#x60;payment_initiation&#x60; is included in the &#x60;products&#x60; array. Either &#x60;payment_id&#x60; or &#x60;consent_id&#x60; must be provided. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payment_id** | str,  | str,  | The &#x60;payment_id&#x60; provided by the &#x60;/payment_initiation/payment/create&#x60; endpoint. | [optional] 
**consent_id** | str,  | str,  | The &#x60;consent_id&#x60; provided by the &#x60;/payment_initiation/consent/create&#x60; endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

