import typing_extensions

from plaid.paths import PathValues
from plaid.apis.paths.asset_report_create import AssetReportCreate
from plaid.apis.paths.asset_report_get import AssetReportGet
from plaid.apis.paths.asset_report_pdf_get import AssetReportPdfGet
from plaid.apis.paths.asset_report_refresh import AssetReportRefresh
from plaid.apis.paths.asset_report_filter import AssetReportFilter
from plaid.apis.paths.asset_report_remove import AssetReportRemove
from plaid.apis.paths.asset_report_audit_copy_create import AssetReportAuditCopyCreate
from plaid.apis.paths.asset_report_audit_copy_get import AssetReportAuditCopyGet
from plaid.apis.paths.asset_report_audit_copy_remove import AssetReportAuditCopyRemove
from plaid.apis.paths.credit_audit_copy_token_update import CreditAuditCopyTokenUpdate
from plaid.apis.paths.statements_list import StatementsList
from plaid.apis.paths.statements_download import StatementsDownload
from plaid.apis.paths.item_activity_list import ItemActivityList
from plaid.apis.paths.item_application_list import ItemApplicationList
from plaid.apis.paths.item_application_scopes_update import ItemApplicationScopesUpdate
from plaid.apis.paths.application_get import ApplicationGet
from plaid.apis.paths.item_get import ItemGet
from plaid.apis.paths.auth_get import AuthGet
from plaid.apis.paths.transactions_get import TransactionsGet
from plaid.apis.paths.transactions_refresh import TransactionsRefresh
from plaid.apis.paths.transactions_recurring_get import TransactionsRecurringGet
from plaid.apis.paths.transactions_recurring_deactivate import TransactionsRecurringDeactivate
from plaid.apis.paths.transactions_sync import TransactionsSync
from plaid.apis.paths.transactions_enrich import TransactionsEnrich
from plaid.apis.paths.institutions_get import InstitutionsGet
from plaid.apis.paths.institutions_search import InstitutionsSearch
from plaid.apis.paths.institutions_get_by_id import InstitutionsGetById
from plaid.apis.paths.item_remove import ItemRemove
from plaid.apis.paths.accounts_get import AccountsGet
from plaid.apis.paths.categories_get import CategoriesGet
from plaid.apis.paths.sandbox_processor_token_create import SandboxProcessorTokenCreate
from plaid.apis.paths.sandbox_public_token_create import SandboxPublicTokenCreate
from plaid.apis.paths.sandbox_item_fire_webhook import SandboxItemFireWebhook
from plaid.apis.paths.accounts_balance_get import AccountsBalanceGet
from plaid.apis.paths.identity_get import IdentityGet
from plaid.apis.paths.identity_match import IdentityMatch
from plaid.apis.paths.identity_refresh import IdentityRefresh
from plaid.apis.paths.dashboard_user_get import DashboardUserGet
from plaid.apis.paths.dashboard_user_list import DashboardUserList
from plaid.apis.paths.identity_verification_create import IdentityVerificationCreate
from plaid.apis.paths.identity_verification_get import IdentityVerificationGet
from plaid.apis.paths.identity_verification_list import IdentityVerificationList
from plaid.apis.paths.identity_verification_retry import IdentityVerificationRetry
from plaid.apis.paths.watchlist_screening_entity_create import WatchlistScreeningEntityCreate
from plaid.apis.paths.watchlist_screening_entity_get import WatchlistScreeningEntityGet
from plaid.apis.paths.watchlist_screening_entity_history_list import WatchlistScreeningEntityHistoryList
from plaid.apis.paths.watchlist_screening_entity_hit_list import WatchlistScreeningEntityHitList
from plaid.apis.paths.watchlist_screening_entity_list import WatchlistScreeningEntityList
from plaid.apis.paths.watchlist_screening_entity_program_get import WatchlistScreeningEntityProgramGet
from plaid.apis.paths.watchlist_screening_entity_program_list import WatchlistScreeningEntityProgramList
from plaid.apis.paths.watchlist_screening_entity_review_create import WatchlistScreeningEntityReviewCreate
from plaid.apis.paths.watchlist_screening_entity_review_list import WatchlistScreeningEntityReviewList
from plaid.apis.paths.watchlist_screening_entity_update import WatchlistScreeningEntityUpdate
from plaid.apis.paths.watchlist_screening_individual_create import WatchlistScreeningIndividualCreate
from plaid.apis.paths.watchlist_screening_individual_get import WatchlistScreeningIndividualGet
from plaid.apis.paths.watchlist_screening_individual_history_list import WatchlistScreeningIndividualHistoryList
from plaid.apis.paths.watchlist_screening_individual_hit_list import WatchlistScreeningIndividualHitList
from plaid.apis.paths.watchlist_screening_individual_list import WatchlistScreeningIndividualList
from plaid.apis.paths.watchlist_screening_individual_program_get import WatchlistScreeningIndividualProgramGet
from plaid.apis.paths.watchlist_screening_individual_program_list import WatchlistScreeningIndividualProgramList
from plaid.apis.paths.watchlist_screening_individual_review_create import WatchlistScreeningIndividualReviewCreate
from plaid.apis.paths.watchlist_screening_individual_review_list import WatchlistScreeningIndividualReviewList
from plaid.apis.paths.watchlist_screening_individual_update import WatchlistScreeningIndividualUpdate
from plaid.apis.paths.processor_auth_get import ProcessorAuthGet
from plaid.apis.paths.processor_transactions_get import ProcessorTransactionsGet
from plaid.apis.paths.processor_transactions_sync import ProcessorTransactionsSync
from plaid.apis.paths.processor_transactions_refresh import ProcessorTransactionsRefresh
from plaid.apis.paths.processor_transactions_recurring_get import ProcessorTransactionsRecurringGet
from plaid.apis.paths.processor_signal_evaluate import ProcessorSignalEvaluate
from plaid.apis.paths.processor_signal_decision_report import ProcessorSignalDecisionReport
from plaid.apis.paths.processor_signal_return_report import ProcessorSignalReturnReport
from plaid.apis.paths.processor_bank_transfer_create import ProcessorBankTransferCreate
from plaid.apis.paths.processor_identity_get import ProcessorIdentityGet
from plaid.apis.paths.processor_identity_match import ProcessorIdentityMatch
from plaid.apis.paths.processor_balance_get import ProcessorBalanceGet
from plaid.apis.paths.item_webhook_update import ItemWebhookUpdate
from plaid.apis.paths.item_access_token_invalidate import ItemAccessTokenInvalidate
from plaid.apis.paths.webhook_verification_key_get import WebhookVerificationKeyGet
from plaid.apis.paths.liabilities_get import LiabilitiesGet
from plaid.apis.paths.payment_initiation_recipient_create import PaymentInitiationRecipientCreate
from plaid.apis.paths.payment_initiation_payment_reverse import PaymentInitiationPaymentReverse
from plaid.apis.paths.payment_initiation_recipient_get import PaymentInitiationRecipientGet
from plaid.apis.paths.payment_initiation_recipient_list import PaymentInitiationRecipientList
from plaid.apis.paths.payment_initiation_payment_create import PaymentInitiationPaymentCreate
from plaid.apis.paths.payment_initiation_payment_token_create import PaymentInitiationPaymentTokenCreate
from plaid.apis.paths.payment_initiation_consent_create import PaymentInitiationConsentCreate
from plaid.apis.paths.payment_initiation_consent_get import PaymentInitiationConsentGet
from plaid.apis.paths.payment_initiation_consent_revoke import PaymentInitiationConsentRevoke
from plaid.apis.paths.payment_initiation_consent_payment_execute import PaymentInitiationConsentPaymentExecute
from plaid.apis.paths.sandbox_item_reset_login import SandboxItemResetLogin
from plaid.apis.paths.sandbox_item_set_verification_status import SandboxItemSetVerificationStatus
from plaid.apis.paths.item_public_token_exchange import ItemPublicTokenExchange
from plaid.apis.paths.item_public_token_create import ItemPublicTokenCreate
from plaid.apis.paths.user_create import UserCreate
from plaid.apis.paths.credit_sessions_get import CreditSessionsGet
from plaid.apis.paths.payment_initiation_payment_get import PaymentInitiationPaymentGet
from plaid.apis.paths.payment_initiation_payment_list import PaymentInitiationPaymentList
from plaid.apis.paths.investments_holdings_get import InvestmentsHoldingsGet
from plaid.apis.paths.investments_transactions_get import InvestmentsTransactionsGet
from plaid.apis.paths.investments_refresh import InvestmentsRefresh
from plaid.apis.paths.investments_auth_get import InvestmentsAuthGet
from plaid.apis.paths.processor_token_create import ProcessorTokenCreate
from plaid.apis.paths.processor_token_permissions_set import ProcessorTokenPermissionsSet
from plaid.apis.paths.processor_token_permissions_get import ProcessorTokenPermissionsGet
from plaid.apis.paths.processor_token_webhook_update import ProcessorTokenWebhookUpdate
from plaid.apis.paths.processor_stripe_bank_account_token_create import ProcessorStripeBankAccountTokenCreate
from plaid.apis.paths.processor_apex_processor_token_create import ProcessorApexProcessorTokenCreate
from plaid.apis.paths.deposit_switch_create import DepositSwitchCreate
from plaid.apis.paths.item_import import ItemImport
from plaid.apis.paths.deposit_switch_token_create import DepositSwitchTokenCreate
from plaid.apis.paths.link_token_create import LinkTokenCreate
from plaid.apis.paths.link_token_get import LinkTokenGet
from plaid.apis.paths.link_oauth_correlation_id_exchange import LinkOauthCorrelationIdExchange
from plaid.apis.paths.deposit_switch_get import DepositSwitchGet
from plaid.apis.paths.transfer_get import TransferGet
from plaid.apis.paths.transfer_recurring_get import TransferRecurringGet
from plaid.apis.paths.bank_transfer_get import BankTransferGet
from plaid.apis.paths.transfer_authorization_create import TransferAuthorizationCreate
from plaid.apis.paths.transfer_balance_get import TransferBalanceGet
from plaid.apis.paths.transfer_capabilities_get import TransferCapabilitiesGet
from plaid.apis.paths.transfer_configuration_get import TransferConfigurationGet
from plaid.apis.paths.transfer_metrics_get import TransferMetricsGet
from plaid.apis.paths.transfer_create import TransferCreate
from plaid.apis.paths.transfer_recurring_create import TransferRecurringCreate
from plaid.apis.paths.bank_transfer_create import BankTransferCreate
from plaid.apis.paths.transfer_list import TransferList
from plaid.apis.paths.transfer_recurring_list import TransferRecurringList
from plaid.apis.paths.bank_transfer_list import BankTransferList
from plaid.apis.paths.transfer_cancel import TransferCancel
from plaid.apis.paths.transfer_recurring_cancel import TransferRecurringCancel
from plaid.apis.paths.bank_transfer_cancel import BankTransferCancel
from plaid.apis.paths.transfer_event_list import TransferEventList
from plaid.apis.paths.bank_transfer_event_list import BankTransferEventList
from plaid.apis.paths.transfer_event_sync import TransferEventSync
from plaid.apis.paths.bank_transfer_event_sync import BankTransferEventSync
from plaid.apis.paths.transfer_sweep_get import TransferSweepGet
from plaid.apis.paths.bank_transfer_sweep_get import BankTransferSweepGet
from plaid.apis.paths.transfer_sweep_list import TransferSweepList
from plaid.apis.paths.bank_transfer_sweep_list import BankTransferSweepList
from plaid.apis.paths.bank_transfer_balance_get import BankTransferBalanceGet
from plaid.apis.paths.bank_transfer_migrate_account import BankTransferMigrateAccount
from plaid.apis.paths.transfer_migrate_account import TransferMigrateAccount
from plaid.apis.paths.transfer_intent_create import TransferIntentCreate
from plaid.apis.paths.transfer_intent_get import TransferIntentGet
from plaid.apis.paths.transfer_repayment_list import TransferRepaymentList
from plaid.apis.paths.transfer_repayment_return_list import TransferRepaymentReturnList
from plaid.apis.paths.transfer_originator_create import TransferOriginatorCreate
from plaid.apis.paths.transfer_questionnaire_create import TransferQuestionnaireCreate
from plaid.apis.paths.transfer_diligence_submit import TransferDiligenceSubmit
from plaid.apis.paths.transfer_diligence_document_upload import TransferDiligenceDocumentUpload
from plaid.apis.paths.transfer_originator_get import TransferOriginatorGet
from plaid.apis.paths.transfer_originator_list import TransferOriginatorList
from plaid.apis.paths.transfer_refund_create import TransferRefundCreate
from plaid.apis.paths.transfer_refund_get import TransferRefundGet
from plaid.apis.paths.transfer_refund_cancel import TransferRefundCancel
from plaid.apis.paths.sandbox_bank_transfer_simulate import SandboxBankTransferSimulate
from plaid.apis.paths.sandbox_transfer_sweep_simulate import SandboxTransferSweepSimulate
from plaid.apis.paths.sandbox_transfer_simulate import SandboxTransferSimulate
from plaid.apis.paths.sandbox_transfer_repayment_simulate import SandboxTransferRepaymentSimulate
from plaid.apis.paths.sandbox_transfer_fire_webhook import SandboxTransferFireWebhook
from plaid.apis.paths.sandbox_transfer_test_clock_create import SandboxTransferTestClockCreate
from plaid.apis.paths.sandbox_transfer_test_clock_advance import SandboxTransferTestClockAdvance
from plaid.apis.paths.sandbox_transfer_test_clock_get import SandboxTransferTestClockGet
from plaid.apis.paths.sandbox_transfer_test_clock_list import SandboxTransferTestClockList
from plaid.apis.paths.sandbox_payment_profile_reset_login import SandboxPaymentProfileResetLogin
from plaid.apis.paths.employers_search import EmployersSearch
from plaid.apis.paths.income_verification_create import IncomeVerificationCreate
from plaid.apis.paths.income_verification_paystubs_get import IncomeVerificationPaystubsGet
from plaid.apis.paths.income_verification_documents_download import IncomeVerificationDocumentsDownload
from plaid.apis.paths.income_verification_taxforms_get import IncomeVerificationTaxformsGet
from plaid.apis.paths.income_verification_precheck import IncomeVerificationPrecheck
from plaid.apis.paths.employment_verification_get import EmploymentVerificationGet
from plaid.apis.paths.deposit_switch_alt_create import DepositSwitchAltCreate
from plaid.apis.paths.credit_audit_copy_token_create import CreditAuditCopyTokenCreate
from plaid.apis.paths.credit_audit_copy_token_remove import CreditAuditCopyTokenRemove
from plaid.apis.paths.credit_asset_report_freddie_mac_get import CreditAssetReportFreddieMacGet
from plaid.apis.paths.credit_freddie_mac_reports_get import CreditFreddieMacReportsGet
from plaid.apis.paths.beta_credit_v1_bank_employment_get import BetaCreditV1BankEmploymentGet
from plaid.apis.paths.credit_bank_income_get import CreditBankIncomeGet
from plaid.apis.paths.credit_bank_income_pdf_get import CreditBankIncomePdfGet
from plaid.apis.paths.credit_bank_income_refresh import CreditBankIncomeRefresh
from plaid.apis.paths.credit_bank_income_webhook_update import CreditBankIncomeWebhookUpdate
from plaid.apis.paths.credit_bank_statements_uploads_get import CreditBankStatementsUploadsGet
from plaid.apis.paths.credit_payroll_income_get import CreditPayrollIncomeGet
from plaid.apis.paths.credit_payroll_income_risk_signals_get import CreditPayrollIncomeRiskSignalsGet
from plaid.apis.paths.credit_payroll_income_precheck import CreditPayrollIncomePrecheck
from plaid.apis.paths.credit_employment_get import CreditEmploymentGet
from plaid.apis.paths.credit_payroll_income_refresh import CreditPayrollIncomeRefresh
from plaid.apis.paths.credit_relay_create import CreditRelayCreate
from plaid.apis.paths.credit_relay_get import CreditRelayGet
from plaid.apis.paths.credit_relay_refresh import CreditRelayRefresh
from plaid.apis.paths.credit_relay_remove import CreditRelayRemove
from plaid.apis.paths.sandbox_bank_transfer_fire_webhook import SandboxBankTransferFireWebhook
from plaid.apis.paths.sandbox_income_fire_webhook import SandboxIncomeFireWebhook
from plaid.apis.paths.sandbox_bank_income_fire_webhook import SandboxBankIncomeFireWebhook
from plaid.apis.paths.sandbox_oauth_select_accounts import SandboxOauthSelectAccounts
from plaid.apis.paths.signal_evaluate import SignalEvaluate
from plaid.apis.paths.signal_decision_report import SignalDecisionReport
from plaid.apis.paths.signal_return_report import SignalReturnReport
from plaid.apis.paths.signal_prepare import SignalPrepare
from plaid.apis.paths.wallet_create import WalletCreate
from plaid.apis.paths.wallet_get import WalletGet
from plaid.apis.paths.wallet_list import WalletList
from plaid.apis.paths.wallet_transaction_execute import WalletTransactionExecute
from plaid.apis.paths.wallet_transaction_get import WalletTransactionGet
from plaid.apis.paths.wallet_transaction_list import WalletTransactionList
from plaid.apis.paths.beta_transactions_v1_enhance import BetaTransactionsV1Enhance
from plaid.apis.paths.beta_transactions_rules_v1_create import BetaTransactionsRulesV1Create
from plaid.apis.paths.beta_transactions_rules_v1_list import BetaTransactionsRulesV1List
from plaid.apis.paths.beta_transactions_rules_v1_remove import BetaTransactionsRulesV1Remove
from plaid.apis.paths.payment_profile_create import PaymentProfileCreate
from plaid.apis.paths.payment_profile_get import PaymentProfileGet
from plaid.apis.paths.payment_profile_remove import PaymentProfileRemove
from plaid.apis.paths.partner_customer_create import PartnerCustomerCreate
from plaid.apis.paths.partner_customer_get import PartnerCustomerGet
from plaid.apis.paths.partner_customer_enable import PartnerCustomerEnable
from plaid.apis.paths.partner_customer_remove import PartnerCustomerRemove
from plaid.apis.paths.partner_customer_oauth_institutions_get import PartnerCustomerOauthInstitutionsGet
from plaid.apis.paths.link_delivery_create import LinkDeliveryCreate
from plaid.apis.paths.link_delivery_get import LinkDeliveryGet
from plaid.apis.paths.fdx_notifications import FdxNotifications

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ASSET_REPORT_CREATE: AssetReportCreate,
        PathValues.ASSET_REPORT_GET: AssetReportGet,
        PathValues.ASSET_REPORT_PDF_GET: AssetReportPdfGet,
        PathValues.ASSET_REPORT_REFRESH: AssetReportRefresh,
        PathValues.ASSET_REPORT_FILTER: AssetReportFilter,
        PathValues.ASSET_REPORT_REMOVE: AssetReportRemove,
        PathValues.ASSET_REPORT_AUDIT_COPY_CREATE: AssetReportAuditCopyCreate,
        PathValues.ASSET_REPORT_AUDIT_COPY_GET: AssetReportAuditCopyGet,
        PathValues.ASSET_REPORT_AUDIT_COPY_REMOVE: AssetReportAuditCopyRemove,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_UPDATE: CreditAuditCopyTokenUpdate,
        PathValues.STATEMENTS_LIST: StatementsList,
        PathValues.STATEMENTS_DOWNLOAD: StatementsDownload,
        PathValues.ITEM_ACTIVITY_LIST: ItemActivityList,
        PathValues.ITEM_APPLICATION_LIST: ItemApplicationList,
        PathValues.ITEM_APPLICATION_SCOPES_UPDATE: ItemApplicationScopesUpdate,
        PathValues.APPLICATION_GET: ApplicationGet,
        PathValues.ITEM_GET: ItemGet,
        PathValues.AUTH_GET: AuthGet,
        PathValues.TRANSACTIONS_GET: TransactionsGet,
        PathValues.TRANSACTIONS_REFRESH: TransactionsRefresh,
        PathValues.TRANSACTIONS_RECURRING_GET: TransactionsRecurringGet,
        PathValues.TRANSACTIONS_RECURRING_DEACTIVATE: TransactionsRecurringDeactivate,
        PathValues.TRANSACTIONS_SYNC: TransactionsSync,
        PathValues.TRANSACTIONS_ENRICH: TransactionsEnrich,
        PathValues.INSTITUTIONS_GET: InstitutionsGet,
        PathValues.INSTITUTIONS_SEARCH: InstitutionsSearch,
        PathValues.INSTITUTIONS_GET_BY_ID: InstitutionsGetById,
        PathValues.ITEM_REMOVE: ItemRemove,
        PathValues.ACCOUNTS_GET: AccountsGet,
        PathValues.CATEGORIES_GET: CategoriesGet,
        PathValues.SANDBOX_PROCESSOR_TOKEN_CREATE: SandboxProcessorTokenCreate,
        PathValues.SANDBOX_PUBLIC_TOKEN_CREATE: SandboxPublicTokenCreate,
        PathValues.SANDBOX_ITEM_FIRE_WEBHOOK: SandboxItemFireWebhook,
        PathValues.ACCOUNTS_BALANCE_GET: AccountsBalanceGet,
        PathValues.IDENTITY_GET: IdentityGet,
        PathValues.IDENTITY_MATCH: IdentityMatch,
        PathValues.IDENTITY_REFRESH: IdentityRefresh,
        PathValues.DASHBOARD_USER_GET: DashboardUserGet,
        PathValues.DASHBOARD_USER_LIST: DashboardUserList,
        PathValues.IDENTITY_VERIFICATION_CREATE: IdentityVerificationCreate,
        PathValues.IDENTITY_VERIFICATION_GET: IdentityVerificationGet,
        PathValues.IDENTITY_VERIFICATION_LIST: IdentityVerificationList,
        PathValues.IDENTITY_VERIFICATION_RETRY: IdentityVerificationRetry,
        PathValues.WATCHLIST_SCREENING_ENTITY_CREATE: WatchlistScreeningEntityCreate,
        PathValues.WATCHLIST_SCREENING_ENTITY_GET: WatchlistScreeningEntityGet,
        PathValues.WATCHLIST_SCREENING_ENTITY_HISTORY_LIST: WatchlistScreeningEntityHistoryList,
        PathValues.WATCHLIST_SCREENING_ENTITY_HIT_LIST: WatchlistScreeningEntityHitList,
        PathValues.WATCHLIST_SCREENING_ENTITY_LIST: WatchlistScreeningEntityList,
        PathValues.WATCHLIST_SCREENING_ENTITY_PROGRAM_GET: WatchlistScreeningEntityProgramGet,
        PathValues.WATCHLIST_SCREENING_ENTITY_PROGRAM_LIST: WatchlistScreeningEntityProgramList,
        PathValues.WATCHLIST_SCREENING_ENTITY_REVIEW_CREATE: WatchlistScreeningEntityReviewCreate,
        PathValues.WATCHLIST_SCREENING_ENTITY_REVIEW_LIST: WatchlistScreeningEntityReviewList,
        PathValues.WATCHLIST_SCREENING_ENTITY_UPDATE: WatchlistScreeningEntityUpdate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_CREATE: WatchlistScreeningIndividualCreate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_GET: WatchlistScreeningIndividualGet,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_HISTORY_LIST: WatchlistScreeningIndividualHistoryList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_HIT_LIST: WatchlistScreeningIndividualHitList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_LIST: WatchlistScreeningIndividualList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_PROGRAM_GET: WatchlistScreeningIndividualProgramGet,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_PROGRAM_LIST: WatchlistScreeningIndividualProgramList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_REVIEW_CREATE: WatchlistScreeningIndividualReviewCreate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_REVIEW_LIST: WatchlistScreeningIndividualReviewList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_UPDATE: WatchlistScreeningIndividualUpdate,
        PathValues.PROCESSOR_AUTH_GET: ProcessorAuthGet,
        PathValues.PROCESSOR_TRANSACTIONS_GET: ProcessorTransactionsGet,
        PathValues.PROCESSOR_TRANSACTIONS_SYNC: ProcessorTransactionsSync,
        PathValues.PROCESSOR_TRANSACTIONS_REFRESH: ProcessorTransactionsRefresh,
        PathValues.PROCESSOR_TRANSACTIONS_RECURRING_GET: ProcessorTransactionsRecurringGet,
        PathValues.PROCESSOR_SIGNAL_EVALUATE: ProcessorSignalEvaluate,
        PathValues.PROCESSOR_SIGNAL_DECISION_REPORT: ProcessorSignalDecisionReport,
        PathValues.PROCESSOR_SIGNAL_RETURN_REPORT: ProcessorSignalReturnReport,
        PathValues.PROCESSOR_BANK_TRANSFER_CREATE: ProcessorBankTransferCreate,
        PathValues.PROCESSOR_IDENTITY_GET: ProcessorIdentityGet,
        PathValues.PROCESSOR_IDENTITY_MATCH: ProcessorIdentityMatch,
        PathValues.PROCESSOR_BALANCE_GET: ProcessorBalanceGet,
        PathValues.ITEM_WEBHOOK_UPDATE: ItemWebhookUpdate,
        PathValues.ITEM_ACCESS_TOKEN_INVALIDATE: ItemAccessTokenInvalidate,
        PathValues.WEBHOOK_VERIFICATION_KEY_GET: WebhookVerificationKeyGet,
        PathValues.LIABILITIES_GET: LiabilitiesGet,
        PathValues.PAYMENT_INITIATION_RECIPIENT_CREATE: PaymentInitiationRecipientCreate,
        PathValues.PAYMENT_INITIATION_PAYMENT_REVERSE: PaymentInitiationPaymentReverse,
        PathValues.PAYMENT_INITIATION_RECIPIENT_GET: PaymentInitiationRecipientGet,
        PathValues.PAYMENT_INITIATION_RECIPIENT_LIST: PaymentInitiationRecipientList,
        PathValues.PAYMENT_INITIATION_PAYMENT_CREATE: PaymentInitiationPaymentCreate,
        PathValues.PAYMENT_INITIATION_PAYMENT_TOKEN_CREATE: PaymentInitiationPaymentTokenCreate,
        PathValues.PAYMENT_INITIATION_CONSENT_CREATE: PaymentInitiationConsentCreate,
        PathValues.PAYMENT_INITIATION_CONSENT_GET: PaymentInitiationConsentGet,
        PathValues.PAYMENT_INITIATION_CONSENT_REVOKE: PaymentInitiationConsentRevoke,
        PathValues.PAYMENT_INITIATION_CONSENT_PAYMENT_EXECUTE: PaymentInitiationConsentPaymentExecute,
        PathValues.SANDBOX_ITEM_RESET_LOGIN: SandboxItemResetLogin,
        PathValues.SANDBOX_ITEM_SET_VERIFICATION_STATUS: SandboxItemSetVerificationStatus,
        PathValues.ITEM_PUBLIC_TOKEN_EXCHANGE: ItemPublicTokenExchange,
        PathValues.ITEM_PUBLIC_TOKEN_CREATE: ItemPublicTokenCreate,
        PathValues.USER_CREATE: UserCreate,
        PathValues.CREDIT_SESSIONS_GET: CreditSessionsGet,
        PathValues.PAYMENT_INITIATION_PAYMENT_GET: PaymentInitiationPaymentGet,
        PathValues.PAYMENT_INITIATION_PAYMENT_LIST: PaymentInitiationPaymentList,
        PathValues.INVESTMENTS_HOLDINGS_GET: InvestmentsHoldingsGet,
        PathValues.INVESTMENTS_TRANSACTIONS_GET: InvestmentsTransactionsGet,
        PathValues.INVESTMENTS_REFRESH: InvestmentsRefresh,
        PathValues.INVESTMENTS_AUTH_GET: InvestmentsAuthGet,
        PathValues.PROCESSOR_TOKEN_CREATE: ProcessorTokenCreate,
        PathValues.PROCESSOR_TOKEN_PERMISSIONS_SET: ProcessorTokenPermissionsSet,
        PathValues.PROCESSOR_TOKEN_PERMISSIONS_GET: ProcessorTokenPermissionsGet,
        PathValues.PROCESSOR_TOKEN_WEBHOOK_UPDATE: ProcessorTokenWebhookUpdate,
        PathValues.PROCESSOR_STRIPE_BANK_ACCOUNT_TOKEN_CREATE: ProcessorStripeBankAccountTokenCreate,
        PathValues.PROCESSOR_APEX_PROCESSOR_TOKEN_CREATE: ProcessorApexProcessorTokenCreate,
        PathValues.DEPOSIT_SWITCH_CREATE: DepositSwitchCreate,
        PathValues.ITEM_IMPORT: ItemImport,
        PathValues.DEPOSIT_SWITCH_TOKEN_CREATE: DepositSwitchTokenCreate,
        PathValues.LINK_TOKEN_CREATE: LinkTokenCreate,
        PathValues.LINK_TOKEN_GET: LinkTokenGet,
        PathValues.LINK_OAUTH_CORRELATION_ID_EXCHANGE: LinkOauthCorrelationIdExchange,
        PathValues.DEPOSIT_SWITCH_GET: DepositSwitchGet,
        PathValues.TRANSFER_GET: TransferGet,
        PathValues.TRANSFER_RECURRING_GET: TransferRecurringGet,
        PathValues.BANK_TRANSFER_GET: BankTransferGet,
        PathValues.TRANSFER_AUTHORIZATION_CREATE: TransferAuthorizationCreate,
        PathValues.TRANSFER_BALANCE_GET: TransferBalanceGet,
        PathValues.TRANSFER_CAPABILITIES_GET: TransferCapabilitiesGet,
        PathValues.TRANSFER_CONFIGURATION_GET: TransferConfigurationGet,
        PathValues.TRANSFER_METRICS_GET: TransferMetricsGet,
        PathValues.TRANSFER_CREATE: TransferCreate,
        PathValues.TRANSFER_RECURRING_CREATE: TransferRecurringCreate,
        PathValues.BANK_TRANSFER_CREATE: BankTransferCreate,
        PathValues.TRANSFER_LIST: TransferList,
        PathValues.TRANSFER_RECURRING_LIST: TransferRecurringList,
        PathValues.BANK_TRANSFER_LIST: BankTransferList,
        PathValues.TRANSFER_CANCEL: TransferCancel,
        PathValues.TRANSFER_RECURRING_CANCEL: TransferRecurringCancel,
        PathValues.BANK_TRANSFER_CANCEL: BankTransferCancel,
        PathValues.TRANSFER_EVENT_LIST: TransferEventList,
        PathValues.BANK_TRANSFER_EVENT_LIST: BankTransferEventList,
        PathValues.TRANSFER_EVENT_SYNC: TransferEventSync,
        PathValues.BANK_TRANSFER_EVENT_SYNC: BankTransferEventSync,
        PathValues.TRANSFER_SWEEP_GET: TransferSweepGet,
        PathValues.BANK_TRANSFER_SWEEP_GET: BankTransferSweepGet,
        PathValues.TRANSFER_SWEEP_LIST: TransferSweepList,
        PathValues.BANK_TRANSFER_SWEEP_LIST: BankTransferSweepList,
        PathValues.BANK_TRANSFER_BALANCE_GET: BankTransferBalanceGet,
        PathValues.BANK_TRANSFER_MIGRATE_ACCOUNT: BankTransferMigrateAccount,
        PathValues.TRANSFER_MIGRATE_ACCOUNT: TransferMigrateAccount,
        PathValues.TRANSFER_INTENT_CREATE: TransferIntentCreate,
        PathValues.TRANSFER_INTENT_GET: TransferIntentGet,
        PathValues.TRANSFER_REPAYMENT_LIST: TransferRepaymentList,
        PathValues.TRANSFER_REPAYMENT_RETURN_LIST: TransferRepaymentReturnList,
        PathValues.TRANSFER_ORIGINATOR_CREATE: TransferOriginatorCreate,
        PathValues.TRANSFER_QUESTIONNAIRE_CREATE: TransferQuestionnaireCreate,
        PathValues.TRANSFER_DILIGENCE_SUBMIT: TransferDiligenceSubmit,
        PathValues.TRANSFER_DILIGENCE_DOCUMENT_UPLOAD: TransferDiligenceDocumentUpload,
        PathValues.TRANSFER_ORIGINATOR_GET: TransferOriginatorGet,
        PathValues.TRANSFER_ORIGINATOR_LIST: TransferOriginatorList,
        PathValues.TRANSFER_REFUND_CREATE: TransferRefundCreate,
        PathValues.TRANSFER_REFUND_GET: TransferRefundGet,
        PathValues.TRANSFER_REFUND_CANCEL: TransferRefundCancel,
        PathValues.SANDBOX_BANK_TRANSFER_SIMULATE: SandboxBankTransferSimulate,
        PathValues.SANDBOX_TRANSFER_SWEEP_SIMULATE: SandboxTransferSweepSimulate,
        PathValues.SANDBOX_TRANSFER_SIMULATE: SandboxTransferSimulate,
        PathValues.SANDBOX_TRANSFER_REPAYMENT_SIMULATE: SandboxTransferRepaymentSimulate,
        PathValues.SANDBOX_TRANSFER_FIRE_WEBHOOK: SandboxTransferFireWebhook,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_CREATE: SandboxTransferTestClockCreate,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_ADVANCE: SandboxTransferTestClockAdvance,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_GET: SandboxTransferTestClockGet,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_LIST: SandboxTransferTestClockList,
        PathValues.SANDBOX_PAYMENT_PROFILE_RESET_LOGIN: SandboxPaymentProfileResetLogin,
        PathValues.EMPLOYERS_SEARCH: EmployersSearch,
        PathValues.INCOME_VERIFICATION_CREATE: IncomeVerificationCreate,
        PathValues.INCOME_VERIFICATION_PAYSTUBS_GET: IncomeVerificationPaystubsGet,
        PathValues.INCOME_VERIFICATION_DOCUMENTS_DOWNLOAD: IncomeVerificationDocumentsDownload,
        PathValues.INCOME_VERIFICATION_TAXFORMS_GET: IncomeVerificationTaxformsGet,
        PathValues.INCOME_VERIFICATION_PRECHECK: IncomeVerificationPrecheck,
        PathValues.EMPLOYMENT_VERIFICATION_GET: EmploymentVerificationGet,
        PathValues.DEPOSIT_SWITCH_ALT_CREATE: DepositSwitchAltCreate,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_CREATE: CreditAuditCopyTokenCreate,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_REMOVE: CreditAuditCopyTokenRemove,
        PathValues.CREDIT_ASSET_REPORT_FREDDIE_MAC_GET: CreditAssetReportFreddieMacGet,
        PathValues.CREDIT_FREDDIE_MAC_REPORTS_GET: CreditFreddieMacReportsGet,
        PathValues.BETA_CREDIT_V1_BANK_EMPLOYMENT_GET: BetaCreditV1BankEmploymentGet,
        PathValues.CREDIT_BANK_INCOME_GET: CreditBankIncomeGet,
        PathValues.CREDIT_BANK_INCOME_PDF_GET: CreditBankIncomePdfGet,
        PathValues.CREDIT_BANK_INCOME_REFRESH: CreditBankIncomeRefresh,
        PathValues.CREDIT_BANK_INCOME_WEBHOOK_UPDATE: CreditBankIncomeWebhookUpdate,
        PathValues.CREDIT_BANK_STATEMENTS_UPLOADS_GET: CreditBankStatementsUploadsGet,
        PathValues.CREDIT_PAYROLL_INCOME_GET: CreditPayrollIncomeGet,
        PathValues.CREDIT_PAYROLL_INCOME_RISK_SIGNALS_GET: CreditPayrollIncomeRiskSignalsGet,
        PathValues.CREDIT_PAYROLL_INCOME_PRECHECK: CreditPayrollIncomePrecheck,
        PathValues.CREDIT_EMPLOYMENT_GET: CreditEmploymentGet,
        PathValues.CREDIT_PAYROLL_INCOME_REFRESH: CreditPayrollIncomeRefresh,
        PathValues.CREDIT_RELAY_CREATE: CreditRelayCreate,
        PathValues.CREDIT_RELAY_GET: CreditRelayGet,
        PathValues.CREDIT_RELAY_REFRESH: CreditRelayRefresh,
        PathValues.CREDIT_RELAY_REMOVE: CreditRelayRemove,
        PathValues.SANDBOX_BANK_TRANSFER_FIRE_WEBHOOK: SandboxBankTransferFireWebhook,
        PathValues.SANDBOX_INCOME_FIRE_WEBHOOK: SandboxIncomeFireWebhook,
        PathValues.SANDBOX_BANK_INCOME_FIRE_WEBHOOK: SandboxBankIncomeFireWebhook,
        PathValues.SANDBOX_OAUTH_SELECT_ACCOUNTS: SandboxOauthSelectAccounts,
        PathValues.SIGNAL_EVALUATE: SignalEvaluate,
        PathValues.SIGNAL_DECISION_REPORT: SignalDecisionReport,
        PathValues.SIGNAL_RETURN_REPORT: SignalReturnReport,
        PathValues.SIGNAL_PREPARE: SignalPrepare,
        PathValues.WALLET_CREATE: WalletCreate,
        PathValues.WALLET_GET: WalletGet,
        PathValues.WALLET_LIST: WalletList,
        PathValues.WALLET_TRANSACTION_EXECUTE: WalletTransactionExecute,
        PathValues.WALLET_TRANSACTION_GET: WalletTransactionGet,
        PathValues.WALLET_TRANSACTION_LIST: WalletTransactionList,
        PathValues.BETA_TRANSACTIONS_V1_ENHANCE: BetaTransactionsV1Enhance,
        PathValues.BETA_TRANSACTIONS_RULES_V1_CREATE: BetaTransactionsRulesV1Create,
        PathValues.BETA_TRANSACTIONS_RULES_V1_LIST: BetaTransactionsRulesV1List,
        PathValues.BETA_TRANSACTIONS_RULES_V1_REMOVE: BetaTransactionsRulesV1Remove,
        PathValues.PAYMENT_PROFILE_CREATE: PaymentProfileCreate,
        PathValues.PAYMENT_PROFILE_GET: PaymentProfileGet,
        PathValues.PAYMENT_PROFILE_REMOVE: PaymentProfileRemove,
        PathValues.PARTNER_CUSTOMER_CREATE: PartnerCustomerCreate,
        PathValues.PARTNER_CUSTOMER_GET: PartnerCustomerGet,
        PathValues.PARTNER_CUSTOMER_ENABLE: PartnerCustomerEnable,
        PathValues.PARTNER_CUSTOMER_REMOVE: PartnerCustomerRemove,
        PathValues.PARTNER_CUSTOMER_OAUTH_INSTITUTIONS_GET: PartnerCustomerOauthInstitutionsGet,
        PathValues.LINK_DELIVERY_CREATE: LinkDeliveryCreate,
        PathValues.LINK_DELIVERY_GET: LinkDeliveryGet,
        PathValues.FDX_NOTIFICATIONS: FdxNotifications,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ASSET_REPORT_CREATE: AssetReportCreate,
        PathValues.ASSET_REPORT_GET: AssetReportGet,
        PathValues.ASSET_REPORT_PDF_GET: AssetReportPdfGet,
        PathValues.ASSET_REPORT_REFRESH: AssetReportRefresh,
        PathValues.ASSET_REPORT_FILTER: AssetReportFilter,
        PathValues.ASSET_REPORT_REMOVE: AssetReportRemove,
        PathValues.ASSET_REPORT_AUDIT_COPY_CREATE: AssetReportAuditCopyCreate,
        PathValues.ASSET_REPORT_AUDIT_COPY_GET: AssetReportAuditCopyGet,
        PathValues.ASSET_REPORT_AUDIT_COPY_REMOVE: AssetReportAuditCopyRemove,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_UPDATE: CreditAuditCopyTokenUpdate,
        PathValues.STATEMENTS_LIST: StatementsList,
        PathValues.STATEMENTS_DOWNLOAD: StatementsDownload,
        PathValues.ITEM_ACTIVITY_LIST: ItemActivityList,
        PathValues.ITEM_APPLICATION_LIST: ItemApplicationList,
        PathValues.ITEM_APPLICATION_SCOPES_UPDATE: ItemApplicationScopesUpdate,
        PathValues.APPLICATION_GET: ApplicationGet,
        PathValues.ITEM_GET: ItemGet,
        PathValues.AUTH_GET: AuthGet,
        PathValues.TRANSACTIONS_GET: TransactionsGet,
        PathValues.TRANSACTIONS_REFRESH: TransactionsRefresh,
        PathValues.TRANSACTIONS_RECURRING_GET: TransactionsRecurringGet,
        PathValues.TRANSACTIONS_RECURRING_DEACTIVATE: TransactionsRecurringDeactivate,
        PathValues.TRANSACTIONS_SYNC: TransactionsSync,
        PathValues.TRANSACTIONS_ENRICH: TransactionsEnrich,
        PathValues.INSTITUTIONS_GET: InstitutionsGet,
        PathValues.INSTITUTIONS_SEARCH: InstitutionsSearch,
        PathValues.INSTITUTIONS_GET_BY_ID: InstitutionsGetById,
        PathValues.ITEM_REMOVE: ItemRemove,
        PathValues.ACCOUNTS_GET: AccountsGet,
        PathValues.CATEGORIES_GET: CategoriesGet,
        PathValues.SANDBOX_PROCESSOR_TOKEN_CREATE: SandboxProcessorTokenCreate,
        PathValues.SANDBOX_PUBLIC_TOKEN_CREATE: SandboxPublicTokenCreate,
        PathValues.SANDBOX_ITEM_FIRE_WEBHOOK: SandboxItemFireWebhook,
        PathValues.ACCOUNTS_BALANCE_GET: AccountsBalanceGet,
        PathValues.IDENTITY_GET: IdentityGet,
        PathValues.IDENTITY_MATCH: IdentityMatch,
        PathValues.IDENTITY_REFRESH: IdentityRefresh,
        PathValues.DASHBOARD_USER_GET: DashboardUserGet,
        PathValues.DASHBOARD_USER_LIST: DashboardUserList,
        PathValues.IDENTITY_VERIFICATION_CREATE: IdentityVerificationCreate,
        PathValues.IDENTITY_VERIFICATION_GET: IdentityVerificationGet,
        PathValues.IDENTITY_VERIFICATION_LIST: IdentityVerificationList,
        PathValues.IDENTITY_VERIFICATION_RETRY: IdentityVerificationRetry,
        PathValues.WATCHLIST_SCREENING_ENTITY_CREATE: WatchlistScreeningEntityCreate,
        PathValues.WATCHLIST_SCREENING_ENTITY_GET: WatchlistScreeningEntityGet,
        PathValues.WATCHLIST_SCREENING_ENTITY_HISTORY_LIST: WatchlistScreeningEntityHistoryList,
        PathValues.WATCHLIST_SCREENING_ENTITY_HIT_LIST: WatchlistScreeningEntityHitList,
        PathValues.WATCHLIST_SCREENING_ENTITY_LIST: WatchlistScreeningEntityList,
        PathValues.WATCHLIST_SCREENING_ENTITY_PROGRAM_GET: WatchlistScreeningEntityProgramGet,
        PathValues.WATCHLIST_SCREENING_ENTITY_PROGRAM_LIST: WatchlistScreeningEntityProgramList,
        PathValues.WATCHLIST_SCREENING_ENTITY_REVIEW_CREATE: WatchlistScreeningEntityReviewCreate,
        PathValues.WATCHLIST_SCREENING_ENTITY_REVIEW_LIST: WatchlistScreeningEntityReviewList,
        PathValues.WATCHLIST_SCREENING_ENTITY_UPDATE: WatchlistScreeningEntityUpdate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_CREATE: WatchlistScreeningIndividualCreate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_GET: WatchlistScreeningIndividualGet,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_HISTORY_LIST: WatchlistScreeningIndividualHistoryList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_HIT_LIST: WatchlistScreeningIndividualHitList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_LIST: WatchlistScreeningIndividualList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_PROGRAM_GET: WatchlistScreeningIndividualProgramGet,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_PROGRAM_LIST: WatchlistScreeningIndividualProgramList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_REVIEW_CREATE: WatchlistScreeningIndividualReviewCreate,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_REVIEW_LIST: WatchlistScreeningIndividualReviewList,
        PathValues.WATCHLIST_SCREENING_INDIVIDUAL_UPDATE: WatchlistScreeningIndividualUpdate,
        PathValues.PROCESSOR_AUTH_GET: ProcessorAuthGet,
        PathValues.PROCESSOR_TRANSACTIONS_GET: ProcessorTransactionsGet,
        PathValues.PROCESSOR_TRANSACTIONS_SYNC: ProcessorTransactionsSync,
        PathValues.PROCESSOR_TRANSACTIONS_REFRESH: ProcessorTransactionsRefresh,
        PathValues.PROCESSOR_TRANSACTIONS_RECURRING_GET: ProcessorTransactionsRecurringGet,
        PathValues.PROCESSOR_SIGNAL_EVALUATE: ProcessorSignalEvaluate,
        PathValues.PROCESSOR_SIGNAL_DECISION_REPORT: ProcessorSignalDecisionReport,
        PathValues.PROCESSOR_SIGNAL_RETURN_REPORT: ProcessorSignalReturnReport,
        PathValues.PROCESSOR_BANK_TRANSFER_CREATE: ProcessorBankTransferCreate,
        PathValues.PROCESSOR_IDENTITY_GET: ProcessorIdentityGet,
        PathValues.PROCESSOR_IDENTITY_MATCH: ProcessorIdentityMatch,
        PathValues.PROCESSOR_BALANCE_GET: ProcessorBalanceGet,
        PathValues.ITEM_WEBHOOK_UPDATE: ItemWebhookUpdate,
        PathValues.ITEM_ACCESS_TOKEN_INVALIDATE: ItemAccessTokenInvalidate,
        PathValues.WEBHOOK_VERIFICATION_KEY_GET: WebhookVerificationKeyGet,
        PathValues.LIABILITIES_GET: LiabilitiesGet,
        PathValues.PAYMENT_INITIATION_RECIPIENT_CREATE: PaymentInitiationRecipientCreate,
        PathValues.PAYMENT_INITIATION_PAYMENT_REVERSE: PaymentInitiationPaymentReverse,
        PathValues.PAYMENT_INITIATION_RECIPIENT_GET: PaymentInitiationRecipientGet,
        PathValues.PAYMENT_INITIATION_RECIPIENT_LIST: PaymentInitiationRecipientList,
        PathValues.PAYMENT_INITIATION_PAYMENT_CREATE: PaymentInitiationPaymentCreate,
        PathValues.PAYMENT_INITIATION_PAYMENT_TOKEN_CREATE: PaymentInitiationPaymentTokenCreate,
        PathValues.PAYMENT_INITIATION_CONSENT_CREATE: PaymentInitiationConsentCreate,
        PathValues.PAYMENT_INITIATION_CONSENT_GET: PaymentInitiationConsentGet,
        PathValues.PAYMENT_INITIATION_CONSENT_REVOKE: PaymentInitiationConsentRevoke,
        PathValues.PAYMENT_INITIATION_CONSENT_PAYMENT_EXECUTE: PaymentInitiationConsentPaymentExecute,
        PathValues.SANDBOX_ITEM_RESET_LOGIN: SandboxItemResetLogin,
        PathValues.SANDBOX_ITEM_SET_VERIFICATION_STATUS: SandboxItemSetVerificationStatus,
        PathValues.ITEM_PUBLIC_TOKEN_EXCHANGE: ItemPublicTokenExchange,
        PathValues.ITEM_PUBLIC_TOKEN_CREATE: ItemPublicTokenCreate,
        PathValues.USER_CREATE: UserCreate,
        PathValues.CREDIT_SESSIONS_GET: CreditSessionsGet,
        PathValues.PAYMENT_INITIATION_PAYMENT_GET: PaymentInitiationPaymentGet,
        PathValues.PAYMENT_INITIATION_PAYMENT_LIST: PaymentInitiationPaymentList,
        PathValues.INVESTMENTS_HOLDINGS_GET: InvestmentsHoldingsGet,
        PathValues.INVESTMENTS_TRANSACTIONS_GET: InvestmentsTransactionsGet,
        PathValues.INVESTMENTS_REFRESH: InvestmentsRefresh,
        PathValues.INVESTMENTS_AUTH_GET: InvestmentsAuthGet,
        PathValues.PROCESSOR_TOKEN_CREATE: ProcessorTokenCreate,
        PathValues.PROCESSOR_TOKEN_PERMISSIONS_SET: ProcessorTokenPermissionsSet,
        PathValues.PROCESSOR_TOKEN_PERMISSIONS_GET: ProcessorTokenPermissionsGet,
        PathValues.PROCESSOR_TOKEN_WEBHOOK_UPDATE: ProcessorTokenWebhookUpdate,
        PathValues.PROCESSOR_STRIPE_BANK_ACCOUNT_TOKEN_CREATE: ProcessorStripeBankAccountTokenCreate,
        PathValues.PROCESSOR_APEX_PROCESSOR_TOKEN_CREATE: ProcessorApexProcessorTokenCreate,
        PathValues.DEPOSIT_SWITCH_CREATE: DepositSwitchCreate,
        PathValues.ITEM_IMPORT: ItemImport,
        PathValues.DEPOSIT_SWITCH_TOKEN_CREATE: DepositSwitchTokenCreate,
        PathValues.LINK_TOKEN_CREATE: LinkTokenCreate,
        PathValues.LINK_TOKEN_GET: LinkTokenGet,
        PathValues.LINK_OAUTH_CORRELATION_ID_EXCHANGE: LinkOauthCorrelationIdExchange,
        PathValues.DEPOSIT_SWITCH_GET: DepositSwitchGet,
        PathValues.TRANSFER_GET: TransferGet,
        PathValues.TRANSFER_RECURRING_GET: TransferRecurringGet,
        PathValues.BANK_TRANSFER_GET: BankTransferGet,
        PathValues.TRANSFER_AUTHORIZATION_CREATE: TransferAuthorizationCreate,
        PathValues.TRANSFER_BALANCE_GET: TransferBalanceGet,
        PathValues.TRANSFER_CAPABILITIES_GET: TransferCapabilitiesGet,
        PathValues.TRANSFER_CONFIGURATION_GET: TransferConfigurationGet,
        PathValues.TRANSFER_METRICS_GET: TransferMetricsGet,
        PathValues.TRANSFER_CREATE: TransferCreate,
        PathValues.TRANSFER_RECURRING_CREATE: TransferRecurringCreate,
        PathValues.BANK_TRANSFER_CREATE: BankTransferCreate,
        PathValues.TRANSFER_LIST: TransferList,
        PathValues.TRANSFER_RECURRING_LIST: TransferRecurringList,
        PathValues.BANK_TRANSFER_LIST: BankTransferList,
        PathValues.TRANSFER_CANCEL: TransferCancel,
        PathValues.TRANSFER_RECURRING_CANCEL: TransferRecurringCancel,
        PathValues.BANK_TRANSFER_CANCEL: BankTransferCancel,
        PathValues.TRANSFER_EVENT_LIST: TransferEventList,
        PathValues.BANK_TRANSFER_EVENT_LIST: BankTransferEventList,
        PathValues.TRANSFER_EVENT_SYNC: TransferEventSync,
        PathValues.BANK_TRANSFER_EVENT_SYNC: BankTransferEventSync,
        PathValues.TRANSFER_SWEEP_GET: TransferSweepGet,
        PathValues.BANK_TRANSFER_SWEEP_GET: BankTransferSweepGet,
        PathValues.TRANSFER_SWEEP_LIST: TransferSweepList,
        PathValues.BANK_TRANSFER_SWEEP_LIST: BankTransferSweepList,
        PathValues.BANK_TRANSFER_BALANCE_GET: BankTransferBalanceGet,
        PathValues.BANK_TRANSFER_MIGRATE_ACCOUNT: BankTransferMigrateAccount,
        PathValues.TRANSFER_MIGRATE_ACCOUNT: TransferMigrateAccount,
        PathValues.TRANSFER_INTENT_CREATE: TransferIntentCreate,
        PathValues.TRANSFER_INTENT_GET: TransferIntentGet,
        PathValues.TRANSFER_REPAYMENT_LIST: TransferRepaymentList,
        PathValues.TRANSFER_REPAYMENT_RETURN_LIST: TransferRepaymentReturnList,
        PathValues.TRANSFER_ORIGINATOR_CREATE: TransferOriginatorCreate,
        PathValues.TRANSFER_QUESTIONNAIRE_CREATE: TransferQuestionnaireCreate,
        PathValues.TRANSFER_DILIGENCE_SUBMIT: TransferDiligenceSubmit,
        PathValues.TRANSFER_DILIGENCE_DOCUMENT_UPLOAD: TransferDiligenceDocumentUpload,
        PathValues.TRANSFER_ORIGINATOR_GET: TransferOriginatorGet,
        PathValues.TRANSFER_ORIGINATOR_LIST: TransferOriginatorList,
        PathValues.TRANSFER_REFUND_CREATE: TransferRefundCreate,
        PathValues.TRANSFER_REFUND_GET: TransferRefundGet,
        PathValues.TRANSFER_REFUND_CANCEL: TransferRefundCancel,
        PathValues.SANDBOX_BANK_TRANSFER_SIMULATE: SandboxBankTransferSimulate,
        PathValues.SANDBOX_TRANSFER_SWEEP_SIMULATE: SandboxTransferSweepSimulate,
        PathValues.SANDBOX_TRANSFER_SIMULATE: SandboxTransferSimulate,
        PathValues.SANDBOX_TRANSFER_REPAYMENT_SIMULATE: SandboxTransferRepaymentSimulate,
        PathValues.SANDBOX_TRANSFER_FIRE_WEBHOOK: SandboxTransferFireWebhook,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_CREATE: SandboxTransferTestClockCreate,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_ADVANCE: SandboxTransferTestClockAdvance,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_GET: SandboxTransferTestClockGet,
        PathValues.SANDBOX_TRANSFER_TEST_CLOCK_LIST: SandboxTransferTestClockList,
        PathValues.SANDBOX_PAYMENT_PROFILE_RESET_LOGIN: SandboxPaymentProfileResetLogin,
        PathValues.EMPLOYERS_SEARCH: EmployersSearch,
        PathValues.INCOME_VERIFICATION_CREATE: IncomeVerificationCreate,
        PathValues.INCOME_VERIFICATION_PAYSTUBS_GET: IncomeVerificationPaystubsGet,
        PathValues.INCOME_VERIFICATION_DOCUMENTS_DOWNLOAD: IncomeVerificationDocumentsDownload,
        PathValues.INCOME_VERIFICATION_TAXFORMS_GET: IncomeVerificationTaxformsGet,
        PathValues.INCOME_VERIFICATION_PRECHECK: IncomeVerificationPrecheck,
        PathValues.EMPLOYMENT_VERIFICATION_GET: EmploymentVerificationGet,
        PathValues.DEPOSIT_SWITCH_ALT_CREATE: DepositSwitchAltCreate,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_CREATE: CreditAuditCopyTokenCreate,
        PathValues.CREDIT_AUDIT_COPY_TOKEN_REMOVE: CreditAuditCopyTokenRemove,
        PathValues.CREDIT_ASSET_REPORT_FREDDIE_MAC_GET: CreditAssetReportFreddieMacGet,
        PathValues.CREDIT_FREDDIE_MAC_REPORTS_GET: CreditFreddieMacReportsGet,
        PathValues.BETA_CREDIT_V1_BANK_EMPLOYMENT_GET: BetaCreditV1BankEmploymentGet,
        PathValues.CREDIT_BANK_INCOME_GET: CreditBankIncomeGet,
        PathValues.CREDIT_BANK_INCOME_PDF_GET: CreditBankIncomePdfGet,
        PathValues.CREDIT_BANK_INCOME_REFRESH: CreditBankIncomeRefresh,
        PathValues.CREDIT_BANK_INCOME_WEBHOOK_UPDATE: CreditBankIncomeWebhookUpdate,
        PathValues.CREDIT_BANK_STATEMENTS_UPLOADS_GET: CreditBankStatementsUploadsGet,
        PathValues.CREDIT_PAYROLL_INCOME_GET: CreditPayrollIncomeGet,
        PathValues.CREDIT_PAYROLL_INCOME_RISK_SIGNALS_GET: CreditPayrollIncomeRiskSignalsGet,
        PathValues.CREDIT_PAYROLL_INCOME_PRECHECK: CreditPayrollIncomePrecheck,
        PathValues.CREDIT_EMPLOYMENT_GET: CreditEmploymentGet,
        PathValues.CREDIT_PAYROLL_INCOME_REFRESH: CreditPayrollIncomeRefresh,
        PathValues.CREDIT_RELAY_CREATE: CreditRelayCreate,
        PathValues.CREDIT_RELAY_GET: CreditRelayGet,
        PathValues.CREDIT_RELAY_REFRESH: CreditRelayRefresh,
        PathValues.CREDIT_RELAY_REMOVE: CreditRelayRemove,
        PathValues.SANDBOX_BANK_TRANSFER_FIRE_WEBHOOK: SandboxBankTransferFireWebhook,
        PathValues.SANDBOX_INCOME_FIRE_WEBHOOK: SandboxIncomeFireWebhook,
        PathValues.SANDBOX_BANK_INCOME_FIRE_WEBHOOK: SandboxBankIncomeFireWebhook,
        PathValues.SANDBOX_OAUTH_SELECT_ACCOUNTS: SandboxOauthSelectAccounts,
        PathValues.SIGNAL_EVALUATE: SignalEvaluate,
        PathValues.SIGNAL_DECISION_REPORT: SignalDecisionReport,
        PathValues.SIGNAL_RETURN_REPORT: SignalReturnReport,
        PathValues.SIGNAL_PREPARE: SignalPrepare,
        PathValues.WALLET_CREATE: WalletCreate,
        PathValues.WALLET_GET: WalletGet,
        PathValues.WALLET_LIST: WalletList,
        PathValues.WALLET_TRANSACTION_EXECUTE: WalletTransactionExecute,
        PathValues.WALLET_TRANSACTION_GET: WalletTransactionGet,
        PathValues.WALLET_TRANSACTION_LIST: WalletTransactionList,
        PathValues.BETA_TRANSACTIONS_V1_ENHANCE: BetaTransactionsV1Enhance,
        PathValues.BETA_TRANSACTIONS_RULES_V1_CREATE: BetaTransactionsRulesV1Create,
        PathValues.BETA_TRANSACTIONS_RULES_V1_LIST: BetaTransactionsRulesV1List,
        PathValues.BETA_TRANSACTIONS_RULES_V1_REMOVE: BetaTransactionsRulesV1Remove,
        PathValues.PAYMENT_PROFILE_CREATE: PaymentProfileCreate,
        PathValues.PAYMENT_PROFILE_GET: PaymentProfileGet,
        PathValues.PAYMENT_PROFILE_REMOVE: PaymentProfileRemove,
        PathValues.PARTNER_CUSTOMER_CREATE: PartnerCustomerCreate,
        PathValues.PARTNER_CUSTOMER_GET: PartnerCustomerGet,
        PathValues.PARTNER_CUSTOMER_ENABLE: PartnerCustomerEnable,
        PathValues.PARTNER_CUSTOMER_REMOVE: PartnerCustomerRemove,
        PathValues.PARTNER_CUSTOMER_OAUTH_INSTITUTIONS_GET: PartnerCustomerOauthInstitutionsGet,
        PathValues.LINK_DELIVERY_CREATE: LinkDeliveryCreate,
        PathValues.LINK_DELIVERY_GET: LinkDeliveryGet,
        PathValues.FDX_NOTIFICATIONS: FdxNotifications,
    }
)
