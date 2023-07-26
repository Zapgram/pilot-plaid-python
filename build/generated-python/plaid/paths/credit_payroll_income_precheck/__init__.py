# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from plaid.paths.credit_payroll_income_precheck import Api

from plaid.paths import PathValues

path = PathValues.CREDIT_PAYROLL_INCOME_PRECHECK