# plaid.model.transfer_recurring_create_request.TransferRecurringCreateRequest

Defines the request schema for `/transfer/recurring/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/recurring/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | 
**user_present** | None, bool,  | NoneClass, BoolClass,  | If the end user is initiating the specific transfer themselves via an interactive UI, this should be &#x60;true&#x60;; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be &#x60;false&#x60;. | 
**schedule** | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) |  | 
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an &#x60;access_token&#x60;. | 
**description** | str,  | str,  | The description of the recurring transfer. | 
**idempotency_key** | [**TransferRecurringIdempotencyKey**](TransferRecurringIdempotencyKey.md) | [**TransferRecurringIdempotencyKey**](TransferRecurringIdempotencyKey.md) |  | 
**type** | [**TransferType**](TransferType.md) | [**TransferType**](TransferType.md) |  | 
**device** | [**TransferDevice**](TransferDevice.md) | [**TransferDevice**](TransferDevice.md) |  | 
**user** | [**TransferUserInRequest**](TransferUserInRequest.md) | [**TransferUserInRequest**](TransferUserInRequest.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) | [**TransferNetwork**](TransferNetwork.md) |  | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**funding_account_id** | [**TransferFundingAccountIDRequest**](TransferFundingAccountIDRequest.md) | [**TransferFundingAccountIDRequest**](TransferFundingAccountIDRequest.md) |  | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**test_clock_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a test clock. This field may only be used when using &#x60;sandbox&#x60; environment. If provided, the created &#x60;recurring_transfer&#x60; is associated with the &#x60;test_clock&#x60;. New originations are automatically generated when the associated &#x60;test_clock&#x60; advances. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

