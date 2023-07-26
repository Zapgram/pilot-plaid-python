# MatchSummaryCode

An enum indicating the match type between data provided by user and data checked against an external data source.   `match` indicates that the provided input data was a strong match against external data.  `partial_match` indicates the data approximately matched against external data. For example, \"Knope\" vs. \"Knope-Wyatt\" for last name.  `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.  `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.  `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | An enum indicating the match type between data provided by user and data checked against an external data source.   &#x60;match&#x60; indicates that the provided input data was a strong match against external data.  &#x60;partial_match&#x60; indicates the data approximately matched against external data. For example, \&quot;Knope\&quot; vs. \&quot;Knope-Wyatt\&quot; for last name.  &#x60;no_match&#x60; indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.  &#x60;no_data&#x60; indicates that Plaid was unable to find external data to compare against the provided input data.  &#x60;no_input&#x60; indicates that Plaid was unable to perform a check because no information was provided for this field by the end user. |  must be one of ["match", "partial_match", "no_match", "no_data", "no_input", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


