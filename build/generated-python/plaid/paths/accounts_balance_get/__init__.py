# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.accounts_balance_get import Api

from plaid.paths import PathValues

path = PathValues.ACCOUNTS_BALANCE_GET