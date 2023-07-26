# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.link_oauth_correlation_id_exchange import Api

from plaid.paths import PathValues

path = PathValues.LINK_OAUTH_CORRELATION_ID_EXCHANGE