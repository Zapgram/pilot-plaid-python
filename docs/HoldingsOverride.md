# HoldingsOverride

Specify the holdings on the account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_price** | **float** | The last price given by the institution for this security | 
**quantity** | **float** | The total quantity of the asset held, as reported by the financial institution. | 
**currency** | **str** | Either a valid &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | 
**security** | [**SecurityOverride**](SecurityOverride.md) |  | 
**institution_price_as_of** | **date** | The date at which &#x60;institution_price&#x60; was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date. | [optional] 
**cost_basis** | **float** | The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


