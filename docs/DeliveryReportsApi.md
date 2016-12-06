# messagemedia_rest_api.DeliveryReportsApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_reports**](DeliveryReportsApi.md#check_reports) | **GET** /delivery_reports | Check delivery reports
[**confirm_reports**](DeliveryReportsApi.md#confirm_reports) | **POST** /delivery_reports/confirmed | Confirm delivery reports as received


# **check_reports**
> Reports check_reports()

Check delivery reports

Return up to 100 delivery reports that have been received and haven't  been confirmed using the confirm reports endpoint

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
api_instance = messagemedia_rest_api.DeliveryReportsApi()

try: 
    # Check delivery reports
    api_response = api_instance.check_reports()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->check_reports: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Reports**](Reports.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_reports**
> confirm_reports(delivery_report_id)

Confirm delivery reports as received

Confirm the specified delivery reports as being received so they will no longer be returned in check delivery reports requests

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
api_instance = messagemedia_rest_api.DeliveryReportsApi()
delivery_report_id = messagemedia_rest_api.DeliveryReportId() # DeliveryReportId | A list of delivery report IDs to mark as confirmed

try: 
    # Confirm delivery reports as received
    api_instance.confirm_reports(delivery_report_id)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->confirm_reports: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_report_id** | [**DeliveryReportId**](DeliveryReportId.md)| A list of delivery report IDs to mark as confirmed | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

