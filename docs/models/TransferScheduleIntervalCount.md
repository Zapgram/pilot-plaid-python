# plaid.model.transfer_schedule_interval_count.TransferScheduleIntervalCount

The number of recurring `interval_units` between originations. The recurring interval(before holiday adjustment) is calculated by multiplying `interval_unit` and `interval_count`. For instance, to schedule a recurring transfer which originates once every two weeks, set `interval_unit` = `week` and `interval_count` = 2.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The number of recurring &#x60;interval_units&#x60; between originations. The recurring interval(before holiday adjustment) is calculated by multiplying &#x60;interval_unit&#x60; and &#x60;interval_count&#x60;. For instance, to schedule a recurring transfer which originates once every two weeks, set &#x60;interval_unit&#x60; &#x3D; &#x60;week&#x60; and &#x60;interval_count&#x60; &#x3D; 2. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

