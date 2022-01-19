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

class PlayerSource(object):
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
        'institution': 'str',
        'institution_path': 'str',
        'institution_key': 'int',
        'logo': 'str'
    }

    attribute_map = {
        'institution': 'institution',
        'institution_path': 'institutionPath',
        'institution_key': 'institutionKey',
        'logo': 'logo'
    }

    def __init__(self, institution=None, institution_path=None, institution_key=None, logo=None):  # noqa: E501
        """PlayerSource - a model defined in Swagger"""  # noqa: E501
        self._institution = None
        self._institution_path = None
        self._institution_key = None
        self._logo = None
        self.discriminator = None
        if institution is not None:
            self.institution = institution
        if institution_path is not None:
            self.institution_path = institution_path
        if institution_key is not None:
            self.institution_key = institution_key
        if logo is not None:
            self.logo = logo

    @property
    def institution(self):
        """Gets the institution of this PlayerSource.  # noqa: E501


        :return: The institution of this PlayerSource.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this PlayerSource.


        :param institution: The institution of this PlayerSource.  # noqa: E501
        :type: str
        """

        self._institution = institution

    @property
    def institution_path(self):
        """Gets the institution_path of this PlayerSource.  # noqa: E501


        :return: The institution_path of this PlayerSource.  # noqa: E501
        :rtype: str
        """
        return self._institution_path

    @institution_path.setter
    def institution_path(self, institution_path):
        """Sets the institution_path of this PlayerSource.


        :param institution_path: The institution_path of this PlayerSource.  # noqa: E501
        :type: str
        """

        self._institution_path = institution_path

    @property
    def institution_key(self):
        """Gets the institution_key of this PlayerSource.  # noqa: E501


        :return: The institution_key of this PlayerSource.  # noqa: E501
        :rtype: int
        """
        return self._institution_key

    @institution_key.setter
    def institution_key(self, institution_key):
        """Sets the institution_key of this PlayerSource.


        :param institution_key: The institution_key of this PlayerSource.  # noqa: E501
        :type: int
        """

        self._institution_key = institution_key

    @property
    def logo(self):
        """Gets the logo of this PlayerSource.  # noqa: E501


        :return: The logo of this PlayerSource.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this PlayerSource.


        :param logo: The logo of this PlayerSource.  # noqa: E501
        :type: str
        """

        self._logo = logo

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
        if issubclass(PlayerSource, dict):
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
        if not isinstance(other, PlayerSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other