# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.item_application_scopes_update import Api

from plaid.paths import PathValues

path = PathValues.ITEM_APPLICATION_SCOPES_UPDATE