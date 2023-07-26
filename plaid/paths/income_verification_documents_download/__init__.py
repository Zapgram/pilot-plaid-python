# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.income_verification_documents_download import Api

from plaid.paths import PathValues

path = PathValues.INCOME_VERIFICATION_DOCUMENTS_DOWNLOAD