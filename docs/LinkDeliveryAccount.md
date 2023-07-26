# LinkDeliveryAccount

Information related to account attached to the connected Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Plaid &#x60;account_id&#x60; | [optional] 
**name** | **str** | The official account name | [optional] 
**mask** | **str** | The last 2-4 alphanumeric characters of an account&#39;s official account number. Note that the mask may be non-unique between an Item&#39;s accounts. It may also not match the mask that the bank displays to the user. | [optional] 
**type** | **str** | The account type. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values | [optional] 
**subtype** | **str** | The account subtype. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values | [optional] 
**verification_status** | [**LinkDeliveryVerificationStatus**](LinkDeliveryVerificationStatus.md) |  | [optional] 
**class_type** | **str** | If micro-deposit verification is being used, indicates whether the account being verified is a &#x60;business&#x60; or &#x60;personal&#x60; account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


