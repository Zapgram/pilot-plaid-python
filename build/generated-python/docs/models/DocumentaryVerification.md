# plaid.model.documentary_verification.DocumentaryVerification

Data, images, analysis, and results from the `documentary_verification` step. This field will be `null` unless `steps.documentary_verification` has reached a terminal state of either `success` or `failed`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Data, images, analysis, and results from the &#x60;documentary_verification&#x60; step. This field will be &#x60;null&#x60; unless &#x60;steps.documentary_verification&#x60; has reached a terminal state of either &#x60;success&#x60; or &#x60;failed&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[documents](#documents)** | list, tuple,  | tuple,  | An array of documents submitted to the &#x60;documentary_verification&#x60; step. Each entry represents one user submission, where each submission will contain both a front and back image, or just a front image, depending on the document type.  Note: Plaid will automatically let a user submit a new set of document images up to three times if we detect that a previous attempt might have failed due to user error. For example, if the first set of document images are blurry or obscured by glare, the user will be asked to capture their documents again, resulting in at least two separate entries within &#x60;documents&#x60;. If the overall &#x60;documentary_verification&#x60; is &#x60;failed&#x60;, the user has exhausted their retry attempts. | 
**status** | str,  | str,  | The outcome status for the associated Identity Verification attempt&#x27;s &#x60;documentary_verification&#x60; step. This field will always have the same value as &#x60;steps.documentary_verification&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# documents

An array of documents submitted to the `documentary_verification` step. Each entry represents one user submission, where each submission will contain both a front and back image, or just a front image, depending on the document type.  Note: Plaid will automatically let a user submit a new set of document images up to three times if we detect that a previous attempt might have failed due to user error. For example, if the first set of document images are blurry or obscured by glare, the user will be asked to capture their documents again, resulting in at least two separate entries within `documents`. If the overall `documentary_verification` is `failed`, the user has exhausted their retry attempts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of documents submitted to the &#x60;documentary_verification&#x60; step. Each entry represents one user submission, where each submission will contain both a front and back image, or just a front image, depending on the document type.  Note: Plaid will automatically let a user submit a new set of document images up to three times if we detect that a previous attempt might have failed due to user error. For example, if the first set of document images are blurry or obscured by glare, the user will be asked to capture their documents again, resulting in at least two separate entries within &#x60;documents&#x60;. If the overall &#x60;documentary_verification&#x60; is &#x60;failed&#x60;, the user has exhausted their retry attempts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DocumentaryVerificationDocument**](DocumentaryVerificationDocument.md) | [**DocumentaryVerificationDocument**](DocumentaryVerificationDocument.md) | [**DocumentaryVerificationDocument**](DocumentaryVerificationDocument.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

