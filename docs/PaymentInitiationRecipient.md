# PaymentInitiationRecipient

PaymentInitiationRecipient defines a payment initiation recipient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | The ID of the recipient. | 
**name** | **str** | The name of the recipient. | 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the recipient. | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


