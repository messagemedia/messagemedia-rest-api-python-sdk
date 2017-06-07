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

from pprint import pformat
from six import iteritems
import re


class SummaryReportItem(object):
    """
    Do not edit the class manually.
    """
    def __init__(self, group=None, value=None, subgroups=None):
        """
        SummaryReportItem - a model

        :param dict types: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.types = {
            'group': 'str',
            'value': 'int',
            'subgroups': 'list[SummaryReportItem]'
        }

        self.attribute_map = {
            'group': 'group',
            'value': 'value',
            'subgroups': 'subgroups'
        }

        self._group = group
        self._value = value
        self._subgroups = subgroups

    @property
    def group(self):
        """
        Gets the group of this SummaryReportItem.


        :return: The group of this SummaryReportItem.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this SummaryReportItem.


        :param group: The group of this SummaryReportItem.
        :type: str
        """

        self._group = group

    @property
    def value(self):
        """
        Gets the value of this SummaryReportItem.


        :return: The value of this SummaryReportItem.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SummaryReportItem.


        :param value: The value of this SummaryReportItem.
        :type: int
        """

        self._value = value

    @property
    def subgroups(self):
        """
        Gets the subgroups of this SummaryReportItem.


        :return: The subgroups of this SummaryReportItem.
        :rtype: list[SummaryReportItem]
        """
        return self._subgroups

    @subgroups.setter
    def subgroups(self, subgroups):
        """
        Sets the subgroups of this SummaryReportItem.


        :param subgroups: The subgroups of this SummaryReportItem.
        :type: list[SummaryReportItem]
        """

        self._subgroups = subgroups

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
