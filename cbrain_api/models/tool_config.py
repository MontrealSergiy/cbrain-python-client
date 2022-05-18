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


class ToolConfig(object):
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
        'id': 'int',
        'version_name': 'str',
        'description': 'str',
        'tool_id': 'int',
        'bourreau_id': 'int',
        'group_id': 'int',
        'ncpus': 'int'
    }

    attribute_map = {
        'id': 'id',
        'version_name': 'version_name',
        'description': 'description',
        'tool_id': 'tool_id',
        'bourreau_id': 'bourreau_id',
        'group_id': 'group_id',
        'ncpus': 'ncpus'
    }

    def __init__(self, id=None, version_name=None, description=None, tool_id=None, bourreau_id=None, group_id=None, ncpus=None, _configuration=None):  # noqa: E501
        """ToolConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._version_name = None
        self._description = None
        self._tool_id = None
        self._bourreau_id = None
        self._group_id = None
        self._ncpus = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_name is not None:
            self.version_name = version_name
        if description is not None:
            self.description = description
        if tool_id is not None:
            self.tool_id = tool_id
        if bourreau_id is not None:
            self.bourreau_id = bourreau_id
        if group_id is not None:
            self.group_id = group_id
        if ncpus is not None:
            self.ncpus = ncpus

    @property
    def id(self):
        """Gets the id of this ToolConfig.  # noqa: E501

        Unique numerical ID for the ToolConfig.  # noqa: E501

        :return: The id of this ToolConfig.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ToolConfig.

        Unique numerical ID for the ToolConfig.  # noqa: E501

        :param id: The id of this ToolConfig.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def version_name(self):
        """Gets the version_name of this ToolConfig.  # noqa: E501

        the version name of the configuration  # noqa: E501

        :return: The version_name of this ToolConfig.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this ToolConfig.

        the version name of the configuration  # noqa: E501

        :param version_name: The version_name of this ToolConfig.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def description(self):
        """Gets the description of this ToolConfig.  # noqa: E501

        a description of the configuration  # noqa: E501

        :return: The description of this ToolConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ToolConfig.

        a description of the configuration  # noqa: E501

        :param description: The description of this ToolConfig.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tool_id(self):
        """Gets the tool_id of this ToolConfig.  # noqa: E501

        the ID of the tool associated with this configuration  # noqa: E501

        :return: The tool_id of this ToolConfig.  # noqa: E501
        :rtype: int
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this ToolConfig.

        the ID of the tool associated with this configuration  # noqa: E501

        :param tool_id: The tool_id of this ToolConfig.  # noqa: E501
        :type: int
        """

        self._tool_id = tool_id

    @property
    def bourreau_id(self):
        """Gets the bourreau_id of this ToolConfig.  # noqa: E501

        The ID of the execution server where this tool configuration is available.   # noqa: E501

        :return: The bourreau_id of this ToolConfig.  # noqa: E501
        :rtype: int
        """
        return self._bourreau_id

    @bourreau_id.setter
    def bourreau_id(self, bourreau_id):
        """Sets the bourreau_id of this ToolConfig.

        The ID of the execution server where this tool configuration is available.   # noqa: E501

        :param bourreau_id: The bourreau_id of this ToolConfig.  # noqa: E501
        :type: int
        """

        self._bourreau_id = bourreau_id

    @property
    def group_id(self):
        """Gets the group_id of this ToolConfig.  # noqa: E501

        the ID of the project controlling access to this ToolConfig  # noqa: E501

        :return: The group_id of this ToolConfig.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ToolConfig.

        the ID of the project controlling access to this ToolConfig  # noqa: E501

        :param group_id: The group_id of this ToolConfig.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def ncpus(self):
        """Gets the ncpus of this ToolConfig.  # noqa: E501

        A hint at how many CPUs the CBRAIN task will allocate to run this tool configuration   # noqa: E501

        :return: The ncpus of this ToolConfig.  # noqa: E501
        :rtype: int
        """
        return self._ncpus

    @ncpus.setter
    def ncpus(self, ncpus):
        """Sets the ncpus of this ToolConfig.

        A hint at how many CPUs the CBRAIN task will allocate to run this tool configuration   # noqa: E501

        :param ncpus: The ncpus of this ToolConfig.  # noqa: E501
        :type: int
        """

        self._ncpus = ncpus

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
        if issubclass(ToolConfig, dict):
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
        if not isinstance(other, ToolConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ToolConfig):
            return True

        return self.to_dict() != other.to_dict()
