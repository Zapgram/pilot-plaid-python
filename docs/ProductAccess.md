# ProductAccess

The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | **bool, none_type** | Allow access to statements. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**identity** | **bool, none_type** | Allow access to the Identity product (name, email, phone, address). Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**auth** | **bool, none_type** | Allow access to account number details. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**transactions** | **bool, none_type** | Allow access to transaction details. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**accounts_details_transactions** | **bool, none_type** | Allow access to \&quot;accounts_details_transactions\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**accounts_routing_number** | **bool, none_type** | Allow access to \&quot;accounts_routing_number\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**accounts_statements** | **bool, none_type** | Allow access to \&quot;accounts_statements\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**accounts_tax_statements** | **bool, none_type** | Allow access to \&quot;accounts_tax_statements\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**customers_profiles** | **bool, none_type** | Allow access to \&quot;customers_profiles\&quot;. Only used by certain partners. If relevant to the partner and unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


