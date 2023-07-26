# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.processor_stripe_bank_account_token_create import Api

from plaid.paths import PathValues

path = PathValues.PROCESSOR_STRIPE_BANK_ACCOUNT_TOKEN_CREATE