# plaid.model.jwk_public_key.JWKPublicKey

A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kty** | str,  | str,  | The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC. | 
**crv** | str,  | str,  | The crv member identifies the cryptographic curve used with the key. | 
**use** | str,  | str,  | The use (public key use) parameter identifies the intended use of the public key. | 
**kid** | str,  | str,  | The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover. | 
**x** | str,  | str,  | The x member contains the x coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate&#x27;s big endian representation. | 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp when the key was created, in Unix time. | 
**y** | str,  | str,  | The y member contains the y coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate&#x27;s big endian representation. | 
**expired_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The timestamp when the key expired, in Unix time. | 
**alg** | str,  | str,  | The alg member identifies the cryptographic algorithm family used with the key. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

