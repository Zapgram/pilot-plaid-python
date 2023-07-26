# plaid.model.asset_report_add_ons.AssetReportAddOns

A list of add-ons that should be included in the Asset Report.  `fast_assets`: When Fast Assets is requested, Plaid will create two versions of the Asset Report: the Fast Asset Report, which will contain only Identity and Balance information, and the Full Asset Report, which will also contain Transactions information. A `PRODUCT_READY` webhook will be fired for each Asset Report when it is ready, and the `report_type` field will indicate whether the webhook is firing for the `full` or `fast` Asset Report. To retrieve the Fast Asset Report, call `/asset_report/get` with `fast_report` set to `true`. There is no additional charge for using Fast Assets.  `investments`: Request an Asset Report with Investments. This add-on is in closed beta and not generally available.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A list of add-ons that should be included in the Asset Report.  &#x60;fast_assets&#x60;: When Fast Assets is requested, Plaid will create two versions of the Asset Report: the Fast Asset Report, which will contain only Identity and Balance information, and the Full Asset Report, which will also contain Transactions information. A &#x60;PRODUCT_READY&#x60; webhook will be fired for each Asset Report when it is ready, and the &#x60;report_type&#x60; field will indicate whether the webhook is firing for the &#x60;full&#x60; or &#x60;fast&#x60; Asset Report. To retrieve the Fast Asset Report, call &#x60;/asset_report/get&#x60; with &#x60;fast_report&#x60; set to &#x60;true&#x60;. There is no additional charge for using Fast Assets.  &#x60;investments&#x60;: Request an Asset Report with Investments. This add-on is in closed beta and not generally available. | must be one of ["investments", "fast_assets", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

