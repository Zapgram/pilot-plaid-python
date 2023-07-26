# IssuingCountry

A binary match indicator specifying whether the country that issued the provided document matches the country that the user separately provided to Plaid.  Note: You can configure whether a `no_match` on `issuing_country` fails the `documentary_verification` by editing your Plaid Template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A binary match indicator specifying whether the country that issued the provided document matches the country that the user separately provided to Plaid.  Note: You can configure whether a &#x60;no_match&#x60; on &#x60;issuing_country&#x60; fails the &#x60;documentary_verification&#x60; by editing your Plaid Template. |  must be one of ["match", "no_match", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


