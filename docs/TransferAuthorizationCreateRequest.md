# TransferAuthorizationCreateRequest

Defines the request schema for `/transfer/authorization/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferType**](TransferType.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**user** | [**TransferAuthorizationUserInRequest**](TransferAuthorizationUserInRequest.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**access_token** | **str** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | [optional] 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an &#x60;access_token&#x60;. | [optional] 
**funding_account_id** | **str, none_type** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding. | [optional] 
**payment_profile_token** | **str** | The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using &#x60;access_token&#x60;. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**device** | [**TransferAuthorizationDevice**](TransferAuthorizationDevice.md) |  | [optional] 
**origination_account_id** | **str** | Plaid&#39;s unique identifier for the origination account for this authorization. If not specified, the default account will be used. | [optional] 
**iso_currency_code** | **str** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**idempotency_key** | [**TransferAuthorizationIdempotencyKey**](TransferAuthorizationIdempotencyKey.md) |  | [optional] 
**user_present** | **bool, none_type** | If the end user is initiating the specific transfer themselves via an interactive UI, this should be &#x60;true&#x60;; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be &#x60;false&#x60;. | [optional] 
**with_guarantee** | **bool, none_type** | If set to &#x60;false&#x60;, Plaid will not offer a &#x60;guarantee_decision&#x60; for this request (Guarantee customers only). | [optional]  if omitted the server will use the default value of True
**beacon_session_id** | **str, none_type** | The unique identifier returned by Plaid&#39;s [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. | [optional] 
**originator_client_id** | **str, none_type** | The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS). | [optional] 
**credit_funds_source** | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) |  | [optional] 
**test_clock_id** | **str, none_type** | Plaid’s unique identifier for a test clock. This field may only be used when using &#x60;sandbox&#x60; environment. If provided, the &#x60;authorization&#x60; is created at the &#x60;virtual_time&#x60; on the provided &#x60;test_clock&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


