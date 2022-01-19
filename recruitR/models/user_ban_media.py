# coding: utf-8

"""
    Recruit Database

    Groups of services that manage the data for the 247Sports recruiting database.<br>                                         Documentation for this silo can be found here:                                         <a target=\"_blank\" href=\"https://atlassian.cbsi.com/confluence/display/TWOSPORTS/RDB+Information\">                                         Recruit Database Documentation</a>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserBanMedia(object):
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
        'key': 'int',
        'admin_user_key': 'int',
        '_date': 'datetime',
        'expire': 'datetime',
        'reason': 'str',
        'site_key': 'int',
        'user_key': 'int',
        'user': 'User',
        'site': 'Site',
        'admin_user': 'User'
    }

    attribute_map = {
        'key': 'key',
        'admin_user_key': 'adminUserKey',
        '_date': 'date',
        'expire': 'expire',
        'reason': 'reason',
        'site_key': 'siteKey',
        'user_key': 'userKey',
        'user': 'user',
        'site': 'site',
        'admin_user': 'adminUser'
    }

    def __init__(self, key=None, admin_user_key=None, _date=None, expire=None, reason=None, site_key=None, user_key=None, user=None, site=None, admin_user=None):  # noqa: E501
        """UserBanMedia - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._admin_user_key = None
        self.__date = None
        self._expire = None
        self._reason = None
        self._site_key = None
        self._user_key = None
        self._user = None
        self._site = None
        self._admin_user = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.admin_user_key = admin_user_key
        if _date is not None:
            self._date = _date
        if expire is not None:
            self.expire = expire
        self.reason = reason
        if site_key is not None:
            self.site_key = site_key
        self.user_key = user_key
        if user is not None:
            self.user = user
        if site is not None:
            self.site = site
        if admin_user is not None:
            self.admin_user = admin_user

    @property
    def key(self):
        """Gets the key of this UserBanMedia.  # noqa: E501


        :return: The key of this UserBanMedia.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserBanMedia.


        :param key: The key of this UserBanMedia.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def admin_user_key(self):
        """Gets the admin_user_key of this UserBanMedia.  # noqa: E501


        :return: The admin_user_key of this UserBanMedia.  # noqa: E501
        :rtype: int
        """
        return self._admin_user_key

    @admin_user_key.setter
    def admin_user_key(self, admin_user_key):
        """Sets the admin_user_key of this UserBanMedia.


        :param admin_user_key: The admin_user_key of this UserBanMedia.  # noqa: E501
        :type: int
        """
        if admin_user_key is None:
            raise ValueError("Invalid value for `admin_user_key`, must not be `None`")  # noqa: E501

        self._admin_user_key = admin_user_key

    @property
    def _date(self):
        """Gets the _date of this UserBanMedia.  # noqa: E501


        :return: The _date of this UserBanMedia.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this UserBanMedia.


        :param _date: The _date of this UserBanMedia.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def expire(self):
        """Gets the expire of this UserBanMedia.  # noqa: E501


        :return: The expire of this UserBanMedia.  # noqa: E501
        :rtype: datetime
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this UserBanMedia.


        :param expire: The expire of this UserBanMedia.  # noqa: E501
        :type: datetime
        """

        self._expire = expire

    @property
    def reason(self):
        """Gets the reason of this UserBanMedia.  # noqa: E501


        :return: The reason of this UserBanMedia.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UserBanMedia.


        :param reason: The reason of this UserBanMedia.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def site_key(self):
        """Gets the site_key of this UserBanMedia.  # noqa: E501


        :return: The site_key of this UserBanMedia.  # noqa: E501
        :rtype: int
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this UserBanMedia.


        :param site_key: The site_key of this UserBanMedia.  # noqa: E501
        :type: int
        """

        self._site_key = site_key

    @property
    def user_key(self):
        """Gets the user_key of this UserBanMedia.  # noqa: E501


        :return: The user_key of this UserBanMedia.  # noqa: E501
        :rtype: int
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this UserBanMedia.


        :param user_key: The user_key of this UserBanMedia.  # noqa: E501
        :type: int
        """
        if user_key is None:
            raise ValueError("Invalid value for `user_key`, must not be `None`")  # noqa: E501

        self._user_key = user_key

    @property
    def user(self):
        """Gets the user of this UserBanMedia.  # noqa: E501


        :return: The user of this UserBanMedia.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserBanMedia.


        :param user: The user of this UserBanMedia.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def site(self):
        """Gets the site of this UserBanMedia.  # noqa: E501


        :return: The site of this UserBanMedia.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this UserBanMedia.


        :param site: The site of this UserBanMedia.  # noqa: E501
        :type: Site
        """

        self._site = site

    @property
    def admin_user(self):
        """Gets the admin_user of this UserBanMedia.  # noqa: E501


        :return: The admin_user of this UserBanMedia.  # noqa: E501
        :rtype: User
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        """Sets the admin_user of this UserBanMedia.


        :param admin_user: The admin_user of this UserBanMedia.  # noqa: E501
        :type: User
        """

        self._admin_user = admin_user

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
        if issubclass(UserBanMedia, dict):
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
        if not isinstance(other, UserBanMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other