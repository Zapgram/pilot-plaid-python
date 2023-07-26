# plaid.model.transfer_authorization_proposed_transfer.TransferAuthorizationProposedTransfer

Details regarding the proposed transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details regarding the proposed transfer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**funding_account_id** | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) |  | 
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**originator_client_id** | None, str,  | NoneClass, str,  | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**credit_funds_source** | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) |  | 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | 
**origination_account_id** | str,  | str,  | Plaid&#x27;s unique identifier for the origination account that was used for this transfer. | 
**type** | [**TransferType**](TransferType.md) | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**network** | str,  | str,  | The network or rails used for the transfer. | 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

