# coding: utf-8

"""
    MessageMedia REST API

    Australia's Leading Messaging Solutions for Business and Enterprise.

    OpenAPI spec version: 1.0.0
    Contact: support@messagemedia.com

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MessagingReportsApi(object):
    """
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_delivery_reports_detail(self, end_date, start_date, **kwargs):
        """
        Returns a list of delivery reports
        Returns a detailed list of all delivery reports received during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_delivery_reports_detail(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: DeliveryReports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_delivery_reports_detail_with_http_info(end_date, start_date, **kwargs)
        else:
            (data) = self.get_delivery_reports_detail_with_http_info(end_date, start_date, **kwargs)
            return data

    def get_delivery_reports_detail_with_http_info(self, end_date, start_date, **kwargs):
        """
        Returns a list of delivery reports
        Returns a detailed list of all delivery reports received during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_delivery_reports_detail_with_http_info(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: DeliveryReports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'start_date', 'account', 'destination_address_country', 'destination_address', 'message_format', 'metadata_key', 'metadata_value', 'status_code', 'status', 'page', 'page_size', 'sort_by', 'sort_direction', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_reports_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_delivery_reports_detail`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_delivery_reports_detail`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_delivery_reports_detail`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_delivery_reports_detail`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_delivery_reports_detail`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_delivery_reports_detail`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        if 'status_code' in params and len(params['status_code']) > 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_delivery_reports_detail`, length must be less than or equal to `3`")
        if 'status_code' in params and len(params['status_code']) < 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_delivery_reports_detail`, length must be greater than or equal to `3`")
        if 'status' in params and len(params['status']) > 15:
            raise ValueError("Invalid value for parameter `status` when calling `get_delivery_reports_detail`, length must be less than or equal to `15`")
        if 'status' in params and len(params['status']) < 1:
            raise ValueError("Invalid value for parameter `status` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        if 'page' in params and params['page'] < 1.0:
            raise ValueError("Invalid value for parameter `page` when calling `get_delivery_reports_detail`, must be a value greater than or equal to `1.0`")
        if 'page_size' in params and params['page_size'] > 100.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_delivery_reports_detail`, must be a value less than or equal to  `100.0`")
        if 'page_size' in params and params['page_size'] < 1.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_delivery_reports_detail`, must be a value greater than or equal to `1.0`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_delivery_reports_detail`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_delivery_reports_detail`, length must be greater than or equal to `1`")
        resource_path = '/reporting/delivery_reports/detail'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'status_code' in params:
            query_params['status_code'] = params['status_code']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']
        if 'sort_by' in params:
            query_params['sort_by'] = params['sort_by']
        if 'sort_direction' in params:
            query_params['sort_direction'] = params['sort_direction']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeliveryReports',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_delivery_reports_summary(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of delivery reports
        Returns a summarised report of all delivery reports received during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_delivery_reports_summary(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_delivery_reports_summary_with_http_info(end_date, group_by, start_date, **kwargs)
        else:
            (data) = self.get_delivery_reports_summary_with_http_info(end_date, group_by, start_date, **kwargs)
            return data

    def get_delivery_reports_summary_with_http_info(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of delivery reports
        Returns a summarised report of all delivery reports received during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_delivery_reports_summary_with_http_info(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'group_by', 'start_date', 'account', 'destination_address_country', 'destination_address', 'message_format', 'metadata_key', 'metadata_value', 'status_code', 'status', 'summary_by', 'summary_field', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_reports_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_delivery_reports_summary`")
        # verify the required parameter 'group_by' is set
        if ('group_by' not in params) or (params['group_by'] is None):
            raise ValueError("Missing the required parameter `group_by` when calling `get_delivery_reports_summary`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_delivery_reports_summary`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_delivery_reports_summary`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_delivery_reports_summary`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_delivery_reports_summary`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_delivery_reports_summary`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        if 'status_code' in params and len(params['status_code']) > 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_delivery_reports_summary`, length must be less than or equal to `3`")
        if 'status_code' in params and len(params['status_code']) < 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_delivery_reports_summary`, length must be greater than or equal to `3`")
        if 'status' in params and len(params['status']) > 15:
            raise ValueError("Invalid value for parameter `status` when calling `get_delivery_reports_summary`, length must be less than or equal to `15`")
        if 'status' in params and len(params['status']) < 1:
            raise ValueError("Invalid value for parameter `status` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_delivery_reports_summary`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_delivery_reports_summary`, length must be greater than or equal to `1`")
        resource_path = '/reporting/delivery_reports/summary'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'status_code' in params:
            query_params['status_code'] = params['status_code']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'summary_by' in params:
            query_params['summary_by'] = params['summary_by']
        if 'summary_field' in params:
            query_params['summary_field'] = params['summary_field']
        if 'group_by' in params:
            query_params['group_by'] = params['group_by']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SummaryReport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_metadata_keys(self, message_type, start_date, end_date, **kwargs):
        """
        Returns a list of metadata keys
        Returns a list of all metadata keys used for the specified message type during the specified time. Results are limited to 100 keys.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata_keys(message_type, start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_type: Message type. Possible values are sent messages, received messages and delivery receipts. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: MetadataKeysResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_metadata_keys_with_http_info(message_type, start_date, end_date, **kwargs)
        else:
            (data) = self.get_metadata_keys_with_http_info(message_type, start_date, end_date, **kwargs)
            return data

    def get_metadata_keys_with_http_info(self, message_type, start_date, end_date, **kwargs):
        """
        Returns a list of metadata keys
        Returns a list of all metadata keys used for the specified message type during the specified time. Results are limited to 100 keys.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata_keys_with_http_info(message_type, start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_type: Message type. Possible values are sent messages, received messages and delivery receipts. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: MetadataKeysResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_type', 'start_date', 'end_date', 'account', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metadata_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_type' is set
        if ('message_type' not in params) or (params['message_type'] is None):
            raise ValueError("Missing the required parameter `message_type` when calling `get_metadata_keys`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_metadata_keys`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_metadata_keys`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_metadata_keys`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_metadata_keys`, length must be greater than or equal to `1`")
        resource_path = '/reporting/{messageType}/metadata/keys'.replace('{format}', 'json')
        path_params = {}
        if 'message_type' in params:
            path_params['messageType'] = params['message_type']

        query_params = {}
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'account' in params:
            query_params['account'] = params['account']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MetadataKeysResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_received_messages_detail(self, end_date, start_date, **kwargs):
        """
        Returns a list message received
        Returns a detailed list of all message received during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_received_messages_detail(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str action: Filter results by the action that was invoked for this message.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: ReceivedMessages
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_received_messages_detail_with_http_info(end_date, start_date, **kwargs)
        else:
            (data) = self.get_received_messages_detail_with_http_info(end_date, start_date, **kwargs)
            return data

    def get_received_messages_detail_with_http_info(self, end_date, start_date, **kwargs):
        """
        Returns a list message received
        Returns a detailed list of all message received during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_received_messages_detail_with_http_info(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str action: Filter results by the action that was invoked for this message.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: ReceivedMessages
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'start_date', 'account', 'action', 'destination_address_country', 'destination_address', 'message_format', 'metadata_key', 'metadata_value', 'page', 'page_size', 'sort_by', 'sort_direction', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_received_messages_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_received_messages_detail`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_received_messages_detail`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_received_messages_detail`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_received_messages_detail`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_received_messages_detail`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_received_messages_detail`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_received_messages_detail`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_received_messages_detail`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_received_messages_detail`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_received_messages_detail`, length must be greater than or equal to `1`")
        if 'page' in params and params['page'] < 1.0:
            raise ValueError("Invalid value for parameter `page` when calling `get_received_messages_detail`, must be a value greater than or equal to `1.0`")
        if 'page_size' in params and params['page_size'] > 100.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_received_messages_detail`, must be a value less than or equal to  `100.0`")
        if 'page_size' in params and params['page_size'] < 1.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_received_messages_detail`, must be a value greater than or equal to `1.0`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_received_messages_detail`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_received_messages_detail`, length must be greater than or equal to `1`")
        resource_path = '/reporting/received_messages/detail'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'action' in params:
            query_params['action'] = params['action']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']
        if 'sort_by' in params:
            query_params['sort_by'] = params['sort_by']
        if 'sort_direction' in params:
            query_params['sort_direction'] = params['sort_direction']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ReceivedMessages',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_received_messages_summary(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of messages received
        Returns a summarised report of all messages received during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_received_messages_summary(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_received_messages_summary_with_http_info(end_date, group_by, start_date, **kwargs)
        else:
            (data) = self.get_received_messages_summary_with_http_info(end_date, group_by, start_date, **kwargs)
            return data

    def get_received_messages_summary_with_http_info(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of messages received
        Returns a summarised report of all messages received during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_received_messages_summary_with_http_info(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'group_by', 'start_date', 'account', 'destination_address_country', 'destination_address', 'message_format', 'metadata_key', 'metadata_value', 'summary_by', 'summary_field', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_received_messages_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_received_messages_summary`")
        # verify the required parameter 'group_by' is set
        if ('group_by' not in params) or (params['group_by'] is None):
            raise ValueError("Missing the required parameter `group_by` when calling `get_received_messages_summary`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_received_messages_summary`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_received_messages_summary`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_received_messages_summary`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_received_messages_summary`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_received_messages_summary`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_received_messages_summary`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_received_messages_summary`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_received_messages_summary`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_received_messages_summary`, length must be greater than or equal to `1`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_received_messages_summary`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_received_messages_summary`, length must be greater than or equal to `1`")
        resource_path = '/reporting/received_messages/summary'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'summary_by' in params:
            query_params['summary_by'] = params['summary_by']
        if 'summary_field' in params:
            query_params['summary_field'] = params['summary_field']
        if 'group_by' in params:
            query_params['group_by'] = params['group_by']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SummaryReport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sent_messages_detail(self, end_date, start_date, **kwargs):
        """
        Returns a list of message sent
        Returns a detailed list of all message sent during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sent_messages_detail(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param bool delivery_report: Filter results by delivery report.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SentMessages
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sent_messages_detail_with_http_info(end_date, start_date, **kwargs)
        else:
            (data) = self.get_sent_messages_detail_with_http_info(end_date, start_date, **kwargs)
            return data

    def get_sent_messages_detail_with_http_info(self, end_date, start_date, **kwargs):
        """
        Returns a list of message sent
        Returns a detailed list of all message sent during the specified time

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sent_messages_detail_with_http_info(end_date, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param bool delivery_report: Filter results by delivery report.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str status: Filter results by message status.
        :param int page: Page number for paging through paginated result sets.
        :param int page_size: Number of results to return in a page for paginated result sets.
        :param str sort_by: Field to sort results set by
        :param str sort_direction: Order to sort results by.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SentMessages
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'start_date', 'account', 'delivery_report', 'destination_address_country', 'destination_address', 'message_format', 'metadata_key', 'metadata_value', 'status_code', 'status', 'page', 'page_size', 'sort_by', 'sort_direction', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sent_messages_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_sent_messages_detail`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_sent_messages_detail`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_sent_messages_detail`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_sent_messages_detail`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_sent_messages_detail`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_sent_messages_detail`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        if 'status_code' in params and len(params['status_code']) > 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_sent_messages_detail`, length must be less than or equal to `3`")
        if 'status_code' in params and len(params['status_code']) < 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_sent_messages_detail`, length must be greater than or equal to `3`")
        if 'status' in params and len(params['status']) > 15:
            raise ValueError("Invalid value for parameter `status` when calling `get_sent_messages_detail`, length must be less than or equal to `15`")
        if 'status' in params and len(params['status']) < 1:
            raise ValueError("Invalid value for parameter `status` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        if 'page' in params and params['page'] < 1.0:
            raise ValueError("Invalid value for parameter `page` when calling `get_sent_messages_detail`, must be a value greater than or equal to `1.0`")
        if 'page_size' in params and params['page_size'] > 100.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_sent_messages_detail`, must be a value less than or equal to  `100.0`")
        if 'page_size' in params and params['page_size'] < 1.0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_sent_messages_detail`, must be a value greater than or equal to `1.0`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_sent_messages_detail`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_sent_messages_detail`, length must be greater than or equal to `1`")
        resource_path = '/reporting/sent_messages/detail'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'delivery_report' in params:
            query_params['delivery_report'] = params['delivery_report']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'status_code' in params:
            query_params['status_code'] = params['status_code']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']
        if 'sort_by' in params:
            query_params['sort_by'] = params['sort_by']
        if 'sort_direction' in params:
            query_params['sort_direction'] = params['sort_direction']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SentMessages',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sent_messages_summary(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of messages sent
        Returns a summarised report of all messages sent during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sent_messages_summary(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param bool delivery_report: Filter results by delivery report.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sent_messages_summary_with_http_info(end_date, group_by, start_date, **kwargs)
        else:
            (data) = self.get_sent_messages_summary_with_http_info(end_date, group_by, start_date, **kwargs)
            return data

    def get_sent_messages_summary_with_http_info(self, end_date, group_by, start_date, **kwargs):
        """
        Returns a summarised report of messages sent
        Returns a summarised report of all messages sent during the specified time, grouped by by the specified grouping parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sent_messages_summary_with_http_info(end_date, group_by, start_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime end_date: End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str group_by: Field to group results set by (required)
        :param datetime start_date: Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. (required)
        :param str account: Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts.
        :param bool delivery_report: Filter results by delivery report.
        :param str destination_address_country: Filter results by destination address country.
        :param str destination_address: Filter results by destination address.
        :param str summary_by: Function to apply when summarising results
        :param str summary_field: Field to summarise results by
        :param str message_format: Filter results by message format.
        :param str metadata_key: Filter results for messages that include a metadata key.
        :param str metadata_value: Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided.
        :param str status_code: Filter results by message status code.
        :param str source_address_country: Filter results by source address country.
        :param str source_address: Filter results by source address.
        :param str timezone: The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'.
        :return: SummaryReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_date', 'group_by', 'start_date', 'account', 'delivery_report', 'destination_address_country', 'destination_address', 'summary_by', 'summary_field', 'message_format', 'metadata_key', 'metadata_value', 'status_code', 'source_address_country', 'source_address', 'timezone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sent_messages_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_sent_messages_summary`")
        # verify the required parameter 'group_by' is set
        if ('group_by' not in params) or (params['group_by'] is None):
            raise ValueError("Missing the required parameter `group_by` when calling `get_sent_messages_summary`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_sent_messages_summary`")

        if 'account' in params and len(params['account']) > 200:
            raise ValueError("Invalid value for parameter `account` when calling `get_sent_messages_summary`, length must be less than or equal to `200`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `get_sent_messages_summary`, length must be greater than or equal to `1`")
        if 'destination_address' in params and len(params['destination_address']) > 15:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_sent_messages_summary`, length must be less than or equal to `15`")
        if 'destination_address' in params and len(params['destination_address']) < 1:
            raise ValueError("Invalid value for parameter `destination_address` when calling `get_sent_messages_summary`, length must be greater than or equal to `1`")
        if 'metadata_key' in params and len(params['metadata_key']) > 100:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_sent_messages_summary`, length must be less than or equal to `100`")
        if 'metadata_key' in params and len(params['metadata_key']) < 1:
            raise ValueError("Invalid value for parameter `metadata_key` when calling `get_sent_messages_summary`, length must be greater than or equal to `1`")
        if 'metadata_value' in params and len(params['metadata_value']) > 256:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_sent_messages_summary`, length must be less than or equal to `256`")
        if 'metadata_value' in params and len(params['metadata_value']) < 1:
            raise ValueError("Invalid value for parameter `metadata_value` when calling `get_sent_messages_summary`, length must be greater than or equal to `1`")
        if 'status_code' in params and len(params['status_code']) > 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_sent_messages_summary`, length must be less than or equal to `3`")
        if 'status_code' in params and len(params['status_code']) < 3:
            raise ValueError("Invalid value for parameter `status_code` when calling `get_sent_messages_summary`, length must be greater than or equal to `3`")
        if 'source_address' in params and len(params['source_address']) > 15:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_sent_messages_summary`, length must be less than or equal to `15`")
        if 'source_address' in params and len(params['source_address']) < 1:
            raise ValueError("Invalid value for parameter `source_address` when calling `get_sent_messages_summary`, length must be greater than or equal to `1`")
        resource_path = '/reporting/sent_messages/summary'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'account' in params:
            query_params['account'] = params['account']
        if 'delivery_report' in params:
            query_params['delivery_report'] = params['delivery_report']
        if 'destination_address_country' in params:
            query_params['destination_address_country'] = params['destination_address_country']
        if 'destination_address' in params:
            query_params['destination_address'] = params['destination_address']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'summary_by' in params:
            query_params['summary_by'] = params['summary_by']
        if 'summary_field' in params:
            query_params['summary_field'] = params['summary_field']
        if 'group_by' in params:
            query_params['group_by'] = params['group_by']
        if 'message_format' in params:
            query_params['message_format'] = params['message_format']
        if 'metadata_key' in params:
            query_params['metadata_key'] = params['metadata_key']
        if 'metadata_value' in params:
            query_params['metadata_value'] = params['metadata_value']
        if 'status_code' in params:
            query_params['status_code'] = params['status_code']
        if 'source_address_country' in params:
            query_params['source_address_country'] = params['source_address_country']
        if 'source_address' in params:
            query_params['source_address'] = params['source_address']
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'timezone' in params:
            query_params['timezone'] = params['timezone']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SummaryReport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
