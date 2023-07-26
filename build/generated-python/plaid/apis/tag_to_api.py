import typing_extensions

from plaid.apis.tags import TagValues
from plaid.apis.tags.plaid_api import PlaidApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PLAID: PlaidApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PLAID: PlaidApi,
    }
)
