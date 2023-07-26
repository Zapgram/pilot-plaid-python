# plaid.model.document_authenticity_match_code.DocumentAuthenticityMatchCode

High level summary of whether the document in the provided image matches the formatting rules and security checks for the associated jurisdiction.  For example, most identity documents have formatting rules like the following:   The image of the person's face must have a certain contrast in order to highlight skin tone   The subject in the document's image must remove eye glasses and pose in a certain way   The informational fields (name, date of birth, ID number, etc.) must be colored and aligned according to specific rules   Security features like watermarks and background patterns must be present  So a `match` status for this field indicates that the document in the provided image seems to conform to the various formatting and security rules associated with the detected document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | High level summary of whether the document in the provided image matches the formatting rules and security checks for the associated jurisdiction.  For example, most identity documents have formatting rules like the following:   The image of the person&#x27;s face must have a certain contrast in order to highlight skin tone   The subject in the document&#x27;s image must remove eye glasses and pose in a certain way   The informational fields (name, date of birth, ID number, etc.) must be colored and aligned according to specific rules   Security features like watermarks and background patterns must be present  So a &#x60;match&#x60; status for this field indicates that the document in the provided image seems to conform to the various formatting and security rules associated with the detected document. | must be one of ["match", "partial_match", "no_match", "no_data", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

