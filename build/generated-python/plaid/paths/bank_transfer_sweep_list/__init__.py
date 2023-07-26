# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.bank_transfer_sweep_list import Api

from plaid.paths import PathValues

path = PathValues.BANK_TRANSFER_SWEEP_LIST