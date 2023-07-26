# plaid.model.transfer_credit_usage_configuration.TransferCreditUsageConfiguration

Specifies the originator's expected usage of credits. For all dollar amounts, use a decimal string with two digits of precision e.g. \"10.00\". This field is required if the originator is expected to process credit transfers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Specifies the originator&#x27;s expected usage of credits. For all dollar amounts, use a decimal string with two digits of precision e.g. \&quot;10.00\&quot;. This field is required if the originator is expected to process credit transfers. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expected_monthly_amount** | str,  | str,  | The originator’s monthly expected ACH credit processing amount for the next 6-12 months. | 
**expected_frequency** | [**OriginatorExpectedTransferFrequency**](OriginatorExpectedTransferFrequency.md) | [**OriginatorExpectedTransferFrequency**](OriginatorExpectedTransferFrequency.md) |  | 
**expected_average_amount** | str,  | str,  | The originator’s expected average amount per credit. | 
**[sec_codes](#sec_codes)** | list, tuple,  | tuple,  | Specifies the expected use cases for the originator’s credit transfers. This should be a list that contains one or more of the following codes:  &#x60;\&quot;ccd\&quot;&#x60; - Corporate Credit or Debit - fund transfer between two corporate bank accounts  &#x60;\&quot;ppd\&quot;&#x60; - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  &#x60;\&quot;web\&quot;&#x60; - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver | 
**expected_highest_amount** | str,  | str,  | The originator’s expected highest amount for a single credit transfer. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sec_codes

Specifies the expected use cases for the originator’s credit transfers. This should be a list that contains one or more of the following codes:  `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts  `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  `\"web\"` - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specifies the expected use cases for the originator’s credit transfers. This should be a list that contains one or more of the following codes:  &#x60;\&quot;ccd\&quot;&#x60; - Corporate Credit or Debit - fund transfer between two corporate bank accounts  &#x60;\&quot;ppd\&quot;&#x60; - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment  &#x60;\&quot;web\&quot;&#x60; - A credit Entry initiated by or on behalf of a holder of a Consumer Account that is intended for a Consumer Account of a Receiver | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditACHClass**](CreditACHClass.md) | [**CreditACHClass**](CreditACHClass.md) | [**CreditACHClass**](CreditACHClass.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

