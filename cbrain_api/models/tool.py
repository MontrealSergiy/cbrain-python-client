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


class Tool(object):
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
        'name': 'str',
        'user_id': 'int',
        'group_id': 'int',
        'category': 'str',
        'cbrain_task_class_name': 'str',
        'select_menu_text': 'str',
        'description': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_id': 'user_id',
        'group_id': 'group_id',
        'category': 'category',
        'cbrain_task_class_name': 'cbrain_task_class_name',
        'select_menu_text': 'select_menu_text',
        'description': 'description',
        'url': 'url'
    }

    def __init__(self, id=None, name=None, user_id=None, group_id=None, category=None, cbrain_task_class_name=None, select_menu_text=None, description=None, url=None, _configuration=None):  # noqa: E501
        """Tool - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._user_id = None
        self._group_id = None
        self._category = None
        self._cbrain_task_class_name = None
        self._select_menu_text = None
        self._description = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id
        if group_id is not None:
            self.group_id = group_id
        if category is not None:
            self.category = category
        if cbrain_task_class_name is not None:
            self.cbrain_task_class_name = cbrain_task_class_name
        if select_menu_text is not None:
            self.select_menu_text = select_menu_text
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Tool.  # noqa: E501

        Unique identifier for the Tool.  # noqa: E501

        :return: The id of this Tool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tool.

        Unique identifier for the Tool.  # noqa: E501

        :param id: The id of this Tool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Tool.  # noqa: E501

        Name of the Tool.  # noqa: E501

        :return: The name of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tool.

        Name of the Tool.  # noqa: E501

        :param name: The name of this Tool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this Tool.  # noqa: E501

        Creator of the Tool.  # noqa: E501

        :return: The user_id of this Tool.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Tool.

        Creator of the Tool.  # noqa: E501

        :param user_id: The user_id of this Tool.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """Gets the group_id of this Tool.  # noqa: E501

        Group that has access to the Tool.  # noqa: E501

        :return: The group_id of this Tool.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Tool.

        Group that has access to the Tool.  # noqa: E501

        :param group_id: The group_id of this Tool.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def category(self):
        """Gets the category of this Tool.  # noqa: E501

        Category of the Tool  # noqa: E501

        :return: The category of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Tool.

        Category of the Tool  # noqa: E501

        :param category: The category of this Tool.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def cbrain_task_class_name(self):
        """Gets the cbrain_task_class_name of this Tool.  # noqa: E501

        The name of the Task class that will be created when jobs are launched using the Tool.  # noqa: E501

        :return: The cbrain_task_class_name of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._cbrain_task_class_name

    @cbrain_task_class_name.setter
    def cbrain_task_class_name(self, cbrain_task_class_name):
        """Sets the cbrain_task_class_name of this Tool.

        The name of the Task class that will be created when jobs are launched using the Tool.  # noqa: E501

        :param cbrain_task_class_name: The cbrain_task_class_name of this Tool.  # noqa: E501
        :type: str
        """

        self._cbrain_task_class_name = cbrain_task_class_name

    @property
    def select_menu_text(self):
        """Gets the select_menu_text of this Tool.  # noqa: E501

        Text that appears for Tool selection.  # noqa: E501

        :return: The select_menu_text of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._select_menu_text

    @select_menu_text.setter
    def select_menu_text(self, select_menu_text):
        """Sets the select_menu_text of this Tool.

        Text that appears for Tool selection.  # noqa: E501

        :param select_menu_text: The select_menu_text of this Tool.  # noqa: E501
        :type: str
        """

        self._select_menu_text = select_menu_text

    @property
    def description(self):
        """Gets the description of this Tool.  # noqa: E501

        Description of the Tool.  # noqa: E501

        :return: The description of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tool.

        Description of the Tool.  # noqa: E501

        :param description: The description of this Tool.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this Tool.  # noqa: E501

        URL of the website that describes the Tool and possibly has code for the Tool.  # noqa: E501

        :return: The url of this Tool.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Tool.

        URL of the website that describes the Tool and possibly has code for the Tool.  # noqa: E501

        :param url: The url of this Tool.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Tool, dict):
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
        if not isinstance(other, Tool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tool):
            return True

        return self.to_dict() != other.to_dict()
