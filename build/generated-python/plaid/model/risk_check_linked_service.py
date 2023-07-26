# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.394.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from plaid import schemas  # noqa: F401


class RiskCheckLinkedService(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enum indicating the type of a linked service.
    """


    class MetaOapg:
        enum_value_to_name = {
            "apple": "APPLE",
            "ebay": "EBAY",
            "facebook": "FACEBOOK",
            "flickr": "FLICKR",
            "foursquare": "FOURSQUARE",
            "github": "GITHUB",
            "google": "GOOGLE",
            "gravatar": "GRAVATAR",
            "instagram": "INSTAGRAM",
            "lastfm": "LASTFM",
            "linkedin": "LINKEDIN",
            "microsoft": "MICROSOFT",
            "myspace": "MYSPACE",
            "pinterest": "PINTEREST",
            "skype": "SKYPE",
            "spotify": "SPOTIFY",
            "telegram": "TELEGRAM",
            "tumblr": "TUMBLR",
            "twitter": "TWITTER",
            "viber": "VIBER",
            "vimeo": "VIMEO",
            "weibo": "WEIBO",
            "whatsapp": "WHATSAPP",
            "yahoo": "YAHOO",
            "airbnb": "AIRBNB",
            "amazon": "AMAZON",
            "booking": "BOOKING",
            "discord": "DISCORD",
            "kakao": "KAKAO",
            "ok": "OK",
            "qzone": "QZONE",
            "line": "LINE",
            "snapchat": "SNAPCHAT",
            "zalo": "ZALO",
        }
    
    @schemas.classproperty
    def APPLE(cls):
        return cls("apple")
    
    @schemas.classproperty
    def EBAY(cls):
        return cls("ebay")
    
    @schemas.classproperty
    def FACEBOOK(cls):
        return cls("facebook")
    
    @schemas.classproperty
    def FLICKR(cls):
        return cls("flickr")
    
    @schemas.classproperty
    def FOURSQUARE(cls):
        return cls("foursquare")
    
    @schemas.classproperty
    def GITHUB(cls):
        return cls("github")
    
    @schemas.classproperty
    def GOOGLE(cls):
        return cls("google")
    
    @schemas.classproperty
    def GRAVATAR(cls):
        return cls("gravatar")
    
    @schemas.classproperty
    def INSTAGRAM(cls):
        return cls("instagram")
    
    @schemas.classproperty
    def LASTFM(cls):
        return cls("lastfm")
    
    @schemas.classproperty
    def LINKEDIN(cls):
        return cls("linkedin")
    
    @schemas.classproperty
    def MICROSOFT(cls):
        return cls("microsoft")
    
    @schemas.classproperty
    def MYSPACE(cls):
        return cls("myspace")
    
    @schemas.classproperty
    def PINTEREST(cls):
        return cls("pinterest")
    
    @schemas.classproperty
    def SKYPE(cls):
        return cls("skype")
    
    @schemas.classproperty
    def SPOTIFY(cls):
        return cls("spotify")
    
    @schemas.classproperty
    def TELEGRAM(cls):
        return cls("telegram")
    
    @schemas.classproperty
    def TUMBLR(cls):
        return cls("tumblr")
    
    @schemas.classproperty
    def TWITTER(cls):
        return cls("twitter")
    
    @schemas.classproperty
    def VIBER(cls):
        return cls("viber")
    
    @schemas.classproperty
    def VIMEO(cls):
        return cls("vimeo")
    
    @schemas.classproperty
    def WEIBO(cls):
        return cls("weibo")
    
    @schemas.classproperty
    def WHATSAPP(cls):
        return cls("whatsapp")
    
    @schemas.classproperty
    def YAHOO(cls):
        return cls("yahoo")
    
    @schemas.classproperty
    def AIRBNB(cls):
        return cls("airbnb")
    
    @schemas.classproperty
    def AMAZON(cls):
        return cls("amazon")
    
    @schemas.classproperty
    def BOOKING(cls):
        return cls("booking")
    
    @schemas.classproperty
    def DISCORD(cls):
        return cls("discord")
    
    @schemas.classproperty
    def KAKAO(cls):
        return cls("kakao")
    
    @schemas.classproperty
    def OK(cls):
        return cls("ok")
    
    @schemas.classproperty
    def QZONE(cls):
        return cls("qzone")
    
    @schemas.classproperty
    def LINE(cls):
        return cls("line")
    
    @schemas.classproperty
    def SNAPCHAT(cls):
        return cls("snapchat")
    
    @schemas.classproperty
    def ZALO(cls):
        return cls("zalo")
