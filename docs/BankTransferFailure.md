# BankTransferFailure

The failure reason if the type of this transfer is `\"failed\"` or `\"reversed\"`. Null value otherwise.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_return_code** | **str, none_type** | The ACH return code, e.g. &#x60;R01&#x60;.  A return code will be provided if and only if the transfer status is &#x60;reversed&#x60;. For a full listing of ACH return codes, see [Bank Transfers errors](https://plaid.com/docs/errors/bank-transfers/#ach-return-codes). | [optional] 
**description** | **str** | A human-readable description of the reason for the failure or reversal. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


