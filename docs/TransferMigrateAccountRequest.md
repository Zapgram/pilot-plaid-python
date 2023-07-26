# TransferMigrateAccountRequest

Defines the request schema for `/transfer/migrate_account`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The user&#39;s account number. | 
**routing_number** | **str** | The user&#39;s routing number. | 
**account_type** | **str** | The type of the bank account (&#x60;checking&#x60; or &#x60;savings&#x60;). | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**wire_routing_number** | **str** | The user&#39;s wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in &#x60;routing_number&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


