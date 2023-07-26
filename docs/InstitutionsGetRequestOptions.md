# InstitutionsGetRequestOptions

An optional object to filter `/institutions/get` results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**[Products], none_type**](Products.md) | Filter the Institutions based on which products they support.  | [optional] 
**routing_numbers** | **[str], none_type** | Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid. | [optional] 
**oauth** | **bool, none_type** | Limit results to institutions with or without OAuth login flows. Note that institutions will have &#x60;oauth&#x60; set to &#x60;true&#x60; if some Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth will have the &#x60;oauth&#x60; attribute set to &#x60;true&#x60;. | [optional] 
**include_optional_metadata** | **bool** | When &#x60;true&#x60;, return the institution&#39;s homepage URL, logo and primary brand color.  Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos. | [optional] 
**include_auth_metadata** | **bool** | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional]  if omitted the server will use the default value of False
**include_payment_initiation_metadata** | **bool** | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


