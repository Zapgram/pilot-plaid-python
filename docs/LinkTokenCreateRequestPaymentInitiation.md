# LinkTokenCreateRequestPaymentInitiation

Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. Either `payment_id` or `consent_id` must be provided.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The &#x60;payment_id&#x60; provided by the &#x60;/payment_initiation/payment/create&#x60; endpoint. | [optional] 
**consent_id** | **str** | The &#x60;consent_id&#x60; provided by the &#x60;/payment_initiation/consent/create&#x60; endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


