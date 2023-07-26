# plaid.model.screening_hit_data.ScreeningHitData

Information associated with the watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information associated with the watchlist hit | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dates_of_birth](#dates_of_birth)** | list, tuple,  | tuple,  | Dates of birth associated with the watchlist hit | [optional] 
**[documents](#documents)** | list, tuple,  | tuple,  | Documents associated with the watchlist hit | [optional] 
**[locations](#locations)** | list, tuple,  | tuple,  | Locations associated with the watchlist hit | [optional] 
**[names](#names)** | list, tuple,  | tuple,  | Names associated with the watchlist hit | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dates_of_birth

Dates of birth associated with the watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Dates of birth associated with the watchlist hit | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScreeningHitDateOfBirthItem**](ScreeningHitDateOfBirthItem.md) | [**ScreeningHitDateOfBirthItem**](ScreeningHitDateOfBirthItem.md) | [**ScreeningHitDateOfBirthItem**](ScreeningHitDateOfBirthItem.md) |  | 

# documents

Documents associated with the watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Documents associated with the watchlist hit | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScreeningHitDocumentsItems**](ScreeningHitDocumentsItems.md) | [**ScreeningHitDocumentsItems**](ScreeningHitDocumentsItems.md) | [**ScreeningHitDocumentsItems**](ScreeningHitDocumentsItems.md) |  | 

# locations

Locations associated with the watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Locations associated with the watchlist hit | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GenericScreeningHitLocationItems**](GenericScreeningHitLocationItems.md) | [**GenericScreeningHitLocationItems**](GenericScreeningHitLocationItems.md) | [**GenericScreeningHitLocationItems**](GenericScreeningHitLocationItems.md) |  | 

# names

Names associated with the watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Names associated with the watchlist hit | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScreeningHitNamesItems**](ScreeningHitNamesItems.md) | [**ScreeningHitNamesItems**](ScreeningHitNamesItems.md) | [**ScreeningHitNamesItems**](ScreeningHitNamesItems.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

