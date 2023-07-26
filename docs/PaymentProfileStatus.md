# PaymentProfileStatus

The status of the given Payment Profile.  `READY`: This Payment Profile is ready to be used to create transfers using `/transfer/authorization/create` and `/transfer/create`.  `PENDING`: This Payment Profile is not ready to be used. You’ll need to call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field to initiate the account linking experience.  `REMOVED`: This Payment Profile has been removed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the given Payment Profile.  &#x60;READY&#x60;: This Payment Profile is ready to be used to create transfers using &#x60;/transfer/authorization/create&#x60; and &#x60;/transfer/create&#x60;.  &#x60;PENDING&#x60;: This Payment Profile is not ready to be used. You’ll need to call &#x60;/link/token/create&#x60; and provide the &#x60;payment_profile_token&#x60; in the &#x60;transfer.payment_profile_token&#x60; field to initiate the account linking experience.  &#x60;REMOVED&#x60;: This Payment Profile has been removed. |  must be one of ["PENDING", "READY", "REMOVED", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


