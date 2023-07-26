# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.sandbox_transfer_test_clock_list import Api

from plaid.paths import PathValues

path = PathValues.SANDBOX_TRANSFER_TEST_CLOCK_LIST