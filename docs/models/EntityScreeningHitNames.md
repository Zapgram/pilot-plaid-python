# plaid.model.entity_screening_hit_names.EntityScreeningHitNames

Name information for the associated entity watchlist hit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Name information for the associated entity watchlist hit | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_primary** | bool,  | BoolClass,  | Primary names are those most commonly used to refer to this entity. Only one name will ever be marked as primary. | 
**weak_alias_determination** | [**WeakAliasDetermination**](WeakAliasDetermination.md) | [**WeakAliasDetermination**](WeakAliasDetermination.md) |  | 
**full** | str,  | str,  | The full name of the entity. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

