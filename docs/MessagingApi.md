# messagemedia_restapi.MessagingApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_status**](MessagingApi.md#get_message_status) | **GET** /messages/{messageId} | Get the status of a submitted message
[**send_messages**](MessagingApi.md#send_messages) | **POST** /messages | Send one or more messages
[**update_message_status**](MessagingApi.md#update_message_status) | **PUT** /messages/{messageId} | Cancel a scheduled message


# **get_message_status**
> SubmittedMessage get_message_status(message_id)

Get the status of a submitted message

Get the status and details of a previously submitted message

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
api_instance = messagemedia_restapi.MessagingApi()
message_id = 'message_id_example' # str | Unique ID representing message that has been submitted

try: 
    # Get the status of a submitted message
    api_response = api_instance.get_message_status(message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_message_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique ID representing message that has been submitted | 

### Return type

[**SubmittedMessage**](SubmittedMessage.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_messages**
> SubmittedMessages send_messages(messages)

Send one or more messages

Submit one or more (up to 100 per request) SMS or text to voice messages to be sent to the destination address. - A callback URL can be included with each message to which MO and DR notifications will be pushed to via a HTTP POST request. - The content of the message can be a Unicode string, up to 5000 characters long - A delivery report can be be requested with the message which will be pushed to a HTTP endpoint if specified, or available via the Check Reports endpoint. - The destination number should be specified in E.164 international format. For information on E.164, please refer to http://en.wikipedia.org/wiki/E.164 - The format specifies which format the message will be sent as, SMS or VOICE - If specified the source number included in the request will be shown as the source number for the message, this feature is not enabled by default, please contact MessageMedia for more information. - If a source number is specified, the type of source number may also be specified. This is recommended when using a source address type that is not an internationally formatted number, available options are INTERNATIONAL, ALPHANUMERIC or SHORTCODE - The message will be scheduled to be delivered in the future if the scheduled parameter is specified. - A message expiry timestamp can be provided, if the message is not delivered by this time, it will be discarded. - Metadata can be included with the message. Up to 10 key value pair strings can be included with each message. This metadata will be available in delivery reports and replies.

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
api_instance = messagemedia_restapi.MessagingApi()
messages = messagemedia_restapi.Messages() # Messages | A list of messages to be sent

try: 
    # Send one or more messages
    api_response = api_instance.send_messages(messages)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->send_messages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messages** | [**Messages**](Messages.md)| A list of messages to be sent | 

### Return type

[**SubmittedMessages**](SubmittedMessages.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message_status**
> update_message_status(message_id, status)

Cancel a scheduled message

Cancel a scheduled message

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
api_instance = messagemedia_restapi.MessagingApi()
message_id = 'message_id_example' # str | Unique ID representing message to be updated
status = messagemedia_restapi.Status() # Status | New status for the message

try: 
    # Cancel a scheduled message
    api_instance.update_message_status(message_id, status)
except ApiException as e:
    print "Exception when calling MessagingApi->update_message_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique ID representing message to be updated | 
 **status** | [**Status**](Status.md)| New status for the message | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

