# TransferAuthorizationIdempotencyKey

A random key provided by the client, per unique authorization, which expires after 48 hours. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.  This idempotency key expires after 48 hours, after which the same key can be reused. Failure to provide this key may result in duplicate charges.  Required for guaranteed ACH customers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A random key provided by the client, per unique authorization, which expires after 48 hours. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.  This idempotency key expires after 48 hours, after which the same key can be reused. Failure to provide this key may result in duplicate charges.  Required for guaranteed ACH customers. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


