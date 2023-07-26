# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.processor_token_permissions_set import Api

from plaid.paths import PathValues

path = PathValues.PROCESSOR_TOKEN_PERMISSIONS_SET