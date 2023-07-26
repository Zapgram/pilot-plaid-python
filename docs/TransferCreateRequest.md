# TransferCreateRequest

Defines the request schema for `/transfer/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_id** | **str** | Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier. | 
**description** | **str** | The transfer description. Maximum of 15 characters. If reprocessing a returned transfer, please note that the &#x60;description&#x60; field must be &#x60;\&quot;Retry\&quot;&#x60; to indicate that it&#39;s a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code &#x60;R01&#x60; or &#x60;R09&#x60; may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes). | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**idempotency_key** | [**TransferCreateIdempotencyKey**](TransferCreateIdempotencyKey.md) |  | [optional] 
**access_token** | **str** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | [optional] 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an &#x60;access_token&#x60;. | [optional] 
**payment_profile_token** | **str** | The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using &#x60;access_token&#x60;. | [optional] 
**type** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**network** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | [optional] 
**ach_class** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**user** | [**TransferUserInRequestDeprecated**](TransferUserInRequestDeprecated.md) |  | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**origination_account_id** | **str, none_type** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank. | [optional] 
**iso_currency_code** | **str** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**test_clock_id** | **str, none_type** | Plaid’s unique identifier for a test clock. This field may only be used when using &#x60;sandbox&#x60; environment. If provided, the &#x60;transfer&#x60; is created at the &#x60;virtual_time&#x60; on the provided &#x60;test_clock&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


