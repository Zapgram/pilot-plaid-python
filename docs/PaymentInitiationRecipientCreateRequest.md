# PaymentInitiationRecipientCreateRequest

PaymentInitiationRecipientCreateRequest defines the request schema for `/payment_initiation/recipient/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required. | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


