# RiskCheckBehaviorUserInteractionsLabel

Field describing the overall user interaction signals of a behavior risk check. This value represents how familiar the user is with the personal data they provide, based on a number of signals that are collected during their session.  `genuine` indicates the user has high familiarity with the data they are providing, and that fraud is unlikely.  `neutral` indicates some signals are present in between `risky` and `genuine`, but there are not enough clear signals to determine an outcome.  `risky` indicates the user has low familiarity with the data they are providing, and that fraud is likely.  `no_data` indicates there is not sufficient information to give an accurate signal.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Field describing the overall user interaction signals of a behavior risk check. This value represents how familiar the user is with the personal data they provide, based on a number of signals that are collected during their session.  &#x60;genuine&#x60; indicates the user has high familiarity with the data they are providing, and that fraud is unlikely.  &#x60;neutral&#x60; indicates some signals are present in between &#x60;risky&#x60; and &#x60;genuine&#x60;, but there are not enough clear signals to determine an outcome.  &#x60;risky&#x60; indicates the user has low familiarity with the data they are providing, and that fraud is likely.  &#x60;no_data&#x60; indicates there is not sufficient information to give an accurate signal. |  must be one of ["genuine", "neutral", "risky", "no_data", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


