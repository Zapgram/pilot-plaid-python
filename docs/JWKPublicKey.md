# JWKPublicKey

A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | The alg member identifies the cryptographic algorithm family used with the key. | 
**crv** | **str** | The crv member identifies the cryptographic curve used with the key. | 
**kid** | **str** | The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover. | 
**kty** | **str** | The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC. | 
**use** | **str** | The use (public key use) parameter identifies the intended use of the public key. | 
**x** | **str** | The x member contains the x coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate&#39;s big endian representation. | 
**y** | **str** | The y member contains the y coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate&#39;s big endian representation. | 
**created_at** | **int** | The timestamp when the key was created, in Unix time. | 
**expired_at** | **int, none_type** | The timestamp when the key expired, in Unix time. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


