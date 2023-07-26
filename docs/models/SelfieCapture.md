# plaid.model.selfie_capture.SelfieCapture

The image or video capture of a selfie. Only one of image or video URL will be populated per selfie.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The image or video capture of a selfie. Only one of image or video URL will be populated per selfie. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**video_url** | [**SelfieCaptureVideoURL**](SelfieCaptureVideoURL.md) | [**SelfieCaptureVideoURL**](SelfieCaptureVideoURL.md) |  | 
**image_url** | [**SelfieCaptureImageURL**](SelfieCaptureImageURL.md) | [**SelfieCaptureImageURL**](SelfieCaptureImageURL.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

