# swagger_client.CloudProfilesApi

All URIs are relative to *http://localhost.multiloginapp.com:35000/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_get**](CloudProfilesApi.md#profile_get) | **GET** /profile | listProfiles
[**profile_post**](CloudProfilesApi.md#profile_post) | **POST** /profile | createProfile
[**profile_uuid_delete**](CloudProfilesApi.md#profile_uuid_delete) | **DELETE** /profile/{uuid} | removeProfile
[**profile_uuid_migrate_post**](CloudProfilesApi.md#profile_uuid_migrate_post) | **POST** /profile/{uuid}/migrate | migrateProfile
[**profile_uuid_post**](CloudProfilesApi.md#profile_uuid_post) | **POST** /profile/{uuid} | updateProfile
[**profile_uuid_update_post**](CloudProfilesApi.md#profile_uuid_update_post) | **POST** /profile/{uuid}/update | updateProfileCore


# **profile_get**
> list[InlineResponse200] profile_get()

listProfiles

Returns a list of profiles as a JSON array.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()

try:
    # listProfiles
    api_response = api_instance.profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_post**
> InlineResponse2001 profile_post(body, browser_version_min=browser_version_min, browser_version_max=browser_version_max)

createProfile

Create a new browser profile. Required fields to be passed in the body are: Name, OS, Browser. All the fields not passed in the body are generated automatically. Returns the ID of the newly created profile.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()
body = swagger_client.Profile() # Profile | 
browser_version_min = 56 # int | Minimum browser version (optional)
browser_version_max = 56 # int | Maximum browser version (optional)

try:
    # createProfile
    api_response = api_instance.profile_post(body, browser_version_min=browser_version_min, browser_version_max=browser_version_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Profile**](Profile.md)|  | 
 **browser_version_min** | **int**| Minimum browser version | [optional] 
 **browser_version_max** | **int**| Maximum browser version | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_uuid_delete**
> profile_uuid_delete(uuid)

removeProfile

Deletes the profile permanently

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()
uuid = 'uuid_example' # str | Profile ID

try:
    # removeProfile
    api_instance.profile_uuid_delete(uuid)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_uuid_migrate_post**
> profile_uuid_migrate_post(uuid)

migrateProfile

Migrates the profile from version 4.x to 5.x

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()
uuid = 'uuid_example' # str | Profile ID

try:
    # migrateProfile
    api_instance.profile_uuid_migrate_post(uuid)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_uuid_migrate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_uuid_post**
> profile_uuid_post(uuid, body)

updateProfile

Updates the profile based on the JSON passed in the body. OS and browser type can not be changed 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()
uuid = 'uuid_example' # str | Profile ID
body = swagger_client.UpdateProfileExample() # UpdateProfileExample | 

try:
    # updateProfile
    api_instance.profile_uuid_post(uuid, body)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Profile ID | 
 **body** | [**UpdateProfileExample**](UpdateProfileExample.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_uuid_update_post**
> profile_uuid_update_post(uuid)

updateProfileCore

Updates the browser core to the latest version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudProfilesApi()
uuid = 'uuid_example' # str | Profile ID

try:
    # updateProfileCore
    api_instance.profile_uuid_update_post(uuid)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->profile_uuid_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

