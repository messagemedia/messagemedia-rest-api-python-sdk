# messagemedia_restapi.RepliesApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_replies**](RepliesApi.md#check_replies) | **GET** /replies | Check replies
[**confirm_replies**](RepliesApi.md#confirm_replies) | **POST** /replies/confirmed | Confirm replies as received


# **check_replies**
> Replies check_replies()

Check replies

Return up to 100 reply messages that have been received and haven't  been confirmed using the confirm replies endpoint

### Example 
```python
import time
import messagemedia_restapi
from messagemedia_restapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_restapi.configuration.username = 'YOUR_USERNAME'
messagemedia_restapi.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_restapi.RepliesApi()

try: 
    # Check replies
    api_response = api_instance.check_replies()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RepliesApi->check_replies: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Replies**](Replies.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_replies**
> confirm_replies(reply_id)

Confirm replies as received

Confirm the specified replies as being received so they will no longer be returned in check replies requests

### Example 
```python
import time
import messagemedia_restapi
from messagemedia_restapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_restapi.configuration.username = 'YOUR_USERNAME'
messagemedia_restapi.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_restapi.RepliesApi()
reply_id = messagemedia_restapi.ReplyId() # ReplyId | A list of reply IDs to mark as confirmed

try: 
    # Confirm replies as received
    api_instance.confirm_replies(reply_id)
except ApiException as e:
    print "Exception when calling RepliesApi->confirm_replies: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_id** | [**ReplyId**](ReplyId.md)| A list of reply IDs to mark as confirmed | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

