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


class User(object):
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
        'login': 'str',
        'password': 'str',
        'password_confirmation': 'str',
        'full_name': 'str',
        'email': 'str',
        'city': 'str',
        'country': 'str',
        'time_zone': 'str',
        'type': 'str',
        'site_id': 'int',
        'last_connected_at': 'str',
        'account_locked': 'str'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'password': 'password',
        'password_confirmation': 'password_confirmation',
        'full_name': 'full_name',
        'email': 'email',
        'city': 'city',
        'country': 'country',
        'time_zone': 'time_zone',
        'type': 'type',
        'site_id': 'site_id',
        'last_connected_at': 'last_connected_at',
        'account_locked': 'account_locked'
    }

    def __init__(self, id=None, login=None, password=None, password_confirmation=None, full_name=None, email=None, city=None, country=None, time_zone=None, type='NormalUser', site_id=None, last_connected_at=None, account_locked=None, _configuration=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._login = None
        self._password = None
        self._password_confirmation = None
        self._full_name = None
        self._email = None
        self._city = None
        self._country = None
        self._time_zone = None
        self._type = None
        self._site_id = None
        self._last_connected_at = None
        self._account_locked = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if password is not None:
            self.password = password
        if password_confirmation is not None:
            self.password_confirmation = password_confirmation
        if full_name is not None:
            self.full_name = full_name
        if email is not None:
            self.email = email
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if time_zone is not None:
            self.time_zone = time_zone
        if type is not None:
            self.type = type
        if site_id is not None:
            self.site_id = site_id
        if last_connected_at is not None:
            self.last_connected_at = last_connected_at
        if account_locked is not None:
            self.account_locked = account_locked

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        Unique numerical ID for the user.  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Unique numerical ID for the user.  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this User.  # noqa: E501

        UNIX-style username.  # noqa: E501

        :return: The login of this User.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this User.

        UNIX-style username.  # noqa: E501

        :param login: The login of this User.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501

        Password field  # noqa: E501

        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        Password field  # noqa: E501

        :param password: The password of this User.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_confirmation(self):
        """Gets the password_confirmation of this User.  # noqa: E501

        Password field (generally same as 'password')  # noqa: E501

        :return: The password_confirmation of this User.  # noqa: E501
        :rtype: str
        """
        return self._password_confirmation

    @password_confirmation.setter
    def password_confirmation(self, password_confirmation):
        """Sets the password_confirmation of this User.

        Password field (generally same as 'password')  # noqa: E501

        :param password_confirmation: The password_confirmation of this User.  # noqa: E501
        :type: str
        """

        self._password_confirmation = password_confirmation

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501

        Full name of the user.  # noqa: E501

        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.

        Full name of the user.  # noqa: E501

        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        email address of the user.  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        email address of the user.  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def city(self):
        """Gets the city of this User.  # noqa: E501

        city where the user is located  # noqa: E501

        :return: The city of this User.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this User.

        city where the user is located  # noqa: E501

        :param city: The city of this User.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this User.  # noqa: E501

        country where the user is located  # noqa: E501

        :return: The country of this User.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this User.

        country where the user is located  # noqa: E501

        :param country: The country of this User.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def time_zone(self):
        """Gets the time_zone of this User.  # noqa: E501

        time-zone (should make it this an enum)  # noqa: E501

        :return: The time_zone of this User.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this User.

        time-zone (should make it this an enum)  # noqa: E501

        :param time_zone: The time_zone of this User.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def type(self):
        """Gets the type of this User.  # noqa: E501

        Classification of user permission level  # noqa: E501

        :return: The type of this User.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this User.

        Classification of user permission level  # noqa: E501

        :param type: The type of this User.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def site_id(self):
        """Gets the site_id of this User.  # noqa: E501

        ID of the site affiliation for the user.  # noqa: E501

        :return: The site_id of this User.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this User.

        ID of the site affiliation for the user.  # noqa: E501

        :param site_id: The site_id of this User.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def last_connected_at(self):
        """Gets the last_connected_at of this User.  # noqa: E501

        time of last connection by the user. (can be empty)  # noqa: E501

        :return: The last_connected_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_connected_at

    @last_connected_at.setter
    def last_connected_at(self, last_connected_at):
        """Sets the last_connected_at of this User.

        time of last connection by the user. (can be empty)  # noqa: E501

        :param last_connected_at: The last_connected_at of this User.  # noqa: E501
        :type: str
        """

        self._last_connected_at = last_connected_at

    @property
    def account_locked(self):
        """Gets the account_locked of this User.  # noqa: E501

        Whether or not the account is locked.  # noqa: E501

        :return: The account_locked of this User.  # noqa: E501
        :rtype: str
        """
        return self._account_locked

    @account_locked.setter
    def account_locked(self, account_locked):
        """Sets the account_locked of this User.

        Whether or not the account is locked.  # noqa: E501

        :param account_locked: The account_locked of this User.  # noqa: E501
        :type: str
        """

        self._account_locked = account_locked

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()