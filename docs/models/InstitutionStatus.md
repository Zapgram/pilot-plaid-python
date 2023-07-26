# plaid.model.institution_status.InstitutionStatus

The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.  Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution&#x27;s status, Plaid will return null rather than potentially inaccurate data.  Institution status is accessible in the Dashboard and via the API using the &#x60;/institutions/get_by_id&#x60; endpoint with the &#x60;include_status&#x60; option set to true. Note that institution status is not available in the Sandbox environment.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item_logins** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**transactions_updates** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**auth** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**identity** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**investments_updates** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**liabilities_updates** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**liabilities** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**investments** | [**ProductStatus**](ProductStatus.md) | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**[health_incidents](#health_incidents)** | list, tuple, None,  | tuple, NoneClass,  | Details of recent health incidents associated with the institution. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# health_incidents

Details of recent health incidents associated with the institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Details of recent health incidents associated with the institution. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**HealthIncident**](HealthIncident.md) | [**HealthIncident**](HealthIncident.md) | [**HealthIncident**](HealthIncident.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

