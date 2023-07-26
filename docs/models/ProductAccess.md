# plaid.model.product_access.ProductAccess

The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statements** | None, bool,  | NoneClass, BoolClass,  | Allow access to statements. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**identity** | None, bool,  | NoneClass, BoolClass,  | Allow access to the Identity product (name, email, phone, address). Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**auth** | None, bool,  | NoneClass, BoolClass,  | Allow access to account number details. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**transactions** | None, bool,  | NoneClass, BoolClass,  | Allow access to transaction details. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**accounts_details_transactions** | None, bool,  | NoneClass, BoolClass,  | Allow access to \&quot;accounts_details_transactions\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**accounts_routing_number** | None, bool,  | NoneClass, BoolClass,  | Allow access to \&quot;accounts_routing_number\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**accounts_statements** | None, bool,  | NoneClass, BoolClass,  | Allow access to \&quot;accounts_statements\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**accounts_tax_statements** | None, bool,  | NoneClass, BoolClass,  | Allow access to \&quot;accounts_tax_statements\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**customers_profiles** | None, bool,  | NoneClass, BoolClass,  | Allow access to \&quot;customers_profiles\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

