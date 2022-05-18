# coding: utf-8

"""
    CBRAIN API

    API for interacting with the CBRAIN Platform  # noqa: E501

    OpenAPI spec version: 6.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cbrain_api.configuration import Configuration


class CbrainTaskModReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cbrain_task': 'CbrainTask'
    }

    attribute_map = {
        'cbrain_task': 'cbrain_task'
    }

    def __init__(self, cbrain_task=None, _configuration=None):  # noqa: E501
        """CbrainTaskModReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cbrain_task = None
        self.discriminator = None

        if cbrain_task is not None:
            self.cbrain_task = cbrain_task

    @property
    def cbrain_task(self):
        """Gets the cbrain_task of this CbrainTaskModReq.  # noqa: E501


        :return: The cbrain_task of this CbrainTaskModReq.  # noqa: E501
        :rtype: CbrainTask
        """
        return self._cbrain_task

    @cbrain_task.setter
    def cbrain_task(self, cbrain_task):
        """Sets the cbrain_task of this CbrainTaskModReq.


        :param cbrain_task: The cbrain_task of this CbrainTaskModReq.  # noqa: E501
        :type: CbrainTask
        """

        self._cbrain_task = cbrain_task

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CbrainTaskModReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CbrainTaskModReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CbrainTaskModReq):
            return True

        return self.to_dict() != other.to_dict()