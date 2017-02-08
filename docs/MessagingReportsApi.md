# messagemedia_rest_api.MessagingReportsApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_reports_detail**](MessagingReportsApi.md#get_delivery_reports_detail) | **GET** /reporting/delivery_reports/detail | Returns a list of delivery reports
[**get_delivery_reports_summary**](MessagingReportsApi.md#get_delivery_reports_summary) | **GET** /reporting/delivery_reports/summary | Returns a summarised report of delivery reports
[**get_metadata_keys**](MessagingReportsApi.md#get_metadata_keys) | **GET** /reporting/{messageType}/metadata/keys | Returns a list of metadata keys
[**get_received_messages_detail**](MessagingReportsApi.md#get_received_messages_detail) | **GET** /reporting/received_messages/detail | Returns a list message received
[**get_received_messages_summary**](MessagingReportsApi.md#get_received_messages_summary) | **GET** /reporting/received_messages/summary | Returns a summarised report of messages received
[**get_sent_messages_detail**](MessagingReportsApi.md#get_sent_messages_detail) | **GET** /reporting/sent_messages/detail | Returns a list of message sent
[**get_sent_messages_summary**](MessagingReportsApi.md#get_sent_messages_summary) | **GET** /reporting/sent_messages/summary | Returns a summarised report of messages sent


# **get_delivery_reports_detail**
> DeliveryReports get_delivery_reports_detail(end_date, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list of delivery reports

Returns a detailed list of all delivery reports received during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of delivery reports
    api_response = api_instance.get_delivery_reports_detail(end_date, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_delivery_reports_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**DeliveryReports**](DeliveryReports.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_reports_summary**
> SummaryReport get_delivery_reports_summary(end_date, group_by, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of delivery reports

Returns a summarised report of all delivery reports received during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
group_by = 'group_by_example' # str | Field to group results set by
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of delivery reports
    api_response = api_instance.get_delivery_reports_summary(end_date, group_by, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_delivery_reports_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_keys**
> MetadataKeysResponse get_metadata_keys(message_type, start_date, end_date, account=account, timezone=timezone)

Returns a list of metadata keys

Returns a list of all metadata keys used for the specified message type during the specified time. Results are limited to 100 keys.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
message_type = 'message_type_example' # str | Message type. Possible values are sent messages, received messages and delivery receipts.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of metadata keys
    api_response = api_instance.get_metadata_keys(message_type, start_date, end_date, account=account, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_metadata_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_type** | **str**| Message type. Possible values are sent messages, received messages and delivery receipts. | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**MetadataKeysResponse**](MetadataKeysResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_messages_detail**
> ReceivedMessages get_received_messages_detail(end_date, start_date, account=account, action=action, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list message received

Returns a detailed list of all message received during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
action = 'action_example' # str | Filter results by the action that was invoked for this message. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list message received
    api_response = api_instance.get_received_messages_detail(end_date, start_date, account=account, action=action, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_received_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **action** | **str**| Filter results by the action that was invoked for this message. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**ReceivedMessages**](ReceivedMessages.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_messages_summary**
> SummaryReport get_received_messages_summary(end_date, group_by, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of messages received

Returns a summarised report of all messages received during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
group_by = 'group_by_example' # str | Field to group results set by
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of messages received
    api_response = api_instance.get_received_messages_summary(end_date, group_by, start_date, account=account, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_received_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_messages_detail**
> SentMessages get_sent_messages_detail(end_date, start_date, account=account, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list of message sent

Returns a detailed list of all message sent during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
delivery_report = true # bool | Filter results by delivery report. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of message sent
    api_response = api_instance.get_sent_messages_detail(end_date, start_date, account=account, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_sent_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **delivery_report** | **bool**| Filter results by delivery report. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SentMessages**](SentMessages.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_messages_summary**
> SummaryReport get_sent_messages_summary(end_date, group_by, start_date, account=account, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, summary_by=summary_by, summary_field=summary_field, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of messages sent

Returns a summarised report of all messages sent during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
group_by = 'group_by_example' # str | Field to group results set by
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request.
account = 'account_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
delivery_report = true # bool | Filter results by delivery report. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of messages sent
    api_response = api_instance.get_sent_messages_summary(end_date, group_by, start_date, account=account, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, summary_by=summary_by, summary_field=summary_field, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_sent_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **datetime**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. | 
 **account** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **delivery_report** | **bool**| Filter results by delivery report. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

