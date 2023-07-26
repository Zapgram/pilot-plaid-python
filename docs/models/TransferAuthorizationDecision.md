# plaid.model.transfer_authorization_decision.TransferAuthorizationDecision

A decision regarding the proposed transfer.  `approved` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `ITEM_LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.  `declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A decision regarding the proposed transfer.  &#x60;approved&#x60; – The proposed transfer has received the end user&#x27;s consent and has been approved for processing by Plaid. The &#x60;decision_rationale&#x60; field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when &#x60;decision_rationale.code&#x60; is &#x60;ITEM_LOGIN_REQUIRED&#x60;). Refer to the &#x60;code&#x60; field in the &#x60;decision_rationale&#x60; object for details.  &#x60;declined&#x60; – Plaid reviewed the proposed transfer and declined processing. Refer to the &#x60;code&#x60; field in the &#x60;decision_rationale&#x60; object for details. | must be one of ["approved", "declined", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

