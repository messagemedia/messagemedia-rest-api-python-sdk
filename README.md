# MessageMedia REST API
Australia's Leading Messaging Solutions for Business and Enterprise.


- API version: 1.0.0
- Package version: 1.0.0
- Build date: 2016-12-06T05:07:32.826Z
For more information, please visit [https://www.messagemedia.com/contact-us](https://www.messagemedia.com/contact-us)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import messagemedia_rest_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import messagemedia_rest_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = messagemedia_rest_api.DeliveryReportsApi

try:
    # Check delivery reports
    api_response = api_instance.check_reports()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->check_reports: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.messagemedia.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeliveryReportsApi* | [**check_reports**](docs/DeliveryReportsApi.md#check_reports) | **GET** /delivery_reports | Check delivery reports
*DeliveryReportsApi* | [**confirm_reports**](docs/DeliveryReportsApi.md#confirm_reports) | **POST** /delivery_reports/confirmed | Confirm delivery reports as received
*MessagingApi* | [**get_message_status**](docs/MessagingApi.md#get_message_status) | **GET** /messages/{messageId} | Get the status of a submitted message
*MessagingApi* | [**send_messages**](docs/MessagingApi.md#send_messages) | **POST** /messages | Send one or more messages
*MessagingApi* | [**update_message_status**](docs/MessagingApi.md#update_message_status) | **PUT** /messages/{messageId} | Cancel a scheduled message
*MessagingReportsApi* | [**get_delivery_reports_detail**](docs/MessagingReportsApi.md#get_delivery_reports_detail) | **GET** /reporting/delivery_reports/detail | Returns a list of delivery reports
*MessagingReportsApi* | [**get_delivery_reports_summary**](docs/MessagingReportsApi.md#get_delivery_reports_summary) | **GET** /reporting/delivery_reports/summary | Returns a summarised report of delivery reports
*MessagingReportsApi* | [**get_received_messages_detail**](docs/MessagingReportsApi.md#get_received_messages_detail) | **GET** /reporting/received_messages/detail | Returns a list message received
*MessagingReportsApi* | [**get_received_messages_summary**](docs/MessagingReportsApi.md#get_received_messages_summary) | **GET** /reporting/received_messages/summary | Returns a summarised report of messages received
*MessagingReportsApi* | [**get_sent_messages_detail**](docs/MessagingReportsApi.md#get_sent_messages_detail) | **GET** /reporting/sent_messages/detail | Returns a list of message sent
*MessagingReportsApi* | [**get_sent_messages_summary**](docs/MessagingReportsApi.md#get_sent_messages_summary) | **GET** /reporting/sent_messages/summary | Returns a summarised report of messages sent
*RepliesApi* | [**check_replies**](docs/RepliesApi.md#check_replies) | **GET** /replies | Check replies
*RepliesApi* | [**confirm_replies**](docs/RepliesApi.md#confirm_replies) | **POST** /replies/confirmed | Confirm replies as received


## Documentation For Models

 - [DeliveryReport](docs/DeliveryReport.md)
 - [DeliveryReportId](docs/DeliveryReportId.md)
 - [DeliveryReports](docs/DeliveryReports.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [MessageFormat](docs/MessageFormat.md)
 - [MessageStatus](docs/MessageStatus.md)
 - [MessageStatusCode](docs/MessageStatusCode.md)
 - [Messages](docs/Messages.md)
 - [NewMessage](docs/NewMessage.md)
 - [Pagination](docs/Pagination.md)
 - [ReceivedMessage](docs/ReceivedMessage.md)
 - [ReceivedMessages](docs/ReceivedMessages.md)
 - [Replies](docs/Replies.md)
 - [Reply](docs/Reply.md)
 - [ReplyId](docs/ReplyId.md)
 - [ReplyVendorAccountId](docs/ReplyVendorAccountId.md)
 - [Report](docs/Report.md)
 - [ReportingDetailProperties](docs/ReportingDetailProperties.md)
 - [ReportingDetailPropertiesFilters](docs/ReportingDetailPropertiesFilters.md)
 - [ReportingDetailPropertiesSorting](docs/ReportingDetailPropertiesSorting.md)
 - [Reports](docs/Reports.md)
 - [SentMessage](docs/SentMessage.md)
 - [SentMessages](docs/SentMessages.md)
 - [Status](docs/Status.md)
 - [SubmittedMessage](docs/SubmittedMessage.md)
 - [SubmittedMessages](docs/SubmittedMessages.md)
 - [SummaryReport](docs/SummaryReport.md)
 - [SummaryReportData](docs/SummaryReportData.md)
 - [SummaryReportProperties](docs/SummaryReportProperties.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

support@messagemedia.com

