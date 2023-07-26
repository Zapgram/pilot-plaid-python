# TransferNetwork

The network or rails used for the transfer.  For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 9:30 AM Pacific Time and the cutoff for next-day transfers is 5:30 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The network or rails used for the transfer.  For transfers submitted as either &#x60;ach&#x60; or &#x60;same-day-ach&#x60; the cutoff for same-day is 9:30 AM Pacific Time and the cutoff for next-day transfers is 5:30 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as &#x60;same-day-ach&#x60; and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable. |  must be one of ["ach", "same-day-ach", "rtp", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


