# plaid.model.image_quality.ImageQuality

A high level description of the quality of the image the user submitted.  For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.  Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we attribute the failure to low image quality.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A high level description of the quality of the image the user submitted.  For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.  Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we attribute the failure to low image quality. | must be one of ["high", "medium", "low", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

