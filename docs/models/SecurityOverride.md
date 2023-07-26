# plaid.model.security_override.SecurityOverride

Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (&#x60;ticker_symbol&#x60;, &#x60;cusip&#x60;, &#x60;isin&#x60;, or &#x60;sedol&#x60;) are required. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isin** | str,  | str,  | 12-character ISIN, a globally unique securities identifier. Please note that Plaid&#x27;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | [optional] 
**cusip** | str,  | str,  | 9-character CUSIP, an identifier assigned to North American securities. Please note that Plaid&#x27;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | [optional] 
**sedol** | str,  | str,  | 7-character SEDOL, an identifier assigned to securities in the UK. | [optional] 
**name** | str,  | str,  | A descriptive name for the security, suitable for display. | [optional] 
**ticker_symbol** | str,  | str,  | The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available. | [optional] 
**currency** | str,  | str,  | Either a valid &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

