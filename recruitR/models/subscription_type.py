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

class SubscriptionType(object):
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
        'name': 'str',
        'base_price': 'float',
        'term': 'int',
        'description': 'str',
        'free_trial': 'int',
        'restricted_network': 'int',
        'alerts': 'int',
        'marketing_name': 'str',
        'recurly_name': 'str',
        'promotions': 'list[Promotion]',
        'subscriptions': 'list[Subscription]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'base_price': 'basePrice',
        'term': 'term',
        'description': 'description',
        'free_trial': 'freeTrial',
        'restricted_network': 'restrictedNetwork',
        'alerts': 'alerts',
        'marketing_name': 'marketingName',
        'recurly_name': 'recurlyName',
        'promotions': 'promotions',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, key=None, name=None, base_price=None, term=None, description=None, free_trial=None, restricted_network=None, alerts=None, marketing_name=None, recurly_name=None, promotions=None, subscriptions=None):  # noqa: E501
        """SubscriptionType - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._base_price = None
        self._term = None
        self._description = None
        self._free_trial = None
        self._restricted_network = None
        self._alerts = None
        self._marketing_name = None
        self._recurly_name = None
        self._promotions = None
        self._subscriptions = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if base_price is not None:
            self.base_price = base_price
        if term is not None:
            self.term = term
        if description is not None:
            self.description = description
        if free_trial is not None:
            self.free_trial = free_trial
        if restricted_network is not None:
            self.restricted_network = restricted_network
        if alerts is not None:
            self.alerts = alerts
        if marketing_name is not None:
            self.marketing_name = marketing_name
        if recurly_name is not None:
            self.recurly_name = recurly_name
        if promotions is not None:
            self.promotions = promotions
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def key(self):
        """Gets the key of this SubscriptionType.  # noqa: E501


        :return: The key of this SubscriptionType.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SubscriptionType.


        :param key: The key of this SubscriptionType.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this SubscriptionType.  # noqa: E501


        :return: The name of this SubscriptionType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionType.


        :param name: The name of this SubscriptionType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_price(self):
        """Gets the base_price of this SubscriptionType.  # noqa: E501


        :return: The base_price of this SubscriptionType.  # noqa: E501
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this SubscriptionType.


        :param base_price: The base_price of this SubscriptionType.  # noqa: E501
        :type: float
        """

        self._base_price = base_price

    @property
    def term(self):
        """Gets the term of this SubscriptionType.  # noqa: E501


        :return: The term of this SubscriptionType.  # noqa: E501
        :rtype: int
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this SubscriptionType.


        :param term: The term of this SubscriptionType.  # noqa: E501
        :type: int
        """

        self._term = term

    @property
    def description(self):
        """Gets the description of this SubscriptionType.  # noqa: E501


        :return: The description of this SubscriptionType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionType.


        :param description: The description of this SubscriptionType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def free_trial(self):
        """Gets the free_trial of this SubscriptionType.  # noqa: E501


        :return: The free_trial of this SubscriptionType.  # noqa: E501
        :rtype: int
        """
        return self._free_trial

    @free_trial.setter
    def free_trial(self, free_trial):
        """Sets the free_trial of this SubscriptionType.


        :param free_trial: The free_trial of this SubscriptionType.  # noqa: E501
        :type: int
        """

        self._free_trial = free_trial

    @property
    def restricted_network(self):
        """Gets the restricted_network of this SubscriptionType.  # noqa: E501


        :return: The restricted_network of this SubscriptionType.  # noqa: E501
        :rtype: int
        """
        return self._restricted_network

    @restricted_network.setter
    def restricted_network(self, restricted_network):
        """Sets the restricted_network of this SubscriptionType.


        :param restricted_network: The restricted_network of this SubscriptionType.  # noqa: E501
        :type: int
        """

        self._restricted_network = restricted_network

    @property
    def alerts(self):
        """Gets the alerts of this SubscriptionType.  # noqa: E501


        :return: The alerts of this SubscriptionType.  # noqa: E501
        :rtype: int
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this SubscriptionType.


        :param alerts: The alerts of this SubscriptionType.  # noqa: E501
        :type: int
        """

        self._alerts = alerts

    @property
    def marketing_name(self):
        """Gets the marketing_name of this SubscriptionType.  # noqa: E501


        :return: The marketing_name of this SubscriptionType.  # noqa: E501
        :rtype: str
        """
        return self._marketing_name

    @marketing_name.setter
    def marketing_name(self, marketing_name):
        """Sets the marketing_name of this SubscriptionType.


        :param marketing_name: The marketing_name of this SubscriptionType.  # noqa: E501
        :type: str
        """

        self._marketing_name = marketing_name

    @property
    def recurly_name(self):
        """Gets the recurly_name of this SubscriptionType.  # noqa: E501


        :return: The recurly_name of this SubscriptionType.  # noqa: E501
        :rtype: str
        """
        return self._recurly_name

    @recurly_name.setter
    def recurly_name(self, recurly_name):
        """Sets the recurly_name of this SubscriptionType.


        :param recurly_name: The recurly_name of this SubscriptionType.  # noqa: E501
        :type: str
        """

        self._recurly_name = recurly_name

    @property
    def promotions(self):
        """Gets the promotions of this SubscriptionType.  # noqa: E501


        :return: The promotions of this SubscriptionType.  # noqa: E501
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this SubscriptionType.


        :param promotions: The promotions of this SubscriptionType.  # noqa: E501
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def subscriptions(self):
        """Gets the subscriptions of this SubscriptionType.  # noqa: E501


        :return: The subscriptions of this SubscriptionType.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this SubscriptionType.


        :param subscriptions: The subscriptions of this SubscriptionType.  # noqa: E501
        :type: list[Subscription]
        """

        self._subscriptions = subscriptions

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
        if issubclass(SubscriptionType, dict):
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
        if not isinstance(other, SubscriptionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other