# SignalDecisionOutcome

The payment decision from the risk assessment.  `APPROVE`: approve the transaction without requiring further actions from your customers. For example, use this field if you are placing a standard hold for all the approved transactions before making funds available to your customers. You should also use this field if you decide to accelerate the fund availability for your customers.  `REVIEW`: the transaction requires manual review  `REJECT`: reject the transaction  `TAKE_OTHER_RISK_MEASURES`: for example, placing a longer hold on funds than those approved transactions or introducing customer frictions such as step-up verification/authentication  `NOT_EVALUATED`: if only logging the Signal results without using them  Possible values:  `APPROVE`, `REVIEW`, `REJECT`, `TAKE_OTHER_RISK_MEASURES`, `NOT_EVALUATED` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The payment decision from the risk assessment.  &#x60;APPROVE&#x60;: approve the transaction without requiring further actions from your customers. For example, use this field if you are placing a standard hold for all the approved transactions before making funds available to your customers. You should also use this field if you decide to accelerate the fund availability for your customers.  &#x60;REVIEW&#x60;: the transaction requires manual review  &#x60;REJECT&#x60;: reject the transaction  &#x60;TAKE_OTHER_RISK_MEASURES&#x60;: for example, placing a longer hold on funds than those approved transactions or introducing customer frictions such as step-up verification/authentication  &#x60;NOT_EVALUATED&#x60;: if only logging the Signal results without using them  Possible values:  &#x60;APPROVE&#x60;, &#x60;REVIEW&#x60;, &#x60;REJECT&#x60;, &#x60;TAKE_OTHER_RISK_MEASURES&#x60;, &#x60;NOT_EVALUATED&#x60;  |  must be one of ["APPROVE", "REVIEW", "REJECT", "TAKE_OTHER_RISK_MEASURES", "NOT_EVALUATED", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


