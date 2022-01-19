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

class PlayerSportRankingDto(object):
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
        'player_sport_key': 'int',
        'ranking_key': 'int',
        'blurb': 'str'
    }

    attribute_map = {
        'player_sport_key': 'playerSportKey',
        'ranking_key': 'rankingKey',
        'blurb': 'blurb'
    }

    def __init__(self, player_sport_key=None, ranking_key=None, blurb=None):  # noqa: E501
        """PlayerSportRankingDto - a model defined in Swagger"""  # noqa: E501
        self._player_sport_key = None
        self._ranking_key = None
        self._blurb = None
        self.discriminator = None
        if player_sport_key is not None:
            self.player_sport_key = player_sport_key
        if ranking_key is not None:
            self.ranking_key = ranking_key
        if blurb is not None:
            self.blurb = blurb

    @property
    def player_sport_key(self):
        """Gets the player_sport_key of this PlayerSportRankingDto.  # noqa: E501


        :return: The player_sport_key of this PlayerSportRankingDto.  # noqa: E501
        :rtype: int
        """
        return self._player_sport_key

    @player_sport_key.setter
    def player_sport_key(self, player_sport_key):
        """Sets the player_sport_key of this PlayerSportRankingDto.


        :param player_sport_key: The player_sport_key of this PlayerSportRankingDto.  # noqa: E501
        :type: int
        """

        self._player_sport_key = player_sport_key

    @property
    def ranking_key(self):
        """Gets the ranking_key of this PlayerSportRankingDto.  # noqa: E501


        :return: The ranking_key of this PlayerSportRankingDto.  # noqa: E501
        :rtype: int
        """
        return self._ranking_key

    @ranking_key.setter
    def ranking_key(self, ranking_key):
        """Sets the ranking_key of this PlayerSportRankingDto.


        :param ranking_key: The ranking_key of this PlayerSportRankingDto.  # noqa: E501
        :type: int
        """

        self._ranking_key = ranking_key

    @property
    def blurb(self):
        """Gets the blurb of this PlayerSportRankingDto.  # noqa: E501


        :return: The blurb of this PlayerSportRankingDto.  # noqa: E501
        :rtype: str
        """
        return self._blurb

    @blurb.setter
    def blurb(self, blurb):
        """Sets the blurb of this PlayerSportRankingDto.


        :param blurb: The blurb of this PlayerSportRankingDto.  # noqa: E501
        :type: str
        """

        self._blurb = blurb

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
        if issubclass(PlayerSportRankingDto, dict):
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
        if not isinstance(other, PlayerSportRankingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other