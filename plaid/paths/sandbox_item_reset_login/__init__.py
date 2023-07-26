# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.sandbox_item_reset_login import Api

from plaid.paths import PathValues

path = PathValues.SANDBOX_ITEM_RESET_LOGIN