# plaid.PlaidApi

All URIs are relative to *https://production.plaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_balance_get**](PlaidApi.md#accounts_balance_get) | **POST** /accounts/balance/get | Retrieve real-time balance data
[**accounts_get**](PlaidApi.md#accounts_get) | **POST** /accounts/get | Retrieve accounts
[**application_get**](PlaidApi.md#application_get) | **POST** /application/get | Retrieve information about a Plaid application
[**asset_report_audit_copy_create**](PlaidApi.md#asset_report_audit_copy_create) | **POST** /asset_report/audit_copy/create | Create Asset Report Audit Copy
[**asset_report_audit_copy_get**](PlaidApi.md#asset_report_audit_copy_get) | **POST** /asset_report/audit_copy/get | Retrieve an Asset Report Audit Copy
[**asset_report_audit_copy_remove**](PlaidApi.md#asset_report_audit_copy_remove) | **POST** /asset_report/audit_copy/remove | Remove Asset Report Audit Copy
[**asset_report_create**](PlaidApi.md#asset_report_create) | **POST** /asset_report/create | Create an Asset Report
[**asset_report_filter**](PlaidApi.md#asset_report_filter) | **POST** /asset_report/filter | Filter Asset Report
[**asset_report_get**](PlaidApi.md#asset_report_get) | **POST** /asset_report/get | Retrieve an Asset Report
[**asset_report_pdf_get**](PlaidApi.md#asset_report_pdf_get) | **POST** /asset_report/pdf/get | Retrieve a PDF Asset Report
[**asset_report_refresh**](PlaidApi.md#asset_report_refresh) | **POST** /asset_report/refresh | Refresh an Asset Report
[**asset_report_remove**](PlaidApi.md#asset_report_remove) | **POST** /asset_report/remove | Delete an Asset Report
[**auth_get**](PlaidApi.md#auth_get) | **POST** /auth/get | Retrieve auth data
[**bank_transfer_balance_get**](PlaidApi.md#bank_transfer_balance_get) | **POST** /bank_transfer/balance/get | Get balance of your Bank Transfer account
[**bank_transfer_cancel**](PlaidApi.md#bank_transfer_cancel) | **POST** /bank_transfer/cancel | Cancel a bank transfer
[**bank_transfer_create**](PlaidApi.md#bank_transfer_create) | **POST** /bank_transfer/create | Create a bank transfer
[**bank_transfer_event_list**](PlaidApi.md#bank_transfer_event_list) | **POST** /bank_transfer/event/list | List bank transfer events
[**bank_transfer_event_sync**](PlaidApi.md#bank_transfer_event_sync) | **POST** /bank_transfer/event/sync | Sync bank transfer events
[**bank_transfer_get**](PlaidApi.md#bank_transfer_get) | **POST** /bank_transfer/get | Retrieve a bank transfer
[**bank_transfer_list**](PlaidApi.md#bank_transfer_list) | **POST** /bank_transfer/list | List bank transfers
[**bank_transfer_migrate_account**](PlaidApi.md#bank_transfer_migrate_account) | **POST** /bank_transfer/migrate_account | Migrate account into Bank Transfers
[**bank_transfer_sweep_get**](PlaidApi.md#bank_transfer_sweep_get) | **POST** /bank_transfer/sweep/get | Retrieve a sweep
[**bank_transfer_sweep_list**](PlaidApi.md#bank_transfer_sweep_list) | **POST** /bank_transfer/sweep/list | List sweeps
[**categories_get**](PlaidApi.md#categories_get) | **POST** /categories/get | Get categories
[**create_payment_token**](PlaidApi.md#create_payment_token) | **POST** /payment_initiation/payment/token/create | Create payment token
[**credit_asset_report_freddie_mac_get**](PlaidApi.md#credit_asset_report_freddie_mac_get) | **POST** /credit/asset_report/freddie_mac/get | Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.
[**credit_audit_copy_token_create**](PlaidApi.md#credit_audit_copy_token_create) | **POST** /credit/audit_copy_token/create | Create Asset or Income Report Audit Copy Token
[**credit_audit_copy_token_update**](PlaidApi.md#credit_audit_copy_token_update) | **POST** /credit/audit_copy_token/update | Update an Audit Copy Token
[**credit_bank_employment_get**](PlaidApi.md#credit_bank_employment_get) | **POST** /beta/credit/v1/bank_employment/get | Retrieve information from the bank accounts used for employment verification
[**credit_bank_income_get**](PlaidApi.md#credit_bank_income_get) | **POST** /credit/bank_income/get | Retrieve information from the bank accounts used for income verification
[**credit_bank_income_pdf_get**](PlaidApi.md#credit_bank_income_pdf_get) | **POST** /credit/bank_income/pdf/get | Retrieve information from the bank accounts used for income verification in PDF format
[**credit_bank_income_refresh**](PlaidApi.md#credit_bank_income_refresh) | **POST** /credit/bank_income/refresh | Refresh a user&#39;s bank income information
[**credit_bank_income_webhook_update**](PlaidApi.md#credit_bank_income_webhook_update) | **POST** /credit/bank_income/webhook/update | Subscribe and unsubscribe to proactive notifications for a user&#39;s income profile
[**credit_bank_statements_uploads_get**](PlaidApi.md#credit_bank_statements_uploads_get) | **POST** /credit/bank_statements/uploads/get | Retrieve data for a user&#39;s uploaded bank statements
[**credit_employment_get**](PlaidApi.md#credit_employment_get) | **POST** /credit/employment/get | Retrieve a summary of an individual&#39;s employment information
[**credit_freddie_mac_reports_get**](PlaidApi.md#credit_freddie_mac_reports_get) | **POST** /credit/freddie_mac/reports/get | Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.
[**credit_payroll_income_get**](PlaidApi.md#credit_payroll_income_get) | **POST** /credit/payroll_income/get | Retrieve a user&#39;s payroll information
[**credit_payroll_income_precheck**](PlaidApi.md#credit_payroll_income_precheck) | **POST** /credit/payroll_income/precheck | Check income verification eligibility and optimize conversion
[**credit_payroll_income_refresh**](PlaidApi.md#credit_payroll_income_refresh) | **POST** /credit/payroll_income/refresh | Refresh a digital payroll income verification
[**credit_payroll_income_risk_signals_get**](PlaidApi.md#credit_payroll_income_risk_signals_get) | **POST** /credit/payroll_income/risk_signals/get | Retrieve fraud insights for a user&#39;s manually uploaded document(s).
[**credit_relay_create**](PlaidApi.md#credit_relay_create) | **POST** /credit/relay/create | Create a relay token to share an Asset Report with a partner client (beta)
[**credit_relay_get**](PlaidApi.md#credit_relay_get) | **POST** /credit/relay/get | Retrieve the reports associated with a relay token that was shared with you (beta)
[**credit_relay_refresh**](PlaidApi.md#credit_relay_refresh) | **POST** /credit/relay/refresh | Refresh a report of a relay token (beta)
[**credit_relay_remove**](PlaidApi.md#credit_relay_remove) | **POST** /credit/relay/remove | Remove relay token (beta)
[**credit_report_audit_copy_remove**](PlaidApi.md#credit_report_audit_copy_remove) | **POST** /credit/audit_copy_token/remove | Remove an Audit Copy token
[**credit_sessions_get**](PlaidApi.md#credit_sessions_get) | **POST** /credit/sessions/get | Retrieve Link sessions for your user
[**dashboard_user_get**](PlaidApi.md#dashboard_user_get) | **POST** /dashboard_user/get | Retrieve a dashboard user
[**dashboard_user_list**](PlaidApi.md#dashboard_user_list) | **POST** /dashboard_user/list | List dashboard users
[**deposit_switch_alt_create**](PlaidApi.md#deposit_switch_alt_create) | **POST** /deposit_switch/alt/create | Create a deposit switch without using Plaid Exchange
[**deposit_switch_create**](PlaidApi.md#deposit_switch_create) | **POST** /deposit_switch/create | Create a deposit switch
[**deposit_switch_get**](PlaidApi.md#deposit_switch_get) | **POST** /deposit_switch/get | Retrieve a deposit switch
[**deposit_switch_token_create**](PlaidApi.md#deposit_switch_token_create) | **POST** /deposit_switch/token/create | Create a deposit switch token
[**employers_search**](PlaidApi.md#employers_search) | **POST** /employers/search | Search employer database
[**employment_verification_get**](PlaidApi.md#employment_verification_get) | **POST** /employment/verification/get | (Deprecated) Retrieve a summary of an individual&#39;s employment information
[**fdx_notifications**](PlaidApi.md#fdx_notifications) | **POST** /fdx/notifications | Webhook receiver for fdx notifications
[**identity_get**](PlaidApi.md#identity_get) | **POST** /identity/get | Retrieve identity data
[**identity_match**](PlaidApi.md#identity_match) | **POST** /identity/match | Retrieve identity match score
[**identity_refresh**](PlaidApi.md#identity_refresh) | **POST** /identity/refresh | Refresh identity data
[**identity_verification_create**](PlaidApi.md#identity_verification_create) | **POST** /identity_verification/create | Create a new identity verification
[**identity_verification_get**](PlaidApi.md#identity_verification_get) | **POST** /identity_verification/get | Retrieve Identity Verification
[**identity_verification_list**](PlaidApi.md#identity_verification_list) | **POST** /identity_verification/list | List Identity Verifications
[**identity_verification_retry**](PlaidApi.md#identity_verification_retry) | **POST** /identity_verification/retry | Retry an Identity Verification
[**income_verification_create**](PlaidApi.md#income_verification_create) | **POST** /income/verification/create | (Deprecated) Create an income verification instance
[**income_verification_documents_download**](PlaidApi.md#income_verification_documents_download) | **POST** /income/verification/documents/download | (Deprecated) Download the original documents used for income verification
[**income_verification_paystubs_get**](PlaidApi.md#income_verification_paystubs_get) | **POST** /income/verification/paystubs/get | (Deprecated) Retrieve information from the paystubs used for income verification
[**income_verification_precheck**](PlaidApi.md#income_verification_precheck) | **POST** /income/verification/precheck | (Deprecated) Check digital income verification eligibility and optimize conversion
[**income_verification_taxforms_get**](PlaidApi.md#income_verification_taxforms_get) | **POST** /income/verification/taxforms/get | (Deprecated) Retrieve information from the tax documents used for income verification
[**institutions_get**](PlaidApi.md#institutions_get) | **POST** /institutions/get | Get details of all supported institutions
[**institutions_get_by_id**](PlaidApi.md#institutions_get_by_id) | **POST** /institutions/get_by_id | Get details of an institution
[**institutions_search**](PlaidApi.md#institutions_search) | **POST** /institutions/search | Search institutions
[**investments_auth_get**](PlaidApi.md#investments_auth_get) | **POST** /investments/auth/get | Get data needed to authorize an investments transfer
[**investments_holdings_get**](PlaidApi.md#investments_holdings_get) | **POST** /investments/holdings/get | Get Investment holdings
[**investments_refresh**](PlaidApi.md#investments_refresh) | **POST** /investments/refresh | Refresh investment data
[**investments_transactions_get**](PlaidApi.md#investments_transactions_get) | **POST** /investments/transactions/get | Get investment transactions
[**item_access_token_invalidate**](PlaidApi.md#item_access_token_invalidate) | **POST** /item/access_token/invalidate | Invalidate access_token
[**item_activity_list**](PlaidApi.md#item_activity_list) | **POST** /item/activity/list | List a historical log of user consent events
[**item_application_list**](PlaidApi.md#item_application_list) | **POST** /item/application/list | List a user’s connected applications
[**item_application_scopes_update**](PlaidApi.md#item_application_scopes_update) | **POST** /item/application/scopes/update | Update the scopes of access for a particular application
[**item_create_public_token**](PlaidApi.md#item_create_public_token) | **POST** /item/public_token/create | Create public token
[**item_get**](PlaidApi.md#item_get) | **POST** /item/get | Retrieve an Item
[**item_import**](PlaidApi.md#item_import) | **POST** /item/import | Import Item
[**item_public_token_exchange**](PlaidApi.md#item_public_token_exchange) | **POST** /item/public_token/exchange | Exchange public token for an access token
[**item_remove**](PlaidApi.md#item_remove) | **POST** /item/remove | Remove an Item
[**item_webhook_update**](PlaidApi.md#item_webhook_update) | **POST** /item/webhook/update | Update Webhook URL
[**liabilities_get**](PlaidApi.md#liabilities_get) | **POST** /liabilities/get | Retrieve Liabilities data
[**link_delivery_create**](PlaidApi.md#link_delivery_create) | **POST** /link_delivery/create | Create Hosted Link session
[**link_delivery_get**](PlaidApi.md#link_delivery_get) | **POST** /link_delivery/get | Get Hosted Link session
[**link_oauth_correlation_id_exchange**](PlaidApi.md#link_oauth_correlation_id_exchange) | **POST** /link/oauth/correlation_id/exchange | Exchange the Link Correlation Id for a Link Token
[**link_token_create**](PlaidApi.md#link_token_create) | **POST** /link/token/create | Create Link Token
[**link_token_get**](PlaidApi.md#link_token_get) | **POST** /link/token/get | Get Link Token
[**partner_customer_create**](PlaidApi.md#partner_customer_create) | **POST** /partner/customer/create | Creates a new end customer for a Plaid reseller.
[**partner_customer_enable**](PlaidApi.md#partner_customer_enable) | **POST** /partner/customer/enable | Enables a Plaid reseller&#39;s end customer in the Production environment.
[**partner_customer_get**](PlaidApi.md#partner_customer_get) | **POST** /partner/customer/get | Returns a Plaid reseller&#39;s end customer.
[**partner_customer_oauth_institutions_get**](PlaidApi.md#partner_customer_oauth_institutions_get) | **POST** /partner/customer/oauth_institutions/get | Returns OAuth-institution registration information for a given end customer.
[**partner_customer_remove**](PlaidApi.md#partner_customer_remove) | **POST** /partner/customer/remove | Removes a Plaid reseller&#39;s end customer.
[**payment_initiation_consent_create**](PlaidApi.md#payment_initiation_consent_create) | **POST** /payment_initiation/consent/create | Create payment consent
[**payment_initiation_consent_get**](PlaidApi.md#payment_initiation_consent_get) | **POST** /payment_initiation/consent/get | Get payment consent
[**payment_initiation_consent_payment_execute**](PlaidApi.md#payment_initiation_consent_payment_execute) | **POST** /payment_initiation/consent/payment/execute | Execute a single payment using consent
[**payment_initiation_consent_revoke**](PlaidApi.md#payment_initiation_consent_revoke) | **POST** /payment_initiation/consent/revoke | Revoke payment consent
[**payment_initiation_payment_create**](PlaidApi.md#payment_initiation_payment_create) | **POST** /payment_initiation/payment/create | Create a payment
[**payment_initiation_payment_get**](PlaidApi.md#payment_initiation_payment_get) | **POST** /payment_initiation/payment/get | Get payment details
[**payment_initiation_payment_list**](PlaidApi.md#payment_initiation_payment_list) | **POST** /payment_initiation/payment/list | List payments
[**payment_initiation_payment_reverse**](PlaidApi.md#payment_initiation_payment_reverse) | **POST** /payment_initiation/payment/reverse | Reverse an existing payment
[**payment_initiation_recipient_create**](PlaidApi.md#payment_initiation_recipient_create) | **POST** /payment_initiation/recipient/create | Create payment recipient
[**payment_initiation_recipient_get**](PlaidApi.md#payment_initiation_recipient_get) | **POST** /payment_initiation/recipient/get | Get payment recipient
[**payment_initiation_recipient_list**](PlaidApi.md#payment_initiation_recipient_list) | **POST** /payment_initiation/recipient/list | List payment recipients
[**payment_profile_create**](PlaidApi.md#payment_profile_create) | **POST** /payment_profile/create | Create payment profile
[**payment_profile_get**](PlaidApi.md#payment_profile_get) | **POST** /payment_profile/get | Get payment profile
[**payment_profile_remove**](PlaidApi.md#payment_profile_remove) | **POST** /payment_profile/remove | Remove payment profile
[**processor_apex_processor_token_create**](PlaidApi.md#processor_apex_processor_token_create) | **POST** /processor/apex/processor_token/create | Create Apex bank account token
[**processor_auth_get**](PlaidApi.md#processor_auth_get) | **POST** /processor/auth/get | Retrieve Auth data
[**processor_balance_get**](PlaidApi.md#processor_balance_get) | **POST** /processor/balance/get | Retrieve Balance data
[**processor_bank_transfer_create**](PlaidApi.md#processor_bank_transfer_create) | **POST** /processor/bank_transfer/create | Create a bank transfer as a processor
[**processor_identity_get**](PlaidApi.md#processor_identity_get) | **POST** /processor/identity/get | Retrieve Identity data
[**processor_identity_match**](PlaidApi.md#processor_identity_match) | **POST** /processor/identity/match | Retrieve identity match score
[**processor_signal_decision_report**](PlaidApi.md#processor_signal_decision_report) | **POST** /processor/signal/decision/report | Report whether you initiated an ACH transaction
[**processor_signal_evaluate**](PlaidApi.md#processor_signal_evaluate) | **POST** /processor/signal/evaluate | Evaluate a planned ACH transaction
[**processor_signal_return_report**](PlaidApi.md#processor_signal_return_report) | **POST** /processor/signal/return/report | Report a return for an ACH transaction
[**processor_stripe_bank_account_token_create**](PlaidApi.md#processor_stripe_bank_account_token_create) | **POST** /processor/stripe/bank_account_token/create | Create Stripe bank account token
[**processor_token_create**](PlaidApi.md#processor_token_create) | **POST** /processor/token/create | Create processor token
[**processor_token_permissions_get**](PlaidApi.md#processor_token_permissions_get) | **POST** /processor/token/permissions/get | Get a processor token&#39;s product permissions
[**processor_token_permissions_set**](PlaidApi.md#processor_token_permissions_set) | **POST** /processor/token/permissions/set | Control a processor&#39;s access to products
[**processor_token_webhook_update**](PlaidApi.md#processor_token_webhook_update) | **POST** /processor/token/webhook/update | Update a processor token&#39;s webhook URL
[**processor_transactions_get**](PlaidApi.md#processor_transactions_get) | **POST** /processor/transactions/get | Get transaction data
[**processor_transactions_recurring_get**](PlaidApi.md#processor_transactions_recurring_get) | **POST** /processor/transactions/recurring/get | Fetch recurring transaction streams
[**processor_transactions_refresh**](PlaidApi.md#processor_transactions_refresh) | **POST** /processor/transactions/refresh | Refresh transaction data
[**processor_transactions_sync**](PlaidApi.md#processor_transactions_sync) | **POST** /processor/transactions/sync | Get incremental transaction updates on an Item
[**sandbox_bank_income_fire_webhook**](PlaidApi.md#sandbox_bank_income_fire_webhook) | **POST** /sandbox/bank_income/fire_webhook | Manually fire a bank income webhook in sandbox
[**sandbox_bank_transfer_fire_webhook**](PlaidApi.md#sandbox_bank_transfer_fire_webhook) | **POST** /sandbox/bank_transfer/fire_webhook | Manually fire a Bank Transfer webhook
[**sandbox_bank_transfer_simulate**](PlaidApi.md#sandbox_bank_transfer_simulate) | **POST** /sandbox/bank_transfer/simulate | Simulate a bank transfer event in Sandbox
[**sandbox_income_fire_webhook**](PlaidApi.md#sandbox_income_fire_webhook) | **POST** /sandbox/income/fire_webhook | Manually fire an Income webhook
[**sandbox_item_fire_webhook**](PlaidApi.md#sandbox_item_fire_webhook) | **POST** /sandbox/item/fire_webhook | Fire a test webhook
[**sandbox_item_reset_login**](PlaidApi.md#sandbox_item_reset_login) | **POST** /sandbox/item/reset_login | Force a Sandbox Item into an error state
[**sandbox_item_set_verification_status**](PlaidApi.md#sandbox_item_set_verification_status) | **POST** /sandbox/item/set_verification_status | Set verification status for Sandbox account
[**sandbox_oauth_select_accounts**](PlaidApi.md#sandbox_oauth_select_accounts) | **POST** /sandbox/oauth/select_accounts | Save the selected accounts when connecting to the Platypus Oauth institution
[**sandbox_payment_profile_reset_login**](PlaidApi.md#sandbox_payment_profile_reset_login) | **POST** /sandbox/payment_profile/reset_login | Reset the login of a Payment Profile
[**sandbox_processor_token_create**](PlaidApi.md#sandbox_processor_token_create) | **POST** /sandbox/processor_token/create | Create a test Item and processor token
[**sandbox_public_token_create**](PlaidApi.md#sandbox_public_token_create) | **POST** /sandbox/public_token/create | Create a test Item
[**sandbox_transfer_fire_webhook**](PlaidApi.md#sandbox_transfer_fire_webhook) | **POST** /sandbox/transfer/fire_webhook | Manually fire a Transfer webhook
[**sandbox_transfer_repayment_simulate**](PlaidApi.md#sandbox_transfer_repayment_simulate) | **POST** /sandbox/transfer/repayment/simulate | Trigger the creation of a repayment
[**sandbox_transfer_simulate**](PlaidApi.md#sandbox_transfer_simulate) | **POST** /sandbox/transfer/simulate | Simulate a transfer event in Sandbox
[**sandbox_transfer_sweep_simulate**](PlaidApi.md#sandbox_transfer_sweep_simulate) | **POST** /sandbox/transfer/sweep/simulate | Simulate creating a sweep
[**sandbox_transfer_test_clock_advance**](PlaidApi.md#sandbox_transfer_test_clock_advance) | **POST** /sandbox/transfer/test_clock/advance | Advance a test clock
[**sandbox_transfer_test_clock_create**](PlaidApi.md#sandbox_transfer_test_clock_create) | **POST** /sandbox/transfer/test_clock/create | Create a test clock
[**sandbox_transfer_test_clock_get**](PlaidApi.md#sandbox_transfer_test_clock_get) | **POST** /sandbox/transfer/test_clock/get | Get a test clock
[**sandbox_transfer_test_clock_list**](PlaidApi.md#sandbox_transfer_test_clock_list) | **POST** /sandbox/transfer/test_clock/list | List test clocks
[**signal_decision_report**](PlaidApi.md#signal_decision_report) | **POST** /signal/decision/report | Report whether you initiated an ACH transaction
[**signal_evaluate**](PlaidApi.md#signal_evaluate) | **POST** /signal/evaluate | Evaluate a planned ACH transaction
[**signal_prepare**](PlaidApi.md#signal_prepare) | **POST** /signal/prepare | Opt-in an Item to Signal
[**signal_return_report**](PlaidApi.md#signal_return_report) | **POST** /signal/return/report | Report a return for an ACH transaction
[**statements_download**](PlaidApi.md#statements_download) | **POST** /statements/download | Retrieve a single statement.
[**statements_list**](PlaidApi.md#statements_list) | **POST** /statements/list | Retrieve a list of all statements associated with the provided item.
[**transactions_enhance**](PlaidApi.md#transactions_enhance) | **POST** /beta/transactions/v1/enhance | enhance locally-held transaction data
[**transactions_enrich**](PlaidApi.md#transactions_enrich) | **POST** /transactions/enrich | Enrich locally-held transaction data
[**transactions_get**](PlaidApi.md#transactions_get) | **POST** /transactions/get | Get transaction data
[**transactions_recurring_get**](PlaidApi.md#transactions_recurring_get) | **POST** /transactions/recurring/get | Fetch recurring transaction streams
[**transactions_refresh**](PlaidApi.md#transactions_refresh) | **POST** /transactions/refresh | Refresh transaction data
[**transactions_rules_create**](PlaidApi.md#transactions_rules_create) | **POST** /beta/transactions/rules/v1/create | Create transaction category rule
[**transactions_rules_list**](PlaidApi.md#transactions_rules_list) | **POST** /beta/transactions/rules/v1/list | Return a list of rules created for the Item associated with the access token.
[**transactions_rules_remove**](PlaidApi.md#transactions_rules_remove) | **POST** /beta/transactions/rules/v1/remove | Remove transaction rule
[**transactions_sync**](PlaidApi.md#transactions_sync) | **POST** /transactions/sync | Get incremental transaction updates on an Item
[**transfer_authorization_create**](PlaidApi.md#transfer_authorization_create) | **POST** /transfer/authorization/create | Create a transfer authorization
[**transfer_balance_get**](PlaidApi.md#transfer_balance_get) | **POST** /transfer/balance/get | Retrieve a balance held with Plaid
[**transfer_cancel**](PlaidApi.md#transfer_cancel) | **POST** /transfer/cancel | Cancel a transfer
[**transfer_capabilities_get**](PlaidApi.md#transfer_capabilities_get) | **POST** /transfer/capabilities/get | Get RTP eligibility information of a transfer
[**transfer_configuration_get**](PlaidApi.md#transfer_configuration_get) | **POST** /transfer/configuration/get | Get transfer product configuration
[**transfer_create**](PlaidApi.md#transfer_create) | **POST** /transfer/create | Create a transfer
[**transfer_diligence_document_upload**](PlaidApi.md#transfer_diligence_document_upload) | **POST** /transfer/diligence/document/upload | This endpoint allows third-party sender customers to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.
[**transfer_diligence_submit**](PlaidApi.md#transfer_diligence_submit) | **POST** /transfer/diligence/submit | Submit transfer diligence on behalf of the end customer (i.e. the originator).
[**transfer_event_list**](PlaidApi.md#transfer_event_list) | **POST** /transfer/event/list | List transfer events
[**transfer_event_sync**](PlaidApi.md#transfer_event_sync) | **POST** /transfer/event/sync | Sync transfer events
[**transfer_get**](PlaidApi.md#transfer_get) | **POST** /transfer/get | Retrieve a transfer
[**transfer_intent_create**](PlaidApi.md#transfer_intent_create) | **POST** /transfer/intent/create | Create a transfer intent object to invoke the Transfer UI
[**transfer_intent_get**](PlaidApi.md#transfer_intent_get) | **POST** /transfer/intent/get | Retrieve more information about a transfer intent
[**transfer_list**](PlaidApi.md#transfer_list) | **POST** /transfer/list | List transfers
[**transfer_metrics_get**](PlaidApi.md#transfer_metrics_get) | **POST** /transfer/metrics/get | Get transfer product usage metrics
[**transfer_migrate_account**](PlaidApi.md#transfer_migrate_account) | **POST** /transfer/migrate_account | Migrate account into Transfers
[**transfer_originator_create**](PlaidApi.md#transfer_originator_create) | **POST** /transfer/originator/create | Create a new originator
[**transfer_originator_get**](PlaidApi.md#transfer_originator_get) | **POST** /transfer/originator/get | Get status of an originator&#39;s onboarding
[**transfer_originator_list**](PlaidApi.md#transfer_originator_list) | **POST** /transfer/originator/list | Get status of all originators&#39; onboarding
[**transfer_questionnaire_create**](PlaidApi.md#transfer_questionnaire_create) | **POST** /transfer/questionnaire/create | Generate a Plaid-hosted onboarding UI URL.
[**transfer_recurring_cancel**](PlaidApi.md#transfer_recurring_cancel) | **POST** /transfer/recurring/cancel | Cancel a recurring transfer.
[**transfer_recurring_create**](PlaidApi.md#transfer_recurring_create) | **POST** /transfer/recurring/create | Create a recurring transfer
[**transfer_recurring_get**](PlaidApi.md#transfer_recurring_get) | **POST** /transfer/recurring/get | Retrieve a recurring transfer
[**transfer_recurring_list**](PlaidApi.md#transfer_recurring_list) | **POST** /transfer/recurring/list | List recurring transfers
[**transfer_refund_cancel**](PlaidApi.md#transfer_refund_cancel) | **POST** /transfer/refund/cancel | Cancel a refund
[**transfer_refund_create**](PlaidApi.md#transfer_refund_create) | **POST** /transfer/refund/create | Create a refund
[**transfer_refund_get**](PlaidApi.md#transfer_refund_get) | **POST** /transfer/refund/get | Retrieve a refund
[**transfer_repayment_list**](PlaidApi.md#transfer_repayment_list) | **POST** /transfer/repayment/list | Lists historical repayments
[**transfer_repayment_return_list**](PlaidApi.md#transfer_repayment_return_list) | **POST** /transfer/repayment/return/list | List the returns included in a repayment
[**transfer_sweep_get**](PlaidApi.md#transfer_sweep_get) | **POST** /transfer/sweep/get | Retrieve a sweep
[**transfer_sweep_list**](PlaidApi.md#transfer_sweep_list) | **POST** /transfer/sweep/list | List sweeps
[**user_create**](PlaidApi.md#user_create) | **POST** /user/create | Create user
[**wallet_create**](PlaidApi.md#wallet_create) | **POST** /wallet/create | Create an e-wallet
[**wallet_get**](PlaidApi.md#wallet_get) | **POST** /wallet/get | Fetch an e-wallet
[**wallet_list**](PlaidApi.md#wallet_list) | **POST** /wallet/list | Fetch a list of e-wallets
[**wallet_transaction_execute**](PlaidApi.md#wallet_transaction_execute) | **POST** /wallet/transaction/execute | Execute a transaction using an e-wallet
[**wallet_transaction_get**](PlaidApi.md#wallet_transaction_get) | **POST** /wallet/transaction/get | Fetch an e-wallet transaction
[**wallet_transaction_list**](PlaidApi.md#wallet_transaction_list) | **POST** /wallet/transaction/list | List e-wallet transactions
[**watchlist_screening_entity_create**](PlaidApi.md#watchlist_screening_entity_create) | **POST** /watchlist_screening/entity/create | Create a watchlist screening for an entity
[**watchlist_screening_entity_get**](PlaidApi.md#watchlist_screening_entity_get) | **POST** /watchlist_screening/entity/get | Get an entity screening
[**watchlist_screening_entity_history_list**](PlaidApi.md#watchlist_screening_entity_history_list) | **POST** /watchlist_screening/entity/history/list | List history for entity watchlist screenings
[**watchlist_screening_entity_hit_list**](PlaidApi.md#watchlist_screening_entity_hit_list) | **POST** /watchlist_screening/entity/hit/list | List hits for entity watchlist screenings
[**watchlist_screening_entity_list**](PlaidApi.md#watchlist_screening_entity_list) | **POST** /watchlist_screening/entity/list | List entity watchlist screenings
[**watchlist_screening_entity_program_get**](PlaidApi.md#watchlist_screening_entity_program_get) | **POST** /watchlist_screening/entity/program/get | Get entity watchlist screening program
[**watchlist_screening_entity_program_list**](PlaidApi.md#watchlist_screening_entity_program_list) | **POST** /watchlist_screening/entity/program/list | List entity watchlist screening programs
[**watchlist_screening_entity_review_create**](PlaidApi.md#watchlist_screening_entity_review_create) | **POST** /watchlist_screening/entity/review/create | Create a review for an entity watchlist screening
[**watchlist_screening_entity_review_list**](PlaidApi.md#watchlist_screening_entity_review_list) | **POST** /watchlist_screening/entity/review/list | List reviews for entity watchlist screenings
[**watchlist_screening_entity_update**](PlaidApi.md#watchlist_screening_entity_update) | **POST** /watchlist_screening/entity/update | Update an entity screening
[**watchlist_screening_individual_create**](PlaidApi.md#watchlist_screening_individual_create) | **POST** /watchlist_screening/individual/create | Create a watchlist screening for a person
[**watchlist_screening_individual_get**](PlaidApi.md#watchlist_screening_individual_get) | **POST** /watchlist_screening/individual/get | Retrieve an individual watchlist screening
[**watchlist_screening_individual_history_list**](PlaidApi.md#watchlist_screening_individual_history_list) | **POST** /watchlist_screening/individual/history/list | List history for individual watchlist screenings
[**watchlist_screening_individual_hit_list**](PlaidApi.md#watchlist_screening_individual_hit_list) | **POST** /watchlist_screening/individual/hit/list | List hits for individual watchlist screening
[**watchlist_screening_individual_list**](PlaidApi.md#watchlist_screening_individual_list) | **POST** /watchlist_screening/individual/list | List Individual Watchlist Screenings
[**watchlist_screening_individual_program_get**](PlaidApi.md#watchlist_screening_individual_program_get) | **POST** /watchlist_screening/individual/program/get | Get individual watchlist screening program
[**watchlist_screening_individual_program_list**](PlaidApi.md#watchlist_screening_individual_program_list) | **POST** /watchlist_screening/individual/program/list | List individual watchlist screening programs
[**watchlist_screening_individual_review_create**](PlaidApi.md#watchlist_screening_individual_review_create) | **POST** /watchlist_screening/individual/review/create | Create a review for an individual watchlist screening
[**watchlist_screening_individual_review_list**](PlaidApi.md#watchlist_screening_individual_review_list) | **POST** /watchlist_screening/individual/review/list | List reviews for individual watchlist screenings
[**watchlist_screening_individual_update**](PlaidApi.md#watchlist_screening_individual_update) | **POST** /watchlist_screening/individual/update | Update individual watchlist screening
[**webhook_verification_key_get**](PlaidApi.md#webhook_verification_key_get) | **POST** /webhook_verification_key/get | Get webhook verification key


# **accounts_balance_get**
> AccountsGetResponse accounts_balance_get(accounts_balance_get_request)

Retrieve real-time balance data

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.accounts_get_response import AccountsGetResponse
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    accounts_balance_get_request = AccountsBalanceGetRequest(
        access_token="access_token_example",
        secret="secret_example",
        client_id="client_id_example",
        options=AccountsBalanceGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
            min_last_updated_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # AccountsBalanceGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve real-time balance data
        api_response = api_instance.accounts_balance_get(accounts_balance_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->accounts_balance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts_balance_get_request** | [**AccountsBalanceGetRequest**](AccountsBalanceGetRequest.md)|  |

### Return type

[**AccountsGetResponse**](AccountsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get**
> AccountsGetResponse accounts_get(accounts_get_request)

Retrieve accounts

The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance. For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.  This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.accounts_get_response import AccountsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    accounts_get_request = AccountsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=AccountsGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # AccountsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve accounts
        api_response = api_instance.accounts_get(accounts_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts_get_request** | [**AccountsGetRequest**](AccountsGetRequest.md)|  |

### Return type

[**AccountsGetResponse**](AccountsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get**
> ApplicationGetResponse application_get(application_get_request)

Retrieve information about a Plaid application

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.application_get_request import ApplicationGetRequest
from plaid.model.application_get_response import ApplicationGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    application_get_request = ApplicationGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        application_id="application_id_example",
    ) # ApplicationGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve information about a Plaid application
        api_response = api_instance.application_get(application_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->application_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_get_request** | [**ApplicationGetRequest**](ApplicationGetRequest.md)|  |

### Return type

[**ApplicationGetResponse**](ApplicationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_audit_copy_create**
> AssetReportAuditCopyCreateResponse asset_report_audit_copy_create(asset_report_audit_copy_create_request)

Create Asset Report Audit Copy

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.  To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_audit_copy_create_request import AssetReportAuditCopyCreateRequest
from plaid.model.asset_report_audit_copy_create_response import AssetReportAuditCopyCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_audit_copy_create_request = AssetReportAuditCopyCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
        auditor_id="auditor_id_example",
    ) # AssetReportAuditCopyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Asset Report Audit Copy
        api_response = api_instance.asset_report_audit_copy_create(asset_report_audit_copy_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_audit_copy_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_audit_copy_create_request** | [**AssetReportAuditCopyCreateRequest**](AssetReportAuditCopyCreateRequest.md)|  |

### Return type

[**AssetReportAuditCopyCreateResponse**](AssetReportAuditCopyCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_audit_copy_get**
> AssetReportGetResponse asset_report_audit_copy_get(asset_report_audit_copy_get_request)

Retrieve an Asset Report Audit Copy

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_audit_copy_get_request import AssetReportAuditCopyGetRequest
from plaid.model.asset_report_get_response import AssetReportGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_audit_copy_get_request = AssetReportAuditCopyGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        audit_copy_token="audit_copy_token_example",
    ) # AssetReportAuditCopyGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Asset Report Audit Copy
        api_response = api_instance.asset_report_audit_copy_get(asset_report_audit_copy_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_audit_copy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_audit_copy_get_request** | [**AssetReportAuditCopyGetRequest**](AssetReportAuditCopyGetRequest.md)|  |

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_audit_copy_remove**
> AssetReportAuditCopyRemoveResponse asset_report_audit_copy_remove(asset_report_audit_copy_remove_request)

Remove Asset Report Audit Copy

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_audit_copy_remove_response import AssetReportAuditCopyRemoveResponse
from plaid.model.asset_report_audit_copy_remove_request import AssetReportAuditCopyRemoveRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_audit_copy_remove_request = AssetReportAuditCopyRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        audit_copy_token="audit_copy_token_example",
    ) # AssetReportAuditCopyRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove Asset Report Audit Copy
        api_response = api_instance.asset_report_audit_copy_remove(asset_report_audit_copy_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_audit_copy_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_audit_copy_remove_request** | [**AssetReportAuditCopyRemoveRequest**](AssetReportAuditCopyRemoveRequest.md)|  |

### Return type

[**AssetReportAuditCopyRemoveResponse**](AssetReportAuditCopyRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_create**
> AssetReportCreateResponse asset_report_create(asset_report_create_request)

Create an Asset Report

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.  The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. The exact amount of time to create the report will vary depending on how many days of history are requested and will typically range from a few seconds to about one minute. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).  The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_create_response import AssetReportCreateResponse
from plaid.model.asset_report_create_request import AssetReportCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_create_request = AssetReportCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_tokens=[
            "access_tokens_example",
        ],
        user_token="user_token_example",
        days_requested=0,
        options=AssetReportCreateRequestOptions(
            client_report_id="client_report_id_example",
            webhook="webhook_example",
            include_fast_report=True,
            products=[
                "products_example",
            ],
            add_ons=[
                AssetReportAddOns("investments"),
            ],
            user=AssetReportUser(),
        ),
    ) # AssetReportCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an Asset Report
        api_response = api_instance.asset_report_create(asset_report_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_create_request** | [**AssetReportCreateRequest**](AssetReportCreateRequest.md)|  |

### Return type

[**AssetReportCreateResponse**](AssetReportCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_filter**
> AssetReportFilterResponse asset_report_filter(asset_report_filter_request)

Filter Asset Report

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.  To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.  Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.  Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_filter_response import AssetReportFilterResponse
from plaid.model.asset_report_filter_request import AssetReportFilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_filter_request = AssetReportFilterRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
        account_ids_to_exclude=[
            "account_ids_to_exclude_example",
        ],
    ) # AssetReportFilterRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Filter Asset Report
        api_response = api_instance.asset_report_filter(asset_report_filter_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_filter_request** | [**AssetReportFilterRequest**](AssetReportFilterRequest.md)|  |

### Return type

[**AssetReportFilterResponse**](AssetReportFilterResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_get**
> AssetReportGetResponse asset_report_get(asset_report_get_request)

Retrieve an Asset Report

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.  If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.  To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_get_response import AssetReportGetResponse
from plaid.model.asset_report_get_request import AssetReportGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_get_request = AssetReportGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
        user_token="user_token_example",
        include_insights=False,
        fast_report=False,
        options=AssetReportGetRequestOptions(
            days_to_include=0,
        ),
    ) # AssetReportGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Asset Report
        api_response = api_instance.asset_report_get(asset_report_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_get_request** | [**AssetReportGetRequest**](AssetReportGetRequest.md)|  |

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_pdf_get**
> file_type asset_report_pdf_get(asset_report_pdf_get_request)

Retrieve a PDF Asset Report

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.  If `report_type` was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in `/asset_report/create`, debit transactions and transaction amounts won’t be included in the report.  [View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_pdf_get_request import AssetReportPDFGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_pdf_get_request = AssetReportPDFGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
        options=AssetReportPDFGetRequestOptions(
            days_to_include=0,
        ),
    ) # AssetReportPDFGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PDF Asset Report
        api_response = api_instance.asset_report_pdf_get(asset_report_pdf_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_pdf_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_pdf_get_request** | [**AssetReportPDFGetRequest**](AssetReportPDFGetRequest.md)|  |

### Return type

**file_type**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PDF of the Asset Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_refresh**
> AssetReportRefreshResponse asset_report_refresh(asset_report_refresh_request)

Refresh an Asset Report

An Asset Report is an immutable snapshot of a user's assets. In order to \"refresh\" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.  The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string (\"\") for any previously-populated fields you would like set as empty.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_refresh_response import AssetReportRefreshResponse
from plaid.model.asset_report_refresh_request import AssetReportRefreshRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_refresh_request = AssetReportRefreshRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
        days_requested=0,
        options=AssetReportRefreshRequestOptions(
            client_report_id="client_report_id_example",
            webhook="webhook_example",
            user=AssetReportUser(),
        ),
    ) # AssetReportRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh an Asset Report
        api_response = api_instance.asset_report_refresh(asset_report_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_refresh_request** | [**AssetReportRefreshRequest**](AssetReportRefreshRequest.md)|  |

### Return type

[**AssetReportRefreshResponse**](AssetReportRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_report_remove**
> AssetReportRemoveResponse asset_report_remove(asset_report_remove_request)

Delete an Asset Report

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.  The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_remove_request import AssetReportRemoveRequest
from plaid.model.asset_report_remove_response import AssetReportRemoveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_remove_request = AssetReportRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        asset_report_token="asset_report_token_example",
    ) # AssetReportRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an Asset Report
        api_response = api_instance.asset_report_remove(asset_report_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->asset_report_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_remove_request** | [**AssetReportRemoveRequest**](AssetReportRemoveRequest.md)|  |

### Return type

[**AssetReportRemoveResponse**](AssetReportRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_get**
> AuthGetResponse auth_get(auth_get_request)

Retrieve auth data

The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.  Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.  Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.auth_get_response import AuthGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    auth_get_request = AuthGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=AuthGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # AuthGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve auth data
        api_response = api_instance.auth_get(auth_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->auth_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_get_request** | [**AuthGetRequest**](AuthGetRequest.md)|  |

### Return type

[**AuthGetResponse**](AuthGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_balance_get**
> BankTransferBalanceGetResponse bank_transfer_balance_get(bank_transfer_balance_get_request)

Get balance of your Bank Transfer account

Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.  The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.  Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.bank_transfer_balance_get_response import BankTransferBalanceGetResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_balance_get_request import BankTransferBalanceGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_balance_get_request = BankTransferBalanceGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        origination_account_id="origination_account_id_example",
    ) # BankTransferBalanceGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get balance of your Bank Transfer account
        api_response = api_instance.bank_transfer_balance_get(bank_transfer_balance_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_balance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_balance_get_request** | [**BankTransferBalanceGetRequest**](BankTransferBalanceGetRequest.md)|  |

### Return type

[**BankTransferBalanceGetResponse**](BankTransferBalanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_cancel**
> BankTransferCancelResponse bank_transfer_cancel(bank_transfer_cancel_request)

Cancel a bank transfer

Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_cancel_request import BankTransferCancelRequest
from plaid.model.bank_transfer_cancel_response import BankTransferCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_cancel_request = BankTransferCancelRequest(
        client_id="client_id_example",
        secret="secret_example",
        bank_transfer_id="bank_transfer_id_example",
    ) # BankTransferCancelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a bank transfer
        api_response = api_instance.bank_transfer_cancel(bank_transfer_cancel_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_cancel_request** | [**BankTransferCancelRequest**](BankTransferCancelRequest.md)|  |

### Return type

[**BankTransferCancelResponse**](BankTransferCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_create**
> BankTransferCreateResponse bank_transfer_create(bank_transfer_create_request)

Create a bank transfer

Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_create_response import BankTransferCreateResponse
from plaid.model.bank_transfer_create_request import BankTransferCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_create_request = BankTransferCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        idempotency_key=BankTransferIdempotencyKey("idempotency_key_example"),
        access_token="access_token_example",
        account_id="account_id_example",
        type=BankTransferType("debit"),
        network=BankTransferNetwork("ach"),
        amount="amount_example",
        iso_currency_code="iso_currency_code_example",
        description="description_example",
        ach_class=ACHClass("ccd"),
        user=BankTransferUser(),
        custom_tag="custom_tag_example",
        metadata=BankTransferMetadata(
            key="key_example",
        ),
        origination_account_id="origination_account_id_example",
    ) # BankTransferCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a bank transfer
        api_response = api_instance.bank_transfer_create(bank_transfer_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_create_request** | [**BankTransferCreateRequest**](BankTransferCreateRequest.md)|  |

### Return type

[**BankTransferCreateResponse**](BankTransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_event_list**
> BankTransferEventListResponse bank_transfer_event_list(bank_transfer_event_list_request)

List bank transfer events

Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.bank_transfer_event_list_response import BankTransferEventListResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_event_list_request import BankTransferEventListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_event_list_request = BankTransferEventListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        bank_transfer_id="bank_transfer_id_example",
        account_id="account_id_example",
        bank_transfer_type=BankTransferEventListBankTransferType("debit"),
        event_types=[
            BankTransferEventType("pending"),
        ],
        count=25,
        offset=0,
        origination_account_id="origination_account_id_example",
        direction=BankTransferEventListDirection("inbound"),
    ) # BankTransferEventListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List bank transfer events
        api_response = api_instance.bank_transfer_event_list(bank_transfer_event_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_event_list_request** | [**BankTransferEventListRequest**](BankTransferEventListRequest.md)|  |

### Return type

[**BankTransferEventListResponse**](BankTransferEventListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_event_sync**
> BankTransferEventSyncResponse bank_transfer_event_sync(bank_transfer_event_sync_request)

Sync bank transfer events

`/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_event_sync_response import BankTransferEventSyncResponse
from plaid.model.bank_transfer_event_sync_request import BankTransferEventSyncRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_event_sync_request = BankTransferEventSyncRequest(
        client_id="client_id_example",
        secret="secret_example",
        after_id=0,
        count=25,
    ) # BankTransferEventSyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sync bank transfer events
        api_response = api_instance.bank_transfer_event_sync(bank_transfer_event_sync_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_event_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_event_sync_request** | [**BankTransferEventSyncRequest**](BankTransferEventSyncRequest.md)|  |

### Return type

[**BankTransferEventSyncResponse**](BankTransferEventSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_get**
> BankTransferGetResponse bank_transfer_get(bank_transfer_get_request)

Retrieve a bank transfer

The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_get_response import BankTransferGetResponse
from plaid.model.bank_transfer_get_request import BankTransferGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_get_request = BankTransferGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        bank_transfer_id="bank_transfer_id_example",
    ) # BankTransferGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bank transfer
        api_response = api_instance.bank_transfer_get(bank_transfer_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_get_request** | [**BankTransferGetRequest**](BankTransferGetRequest.md)|  |

### Return type

[**BankTransferGetResponse**](BankTransferGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_list**
> BankTransferListResponse bank_transfer_list(bank_transfer_list_request)

List bank transfers

Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.bank_transfer_list_response import BankTransferListResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_list_request import BankTransferListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_list_request = BankTransferListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
        origination_account_id="origination_account_id_example",
        direction=BankTransferDirection("outbound"),
    ) # BankTransferListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List bank transfers
        api_response = api_instance.bank_transfer_list(bank_transfer_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_list_request** | [**BankTransferListRequest**](BankTransferListRequest.md)|  |

### Return type

[**BankTransferListResponse**](BankTransferListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_migrate_account**
> BankTransferMigrateAccountResponse bank_transfer_migrate_account(bank_transfer_migrate_account_request)

Migrate account into Bank Transfers

As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_migrate_account_response import BankTransferMigrateAccountResponse
from plaid.model.bank_transfer_migrate_account_request import BankTransferMigrateAccountRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_migrate_account_request = BankTransferMigrateAccountRequest(
        client_id="client_id_example",
        secret="secret_example",
        account_number="account_number_example",
        routing_number="routing_number_example",
        wire_routing_number="wire_routing_number_example",
        account_type="account_type_example",
    ) # BankTransferMigrateAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Migrate account into Bank Transfers
        api_response = api_instance.bank_transfer_migrate_account(bank_transfer_migrate_account_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_migrate_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_migrate_account_request** | [**BankTransferMigrateAccountRequest**](BankTransferMigrateAccountRequest.md)|  |

### Return type

[**BankTransferMigrateAccountResponse**](BankTransferMigrateAccountResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_sweep_get**
> BankTransferSweepGetResponse bank_transfer_sweep_get(bank_transfer_sweep_get_request)

Retrieve a sweep

The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.bank_transfer_sweep_get_request import BankTransferSweepGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_sweep_get_response import BankTransferSweepGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_sweep_get_request = BankTransferSweepGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        sweep_id="sweep_id_example",
    ) # BankTransferSweepGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a sweep
        api_response = api_instance.bank_transfer_sweep_get(bank_transfer_sweep_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_sweep_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_sweep_get_request** | [**BankTransferSweepGetRequest**](BankTransferSweepGetRequest.md)|  |

### Return type

[**BankTransferSweepGetResponse**](BankTransferSweepGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transfer_sweep_list**
> BankTransferSweepListResponse bank_transfer_sweep_list(bank_transfer_sweep_list_request)

List sweeps

The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.bank_transfer_sweep_list_request import BankTransferSweepListRequest
from plaid.model.bank_transfer_sweep_list_response import BankTransferSweepListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    bank_transfer_sweep_list_request = BankTransferSweepListRequest(
        client_id="client_id_example",
        secret="secret_example",
        origination_account_id="origination_account_id_example",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
    ) # BankTransferSweepListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List sweeps
        api_response = api_instance.bank_transfer_sweep_list(bank_transfer_sweep_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->bank_transfer_sweep_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_sweep_list_request** | [**BankTransferSweepListRequest**](BankTransferSweepListRequest.md)|  |

### Return type

[**BankTransferSweepListResponse**](BankTransferSweepListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_get**
> CategoriesGetResponse categories_get(body)

Get categories

Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.  All implementations are recommended to use the newer `personal_finance_category` taxonomy instead of the older `category` taxonomy supported by this endpoint. The [`personal_finance_category taxonomy` CSV file](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) is available for download and is not accessible via API.

### Example


```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.categories_get_response import CategoriesGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)


# Enter a context with an instance of the API client
with plaid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Get categories
        api_response = api_instance.categories_get(body)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->categories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**CategoriesGetResponse**](CategoriesGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_token**
> PaymentInitiationPaymentTokenCreateResponse create_payment_token(payment_initiation_payment_token_create_request)

Create payment token

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.  The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_payment_token_create_response import PaymentInitiationPaymentTokenCreateResponse
from plaid.model.payment_initiation_payment_token_create_request import PaymentInitiationPaymentTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_payment_token_create_request = PaymentInitiationPaymentTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_id="payment_id_example",
    ) # PaymentInitiationPaymentTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create payment token
        api_response = api_instance.create_payment_token(payment_initiation_payment_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->create_payment_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_payment_token_create_request** | [**PaymentInitiationPaymentTokenCreateRequest**](PaymentInitiationPaymentTokenCreateRequest.md)|  |

### Return type

[**PaymentInitiationPaymentTokenCreateResponse**](PaymentInitiationPaymentTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_asset_report_freddie_mac_get**
> AssetReportFreddieGetResponse credit_asset_report_freddie_mac_get(asset_report_freddie_get_request)

Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_freddie_get_request import AssetReportFreddieGetRequest
from plaid.model.asset_report_freddie_get_response import AssetReportFreddieGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    asset_report_freddie_get_request = AssetReportFreddieGetRequest() # AssetReportFreddieGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.
        api_response = api_instance.credit_asset_report_freddie_mac_get(asset_report_freddie_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_asset_report_freddie_mac_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_report_freddie_get_request** | [**AssetReportFreddieGetRequest**](AssetReportFreddieGetRequest.md)|  |

### Return type

[**AssetReportFreddieGetResponse**](AssetReportFreddieGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_audit_copy_token_create**
> CreditAuditCopyTokenCreateResponse credit_audit_copy_token_create(credit_audit_copy_token_create_request)

Create Asset or Income Report Audit Copy Token

Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).  Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_audit_copy_token_create_response import CreditAuditCopyTokenCreateResponse
from plaid.model.credit_audit_copy_token_create_request import CreditAuditCopyTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_audit_copy_token_create_request = CreditAuditCopyTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        report_tokens=[
            "report_tokens_example",
        ],
    ) # CreditAuditCopyTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Asset or Income Report Audit Copy Token
        api_response = api_instance.credit_audit_copy_token_create(credit_audit_copy_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_audit_copy_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_audit_copy_token_create_request** | [**CreditAuditCopyTokenCreateRequest**](CreditAuditCopyTokenCreateRequest.md)|  |

### Return type

[**CreditAuditCopyTokenCreateResponse**](CreditAuditCopyTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_audit_copy_token_update**
> CreditAuditCopyTokenUpdateResponse credit_audit_copy_token_update(credit_audit_copy_token_update_request)

Update an Audit Copy Token

The `/credit/audit_copy_token/update` endpoint updates an existing  Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_audit_copy_token_update_request import CreditAuditCopyTokenUpdateRequest
from plaid.model.credit_audit_copy_token_update_response import CreditAuditCopyTokenUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_audit_copy_token_update_request = CreditAuditCopyTokenUpdateRequest(
        client_id="client_id_example",
        secret="secret_example",
        audit_copy_token="audit_copy_token_example",
        report_tokens=[
            "report_tokens_example",
        ],
    ) # CreditAuditCopyTokenUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update an Audit Copy Token
        api_response = api_instance.credit_audit_copy_token_update(credit_audit_copy_token_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_audit_copy_token_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_audit_copy_token_update_request** | [**CreditAuditCopyTokenUpdateRequest**](CreditAuditCopyTokenUpdateRequest.md)|  |

### Return type

[**CreditAuditCopyTokenUpdateResponse**](CreditAuditCopyTokenUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_employment_get**
> CreditBankEmploymentGetResponse credit_bank_employment_get(credit_bank_employment_get_request)

Retrieve information from the bank accounts used for employment verification

`/credit/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_bank_employment_get_request import CreditBankEmploymentGetRequest
from plaid.model.credit_bank_employment_get_response import CreditBankEmploymentGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_employment_get_request = CreditBankEmploymentGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditBankEmploymentGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve information from the bank accounts used for employment verification
        api_response = api_instance.credit_bank_employment_get(credit_bank_employment_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_employment_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_employment_get_request** | [**CreditBankEmploymentGetRequest**](CreditBankEmploymentGetRequest.md)|  |

### Return type

[**CreditBankEmploymentGetResponse**](CreditBankEmploymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_income_get**
> CreditBankIncomeGetResponse credit_bank_income_get(credit_bank_income_get_request)

Retrieve information from the bank accounts used for income verification

`/credit/bank_income/get` returns the bank income report(s) for a specified user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_bank_income_get_request import CreditBankIncomeGetRequest
from plaid.model.credit_bank_income_get_response import CreditBankIncomeGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_income_get_request = CreditBankIncomeGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
        options=CreditBankIncomeGetRequestOptions(
            count=1,
        ),
    ) # CreditBankIncomeGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve information from the bank accounts used for income verification
        api_response = api_instance.credit_bank_income_get(credit_bank_income_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_income_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_income_get_request** | [**CreditBankIncomeGetRequest**](CreditBankIncomeGetRequest.md)|  |

### Return type

[**CreditBankIncomeGetResponse**](CreditBankIncomeGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_income_pdf_get**
> file_type credit_bank_income_pdf_get(credit_bank_income_pdf_get_request)

Retrieve information from the bank accounts used for income verification in PDF format

`/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_bank_income_pdf_get_request import CreditBankIncomePDFGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_income_pdf_get_request = CreditBankIncomePDFGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditBankIncomePDFGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve information from the bank accounts used for income verification in PDF format
        api_response = api_instance.credit_bank_income_pdf_get(credit_bank_income_pdf_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_income_pdf_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_income_pdf_get_request** | [**CreditBankIncomePDFGetRequest**](CreditBankIncomePDFGetRequest.md)|  |

### Return type

**file_type**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PDF of the Bank Income Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_income_refresh**
> CreditBankIncomeRefreshResponse credit_bank_income_refresh(credit_bank_income_refresh_request)

Refresh a user's bank income information

`/credit/bank_income/refresh` refreshes the bank income report data for a specific user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_bank_income_refresh_request import CreditBankIncomeRefreshRequest
from plaid.model.credit_bank_income_refresh_response import CreditBankIncomeRefreshResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_income_refresh_request = CreditBankIncomeRefreshRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
        options=CreditBankIncomeRefreshRequestOptions(
            days_requested=1,
        ),
    ) # CreditBankIncomeRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh a user's bank income information
        api_response = api_instance.credit_bank_income_refresh(credit_bank_income_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_income_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_income_refresh_request** | [**CreditBankIncomeRefreshRequest**](CreditBankIncomeRefreshRequest.md)|  |

### Return type

[**CreditBankIncomeRefreshResponse**](CreditBankIncomeRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_income_webhook_update**
> credit_bank_income_webhook_update(credit_bank_income_webhook_update_request)

Subscribe and unsubscribe to proactive notifications for a user's income profile

`/credit/bank_income/webhook/update` allows you to subscribe or unsubscribe a user for income webhook notifications.  If a user is subscribed, on significant changes to the user's income profile, you will receive a `BANK_INCOME_REFRESH_UPDATE` webhook, prompting you to refresh bank income data for the user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_bank_income_webhook_update_request import CreditBankIncomeWebhookUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_income_webhook_update_request = CreditBankIncomeWebhookUpdateRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
        enable_webhooks=True,
    ) # CreditBankIncomeWebhookUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Subscribe and unsubscribe to proactive notifications for a user's income profile
        api_instance.credit_bank_income_webhook_update(credit_bank_income_webhook_update_request)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_income_webhook_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_income_webhook_update_request** | [**CreditBankIncomeWebhookUpdateRequest**](CreditBankIncomeWebhookUpdateRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_bank_statements_uploads_get**
> CreditBankStatementsUploadsGetResponse credit_bank_statements_uploads_get(credit_bank_statements_uploads_get_request)

Retrieve data for a user's uploaded bank statements

`/credit/bank_statements/uploads/get` returns data from user-uploaded bank statements.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.credit_bank_statements_uploads_get_request import CreditBankStatementsUploadsGetRequest
from plaid.model.credit_bank_statements_uploads_get_response import CreditBankStatementsUploadsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_bank_statements_uploads_get_request = CreditBankStatementsUploadsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditBankStatementsUploadsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve data for a user's uploaded bank statements
        api_response = api_instance.credit_bank_statements_uploads_get(credit_bank_statements_uploads_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_bank_statements_uploads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bank_statements_uploads_get_request** | [**CreditBankStatementsUploadsGetRequest**](CreditBankStatementsUploadsGetRequest.md)|  |

### Return type

[**CreditBankStatementsUploadsGetResponse**](CreditBankStatementsUploadsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_employment_get**
> CreditEmploymentGetResponse credit_employment_get(credit_employment_get_request)

Retrieve a summary of an individual's employment information

`/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_employment_get_request import CreditEmploymentGetRequest
from plaid.model.credit_employment_get_response import CreditEmploymentGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_employment_get_request = CreditEmploymentGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditEmploymentGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a summary of an individual's employment information
        api_response = api_instance.credit_employment_get(credit_employment_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_employment_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_employment_get_request** | [**CreditEmploymentGetRequest**](CreditEmploymentGetRequest.md)|  |

### Return type

[**CreditEmploymentGetResponse**](CreditEmploymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_freddie_mac_reports_get**
> CreditFreddieMacReportsGetResponse credit_freddie_mac_reports_get(credit_freddie_mac_reports_get_request)

Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_freddie_mac_reports_get_request import CreditFreddieMacReportsGetRequest
from plaid.model.credit_freddie_mac_reports_get_response import CreditFreddieMacReportsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_freddie_mac_reports_get_request = CreditFreddieMacReportsGetRequest(
        audit_copy_token="audit_copy_token_example",
        client_id="client_id_example",
        secret="secret_example",
    ) # CreditFreddieMacReportsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.
        api_response = api_instance.credit_freddie_mac_reports_get(credit_freddie_mac_reports_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_freddie_mac_reports_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_freddie_mac_reports_get_request** | [**CreditFreddieMacReportsGetRequest**](CreditFreddieMacReportsGetRequest.md)|  |

### Return type

[**CreditFreddieMacReportsGetResponse**](CreditFreddieMacReportsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_payroll_income_get**
> CreditPayrollIncomeGetResponse credit_payroll_income_get(credit_payroll_income_get_request)

Retrieve a user's payroll information

This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_payroll_income_get_response import CreditPayrollIncomeGetResponse
from plaid.model.credit_payroll_income_get_request import CreditPayrollIncomeGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_payroll_income_get_request = CreditPayrollIncomeGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditPayrollIncomeGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a user's payroll information
        api_response = api_instance.credit_payroll_income_get(credit_payroll_income_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_payroll_income_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_payroll_income_get_request** | [**CreditPayrollIncomeGetRequest**](CreditPayrollIncomeGetRequest.md)|  |

### Return type

[**CreditPayrollIncomeGetResponse**](CreditPayrollIncomeGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_payroll_income_precheck**
> CreditPayrollIncomePrecheckResponse credit_payroll_income_precheck(credit_payroll_income_precheck_request)

Check income verification eligibility and optimize conversion

`/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.  While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.  When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_payroll_income_precheck_response import CreditPayrollIncomePrecheckResponse
from plaid.model.credit_payroll_income_precheck_request import CreditPayrollIncomePrecheckRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_payroll_income_precheck_request = CreditPayrollIncomePrecheckRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
        access_tokens=[
            "access_tokens_example",
        ],
        employer=IncomeVerificationPrecheckEmployer(
            name="name_example",
            address=IncomeVerificationPrecheckEmployerAddress(),
            tax_id="tax_id_example",
            url="url_example",
        ),
        us_military_info=IncomeVerificationPrecheckMilitaryInfo(
            is_active_duty=True,
            branch="branch_example",
        ),
        payroll_institution=IncomeVerificationPrecheckPayrollInstitution(
            name="name_example",
        ),
    ) # CreditPayrollIncomePrecheckRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Check income verification eligibility and optimize conversion
        api_response = api_instance.credit_payroll_income_precheck(credit_payroll_income_precheck_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_payroll_income_precheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_payroll_income_precheck_request** | [**CreditPayrollIncomePrecheckRequest**](CreditPayrollIncomePrecheckRequest.md)|  |

### Return type

[**CreditPayrollIncomePrecheckResponse**](CreditPayrollIncomePrecheckResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_payroll_income_refresh**
> CreditPayrollIncomeRefreshResponse credit_payroll_income_refresh(credit_payroll_income_refresh_request)

Refresh a digital payroll income verification

`/credit/payroll_income/refresh` refreshes a given digital payroll income verification.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.credit_payroll_income_refresh_response import CreditPayrollIncomeRefreshResponse
from plaid.model.credit_payroll_income_refresh_request import CreditPayrollIncomeRefreshRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_payroll_income_refresh_request = CreditPayrollIncomeRefreshRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
        options=CreditPayrollIncomeRefreshRequestOptions(
            item_ids=[
                "item_ids_example",
            ],
            webhook="webhook_example",
        ),
    ) # CreditPayrollIncomeRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh a digital payroll income verification
        api_response = api_instance.credit_payroll_income_refresh(credit_payroll_income_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_payroll_income_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_payroll_income_refresh_request** | [**CreditPayrollIncomeRefreshRequest**](CreditPayrollIncomeRefreshRequest.md)|  |

### Return type

[**CreditPayrollIncomeRefreshResponse**](CreditPayrollIncomeRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_payroll_income_risk_signals_get**
> CreditPayrollIncomeRiskSignalsGetResponse credit_payroll_income_risk_signals_get(credit_payroll_income_risk_signals_get_request)

Retrieve fraud insights for a user's manually uploaded document(s).

`/credit/payroll_income/risk_signals/get` can be used as part of the Document Income flow to assess a user-uploaded document for signs of potential fraud or tampering. It returns a risk score for each uploaded document that indicates the likelihood of the document being fraudulent, in addition to details on the individual risk signals contributing to the score. `/credit/payroll_income/risk_signals/get` can be called at any time after the `INCOME_VERIFICATION_RISK_SIGNALS` webhook has been fired.  `/credit/payroll_income/risk_signals/get` is offered as an add-on to Document Income and is billed separately. To request access to this endpoint, submit a product access request or contact your Plaid account manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_payroll_income_risk_signals_get_response import CreditPayrollIncomeRiskSignalsGetResponse
from plaid.model.credit_payroll_income_risk_signals_get_request import CreditPayrollIncomeRiskSignalsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_payroll_income_risk_signals_get_request = CreditPayrollIncomeRiskSignalsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditPayrollIncomeRiskSignalsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve fraud insights for a user's manually uploaded document(s).
        api_response = api_instance.credit_payroll_income_risk_signals_get(credit_payroll_income_risk_signals_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_payroll_income_risk_signals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_payroll_income_risk_signals_get_request** | [**CreditPayrollIncomeRiskSignalsGetRequest**](CreditPayrollIncomeRiskSignalsGetRequest.md)|  |

### Return type

[**CreditPayrollIncomeRiskSignalsGetResponse**](CreditPayrollIncomeRiskSignalsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_relay_create**
> CreditRelayCreateResponse credit_relay_create(credit_relay_create_request)

Create a relay token to share an Asset Report with a partner client (beta)

Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.  To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_relay_create_request import CreditRelayCreateRequest
from plaid.model.credit_relay_create_response import CreditRelayCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_relay_create_request = CreditRelayCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        report_tokens=[
            "report_tokens_example",
        ],
        secondary_client_id="secondary_client_id_example",
        webhook="webhook_example",
    ) # CreditRelayCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a relay token to share an Asset Report with a partner client (beta)
        api_response = api_instance.credit_relay_create(credit_relay_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_relay_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_relay_create_request** | [**CreditRelayCreateRequest**](CreditRelayCreateRequest.md)|  |

### Return type

[**CreditRelayCreateResponse**](CreditRelayCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_relay_get**
> AssetReportGetResponse credit_relay_get(credit_relay_get_request)

Retrieve the reports associated with a relay token that was shared with you (beta)

`/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.asset_report_get_response import AssetReportGetResponse
from plaid.model.credit_relay_get_request import CreditRelayGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_relay_get_request = CreditRelayGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        relay_token="relay_token_example",
        report_type=ReportType("assets"),
    ) # CreditRelayGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the reports associated with a relay token that was shared with you (beta)
        api_response = api_instance.credit_relay_get(credit_relay_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_relay_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_relay_get_request** | [**CreditRelayGetRequest**](CreditRelayGetRequest.md)|  |

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_relay_refresh**
> CreditRelayRefreshResponse credit_relay_refresh(credit_relay_refresh_request)

Refresh a report of a relay token (beta)

The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_relay_refresh_request import CreditRelayRefreshRequest
from plaid.model.credit_relay_refresh_response import CreditRelayRefreshResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_relay_refresh_request = CreditRelayRefreshRequest(
        client_id="client_id_example",
        secret="secret_example",
        relay_token="relay_token_example",
        report_type=ReportType("assets"),
        webhook="webhook_example",
    ) # CreditRelayRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh a report of a relay token (beta)
        api_response = api_instance.credit_relay_refresh(credit_relay_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_relay_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_relay_refresh_request** | [**CreditRelayRefreshRequest**](CreditRelayRefreshRequest.md)|  |

### Return type

[**CreditRelayRefreshResponse**](CreditRelayRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_relay_remove**
> CreditRelayRemoveResponse credit_relay_remove(credit_relay_remove_request)

Remove relay token (beta)

The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_relay_remove_request import CreditRelayRemoveRequest
from plaid.model.credit_relay_remove_response import CreditRelayRemoveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_relay_remove_request = CreditRelayRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        relay_token="relay_token_example",
    ) # CreditRelayRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove relay token (beta)
        api_response = api_instance.credit_relay_remove(credit_relay_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_relay_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_relay_remove_request** | [**CreditRelayRemoveRequest**](CreditRelayRemoveRequest.md)|  |

### Return type

[**CreditRelayRemoveResponse**](CreditRelayRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_report_audit_copy_remove**
> CreditAuditCopyTokenRemoveResponse credit_report_audit_copy_remove(credit_audit_copy_token_remove_request)

Remove an Audit Copy token

The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_audit_copy_token_remove_response import CreditAuditCopyTokenRemoveResponse
from plaid.model.credit_audit_copy_token_remove_request import CreditAuditCopyTokenRemoveRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_audit_copy_token_remove_request = CreditAuditCopyTokenRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        audit_copy_token="audit_copy_token_example",
    ) # CreditAuditCopyTokenRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove an Audit Copy token
        api_response = api_instance.credit_report_audit_copy_remove(credit_audit_copy_token_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_report_audit_copy_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_audit_copy_token_remove_request** | [**CreditAuditCopyTokenRemoveRequest**](CreditAuditCopyTokenRemoveRequest.md)|  |

### Return type

[**CreditAuditCopyTokenRemoveResponse**](CreditAuditCopyTokenRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_sessions_get**
> CreditSessionsGetResponse credit_sessions_get(credit_sessions_get_request)

Retrieve Link sessions for your user

This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.  These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.credit_sessions_get_request import CreditSessionsGetRequest
from plaid.model.credit_sessions_get_response import CreditSessionsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    credit_sessions_get_request = CreditSessionsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        user_token="user_token_example",
    ) # CreditSessionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Link sessions for your user
        api_response = api_instance.credit_sessions_get(credit_sessions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->credit_sessions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_sessions_get_request** | [**CreditSessionsGetRequest**](CreditSessionsGetRequest.md)|  |

### Return type

[**CreditSessionsGetResponse**](CreditSessionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_user_get**
> DashboardUserGetResponse dashboard_user_get(dashboard_user_get_request)

Retrieve a dashboard user

Retrieve information about a dashboard user.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.dashboard_user_get_request import DashboardUserGetRequest
from plaid.model.dashboard_user_get_response import DashboardUserGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    dashboard_user_get_request = DashboardUserGetRequest(
        dashboard_user_id="54350110fedcbaf01234ffee",
        secret="secret_example",
        client_id="client_id_example",
    ) # DashboardUserGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a dashboard user
        api_response = api_instance.dashboard_user_get(dashboard_user_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->dashboard_user_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_user_get_request** | [**DashboardUserGetRequest**](DashboardUserGetRequest.md)|  |

### Return type

[**DashboardUserGetResponse**](DashboardUserGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_user_list**
> DashboardUserListResponse dashboard_user_list(dashboard_user_list_request)

List dashboard users

List all dashboard users associated with your account.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.dashboard_user_list_response import DashboardUserListResponse
from plaid.model.dashboard_user_list_request import DashboardUserListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    dashboard_user_list_request = DashboardUserListRequest(
        secret="secret_example",
        client_id="client_id_example",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # DashboardUserListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List dashboard users
        api_response = api_instance.dashboard_user_list(dashboard_user_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->dashboard_user_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_user_list_request** | [**DashboardUserListRequest**](DashboardUserListRequest.md)|  |

### Return type

[**DashboardUserListResponse**](DashboardUserListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit_switch_alt_create**
> DepositSwitchAltCreateResponse deposit_switch_alt_create(deposit_switch_alt_create_request)

Create a deposit switch without using Plaid Exchange

This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.deposit_switch_alt_create_request import DepositSwitchAltCreateRequest
from plaid.model.deposit_switch_alt_create_response import DepositSwitchAltCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    deposit_switch_alt_create_request = DepositSwitchAltCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        target_account=DepositSwitchTargetAccount(),
        target_user=DepositSwitchTargetUser(),
        options=DepositSwitchCreateRequestOptions(
            webhook="webhook_example",
            transaction_item_access_tokens=[
                "transaction_item_access_tokens_example",
            ],
        ),
        country_code="US",
    ) # DepositSwitchAltCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a deposit switch without using Plaid Exchange
        api_response = api_instance.deposit_switch_alt_create(deposit_switch_alt_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->deposit_switch_alt_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_switch_alt_create_request** | [**DepositSwitchAltCreateRequest**](DepositSwitchAltCreateRequest.md)|  |

### Return type

[**DepositSwitchAltCreateResponse**](DepositSwitchAltCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit_switch_create**
> DepositSwitchCreateResponse deposit_switch_create(deposit_switch_create_request)

Create a deposit switch

This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.deposit_switch_create_response import DepositSwitchCreateResponse
from plaid.model.deposit_switch_create_request import DepositSwitchCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    deposit_switch_create_request = DepositSwitchCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        target_access_token="target_access_token_example",
        target_account_id="target_account_id_example",
        country_code="US",
        options=DepositSwitchCreateRequestOptions(
            webhook="webhook_example",
            transaction_item_access_tokens=[
                "transaction_item_access_tokens_example",
            ],
        ),
    ) # DepositSwitchCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a deposit switch
        api_response = api_instance.deposit_switch_create(deposit_switch_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->deposit_switch_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_switch_create_request** | [**DepositSwitchCreateRequest**](DepositSwitchCreateRequest.md)|  |

### Return type

[**DepositSwitchCreateResponse**](DepositSwitchCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit_switch_get**
> DepositSwitchGetResponse deposit_switch_get(deposit_switch_get_request)

Retrieve a deposit switch

This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.deposit_switch_get_request import DepositSwitchGetRequest
from plaid.model.deposit_switch_get_response import DepositSwitchGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    deposit_switch_get_request = DepositSwitchGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        deposit_switch_id="deposit_switch_id_example",
    ) # DepositSwitchGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a deposit switch
        api_response = api_instance.deposit_switch_get(deposit_switch_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->deposit_switch_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_switch_get_request** | [**DepositSwitchGetRequest**](DepositSwitchGetRequest.md)|  |

### Return type

[**DepositSwitchGetResponse**](DepositSwitchGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit_switch_token_create**
> DepositSwitchTokenCreateResponse deposit_switch_token_create(deposit_switch_token_create_request)

Create a deposit switch token

In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.deposit_switch_token_create_response import DepositSwitchTokenCreateResponse
from plaid.model.deposit_switch_token_create_request import DepositSwitchTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    deposit_switch_token_create_request = DepositSwitchTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        deposit_switch_id="deposit_switch_id_example",
    ) # DepositSwitchTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a deposit switch token
        api_response = api_instance.deposit_switch_token_create(deposit_switch_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->deposit_switch_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_switch_token_create_request** | [**DepositSwitchTokenCreateRequest**](DepositSwitchTokenCreateRequest.md)|  |

### Return type

[**DepositSwitchTokenCreateResponse**](DepositSwitchTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employers_search**
> EmployersSearchResponse employers_search(employers_search_request)

Search employer database

`/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.  The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.employers_search_response import EmployersSearchResponse
from plaid.model.employers_search_request import EmployersSearchRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    employers_search_request = EmployersSearchRequest(
        client_id="client_id_example",
        secret="secret_example",
        query="query_example",
        products=[
            "products_example",
        ],
    ) # EmployersSearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Search employer database
        api_response = api_instance.employers_search(employers_search_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->employers_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employers_search_request** | [**EmployersSearchRequest**](EmployersSearchRequest.md)|  |

### Return type

[**EmployersSearchResponse**](EmployersSearchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employment_verification_get**
> EmploymentVerificationGetResponse employment_verification_get(employment_verification_get_request)

(Deprecated) Retrieve a summary of an individual's employment information

`/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.  This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.employment_verification_get_request import EmploymentVerificationGetRequest
from plaid.model.employment_verification_get_response import EmploymentVerificationGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    employment_verification_get_request = EmploymentVerificationGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # EmploymentVerificationGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Retrieve a summary of an individual's employment information
        api_response = api_instance.employment_verification_get(employment_verification_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->employment_verification_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_verification_get_request** | [**EmploymentVerificationGetRequest**](EmploymentVerificationGetRequest.md)|  |

### Return type

[**EmploymentVerificationGetResponse**](EmploymentVerificationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fdx_notifications**
> fdx_notifications(fdx_notification)

Webhook receiver for fdx notifications

A generic webhook receiver endpoint for FDX Event Notifications

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.fdx_notification import FDXNotification
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    fdx_notification = FDXNotification(
        notification_id="notification_id_example",
        type=FDXNotificationType("CONSENT_REVOKED"),
        sent_on=dateutil_parser('2021-07-15T14:46:41.375Z'),
        category=FDXNotificationCategory("SECURITY"),
        severity=FDXNotificationSeverity("EMERGENCY"),
        priority=FDXNotificationPriority("HIGH"),
        publisher=FDXParty(
            name="name_example",
            type=FDXPartyType("DATA_ACCESS_PLATFORM"),
            home_uri="home_uri_example",
            logo_uri="logo_uri_example",
            registry=FDXPartyRegistry("FDX"),
            registered_entity_name="registered_entity_name_example",
            registered_entity_id="registered_entity_id_example",
        ),
        subscriber=FDXParty(
            name="name_example",
            type=FDXPartyType("DATA_ACCESS_PLATFORM"),
            home_uri="home_uri_example",
            logo_uri="logo_uri_example",
            registry=FDXPartyRegistry("FDX"),
            registered_entity_name="registered_entity_name_example",
            registered_entity_id="registered_entity_id_example",
        ),
        notification_payload=FDXNotificationPayload(
            id="id_example",
            id_type=FDXNotificationPayloadIdType("ACCOUNT"),
            custom_fields=[
                FDXFiAttribute(
                    name="name_example",
                    value="value_example",
                ),
            ],
        ),
        url=FDXHateoasLink(
            href="https://api.fi.com/fdx/v4/accounts/12345",
            action=FDXHateoasLinkAction("GET"),
            rel="rel_example",
            types=[
                FDXContentTypes("application/pdf"),
            ],
        ),
    ) # FDXNotification | 

    # example passing only required values which don't have defaults set
    try:
        # Webhook receiver for fdx notifications
        api_instance.fdx_notifications(fdx_notification)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->fdx_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdx_notification** | [**FDXNotification**](FDXNotification.md)|  |

### Return type

void (empty response body)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_get**
> IdentityGetResponse identity_get(identity_get_request)

Retrieve identity data

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.  This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.  Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_get_request import IdentityGetRequest
from plaid.model.identity_get_response import IdentityGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_get_request = IdentityGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=IdentityGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # IdentityGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve identity data
        api_response = api_instance.identity_get(identity_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_get_request** | [**IdentityGetRequest**](IdentityGetRequest.md)|  |

### Return type

[**IdentityGetResponse**](IdentityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_match**
> IdentityMatchResponse identity_match(identity_match_request)

Retrieve identity match score

The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.  This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_match_request import IdentityMatchRequest
from plaid.model.identity_match_response import IdentityMatchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_match_request = IdentityMatchRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        user=IdentityMatchUser(),
        options=IdentityMatchRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # IdentityMatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve identity match score
        api_response = api_instance.identity_match(identity_match_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_match: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_match_request** | [**IdentityMatchRequest**](IdentityMatchRequest.md)|  |

### Return type

[**IdentityMatchResponse**](IdentityMatchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_refresh**
> IdentityRefreshResponse identity_refresh(identity_refresh_request)

Refresh identity data

`/identity/refresh` is an optional endpoint for users of the Identity product. It initiates an on-demand extraction to fetch the most up to date Identity information from the Financial Institution. This on-demand extraction takes place in addition to the periodic extractions that automatically occur any Identity-enabled Item. If changes to Identity are discovered after calling `/identity/refresh`, Plaid will fire a webhook [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/identity/#default_update). `/identity/refresh` is offered as an add-on to Identity and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.identity_refresh_request import IdentityRefreshRequest
from plaid.model.identity_refresh_response import IdentityRefreshResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_refresh_request = IdentityRefreshRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
    ) # IdentityRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh identity data
        api_response = api_instance.identity_refresh(identity_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_refresh_request** | [**IdentityRefreshRequest**](IdentityRefreshRequest.md)|  |

### Return type

[**IdentityRefreshResponse**](IdentityRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_verification_create**
> IdentityVerificationCreateResponse identity_verification_create(identity_verification_create_request)

Create a new identity verification

Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided. If you don't know whether the associated user already has an active Identity Verification, you can specify `\"is_idempotent\": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.  You can also use this endpoint to supply information you already have collected about the user; if any of these fields are specified, the screens prompting the user to enter them will be skipped during the Link flow. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_verification_create_response import IdentityVerificationCreateResponse
from plaid.model.identity_verification_create_request import IdentityVerificationCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_verification_create_request = IdentityVerificationCreateRequest(
        client_user_id=ClientUserID("your-db-id-3b24110"),
        is_shareable=True,
        template_id="idvtmp_4FrXJvfQU3zGUR",
        gave_consent=True,
        user=IdentityVerificationCreateRequestUser(
            email_address="user@example.com",
            phone_number="+19876543212",
            date_of_birth=dateutil_parser('Mon May 28 17:00:00 PDT 1990').date(),
            name=IdentityVerificationRequestUserName(
                given_name="Leslie",
                family_name="Knope",
            ),
            address=UserAddress(),
            id_number=UserIDNumber(),
            client_user_id=DeprecatedClientUserID("your-db-id-3b24110"),
        ),
        client_id="client_id_example",
        secret="secret_example",
        is_idempotent=True,
    ) # IdentityVerificationCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new identity verification
        api_response = api_instance.identity_verification_create(identity_verification_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_verification_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_verification_create_request** | [**IdentityVerificationCreateRequest**](IdentityVerificationCreateRequest.md)|  |

### Return type

[**IdentityVerificationCreateResponse**](IdentityVerificationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_verification_get**
> IdentityVerificationGetResponse identity_verification_get(identity_verification_get_request)

Retrieve Identity Verification

Retrieve a previously created identity verification.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_verification_get_response import IdentityVerificationGetResponse
from plaid.model.identity_verification_get_request import IdentityVerificationGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_verification_get_request = IdentityVerificationGetRequest(
        identity_verification_id="idv_52xR9LKo77r1Np",
        secret="secret_example",
        client_id="client_id_example",
    ) # IdentityVerificationGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Identity Verification
        api_response = api_instance.identity_verification_get(identity_verification_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_verification_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_verification_get_request** | [**IdentityVerificationGetRequest**](IdentityVerificationGetRequest.md)|  |

### Return type

[**IdentityVerificationGetResponse**](IdentityVerificationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_verification_list**
> IdentityVerificationListResponse identity_verification_list(identity_verification_list_request)

List Identity Verifications

Filter and list Identity Verifications created by your account

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_verification_list_request import IdentityVerificationListRequest
from plaid.model.identity_verification_list_response import IdentityVerificationListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_verification_list_request = IdentityVerificationListRequest(
        secret="secret_example",
        client_id="client_id_example",
        template_id="idvtmp_4FrXJvfQU3zGUR",
        client_user_id=ClientUserID("your-db-id-3b24110"),
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # IdentityVerificationListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List Identity Verifications
        api_response = api_instance.identity_verification_list(identity_verification_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_verification_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_verification_list_request** | [**IdentityVerificationListRequest**](IdentityVerificationListRequest.md)|  |

### Return type

[**IdentityVerificationListResponse**](IdentityVerificationListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_verification_retry**
> IdentityVerificationRetryResponse identity_verification_retry(identity_verification_retry_request)

Retry an Identity Verification

Allow a customer to retry their identity verification

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.identity_verification_retry_request import IdentityVerificationRetryRequest
from plaid.model.identity_verification_retry_response import IdentityVerificationRetryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    identity_verification_retry_request = IdentityVerificationRetryRequest(
        client_user_id=ClientUserID("your-db-id-3b24110"),
        template_id="idvtmp_4FrXJvfQU3zGUR",
        strategy=Strategy("reset"),
        user=IdentityVerificationRequestUser(),
        steps=IdentityVerificationRetryRequestStepsObject(
            verify_sms=True,
            kyc_check=True,
            documentary_verification=True,
            selfie_check=True,
        ),
        client_id="client_id_example",
        secret="secret_example",
    ) # IdentityVerificationRetryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retry an Identity Verification
        api_response = api_instance.identity_verification_retry(identity_verification_retry_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->identity_verification_retry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_verification_retry_request** | [**IdentityVerificationRetryRequest**](IdentityVerificationRetryRequest.md)|  |

### Return type

[**IdentityVerificationRetryResponse**](IdentityVerificationRetryResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **income_verification_create**
> IncomeVerificationCreateResponse income_verification_create(income_verification_create_request)

(Deprecated) Create an income verification instance

`/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.income_verification_create_response import IncomeVerificationCreateResponse
from plaid.model.income_verification_create_request import IncomeVerificationCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    income_verification_create_request = IncomeVerificationCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        webhook="webhook_example",
        precheck_id="precheck_id_example",
        options=IncomeVerificationCreateRequestOptions(
            access_tokens=[
                "access_tokens_example",
            ],
        ),
    ) # IncomeVerificationCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Create an income verification instance
        api_response = api_instance.income_verification_create(income_verification_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->income_verification_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_verification_create_request** | [**IncomeVerificationCreateRequest**](IncomeVerificationCreateRequest.md)|  |

### Return type

[**IncomeVerificationCreateResponse**](IncomeVerificationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **income_verification_documents_download**
> file_type income_verification_documents_download(income_verification_documents_download_request)

(Deprecated) Download the original documents used for income verification

`/income/verification/documents/download` provides the ability to download the source documents associated with the verification.  If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available for download from the payroll provider will be available from this endpoint.  The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file. If not, the response will contain all documents associated with the verification.  The `request_id` is returned in the `Plaid-Request-ID` header.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.income_verification_documents_download_request import IncomeVerificationDocumentsDownloadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    income_verification_documents_download_request = IncomeVerificationDocumentsDownloadRequest(
        client_id="client_id_example",
        secret="secret_example",
        income_verification_id="income_verification_id_example",
        access_token="access_token_example",
        document_id="document_id_example",
    ) # IncomeVerificationDocumentsDownloadRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Download the original documents used for income verification
        api_response = api_instance.income_verification_documents_download(income_verification_documents_download_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->income_verification_documents_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_verification_documents_download_request** | [**IncomeVerificationDocumentsDownloadRequest**](IncomeVerificationDocumentsDownloadRequest.md)|  |

### Return type

**file_type**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ZIP file containing source documents(s) used as the basis for income verification. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **income_verification_paystubs_get**
> IncomeVerificationPaystubsGetResponse income_verification_paystubs_get(income_verification_paystubs_get_request)

(Deprecated) Retrieve information from the paystubs used for income verification

`/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.  This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.income_verification_paystubs_get_response import IncomeVerificationPaystubsGetResponse
from plaid.model.income_verification_paystubs_get_request import IncomeVerificationPaystubsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    income_verification_paystubs_get_request = IncomeVerificationPaystubsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        income_verification_id="income_verification_id_example",
        access_token="access_token_example",
    ) # IncomeVerificationPaystubsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Retrieve information from the paystubs used for income verification
        api_response = api_instance.income_verification_paystubs_get(income_verification_paystubs_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->income_verification_paystubs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_verification_paystubs_get_request** | [**IncomeVerificationPaystubsGetRequest**](IncomeVerificationPaystubsGetRequest.md)|  |

### Return type

[**IncomeVerificationPaystubsGetResponse**](IncomeVerificationPaystubsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **income_verification_precheck**
> IncomeVerificationPrecheckResponse income_verification_precheck(income_verification_precheck_request)

(Deprecated) Check digital income verification eligibility and optimize conversion

`/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.  While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.  This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.income_verification_precheck_response import IncomeVerificationPrecheckResponse
from plaid.model.income_verification_precheck_request import IncomeVerificationPrecheckRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    income_verification_precheck_request = IncomeVerificationPrecheckRequest(
        client_id="client_id_example",
        secret="secret_example",
        user=IncomeVerificationPrecheckUser(
            first_name="first_name_example",
            last_name="last_name_example",
            email_address="email_address_example",
            home_address=SignalAddressData(),
        ),
        employer=IncomeVerificationPrecheckEmployer(
            name="name_example",
            address=IncomeVerificationPrecheckEmployerAddress(),
            tax_id="tax_id_example",
            url="url_example",
        ),
        payroll_institution=IncomeVerificationPrecheckPayrollInstitution(
            name="name_example",
        ),
        transactions_access_token=None,
        transactions_access_tokens=[
            "transactions_access_tokens_example",
        ],
        us_military_info=IncomeVerificationPrecheckMilitaryInfo(
            is_active_duty=True,
            branch="branch_example",
        ),
    ) # IncomeVerificationPrecheckRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Check digital income verification eligibility and optimize conversion
        api_response = api_instance.income_verification_precheck(income_verification_precheck_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->income_verification_precheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_verification_precheck_request** | [**IncomeVerificationPrecheckRequest**](IncomeVerificationPrecheckRequest.md)|  |

### Return type

[**IncomeVerificationPrecheckResponse**](IncomeVerificationPrecheckResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **income_verification_taxforms_get**
> IncomeVerificationTaxformsGetResponse income_verification_taxforms_get(income_verification_taxforms_get_request)

(Deprecated) Retrieve information from the tax documents used for income verification

`/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.  This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.income_verification_taxforms_get_request import IncomeVerificationTaxformsGetRequest
from plaid.model.income_verification_taxforms_get_response import IncomeVerificationTaxformsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    income_verification_taxforms_get_request = IncomeVerificationTaxformsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        income_verification_id="income_verification_id_example",
        access_token="access_token_example",
    ) # IncomeVerificationTaxformsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # (Deprecated) Retrieve information from the tax documents used for income verification
        api_response = api_instance.income_verification_taxforms_get(income_verification_taxforms_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->income_verification_taxforms_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_verification_taxforms_get_request** | [**IncomeVerificationTaxformsGetRequest**](IncomeVerificationTaxformsGetRequest.md)|  |

### Return type

[**IncomeVerificationTaxformsGetResponse**](IncomeVerificationTaxformsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institutions_get**
> InstitutionsGetResponse institutions_get(institutions_get_request)

Get details of all supported institutions

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.  If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.institutions_get_request import InstitutionsGetRequest
from plaid.model.institutions_get_response import InstitutionsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    institutions_get_request = InstitutionsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        count=1,
        offset=0,
        country_codes=[
            CountryCode("US"),
        ],
        options=InstitutionsGetRequestOptions(
            products=[
                Products("assets"),
            ],
            routing_numbers=[
                "routing_numbers_example",
            ],
            oauth=True,
            include_optional_metadata=True,
            include_auth_metadata=False,
            include_payment_initiation_metadata=False,
        ),
    ) # InstitutionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get details of all supported institutions
        api_response = api_instance.institutions_get(institutions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->institutions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutions_get_request** | [**InstitutionsGetRequest**](InstitutionsGetRequest.md)|  |

### Return type

[**InstitutionsGetResponse**](InstitutionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institutions_get_by_id**
> InstitutionsGetByIdResponse institutions_get_by_id(institutions_get_by_id_request)

Get details of an institution

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.  Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.institutions_get_by_id_response import InstitutionsGetByIdResponse
from plaid.model.institutions_get_by_id_request import InstitutionsGetByIdRequest
from plaid.model.plaid_error import PlaidError
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    institutions_get_by_id_request = InstitutionsGetByIdRequest(
        client_id="client_id_example",
        secret="secret_example",
        institution_id="institution_id_example",
        country_codes=[
            CountryCode("US"),
        ],
        options=InstitutionsGetByIdRequestOptions(
            include_optional_metadata=False,
            include_status=False,
            include_auth_metadata=False,
            include_payment_initiation_metadata=False,
        ),
    ) # InstitutionsGetByIdRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get details of an institution
        api_response = api_instance.institutions_get_by_id(institutions_get_by_id_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->institutions_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutions_get_by_id_request** | [**InstitutionsGetByIdRequest**](InstitutionsGetByIdRequest.md)|  |

### Return type

[**InstitutionsGetByIdResponse**](InstitutionsGetByIdResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institutions_search**
> InstitutionsSearchResponse institutions_search(institutions_search_request)

Search institutions

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.  Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.institutions_search_request import InstitutionsSearchRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.institutions_search_response import InstitutionsSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    institutions_search_request = InstitutionsSearchRequest(
        client_id="client_id_example",
        secret="secret_example",
        query="query_example",
        products=[
            Products("assets"),
        ],
        country_codes=[
            CountryCode("US"),
        ],
        options=InstitutionsSearchRequestOptions(
            oauth=True,
            include_optional_metadata=True,
            include_auth_metadata=False,
            include_payment_initiation_metadata=False,
            payment_initiation=InstitutionsSearchPaymentInitiationOptions(
                payment_id="payment_id_example",
                consent_id="consent_id_example",
            ),
        ),
    ) # InstitutionsSearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Search institutions
        api_response = api_instance.institutions_search(institutions_search_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->institutions_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutions_search_request** | [**InstitutionsSearchRequest**](InstitutionsSearchRequest.md)|  |

### Return type

[**InstitutionsSearchResponse**](InstitutionsSearchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_auth_get**
> InvestmentsAuthGetResponse investments_auth_get(investments_auth_get_request)

Get data needed to authorize an investments transfer

The `/investments/auth/get` endpoint allows developers to receive user-authorized data to facilitate the transfer of holdings

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.investments_auth_get_request import InvestmentsAuthGetRequest
from plaid.model.investments_auth_get_response import InvestmentsAuthGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    investments_auth_get_request = InvestmentsAuthGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=InvestmentsAuthGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # InvestmentsAuthGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get data needed to authorize an investments transfer
        api_response = api_instance.investments_auth_get(investments_auth_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->investments_auth_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investments_auth_get_request** | [**InvestmentsAuthGetRequest**](InvestmentsAuthGetRequest.md)|  |

### Return type

[**InvestmentsAuthGetResponse**](InvestmentsAuthGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_holdings_get**
> InvestmentsHoldingsGetResponse investments_holdings_get(investments_holdings_get_request)

Get Investment holdings

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.investments_holdings_get_request import InvestmentsHoldingsGetRequest
from plaid.model.investments_holdings_get_response import InvestmentsHoldingsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    investments_holdings_get_request = InvestmentsHoldingsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=InvestmentHoldingsGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # InvestmentsHoldingsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Investment holdings
        api_response = api_instance.investments_holdings_get(investments_holdings_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->investments_holdings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investments_holdings_get_request** | [**InvestmentsHoldingsGetRequest**](InvestmentsHoldingsGetRequest.md)|  |

### Return type

[**InvestmentsHoldingsGetResponse**](InvestmentsHoldingsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_refresh**
> InvestmentsRefreshResponse investments_refresh(investments_refresh_request)

Refresh investment data

`/investments/refresh` is an optional endpoint for users of the Investments product. It initiates an on-demand extraction to fetch the newest investments, holdings and investment transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Investments-enabled Item. If changes to investments are discovered after calling `/investments/refresh`, Plaid will fire webhooks: [`HOLDINGS: DEFAULT_UPDATE`](https://plaid.com/docs/api/products/investments/#holdings-default_update) if any new holdings are detected, and [INVESTMENTS_TRANSACTIONS: DEFAULT_UPDATE](https://plaid.com/docs/api/products/investments/#investments_transactions-default_update) if any new investment transactions are detected. Updated holdings and investment transactions can be fetched by calling `/investments/holdings/get` and `/investments/transactions/get`. \"Note that the `/investments/refresh` endpoint is not supported by all institutions. If called on an Item from an institution that does not support this functionality, it will return a `PRODUCT_NOT_SUPPORTED` error. `/investments/refresh` is offered as an add-on to Investments and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.investments_refresh_response import InvestmentsRefreshResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.investments_refresh_request import InvestmentsRefreshRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    investments_refresh_request = InvestmentsRefreshRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
    ) # InvestmentsRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh investment data
        api_response = api_instance.investments_refresh(investments_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->investments_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investments_refresh_request** | [**InvestmentsRefreshRequest**](InvestmentsRefreshRequest.md)|  |

### Return type

[**InvestmentsRefreshResponse**](InvestmentsRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investments_transactions_get**
> InvestmentsTransactionsGetResponse investments_transactions_get(investments_transactions_get_request)

Get investment transactions

The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.  Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.  Note that Investments does not have a webhook to indicate when initial transaction data has loaded (unless you use the `async_update` option). Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.  Data returned by the asynchronous investments extraction flow (when `async_update` is set to true) may not be immediately available to `/investments/transactions/get`. To be alerted when the data is ready to be fetched, listen for the `HISTORICAL_UPDATE` webhook. If no investments history is ready when `/investments/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.investments_transactions_get_response import InvestmentsTransactionsGetResponse
from plaid.model.investments_transactions_get_request import InvestmentsTransactionsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    investments_transactions_get_request = InvestmentsTransactionsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        start_date=dateutil_parser('1970-01-01').date(),
        end_date=dateutil_parser('1970-01-01').date(),
        options=InvestmentsTransactionsGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
            count=100,
            offset=0,
            async_update=False,
        ),
    ) # InvestmentsTransactionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get investment transactions
        api_response = api_instance.investments_transactions_get(investments_transactions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->investments_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investments_transactions_get_request** | [**InvestmentsTransactionsGetRequest**](InvestmentsTransactionsGetRequest.md)|  |

### Return type

[**InvestmentsTransactionsGetResponse**](InvestmentsTransactionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_access_token_invalidate**
> ItemAccessTokenInvalidateResponse item_access_token_invalidate(item_access_token_invalidate_request)

Invalidate access_token

By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.  You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_access_token_invalidate_request import ItemAccessTokenInvalidateRequest
from plaid.model.item_access_token_invalidate_response import ItemAccessTokenInvalidateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_access_token_invalidate_request = ItemAccessTokenInvalidateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # ItemAccessTokenInvalidateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Invalidate access_token
        api_response = api_instance.item_access_token_invalidate(item_access_token_invalidate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_access_token_invalidate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_access_token_invalidate_request** | [**ItemAccessTokenInvalidateRequest**](ItemAccessTokenInvalidateRequest.md)|  |

### Return type

[**ItemAccessTokenInvalidateResponse**](ItemAccessTokenInvalidateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_activity_list**
> ItemActivityListResponse item_activity_list(item_activity_list_request)

List a historical log of user consent events

List a historical log of user consent events

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.item_activity_list_request import ItemActivityListRequest
from plaid.model.item_activity_list_response import ItemActivityListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_activity_list_request = ItemActivityListRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        cursor="cursor_example",
        count=50,
    ) # ItemActivityListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List a historical log of user consent events
        api_response = api_instance.item_activity_list(item_activity_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_activity_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_list_request** | [**ItemActivityListRequest**](ItemActivityListRequest.md)|  |

### Return type

[**ItemActivityListResponse**](ItemActivityListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_application_list**
> ItemApplicationListResponse item_application_list(item_application_list_request)

List a user’s connected applications

List a user’s connected applications

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.item_application_list_request import ItemApplicationListRequest
from plaid.model.item_application_list_response import ItemApplicationListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_application_list_request = ItemApplicationListRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # ItemApplicationListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List a user’s connected applications
        api_response = api_instance.item_application_list(item_application_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_application_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_application_list_request** | [**ItemApplicationListRequest**](ItemApplicationListRequest.md)|  |

### Return type

[**ItemApplicationListResponse**](ItemApplicationListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_application_scopes_update**
> ItemApplicationScopesUpdateResponse item_application_scopes_update(item_application_scopes_update_request)

Update the scopes of access for a particular application

Enable consumers to update product access on selected accounts for an application.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_application_scopes_update_request import ItemApplicationScopesUpdateRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.item_application_scopes_update_response import ItemApplicationScopesUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_application_scopes_update_request = ItemApplicationScopesUpdateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        application_id="application_id_example",
        scopes=Scopes(
            product_access=ProductAccess(),
            accounts=[
                AccountAccess(
                    unique_id="unique_id_example",
                    authorized=True,
                    account_product_access=AccountProductAccessNullable(None),
                ),
            ],
            new_accounts=True,
        ),
        state="state_example",
        context=ScopesContext("ENROLLMENT"),
    ) # ItemApplicationScopesUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update the scopes of access for a particular application
        api_response = api_instance.item_application_scopes_update(item_application_scopes_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_application_scopes_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_application_scopes_update_request** | [**ItemApplicationScopesUpdateRequest**](ItemApplicationScopesUpdateRequest.md)|  |

### Return type

[**ItemApplicationScopesUpdateResponse**](ItemApplicationScopesUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_create_public_token**
> ItemPublicTokenCreateResponse item_create_public_token(item_public_token_create_request)

Create public token

Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).  If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.  A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.  The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_create_request import ItemPublicTokenCreateRequest
from plaid.model.item_public_token_create_response import ItemPublicTokenCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_public_token_create_request = ItemPublicTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # ItemPublicTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create public token
        api_response = api_instance.item_create_public_token(item_public_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_create_public_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_public_token_create_request** | [**ItemPublicTokenCreateRequest**](ItemPublicTokenCreateRequest.md)|  |

### Return type

[**ItemPublicTokenCreateResponse**](ItemPublicTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_get**
> ItemGetResponse item_get(item_get_request)

Retrieve an Item

Returns information about the status of an Item.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.item_get_response import ItemGetResponse
from plaid.model.item_get_request import ItemGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_get_request = ItemGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # ItemGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Item
        api_response = api_instance.item_get(item_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_get_request** | [**ItemGetRequest**](ItemGetRequest.md)|  |

### Return type

[**ItemGetResponse**](ItemGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_import**
> ItemImportResponse item_import(item_import_request)

Import Item

`/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.  Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_import_response import ItemImportResponse
from plaid.model.item_import_request import ItemImportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_import_request = ItemImportRequest(
        client_id="client_id_example",
        secret="secret_example",
        products=[
            Products("assets"),
        ],
        user_auth=ItemImportRequestUserAuth(
            user_id="user_id_example",
            auth_token="auth_token_example",
        ),
        options=ItemImportRequestOptions(
            webhook="webhook_example",
        ),
    ) # ItemImportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Import Item
        api_response = api_instance.item_import(item_import_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_import_request** | [**ItemImportRequest**](ItemImportRequest.md)|  |

### Return type

[**ItemImportResponse**](ItemImportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_public_token_exchange**
> ItemPublicTokenExchangeResponse item_public_token_exchange(item_public_token_exchange_request)

Exchange public token for an access token

Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.  The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_public_token_exchange_response import ItemPublicTokenExchangeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_public_token_exchange_request = ItemPublicTokenExchangeRequest(
        client_id="client_id_example",
        secret="secret_example",
        public_token="public_token_example",
    ) # ItemPublicTokenExchangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Exchange public token for an access token
        api_response = api_instance.item_public_token_exchange(item_public_token_exchange_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_public_token_exchange: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_public_token_exchange_request** | [**ItemPublicTokenExchangeRequest**](ItemPublicTokenExchangeRequest.md)|  |

### Return type

[**ItemPublicTokenExchangeResponse**](ItemPublicTokenExchangeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_remove**
> ItemRemoveResponse item_remove(item_remove_request)

Remove an Item

The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.  Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.  Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.  API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.item_remove_response import ItemRemoveResponse
from plaid.model.item_remove_request import ItemRemoveRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_remove_request = ItemRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # ItemRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove an Item
        api_response = api_instance.item_remove(item_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_remove_request** | [**ItemRemoveRequest**](ItemRemoveRequest.md)|  |

### Return type

[**ItemRemoveResponse**](ItemRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_webhook_update**
> ItemWebhookUpdateResponse item_webhook_update(item_webhook_update_request)

Update Webhook URL

The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.item_webhook_update_response import ItemWebhookUpdateResponse
from plaid.model.item_webhook_update_request import ItemWebhookUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    item_webhook_update_request = ItemWebhookUpdateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        webhook="webhook_example",
    ) # ItemWebhookUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Webhook URL
        api_response = api_instance.item_webhook_update(item_webhook_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->item_webhook_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_webhook_update_request** | [**ItemWebhookUpdateRequest**](ItemWebhookUpdateRequest.md)|  |

### Return type

[**ItemWebhookUpdateResponse**](ItemWebhookUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liabilities_get**
> LiabilitiesGetResponse liabilities_get(liabilities_get_request)

Retrieve Liabilities data

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).  The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.  Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.liabilities_get_request import LiabilitiesGetRequest
from plaid.model.liabilities_get_response import LiabilitiesGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    liabilities_get_request = LiabilitiesGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        options=LiabilitiesGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
        ),
    ) # LiabilitiesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Liabilities data
        api_response = api_instance.liabilities_get(liabilities_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->liabilities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liabilities_get_request** | [**LiabilitiesGetRequest**](LiabilitiesGetRequest.md)|  |

### Return type

[**LiabilitiesGetResponse**](LiabilitiesGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_delivery_create**
> LinkDeliveryCreateResponse link_delivery_create(link_delivery_create_request)

Create Hosted Link session

Use the `/link_delivery/create` endpoint to create a Hosted Link session.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.link_delivery_create_request import LinkDeliveryCreateRequest
from plaid.model.link_delivery_create_response import LinkDeliveryCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    link_delivery_create_request = LinkDeliveryCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        link_token="link_token_example",
        options=LinkDeliveryOptions(
            recipient=LinkDeliveryRecipient(
                communication_methods=[
                    LinkDeliveryCommunicationMethod(
                        method=LinkDeliveryDeliveryMethod("SMS"),
                        address="address_example",
                    ),
                ],
                first_name="first_name_example",
            ),
        ),
    ) # LinkDeliveryCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Hosted Link session
        api_response = api_instance.link_delivery_create(link_delivery_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->link_delivery_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_delivery_create_request** | [**LinkDeliveryCreateRequest**](LinkDeliveryCreateRequest.md)|  |

### Return type

[**LinkDeliveryCreateResponse**](LinkDeliveryCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_delivery_get**
> LinkDeliveryGetResponse link_delivery_get(link_delivery_get_request)

Get Hosted Link session

Use the `/link_delivery/get` endpoint to get the status of a Hosted Link session.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.link_delivery_get_request import LinkDeliveryGetRequest
from plaid.model.link_delivery_get_response import LinkDeliveryGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    link_delivery_get_request = LinkDeliveryGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        link_delivery_session_id="link_delivery_session_id_example",
    ) # LinkDeliveryGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Hosted Link session
        api_response = api_instance.link_delivery_get(link_delivery_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->link_delivery_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_delivery_get_request** | [**LinkDeliveryGetRequest**](LinkDeliveryGetRequest.md)|  |

### Return type

[**LinkDeliveryGetResponse**](LinkDeliveryGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_oauth_correlation_id_exchange**
> LinkOAuthCorrelationIdExchangeResponse link_oauth_correlation_id_exchange(link_o_auth_correlation_id_exchange_request)

Exchange the Link Correlation Id for a Link Token

Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for 'payment_initiation' products and is provided to the client via the OAuth `redirect_uri` as a query parameter. The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the 'link_token'.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.link_o_auth_correlation_id_exchange_response import LinkOAuthCorrelationIdExchangeResponse
from plaid.model.link_o_auth_correlation_id_exchange_request import LinkOAuthCorrelationIdExchangeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    link_o_auth_correlation_id_exchange_request = LinkOAuthCorrelationIdExchangeRequest(
        client_id="client_id_example",
        secret="secret_example",
        link_correlation_id="link_correlation_id_example",
    ) # LinkOAuthCorrelationIdExchangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Exchange the Link Correlation Id for a Link Token
        api_response = api_instance.link_oauth_correlation_id_exchange(link_o_auth_correlation_id_exchange_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->link_oauth_correlation_id_exchange: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_o_auth_correlation_id_exchange_request** | [**LinkOAuthCorrelationIdExchangeRequest**](LinkOAuthCorrelationIdExchangeRequest.md)|  |

### Return type

[**LinkOAuthCorrelationIdExchangeResponse**](LinkOAuthCorrelationIdExchangeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_token_create**
> LinkTokenCreateResponse link_token_create(link_token_create_request)

Create Link Token

The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.  A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_response import LinkTokenCreateResponse
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    link_token_create_request = LinkTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        client_name="client_name_example",
        language="language_example",
        country_codes=[
            CountryCode("US"),
        ],
        user=LinkTokenCreateRequestUser(
            client_user_id="client_user_id_example",
            legal_name="legal_name_example",
            name=LinkTokenCreateRequestUserName(None),
            phone_number="phone_number_example",
            phone_number_verified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            email_address="email_address_example",
            email_address_verified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ssn="ssn_example",
            date_of_birth=dateutil_parser('1970-01-01').date(),
            address=LinkTokenCreateRequestUserAddress(None),
            id_number=LinkTokenCreateRequestUserIdNumber(None),
        ),
        products=[
            Products("assets"),
        ],
        additional_consented_products=[
            Products("assets"),
        ],
        required_if_supported_products=[
            Products("assets"),
        ],
        webhook="webhook_example",
        access_token="access_token_example",
        link_customization_name="link_customization_name_example",
        redirect_uri="redirect_uri_example",
        android_package_name="android_package_name_example",
        institution_data=LinkTokenCreateInstitutionData(
            routing_number="routing_number_example",
        ),
        account_filters=LinkTokenAccountFilters(),
        eu_config=LinkTokenEUConfig(
            headless=True,
        ),
        institution_id="institution_id_example",
        payment_initiation=LinkTokenCreateRequestPaymentInitiation(
            payment_id="payment_id_example",
            consent_id="consent_id_example",
        ),
        deposit_switch=LinkTokenCreateRequestDepositSwitch(
            deposit_switch_id="deposit_switch_id_example",
        ),
        employment=LinkTokenCreateRequestEmployment(
            employment_source_types=[
                EmploymentSourceType("bank"),
            ],
            bank_employment=LinkTokenCreateRequestEmploymentBankIncome(
                days_requested=1,
            ),
        ),
        income_verification=LinkTokenCreateRequestIncomeVerification(
            income_verification_id="income_verification_id_example",
            asset_report_id="asset_report_id_example",
            precheck_id="precheck_id_example",
            access_tokens=[
                "access_tokens_example",
            ],
            income_source_types=[
                IncomeVerificationSourceType("bank"),
            ],
            bank_income=LinkTokenCreateRequestIncomeVerificationBankIncome(
                days_requested=1,
                enable_multiple_items=False,
            ),
            payroll_income=LinkTokenCreateRequestIncomeVerificationPayrollIncome(
                flow_types=[
                    IncomeVerificationPayrollFlowType("payroll_digital_income"),
                ],
                is_update_mode=False,
                item_id_to_update="item_id_to_update_example",
            ),
            stated_income_sources=[
                LinkTokenCreateRequestUserStatedIncomeSource(
                    employer="employer_example",
                    category=UserStatedIncomeSourceCategory("OTHER"),
                    pay_per_cycle=3.14,
                    pay_annual=3.14,
                    pay_type=UserStatedIncomeSourcePayType("UNKNOWN"),
                    pay_frequency=UserStatedIncomeSourceFrequency("UNKNOWN"),
                ),
            ],
        ),
        auth=LinkTokenCreateRequestAuth(
            auth_type_select_enabled=False,
            automated_microdeposits_enabled=True,
            instant_match_enabled=True,
            same_day_microdeposits_enabled=True,
            reroute_to_credentials="OFF",
            flow_type="FLEXIBLE_AUTH",
        ),
        transfer=LinkTokenCreateRequestTransfer(
            intent_id="intent_id_example",
            payment_profile_token="payment_profile_token_example",
        ),
        update=LinkTokenCreateRequestUpdate(
            account_selection_enabled=False,
        ),
        identity_verification=LinkTokenCreateRequestIdentityVerification(
            template_id="idvtmp_4FrXJvfQU3zGUR",
            consent=None,
            gave_consent=True,
        ),
        user_token="user_token_example",
        investments=LinkTokenInvestments(
            allow_unverified_crypto_wallets=True,
        ),
        investments_auth=LinkTokenInvestmentsAuth(
            manual_entry_enabled=False,
            masked_number_match_enabled=False,
        ),
    ) # LinkTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Link Token
        api_response = api_instance.link_token_create(link_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->link_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_token_create_request** | [**LinkTokenCreateRequest**](LinkTokenCreateRequest.md)|  |

### Return type

[**LinkTokenCreateResponse**](LinkTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_token_get**
> LinkTokenGetResponse link_token_get(link_token_get_request)

Get Link Token

The `/link/token/get` endpoint gets information about a previously-created `link_token` using the `/link/token/create` endpoint. It can be useful for debugging purposes.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_get_response import LinkTokenGetResponse
from plaid.model.link_token_get_request import LinkTokenGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    link_token_get_request = LinkTokenGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        link_token="link_token_example",
    ) # LinkTokenGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Link Token
        api_response = api_instance.link_token_get(link_token_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->link_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_token_get_request** | [**LinkTokenGetRequest**](LinkTokenGetRequest.md)|  |

### Return type

[**LinkTokenGetResponse**](LinkTokenGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_customer_create**
> PartnerCustomerCreateResponse partner_customer_create(partner_customer_create_request)

Creates a new end customer for a Plaid reseller.

The `/partner/customer/create` endpoint is used by reseller partners to create end customers.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.partner_customer_create_request import PartnerCustomerCreateRequest
from plaid.model.partner_customer_create_response import PartnerCustomerCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    partner_customer_create_request = PartnerCustomerCreateRequest(None) # PartnerCustomerCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new end customer for a Plaid reseller.
        api_response = api_instance.partner_customer_create(partner_customer_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->partner_customer_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_customer_create_request** | [**PartnerCustomerCreateRequest**](PartnerCustomerCreateRequest.md)|  |

### Return type

[**PartnerCustomerCreateResponse**](PartnerCustomerCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_customer_enable**
> PartnerCustomerEnableResponse partner_customer_enable(partner_customer_enable_request)

Enables a Plaid reseller's end customer in the Production environment.

The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the Production environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.partner_customer_enable_request import PartnerCustomerEnableRequest
from plaid.model.partner_customer_enable_response import PartnerCustomerEnableResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    partner_customer_enable_request = PartnerCustomerEnableRequest(None) # PartnerCustomerEnableRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Enables a Plaid reseller's end customer in the Production environment.
        api_response = api_instance.partner_customer_enable(partner_customer_enable_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->partner_customer_enable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_customer_enable_request** | [**PartnerCustomerEnableRequest**](PartnerCustomerEnableRequest.md)|  |

### Return type

[**PartnerCustomerEnableResponse**](PartnerCustomerEnableResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_customer_get**
> PartnerCustomerGetResponse partner_customer_get(partner_customer_get_request)

Returns a Plaid reseller's end customer.

The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.partner_customer_get_response import PartnerCustomerGetResponse
from plaid.model.partner_customer_get_request import PartnerCustomerGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    partner_customer_get_request = PartnerCustomerGetRequest(None) # PartnerCustomerGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Plaid reseller's end customer.
        api_response = api_instance.partner_customer_get(partner_customer_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->partner_customer_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_customer_get_request** | [**PartnerCustomerGetRequest**](PartnerCustomerGetRequest.md)|  |

### Return type

[**PartnerCustomerGetResponse**](PartnerCustomerGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_customer_oauth_institutions_get**
> PartnerCustomerOAuthInstitutionsGetResponse partner_customer_oauth_institutions_get(partner_customer_o_auth_institutions_get_request)

Returns OAuth-institution registration information for a given end customer.

The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.partner_customer_o_auth_institutions_get_response import PartnerCustomerOAuthInstitutionsGetResponse
from plaid.model.partner_customer_o_auth_institutions_get_request import PartnerCustomerOAuthInstitutionsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    partner_customer_o_auth_institutions_get_request = PartnerCustomerOAuthInstitutionsGetRequest(None) # PartnerCustomerOAuthInstitutionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Returns OAuth-institution registration information for a given end customer.
        api_response = api_instance.partner_customer_oauth_institutions_get(partner_customer_o_auth_institutions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->partner_customer_oauth_institutions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_customer_o_auth_institutions_get_request** | [**PartnerCustomerOAuthInstitutionsGetRequest**](PartnerCustomerOAuthInstitutionsGetRequest.md)|  |

### Return type

[**PartnerCustomerOAuthInstitutionsGetResponse**](PartnerCustomerOAuthInstitutionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_customer_remove**
> PartnerCustomerRemoveResponse partner_customer_remove(partner_customer_remove_request)

Removes a Plaid reseller's end customer.

The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.partner_customer_remove_response import PartnerCustomerRemoveResponse
from plaid.model.partner_customer_remove_request import PartnerCustomerRemoveRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    partner_customer_remove_request = PartnerCustomerRemoveRequest(None) # PartnerCustomerRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Removes a Plaid reseller's end customer.
        api_response = api_instance.partner_customer_remove(partner_customer_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->partner_customer_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_customer_remove_request** | [**PartnerCustomerRemoveRequest**](PartnerCustomerRemoveRequest.md)|  |

### Return type

[**PartnerCustomerRemoveResponse**](PartnerCustomerRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_consent_create**
> PaymentInitiationConsentCreateResponse payment_initiation_consent_create(payment_initiation_consent_create_request)

Create payment consent

The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.  Consents can be limited in time and scope, and have constraints that describe limitations for payments.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_consent_create_request import PaymentInitiationConsentCreateRequest
from plaid.model.payment_initiation_consent_create_response import PaymentInitiationConsentCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_consent_create_request = PaymentInitiationConsentCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        recipient_id="recipient_id_example",
        reference="reference_example",
        scopes=[
            PaymentInitiationConsentScope("ME_TO_ME"),
        ],
        constraints=PaymentInitiationConsentConstraints(
            valid_date_time=PaymentConsentValidDateTime(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            max_payment_amount=PaymentConsentMaxPaymentAmount(None),
            periodic_amounts=[
                PaymentConsentPeriodicAmount(
                    amount=PaymentConsentPeriodicAmountAmount(None),
                    interval=PaymentConsentPeriodicInterval("DAY"),
                    alignment=PaymentConsentPeriodicAlignment("CALENDAR"),
                ),
            ],
        ),
        options=ExternalPaymentInitiationConsentOptions(
            request_refund_details=True,
            iban="iban_example",
            bacs=PaymentInitiationOptionalRestrictionBacs(None),
        ),
    ) # PaymentInitiationConsentCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create payment consent
        api_response = api_instance.payment_initiation_consent_create(payment_initiation_consent_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_consent_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_consent_create_request** | [**PaymentInitiationConsentCreateRequest**](PaymentInitiationConsentCreateRequest.md)|  |

### Return type

[**PaymentInitiationConsentCreateResponse**](PaymentInitiationConsentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_consent_get**
> PaymentInitiationConsentGetResponse payment_initiation_consent_get(payment_initiation_consent_get_request)

Get payment consent

The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_consent_get_request import PaymentInitiationConsentGetRequest
from plaid.model.payment_initiation_consent_get_response import PaymentInitiationConsentGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_consent_get_request = PaymentInitiationConsentGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        consent_id="consent_id_example",
    ) # PaymentInitiationConsentGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get payment consent
        api_response = api_instance.payment_initiation_consent_get(payment_initiation_consent_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_consent_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_consent_get_request** | [**PaymentInitiationConsentGetRequest**](PaymentInitiationConsentGetRequest.md)|  |

### Return type

[**PaymentInitiationConsentGetResponse**](PaymentInitiationConsentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_consent_payment_execute**
> PaymentInitiationConsentPaymentExecuteResponse payment_initiation_consent_payment_execute(payment_initiation_consent_payment_execute_request)

Execute a single payment using consent

The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_consent_payment_execute_response import PaymentInitiationConsentPaymentExecuteResponse
from plaid.model.payment_initiation_consent_payment_execute_request import PaymentInitiationConsentPaymentExecuteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_consent_payment_execute_request = PaymentInitiationConsentPaymentExecuteRequest(
        client_id="client_id_example",
        secret="secret_example",
        consent_id="consent_id_example",
        amount=PaymentAmount(
            currency=PaymentAmountCurrency("GBP"),
            value=3.14,
        ),
        idempotency_key=ConsentPaymentIdempotencyKey("idempotency_key_example"),
    ) # PaymentInitiationConsentPaymentExecuteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Execute a single payment using consent
        api_response = api_instance.payment_initiation_consent_payment_execute(payment_initiation_consent_payment_execute_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_consent_payment_execute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_consent_payment_execute_request** | [**PaymentInitiationConsentPaymentExecuteRequest**](PaymentInitiationConsentPaymentExecuteRequest.md)|  |

### Return type

[**PaymentInitiationConsentPaymentExecuteResponse**](PaymentInitiationConsentPaymentExecuteResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_consent_revoke**
> PaymentInitiationConsentRevokeResponse payment_initiation_consent_revoke(payment_initiation_consent_revoke_request)

Revoke payment consent

The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_consent_revoke_response import PaymentInitiationConsentRevokeResponse
from plaid.model.payment_initiation_consent_revoke_request import PaymentInitiationConsentRevokeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_consent_revoke_request = PaymentInitiationConsentRevokeRequest(
        client_id="client_id_example",
        secret="secret_example",
        consent_id="consent_id_example",
    ) # PaymentInitiationConsentRevokeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke payment consent
        api_response = api_instance.payment_initiation_consent_revoke(payment_initiation_consent_revoke_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_consent_revoke: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_consent_revoke_request** | [**PaymentInitiationConsentRevokeRequest**](PaymentInitiationConsentRevokeRequest.md)|  |

### Return type

[**PaymentInitiationConsentRevokeResponse**](PaymentInitiationConsentRevokeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_payment_create**
> PaymentInitiationPaymentCreateResponse payment_initiation_payment_create(payment_initiation_payment_create_request)

Create a payment

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.  Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.  In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_payment_create_response import PaymentInitiationPaymentCreateResponse
from plaid.model.payment_initiation_payment_create_request import PaymentInitiationPaymentCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_payment_create_request = PaymentInitiationPaymentCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        recipient_id="recipient_id_example",
        reference="reference_example",
        amount=PaymentAmount(
            currency=PaymentAmountCurrency("GBP"),
            value=3.14,
        ),
        schedule=ExternalPaymentScheduleRequest(None),
        options=ExternalPaymentOptions(
            request_refund_details=True,
            iban="iban_example",
            bacs=PaymentInitiationOptionalRestrictionBacs(None),
            scheme=PaymentScheme("scheme_example"),
        ),
    ) # PaymentInitiationPaymentCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a payment
        api_response = api_instance.payment_initiation_payment_create(payment_initiation_payment_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_payment_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_payment_create_request** | [**PaymentInitiationPaymentCreateRequest**](PaymentInitiationPaymentCreateRequest.md)|  |

### Return type

[**PaymentInitiationPaymentCreateResponse**](PaymentInitiationPaymentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_payment_get**
> PaymentInitiationPaymentGetResponse payment_initiation_payment_get(payment_initiation_payment_get_request)

Get payment details

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_payment_get_request import PaymentInitiationPaymentGetRequest
from plaid.model.payment_initiation_payment_get_response import PaymentInitiationPaymentGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_payment_get_request = PaymentInitiationPaymentGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_id="payment_id_example",
    ) # PaymentInitiationPaymentGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get payment details
        api_response = api_instance.payment_initiation_payment_get(payment_initiation_payment_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_payment_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_payment_get_request** | [**PaymentInitiationPaymentGetRequest**](PaymentInitiationPaymentGetRequest.md)|  |

### Return type

[**PaymentInitiationPaymentGetResponse**](PaymentInitiationPaymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_payment_list**
> PaymentInitiationPaymentListResponse payment_initiation_payment_list(payment_initiation_payment_list_request)

List payments

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_payment_list_response import PaymentInitiationPaymentListResponse
from plaid.model.payment_initiation_payment_list_request import PaymentInitiationPaymentListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_payment_list_request = PaymentInitiationPaymentListRequest(
        client_id="client_id_example",
        secret="secret_example",
        count=10,
        cursor=dateutil_parser('1970-01-01T00:00:00.00Z'),
        consent_id="consent_id_example",
    ) # PaymentInitiationPaymentListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List payments
        api_response = api_instance.payment_initiation_payment_list(payment_initiation_payment_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_payment_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_payment_list_request** | [**PaymentInitiationPaymentListRequest**](PaymentInitiationPaymentListRequest.md)|  |

### Return type

[**PaymentInitiationPaymentListResponse**](PaymentInitiationPaymentListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_payment_reverse**
> PaymentInitiationPaymentReverseResponse payment_initiation_payment_reverse(payment_initiation_payment_reverse_request)

Reverse an existing payment

Reverse a settled payment from a Plaid virtual account.  The original payment must be in a settled state to be refunded. To refund partially, specify the amount as part of the request. If the amount is not specified, the refund amount will be equal to all of the remaining payment amount that has not been refunded yet.  The refund will go back to the source account that initiated the payment. The original payment must have been initiated to a Plaid virtual account so that this account can be used to initiate the refund. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_payment_reverse_response import PaymentInitiationPaymentReverseResponse
from plaid.model.payment_initiation_payment_reverse_request import PaymentInitiationPaymentReverseRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_payment_reverse_request = PaymentInitiationPaymentReverseRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_id="payment_id_example",
        idempotency_key=WalletTransactionIdempotencyKey("idempotency_key_example"),
        reference="reference_example",
        amount=PaymentAmountToRefund(None),
    ) # PaymentInitiationPaymentReverseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Reverse an existing payment
        api_response = api_instance.payment_initiation_payment_reverse(payment_initiation_payment_reverse_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_payment_reverse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_payment_reverse_request** | [**PaymentInitiationPaymentReverseRequest**](PaymentInitiationPaymentReverseRequest.md)|  |

### Return type

[**PaymentInitiationPaymentReverseResponse**](PaymentInitiationPaymentReverseResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_recipient_create**
> PaymentInitiationRecipientCreateResponse payment_initiation_recipient_create(payment_initiation_recipient_create_request)

Create payment recipient

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.  It is recommended to use `bacs` in the UK and `iban` in EU.  The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_recipient_create_request import PaymentInitiationRecipientCreateRequest
from plaid.model.payment_initiation_recipient_create_response import PaymentInitiationRecipientCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_recipient_create_request = PaymentInitiationRecipientCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        name="name_example",
        iban="iban_example",
        bacs=RecipientBACSNullable(None),
        address=PaymentInitiationAddress(),
    ) # PaymentInitiationRecipientCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create payment recipient
        api_response = api_instance.payment_initiation_recipient_create(payment_initiation_recipient_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_recipient_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_recipient_create_request** | [**PaymentInitiationRecipientCreateRequest**](PaymentInitiationRecipientCreateRequest.md)|  |

### Return type

[**PaymentInitiationRecipientCreateResponse**](PaymentInitiationRecipientCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_recipient_get**
> PaymentInitiationRecipientGetResponse payment_initiation_recipient_get(payment_initiation_recipient_get_request)

Get payment recipient

Get details about a payment recipient you have previously created.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_recipient_get_response import PaymentInitiationRecipientGetResponse
from plaid.model.payment_initiation_recipient_get_request import PaymentInitiationRecipientGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_recipient_get_request = PaymentInitiationRecipientGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        recipient_id="recipient_id_example",
    ) # PaymentInitiationRecipientGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get payment recipient
        api_response = api_instance.payment_initiation_recipient_get(payment_initiation_recipient_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_recipient_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_recipient_get_request** | [**PaymentInitiationRecipientGetRequest**](PaymentInitiationRecipientGetRequest.md)|  |

### Return type

[**PaymentInitiationRecipientGetResponse**](PaymentInitiationRecipientGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_initiation_recipient_list**
> PaymentInitiationRecipientListResponse payment_initiation_recipient_list(payment_initiation_recipient_list_request)

List payment recipients

The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_initiation_recipient_list_response import PaymentInitiationRecipientListResponse
from plaid.model.payment_initiation_recipient_list_request import PaymentInitiationRecipientListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_initiation_recipient_list_request = PaymentInitiationRecipientListRequest(
        client_id="client_id_example",
        secret="secret_example",
    ) # PaymentInitiationRecipientListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List payment recipients
        api_response = api_instance.payment_initiation_recipient_list(payment_initiation_recipient_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_initiation_recipient_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_initiation_recipient_list_request** | [**PaymentInitiationRecipientListRequest**](PaymentInitiationRecipientListRequest.md)|  |

### Return type

[**PaymentInitiationRecipientListResponse**](PaymentInitiationRecipientListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_profile_create**
> PaymentProfileCreateResponse payment_profile_create(payment_profile_create_request)

Create payment profile

Use `/payment_profile/create` endpoint to create a new payment profile. To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field. You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.payment_profile_create_response import PaymentProfileCreateResponse
from plaid.model.payment_profile_create_request import PaymentProfileCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_profile_create_request = PaymentProfileCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
    ) # PaymentProfileCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create payment profile
        api_response = api_instance.payment_profile_create(payment_profile_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_profile_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_profile_create_request** | [**PaymentProfileCreateRequest**](PaymentProfileCreateRequest.md)|  |

### Return type

[**PaymentProfileCreateResponse**](PaymentProfileCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_profile_get**
> PaymentProfileGetResponse payment_profile_get(payment_profile_get_request)

Get payment profile

Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.payment_profile_get_response import PaymentProfileGetResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.payment_profile_get_request import PaymentProfileGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_profile_get_request = PaymentProfileGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_profile_token="payment_profile_token_example",
    ) # PaymentProfileGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get payment profile
        api_response = api_instance.payment_profile_get(payment_profile_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_profile_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_profile_get_request** | [**PaymentProfileGetRequest**](PaymentProfileGetRequest.md)|  |

### Return type

[**PaymentProfileGetResponse**](PaymentProfileGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_profile_remove**
> PaymentProfileRemoveResponse payment_profile_remove(payment_profile_remove_request)

Remove payment profile

Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.payment_profile_remove_request import PaymentProfileRemoveRequest
from plaid.model.payment_profile_remove_response import PaymentProfileRemoveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    payment_profile_remove_request = PaymentProfileRemoveRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_profile_token="payment_profile_token_example",
    ) # PaymentProfileRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove payment profile
        api_response = api_instance.payment_profile_remove(payment_profile_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->payment_profile_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_profile_remove_request** | [**PaymentProfileRemoveRequest**](PaymentProfileRemoveRequest.md)|  |

### Return type

[**PaymentProfileRemoveResponse**](PaymentProfileRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_apex_processor_token_create**
> ProcessorTokenCreateResponse processor_apex_processor_token_create(processor_apex_processor_token_create_request)

Create Apex bank account token

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_token_create_response import ProcessorTokenCreateResponse
from plaid.model.processor_apex_processor_token_create_request import ProcessorApexProcessorTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_apex_processor_token_create_request = ProcessorApexProcessorTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
    ) # ProcessorApexProcessorTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Apex bank account token
        api_response = api_instance.processor_apex_processor_token_create(processor_apex_processor_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_apex_processor_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_apex_processor_token_create_request** | [**ProcessorApexProcessorTokenCreateRequest**](ProcessorApexProcessorTokenCreateRequest.md)|  |

### Return type

[**ProcessorTokenCreateResponse**](ProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_auth_get**
> ProcessorAuthGetResponse processor_auth_get(processor_auth_get_request)

Retrieve Auth data

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.  Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14). 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_auth_get_request import ProcessorAuthGetRequest
from plaid.model.processor_auth_get_response import ProcessorAuthGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_auth_get_request = ProcessorAuthGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
    ) # ProcessorAuthGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Auth data
        api_response = api_instance.processor_auth_get(processor_auth_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_auth_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_auth_get_request** | [**ProcessorAuthGetRequest**](ProcessorAuthGetRequest.md)|  |

### Return type

[**ProcessorAuthGetResponse**](ProcessorAuthGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_balance_get**
> ProcessorBalanceGetResponse processor_balance_get(processor_balance_get_request)

Retrieve Balance data

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_balance_get_response import ProcessorBalanceGetResponse
from plaid.model.processor_balance_get_request import ProcessorBalanceGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_balance_get_request = ProcessorBalanceGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        options=ProcessorBalanceGetRequestOptions(
            min_last_updated_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # ProcessorBalanceGetRequest | The `/processor/balance/get` endpoint returns the real-time balance for the account associated with a given `processor_token`.  The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.  Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of `null`.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Balance data
        api_response = api_instance.processor_balance_get(processor_balance_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_balance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_balance_get_request** | [**ProcessorBalanceGetRequest**](ProcessorBalanceGetRequest.md)| The &#x60;/processor/balance/get&#x60; endpoint returns the real-time balance for the account associated with a given &#x60;processor_token&#x60;.  The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.  Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of &#x60;null&#x60;. |

### Return type

[**ProcessorBalanceGetResponse**](ProcessorBalanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_bank_transfer_create**
> ProcessorBankTransferCreateResponse processor_bank_transfer_create(processor_bank_transfer_create_request)

Create a bank transfer as a processor

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_bank_transfer_create_response import ProcessorBankTransferCreateResponse
from plaid.model.processor_bank_transfer_create_request import ProcessorBankTransferCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_bank_transfer_create_request = ProcessorBankTransferCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        idempotency_key=BankTransferIdempotencyKey("idempotency_key_example"),
        processor_token="processor_token_example",
        type=BankTransferType("debit"),
        network=BankTransferNetwork("ach"),
        amount="amount_example",
        iso_currency_code="iso_currency_code_example",
        description="description_example",
        ach_class=ACHClass("ccd"),
        user=BankTransferUser(),
        custom_tag="custom_tag_example",
        metadata=BankTransferMetadata(
            key="key_example",
        ),
        origination_account_id="origination_account_id_example",
    ) # ProcessorBankTransferCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a bank transfer as a processor
        api_response = api_instance.processor_bank_transfer_create(processor_bank_transfer_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_bank_transfer_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_bank_transfer_create_request** | [**ProcessorBankTransferCreateRequest**](ProcessorBankTransferCreateRequest.md)|  |

### Return type

[**ProcessorBankTransferCreateResponse**](ProcessorBankTransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_identity_get**
> ProcessorIdentityGetResponse processor_identity_get(processor_identity_get_request)

Retrieve Identity data

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_identity_get_response import ProcessorIdentityGetResponse
from plaid.model.processor_identity_get_request import ProcessorIdentityGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_identity_get_request = ProcessorIdentityGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
    ) # ProcessorIdentityGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Identity data
        api_response = api_instance.processor_identity_get(processor_identity_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_identity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_identity_get_request** | [**ProcessorIdentityGetRequest**](ProcessorIdentityGetRequest.md)|  |

### Return type

[**ProcessorIdentityGetResponse**](ProcessorIdentityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_identity_match**
> ProcessorIdentityMatchResponse processor_identity_match(processor_identity_match_request)

Retrieve identity match score

The `/processor/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.  This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_identity_match_request import ProcessorIdentityMatchRequest
from plaid.model.processor_identity_match_response import ProcessorIdentityMatchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_identity_match_request = ProcessorIdentityMatchRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        user=IdentityMatchUser(),
    ) # ProcessorIdentityMatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve identity match score
        api_response = api_instance.processor_identity_match(processor_identity_match_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_identity_match: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_identity_match_request** | [**ProcessorIdentityMatchRequest**](ProcessorIdentityMatchRequest.md)|  |

### Return type

[**ProcessorIdentityMatchResponse**](ProcessorIdentityMatchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_signal_decision_report**
> ProcessorSignalDecisionReportResponse processor_signal_decision_report(processor_signal_decision_report_request)

Report whether you initiated an ACH transaction

After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_signal_decision_report_request import ProcessorSignalDecisionReportRequest
from plaid.model.processor_signal_decision_report_response import ProcessorSignalDecisionReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_signal_decision_report_request = ProcessorSignalDecisionReportRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        client_transaction_id="client_transaction_id_example",
        initiated=True,
        days_funds_on_hold=0,
        decision_outcome=SignalDecisionOutcome("APPROVE"),
        payment_method=SignalPaymentMethod("SAME_DAY_ACH"),
        amount_instantly_available=3.14,
    ) # ProcessorSignalDecisionReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Report whether you initiated an ACH transaction
        api_response = api_instance.processor_signal_decision_report(processor_signal_decision_report_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_signal_decision_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_signal_decision_report_request** | [**ProcessorSignalDecisionReportRequest**](ProcessorSignalDecisionReportRequest.md)|  |

### Return type

[**ProcessorSignalDecisionReportResponse**](ProcessorSignalDecisionReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_signal_evaluate**
> ProcessorSignalEvaluateResponse processor_signal_evaluate(processor_signal_evaluate_request)

Evaluate a planned ACH transaction

Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.  In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/processor/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).  Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time. To reduce this latency, you can call `/signal/prepare` on the Item before you need to request Signal data.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_signal_evaluate_response import ProcessorSignalEvaluateResponse
from plaid.model.processor_signal_evaluate_request import ProcessorSignalEvaluateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_signal_evaluate_request = ProcessorSignalEvaluateRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        client_transaction_id="client_transaction_id_example",
        amount=3.14,
        user_present=True,
        client_user_id="client_user_id_example",
        is_recurring=True,
        default_payment_method="default_payment_method_example",
        user=SignalUser(
            name=SignalPersonName(
                prefix="prefix_example",
                given_name="given_name_example",
                middle_name="middle_name_example",
                family_name="family_name_example",
                suffix="suffix_example",
            ),
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=SignalAddressData(),
        ),
        device=SignalDevice(
            ip_address="ip_address_example",
            user_agent="user_agent_example",
        ),
    ) # ProcessorSignalEvaluateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Evaluate a planned ACH transaction
        api_response = api_instance.processor_signal_evaluate(processor_signal_evaluate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_signal_evaluate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_signal_evaluate_request** | [**ProcessorSignalEvaluateRequest**](ProcessorSignalEvaluateRequest.md)|  |

### Return type

[**ProcessorSignalEvaluateResponse**](ProcessorSignalEvaluateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_signal_return_report**
> ProcessorSignalReturnReportResponse processor_signal_return_report(processor_signal_return_report_request)

Report a return for an ACH transaction

Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_signal_return_report_response import ProcessorSignalReturnReportResponse
from plaid.model.processor_signal_return_report_request import ProcessorSignalReturnReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_signal_return_report_request = ProcessorSignalReturnReportRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        client_transaction_id="client_transaction_id_example",
        return_code="return_code_example",
        returned_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ProcessorSignalReturnReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Report a return for an ACH transaction
        api_response = api_instance.processor_signal_return_report(processor_signal_return_report_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_signal_return_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_signal_return_report_request** | [**ProcessorSignalReturnReportRequest**](ProcessorSignalReturnReportRequest.md)|  |

### Return type

[**ProcessorSignalReturnReportResponse**](ProcessorSignalReturnReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_stripe_bank_account_token_create**
> ProcessorStripeBankAccountTokenCreateResponse processor_stripe_bank_account_token_create(processor_stripe_bank_account_token_create_request)

Create Stripe bank account token

Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).  Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.  Bank account tokens can also be revoked, using `/item/remove`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_stripe_bank_account_token_create_response import ProcessorStripeBankAccountTokenCreateResponse
from plaid.model.processor_stripe_bank_account_token_create_request import ProcessorStripeBankAccountTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_stripe_bank_account_token_create_request = ProcessorStripeBankAccountTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
    ) # ProcessorStripeBankAccountTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Stripe bank account token
        api_response = api_instance.processor_stripe_bank_account_token_create(processor_stripe_bank_account_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_stripe_bank_account_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_stripe_bank_account_token_create_request** | [**ProcessorStripeBankAccountTokenCreateRequest**](ProcessorStripeBankAccountTokenCreateRequest.md)|  |

### Return type

[**ProcessorStripeBankAccountTokenCreateResponse**](ProcessorStripeBankAccountTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_token_create**
> ProcessorTokenCreateResponse processor_token_create(processor_token_create_request)

Create processor token

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new `access_token`. Processor tokens can also be revoked, using `/item/remove`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_token_create_response import ProcessorTokenCreateResponse
from plaid.model.processor_token_create_request import ProcessorTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_token_create_request = ProcessorTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
        processor="dwolla",
    ) # ProcessorTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create processor token
        api_response = api_instance.processor_token_create(processor_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token_create_request** | [**ProcessorTokenCreateRequest**](ProcessorTokenCreateRequest.md)|  |

### Return type

[**ProcessorTokenCreateResponse**](ProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_token_permissions_get**
> ProcessorTokenPermissionsGetResponse processor_token_permissions_get(processor_token_permissions_get_request)

Get a processor token's product permissions

Used to get a processor token's product permissions. The `products` field will be an empty list if the processor can access all available products.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_token_permissions_get_response import ProcessorTokenPermissionsGetResponse
from plaid.model.processor_token_permissions_get_request import ProcessorTokenPermissionsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_token_permissions_get_request = ProcessorTokenPermissionsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
    ) # ProcessorTokenPermissionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get a processor token's product permissions
        api_response = api_instance.processor_token_permissions_get(processor_token_permissions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_token_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token_permissions_get_request** | [**ProcessorTokenPermissionsGetRequest**](ProcessorTokenPermissionsGetRequest.md)|  |

### Return type

[**ProcessorTokenPermissionsGetResponse**](ProcessorTokenPermissionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_token_permissions_set**
> ProcessorTokenPermissionsSetResponse processor_token_permissions_set(processor_token_permissions_set_request)

Control a processor's access to products

Used to control a processor's access to products on the given processor token. By default, a processor will have access to all available products on the corresponding item. To restrict access to a particular set of products, call this endpoint with the desired products. To restore access to all available products, call this endpoint with an empty list. This endpoint can be called multiple times as your needs and your processor's needs change.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_token_permissions_set_response import ProcessorTokenPermissionsSetResponse
from plaid.model.processor_token_permissions_set_request import ProcessorTokenPermissionsSetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_token_permissions_set_request = ProcessorTokenPermissionsSetRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        products=[
            Products("assets"),
        ],
    ) # ProcessorTokenPermissionsSetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Control a processor's access to products
        api_response = api_instance.processor_token_permissions_set(processor_token_permissions_set_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_token_permissions_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token_permissions_set_request** | [**ProcessorTokenPermissionsSetRequest**](ProcessorTokenPermissionsSetRequest.md)|  |

### Return type

[**ProcessorTokenPermissionsSetResponse**](ProcessorTokenPermissionsSetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_token_webhook_update**
> ProcessorTokenWebhookUpdateResponse processor_token_webhook_update(processor_token_webhook_update_request)

Update a processor token's webhook URL

This endpoint allows you to update the webhook URL associated with a processor token. This request triggers a `WEBHOOK_UPDATE_ACKNOWLEDGED` webhook to the newly specified webhook URL.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_token_webhook_update_request import ProcessorTokenWebhookUpdateRequest
from plaid.model.processor_token_webhook_update_response import ProcessorTokenWebhookUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_token_webhook_update_request = ProcessorTokenWebhookUpdateRequest(
        client_id="client_id_example",
        secret="secret_example",
        processor_token="processor_token_example",
        webhook="webhook_example",
    ) # ProcessorTokenWebhookUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a processor token's webhook URL
        api_response = api_instance.processor_token_webhook_update(processor_token_webhook_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_token_webhook_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token_webhook_update_request** | [**ProcessorTokenWebhookUpdateRequest**](ProcessorTokenWebhookUpdateRequest.md)|  |

### Return type

[**ProcessorTokenWebhookUpdateResponse**](ProcessorTokenWebhookUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_transactions_get**
> ProcessorTransactionsGetResponse processor_transactions_get(processor_transactions_get_request)

Get transaction data

The `/processor/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.  Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/processor/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).  Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.  Data returned by `/processor/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/processor/transactions/refresh` endpoint.  Note that data may not be immediately available to `/processor/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/processor/transactions/get`, if it wasn't. If no transaction history is ready when `/processor/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_transactions_get_request import ProcessorTransactionsGetRequest
from plaid.model.processor_transactions_get_response import ProcessorTransactionsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_transactions_get_request = ProcessorTransactionsGetRequest(
        client_id="client_id_example",
        options=TransactionsGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
            count=100,
            offset=0,
            include_original_description=False,
            include_personal_finance_category_beta=False,
            include_personal_finance_category=False,
            include_logo_and_counterparty_beta=False,
        ),
        processor_token="processor_token_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01').date(),
        end_date=dateutil_parser('1970-01-01').date(),
    ) # ProcessorTransactionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get transaction data
        api_response = api_instance.processor_transactions_get(processor_transactions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_transactions_get_request** | [**ProcessorTransactionsGetRequest**](ProcessorTransactionsGetRequest.md)|  |

### Return type

[**ProcessorTransactionsGetResponse**](ProcessorTransactionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_transactions_recurring_get**
> ProcessorTransactionsRecurringGetResponse processor_transactions_recurring_get(processor_transactions_recurring_get_request)

Fetch recurring transaction streams

The `/processor/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.  This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.  This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/processor/transactions/get` or `/processor/transactions/sync`). Once all historical transactions have been fetched, call `/processor/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.  After the initial call, you can call `/processor/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.processor_transactions_recurring_get_request import ProcessorTransactionsRecurringGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_transactions_recurring_get_response import ProcessorTransactionsRecurringGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_transactions_recurring_get_request = ProcessorTransactionsRecurringGetRequest(
        client_id="client_id_example",
        processor_token="processor_token_example",
        secret="secret_example",
        options=TransactionsRecurringGetRequestOptions(
            include_personal_finance_category=False,
        ),
        account_ids=[
            "account_ids_example",
        ],
    ) # ProcessorTransactionsRecurringGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch recurring transaction streams
        api_response = api_instance.processor_transactions_recurring_get(processor_transactions_recurring_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_transactions_recurring_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_transactions_recurring_get_request** | [**ProcessorTransactionsRecurringGetRequest**](ProcessorTransactionsRecurringGetRequest.md)|  |

### Return type

[**ProcessorTransactionsRecurringGetResponse**](ProcessorTransactionsRecurringGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_transactions_refresh**
> ProcessorTransactionsRefreshResponse processor_transactions_refresh(processor_transactions_refresh_request)

Refresh transaction data

`/processor/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/processor/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/processor/transactions/sync` and `/processor/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/processor/transactions/get` or `/processor/transactions/sync`. Note that the `/processor/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.  `/processor/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_transactions_refresh_request import ProcessorTransactionsRefreshRequest
from plaid.model.processor_transactions_refresh_response import ProcessorTransactionsRefreshResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_transactions_refresh_request = ProcessorTransactionsRefreshRequest(
        client_id="client_id_example",
        processor_token="processor_token_example",
        secret="secret_example",
    ) # ProcessorTransactionsRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh transaction data
        api_response = api_instance.processor_transactions_refresh(processor_transactions_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_transactions_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_transactions_refresh_request** | [**ProcessorTransactionsRefreshRequest**](ProcessorTransactionsRefreshRequest.md)|  |

### Return type

[**ProcessorTransactionsRefreshResponse**](ProcessorTransactionsRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processor_transactions_sync**
> ProcessorTransactionsSyncResponse processor_transactions_sync(processor_transactions_sync_request)

Get incremental transaction updates on an Item

This endpoint replaces `/processor/transactions/get` and its associated webhooks for most common use-cases.  The `/processor/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/processor/transactions/sync` provides the same functionality as `/processor/transactions/get` and can be used instead of `/processor/transactions/get` to simplify the process of tracking transactions updates.  This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.  Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.  In the first call to `/processor/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as \"adds\"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.  Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/processor/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.  When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/processor/transactions/sync` fails when retrieving a paginated update, which can occur as a result of the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.  Whenever new or updated transaction data becomes available, `/processor/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/processor/transactions/refresh` endpoint.  Note that for newly created Items, data may not be immediately available to `/processor/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.processor_transactions_sync_request import ProcessorTransactionsSyncRequest
from plaid.model.processor_transactions_sync_response import ProcessorTransactionsSyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    processor_transactions_sync_request = ProcessorTransactionsSyncRequest(
        client_id="client_id_example",
        processor_token="processor_token_example",
        secret="secret_example",
        cursor="cursor_example",
        count=100,
        options=TransactionsSyncRequestOptions(
            include_original_description=False,
            include_personal_finance_category=False,
            include_logo_and_counterparty_beta=False,
        ),
    ) # ProcessorTransactionsSyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get incremental transaction updates on an Item
        api_response = api_instance.processor_transactions_sync(processor_transactions_sync_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->processor_transactions_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_transactions_sync_request** | [**ProcessorTransactionsSyncRequest**](ProcessorTransactionsSyncRequest.md)|  |

### Return type

[**ProcessorTransactionsSyncResponse**](ProcessorTransactionsSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_bank_income_fire_webhook**
> SandboxBankIncomeFireWebhookResponse sandbox_bank_income_fire_webhook(sandbox_bank_income_fire_webhook_request)

Manually fire a bank income webhook in sandbox

Use the `/sandbox/bank_income/fire_webhook` endpoint to manually trigger a Bank Income webhook in the Sandbox environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_bank_income_fire_webhook_request import SandboxBankIncomeFireWebhookRequest
from plaid.model.sandbox_bank_income_fire_webhook_response import SandboxBankIncomeFireWebhookResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_bank_income_fire_webhook_request = SandboxBankIncomeFireWebhookRequest(
        client_id="client_id_example",
        secret="secret_example",
        webhook_override="webhook_override_example",
        webhook_code=SandboxBankIncomeWebhookFireRequestWebhookCode("BANK_INCOME_REFRESH_UPDATE"),
        webhook_fields=SandboxBankIncomeWebhookFireRequestWebhookFields(
            user_id="user_id_example",
            bank_income_refresh_complete_result=BankIncomeRefreshCompleteResult("SUCCESS"),
        ),
    ) # SandboxBankIncomeFireWebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Manually fire a bank income webhook in sandbox
        api_response = api_instance.sandbox_bank_income_fire_webhook(sandbox_bank_income_fire_webhook_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_bank_income_fire_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_bank_income_fire_webhook_request** | [**SandboxBankIncomeFireWebhookRequest**](SandboxBankIncomeFireWebhookRequest.md)|  |

### Return type

[**SandboxBankIncomeFireWebhookResponse**](SandboxBankIncomeFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_bank_transfer_fire_webhook**
> SandboxBankTransferFireWebhookResponse sandbox_bank_transfer_fire_webhook(sandbox_bank_transfer_fire_webhook_request)

Manually fire a Bank Transfer webhook

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_bank_transfer_fire_webhook_response import SandboxBankTransferFireWebhookResponse
from plaid.model.sandbox_bank_transfer_fire_webhook_request import SandboxBankTransferFireWebhookRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_bank_transfer_fire_webhook_request = SandboxBankTransferFireWebhookRequest(
        client_id="client_id_example",
        secret="secret_example",
        webhook="webhook_example",
    ) # SandboxBankTransferFireWebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Manually fire a Bank Transfer webhook
        api_response = api_instance.sandbox_bank_transfer_fire_webhook(sandbox_bank_transfer_fire_webhook_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_bank_transfer_fire_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_bank_transfer_fire_webhook_request** | [**SandboxBankTransferFireWebhookRequest**](SandboxBankTransferFireWebhookRequest.md)|  |

### Return type

[**SandboxBankTransferFireWebhookResponse**](SandboxBankTransferFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_bank_transfer_simulate**
> SandboxBankTransferSimulateResponse sandbox_bank_transfer_simulate(sandbox_bank_transfer_simulate_request)

Simulate a bank transfer event in Sandbox

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_bank_transfer_simulate_request import SandboxBankTransferSimulateRequest
from plaid.model.sandbox_bank_transfer_simulate_response import SandboxBankTransferSimulateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_bank_transfer_simulate_request = SandboxBankTransferSimulateRequest(
        client_id="client_id_example",
        secret="secret_example",
        bank_transfer_id="bank_transfer_id_example",
        event_type="event_type_example",
        failure_reason=BankTransferFailure(),
    ) # SandboxBankTransferSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Simulate a bank transfer event in Sandbox
        api_response = api_instance.sandbox_bank_transfer_simulate(sandbox_bank_transfer_simulate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_bank_transfer_simulate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_bank_transfer_simulate_request** | [**SandboxBankTransferSimulateRequest**](SandboxBankTransferSimulateRequest.md)|  |

### Return type

[**SandboxBankTransferSimulateResponse**](SandboxBankTransferSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_income_fire_webhook**
> SandboxIncomeFireWebhookResponse sandbox_income_fire_webhook(sandbox_income_fire_webhook_request)

Manually fire an Income webhook

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger a Payroll Income webhook in the Sandbox environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_income_fire_webhook_response import SandboxIncomeFireWebhookResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_income_fire_webhook_request import SandboxIncomeFireWebhookRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_income_fire_webhook_request = SandboxIncomeFireWebhookRequest(
        client_id="client_id_example",
        secret="secret_example",
        item_id="item_id_example",
        user_id="user_id_example",
        webhook="webhook_example",
        verification_status="VERIFICATION_STATUS_PROCESSING_COMPLETE",
    ) # SandboxIncomeFireWebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Manually fire an Income webhook
        api_response = api_instance.sandbox_income_fire_webhook(sandbox_income_fire_webhook_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_income_fire_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_income_fire_webhook_request** | [**SandboxIncomeFireWebhookRequest**](SandboxIncomeFireWebhookRequest.md)|  |

### Return type

[**SandboxIncomeFireWebhookResponse**](SandboxIncomeFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_item_fire_webhook**
> SandboxItemFireWebhookResponse sandbox_item_fire_webhook(sandbox_item_fire_webhook_request)

Fire a test webhook

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:  `DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.  `NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.  `AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.  `RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.  `SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.  `PRODUCT_READY`: Assets webhook to be fired when a given asset report has been successfully generated. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.  `ERROR`: Assets webhook to be fired when asset report generation has failed. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.  Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_item_fire_webhook_request import SandboxItemFireWebhookRequest
from plaid.model.sandbox_item_fire_webhook_response import SandboxItemFireWebhookResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_item_fire_webhook_request = SandboxItemFireWebhookRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        webhook_type=WebhookType("AUTH"),
        webhook_code="DEFAULT_UPDATE",
    ) # SandboxItemFireWebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fire a test webhook
        api_response = api_instance.sandbox_item_fire_webhook(sandbox_item_fire_webhook_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_item_fire_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_item_fire_webhook_request** | [**SandboxItemFireWebhookRequest**](SandboxItemFireWebhookRequest.md)|  |

### Return type

[**SandboxItemFireWebhookResponse**](SandboxItemFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_item_reset_login**
> SandboxItemResetLoginResponse sandbox_item_reset_login(sandbox_item_reset_login_request)

Force a Sandbox Item into an error state

`/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.   In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_item_reset_login_response import SandboxItemResetLoginResponse
from plaid.model.sandbox_item_reset_login_request import SandboxItemResetLoginRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_item_reset_login_request = SandboxItemResetLoginRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # SandboxItemResetLoginRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Force a Sandbox Item into an error state
        api_response = api_instance.sandbox_item_reset_login(sandbox_item_reset_login_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_item_reset_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_item_reset_login_request** | [**SandboxItemResetLoginRequest**](SandboxItemResetLoginRequest.md)|  |

### Return type

[**SandboxItemResetLoginResponse**](SandboxItemResetLoginResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_item_set_verification_status**
> SandboxItemSetVerificationStatusResponse sandbox_item_set_verification_status(sandbox_item_set_verification_status_request)

Set verification status for Sandbox account

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.  Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).  For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_item_set_verification_status_request import SandboxItemSetVerificationStatusRequest
from plaid.model.sandbox_item_set_verification_status_response import SandboxItemSetVerificationStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_item_set_verification_status_request = SandboxItemSetVerificationStatusRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
        verification_status="automatically_verified",
    ) # SandboxItemSetVerificationStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set verification status for Sandbox account
        api_response = api_instance.sandbox_item_set_verification_status(sandbox_item_set_verification_status_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_item_set_verification_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_item_set_verification_status_request** | [**SandboxItemSetVerificationStatusRequest**](SandboxItemSetVerificationStatusRequest.md)|  |

### Return type

[**SandboxItemSetVerificationStatusResponse**](SandboxItemSetVerificationStatusResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_oauth_select_accounts**
> SandboxOauthSelectAccountsResponse sandbox_oauth_select_accounts(sandbox_oauth_select_accounts_request)

Save the selected accounts when connecting to the Platypus Oauth institution

Save the selected accounts when connecting to the Platypus Oauth institution

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_oauth_select_accounts_response import SandboxOauthSelectAccountsResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_oauth_select_accounts_request import SandboxOauthSelectAccountsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_oauth_select_accounts_request = SandboxOauthSelectAccountsRequest(
        oauth_state_id="oauth_state_id_example",
        accounts=[
            "accounts_example",
        ],
    ) # SandboxOauthSelectAccountsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Save the selected accounts when connecting to the Platypus Oauth institution
        api_response = api_instance.sandbox_oauth_select_accounts(sandbox_oauth_select_accounts_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_oauth_select_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_oauth_select_accounts_request** | [**SandboxOauthSelectAccountsRequest**](SandboxOauthSelectAccountsRequest.md)|  |

### Return type

[**SandboxOauthSelectAccountsResponse**](SandboxOauthSelectAccountsResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_payment_profile_reset_login**
> SandboxPaymentProfileResetLoginResponse sandbox_payment_profile_reset_login(sandbox_payment_profile_reset_login_request)

Reset the login of a Payment Profile

`/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.   After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.   In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_payment_profile_reset_login_request import SandboxPaymentProfileResetLoginRequest
from plaid.model.sandbox_payment_profile_reset_login_response import SandboxPaymentProfileResetLoginResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_payment_profile_reset_login_request = SandboxPaymentProfileResetLoginRequest(
        client_id="client_id_example",
        secret="secret_example",
        payment_profile_token="payment_profile_token_example",
    ) # SandboxPaymentProfileResetLoginRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Reset the login of a Payment Profile
        api_response = api_instance.sandbox_payment_profile_reset_login(sandbox_payment_profile_reset_login_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_payment_profile_reset_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_payment_profile_reset_login_request** | [**SandboxPaymentProfileResetLoginRequest**](SandboxPaymentProfileResetLoginRequest.md)|  |

### Return type

[**SandboxPaymentProfileResetLoginResponse**](SandboxPaymentProfileResetLoginResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_processor_token_create**
> SandboxProcessorTokenCreateResponse sandbox_processor_token_create(sandbox_processor_token_create_request)

Create a test Item and processor token

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_processor_token_create_response import SandboxProcessorTokenCreateResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_processor_token_create_request import SandboxProcessorTokenCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_processor_token_create_request = SandboxProcessorTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        institution_id="institution_id_example",
        options=SandboxProcessorTokenCreateRequestOptions(
            override_username="user_good",
            override_password="pass_good",
        ),
    ) # SandboxProcessorTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a test Item and processor token
        api_response = api_instance.sandbox_processor_token_create(sandbox_processor_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_processor_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_processor_token_create_request** | [**SandboxProcessorTokenCreateRequest**](SandboxProcessorTokenCreateRequest.md)|  |

### Return type

[**SandboxProcessorTokenCreateResponse**](SandboxProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_public_token_create**
> SandboxPublicTokenCreateResponse sandbox_public_token_create(sandbox_public_token_create_request)

Create a test Item

Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_response import SandboxPublicTokenCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_public_token_create_request = SandboxPublicTokenCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        institution_id="institution_id_example",
        initial_products=[
            Products("assets"),
        ],
        options=SandboxPublicTokenCreateRequestOptions(
            webhook="webhook_example",
            override_username="user_good",
            override_password="pass_good",
            transactions=SandboxPublicTokenCreateRequestOptionsTransactions(
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
            ),
            income_verification=SandboxPublicTokenCreateRequestOptionsIncomeVerification(
                income_source_types=[
                    IncomeVerificationSourceType("bank"),
                ],
                bank_income=SandboxPublicTokenCreateRequestIncomeVerificationBankIncome(
                    days_requested=1,
                ),
            ),
        ),
        user_token="user_token_example",
    ) # SandboxPublicTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a test Item
        api_response = api_instance.sandbox_public_token_create(sandbox_public_token_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_public_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_public_token_create_request** | [**SandboxPublicTokenCreateRequest**](SandboxPublicTokenCreateRequest.md)|  |

### Return type

[**SandboxPublicTokenCreateResponse**](SandboxPublicTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_fire_webhook**
> SandboxTransferFireWebhookResponse sandbox_transfer_fire_webhook(sandbox_transfer_fire_webhook_request)

Manually fire a Transfer webhook

Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_fire_webhook_request import SandboxTransferFireWebhookRequest
from plaid.model.sandbox_transfer_fire_webhook_response import SandboxTransferFireWebhookResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_fire_webhook_request = SandboxTransferFireWebhookRequest(
        client_id="client_id_example",
        secret="secret_example",
        webhook="webhook_example",
    ) # SandboxTransferFireWebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Manually fire a Transfer webhook
        api_response = api_instance.sandbox_transfer_fire_webhook(sandbox_transfer_fire_webhook_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_fire_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_fire_webhook_request** | [**SandboxTransferFireWebhookRequest**](SandboxTransferFireWebhookRequest.md)|  |

### Return type

[**SandboxTransferFireWebhookResponse**](SandboxTransferFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_repayment_simulate**
> SandboxTransferRepaymentSimulateResponse sandbox_transfer_repayment_simulate(sandbox_transfer_repayment_simulate_request)

Trigger the creation of a repayment

Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_repayment_simulate_response import SandboxTransferRepaymentSimulateResponse
from plaid.model.sandbox_transfer_repayment_simulate_request import SandboxTransferRepaymentSimulateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_repayment_simulate_request = SandboxTransferRepaymentSimulateRequest(
        client_id="client_id_example",
        secret="secret_example",
    ) # SandboxTransferRepaymentSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger the creation of a repayment
        api_response = api_instance.sandbox_transfer_repayment_simulate(sandbox_transfer_repayment_simulate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_repayment_simulate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_repayment_simulate_request** | [**SandboxTransferRepaymentSimulateRequest**](SandboxTransferRepaymentSimulateRequest.md)|  |

### Return type

[**SandboxTransferRepaymentSimulateResponse**](SandboxTransferRepaymentSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_simulate**
> SandboxTransferSimulateResponse sandbox_transfer_simulate(sandbox_transfer_simulate_request)

Simulate a transfer event in Sandbox

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_simulate_request import SandboxTransferSimulateRequest
from plaid.model.sandbox_transfer_simulate_response import SandboxTransferSimulateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_simulate_request = SandboxTransferSimulateRequest(
        client_id="client_id_example",
        secret="secret_example",
        transfer_id="transfer_id_example",
        test_clock_id="test_clock_id_example",
        event_type="event_type_example",
        failure_reason=TransferFailure(),
    ) # SandboxTransferSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Simulate a transfer event in Sandbox
        api_response = api_instance.sandbox_transfer_simulate(sandbox_transfer_simulate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_simulate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_simulate_request** | [**SandboxTransferSimulateRequest**](SandboxTransferSimulateRequest.md)|  |

### Return type

[**SandboxTransferSimulateResponse**](SandboxTransferSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_sweep_simulate**
> SandboxTransferSweepSimulateResponse sandbox_transfer_sweep_simulate(sandbox_transfer_sweep_simulate_request)

Simulate creating a sweep

Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_sweep_simulate_response import SandboxTransferSweepSimulateResponse
from plaid.model.sandbox_transfer_sweep_simulate_request import SandboxTransferSweepSimulateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_sweep_simulate_request = SandboxTransferSweepSimulateRequest(
        client_id="client_id_example",
        secret="secret_example",
        test_clock_id="test_clock_id_example",
    ) # SandboxTransferSweepSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Simulate creating a sweep
        api_response = api_instance.sandbox_transfer_sweep_simulate(sandbox_transfer_sweep_simulate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_sweep_simulate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_sweep_simulate_request** | [**SandboxTransferSweepSimulateRequest**](SandboxTransferSweepSimulateRequest.md)|  |

### Return type

[**SandboxTransferSweepSimulateResponse**](SandboxTransferSweepSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_test_clock_advance**
> SandboxTransferTestClockAdvanceResponse sandbox_transfer_test_clock_advance(sandbox_transfer_test_clock_advance_request)

Advance a test clock

Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.  A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.  If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed. For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.  The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`. For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_test_clock_advance_request import SandboxTransferTestClockAdvanceRequest
from plaid.model.sandbox_transfer_test_clock_advance_response import SandboxTransferTestClockAdvanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_test_clock_advance_request = SandboxTransferTestClockAdvanceRequest(
        client_id="client_id_example",
        secret="secret_example",
        test_clock_id="test_clock_id_example",
        new_virtual_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # SandboxTransferTestClockAdvanceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Advance a test clock
        api_response = api_instance.sandbox_transfer_test_clock_advance(sandbox_transfer_test_clock_advance_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_test_clock_advance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_test_clock_advance_request** | [**SandboxTransferTestClockAdvanceRequest**](SandboxTransferTestClockAdvanceRequest.md)|  |

### Return type

[**SandboxTransferTestClockAdvanceResponse**](SandboxTransferTestClockAdvanceResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_test_clock_create**
> SandboxTransferTestClockCreateResponse sandbox_transfer_test_clock_create(sandbox_transfer_test_clock_create_request)

Create a test clock

Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.  A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.  A test clock can be associated with up to 5 recurring transfers.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_test_clock_create_request import SandboxTransferTestClockCreateRequest
from plaid.model.sandbox_transfer_test_clock_create_response import SandboxTransferTestClockCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_test_clock_create_request = SandboxTransferTestClockCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        virtual_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # SandboxTransferTestClockCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a test clock
        api_response = api_instance.sandbox_transfer_test_clock_create(sandbox_transfer_test_clock_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_test_clock_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_test_clock_create_request** | [**SandboxTransferTestClockCreateRequest**](SandboxTransferTestClockCreateRequest.md)|  |

### Return type

[**SandboxTransferTestClockCreateResponse**](SandboxTransferTestClockCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_test_clock_get**
> SandboxTransferTestClockGetResponse sandbox_transfer_test_clock_get(sandbox_transfer_test_clock_get_request)

Get a test clock

Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_transfer_test_clock_get_request import SandboxTransferTestClockGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_test_clock_get_response import SandboxTransferTestClockGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_test_clock_get_request = SandboxTransferTestClockGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        test_clock_id="test_clock_id_example",
    ) # SandboxTransferTestClockGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get a test clock
        api_response = api_instance.sandbox_transfer_test_clock_get(sandbox_transfer_test_clock_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_test_clock_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_test_clock_get_request** | [**SandboxTransferTestClockGetRequest**](SandboxTransferTestClockGetRequest.md)|  |

### Return type

[**SandboxTransferTestClockGetResponse**](SandboxTransferTestClockGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_transfer_test_clock_list**
> SandboxTransferTestClockListResponse sandbox_transfer_test_clock_list(sandbox_transfer_test_clock_list_request)

List test clocks

Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.sandbox_transfer_test_clock_list_response import SandboxTransferTestClockListResponse
from plaid.model.sandbox_transfer_test_clock_list_request import SandboxTransferTestClockListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    sandbox_transfer_test_clock_list_request = SandboxTransferTestClockListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_virtual_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_virtual_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
    ) # SandboxTransferTestClockListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List test clocks
        api_response = api_instance.sandbox_transfer_test_clock_list(sandbox_transfer_test_clock_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->sandbox_transfer_test_clock_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_transfer_test_clock_list_request** | [**SandboxTransferTestClockListRequest**](SandboxTransferTestClockListRequest.md)|  |

### Return type

[**SandboxTransferTestClockListResponse**](SandboxTransferTestClockListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_decision_report**
> SignalDecisionReportResponse signal_decision_report(signal_decision_report_request)

Report whether you initiated an ACH transaction

After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.signal_decision_report_response import SignalDecisionReportResponse
from plaid.model.signal_decision_report_request import SignalDecisionReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    signal_decision_report_request = SignalDecisionReportRequest(
        client_id="client_id_example",
        secret="secret_example",
        client_transaction_id="client_transaction_id_example",
        initiated=True,
        days_funds_on_hold=0,
        decision_outcome=SignalDecisionOutcome("APPROVE"),
        payment_method=SignalPaymentMethod("SAME_DAY_ACH"),
        amount_instantly_available=3.14,
    ) # SignalDecisionReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Report whether you initiated an ACH transaction
        api_response = api_instance.signal_decision_report(signal_decision_report_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->signal_decision_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_decision_report_request** | [**SignalDecisionReportRequest**](SignalDecisionReportRequest.md)|  |

### Return type

[**SignalDecisionReportResponse**](SignalDecisionReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_evaluate**
> SignalEvaluateResponse signal_evaluate(signal_evaluate_request)

Evaluate a planned ACH transaction

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.  In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).  Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.signal_evaluate_response import SignalEvaluateResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.signal_evaluate_request import SignalEvaluateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    signal_evaluate_request = SignalEvaluateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
        client_transaction_id="client_transaction_id_example",
        amount=3.14,
        user_present=True,
        client_user_id="client_user_id_example",
        is_recurring=True,
        default_payment_method="default_payment_method_example",
        user=SignalUser(
            name=SignalPersonName(
                prefix="prefix_example",
                given_name="given_name_example",
                middle_name="middle_name_example",
                family_name="family_name_example",
                suffix="suffix_example",
            ),
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=SignalAddressData(),
        ),
        device=SignalDevice(
            ip_address="ip_address_example",
            user_agent="user_agent_example",
        ),
    ) # SignalEvaluateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Evaluate a planned ACH transaction
        api_response = api_instance.signal_evaluate(signal_evaluate_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->signal_evaluate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_evaluate_request** | [**SignalEvaluateRequest**](SignalEvaluateRequest.md)|  |

### Return type

[**SignalEvaluateResponse**](SignalEvaluateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_prepare**
> SignalPrepareResponse signal_prepare(signal_prepare_request)

Opt-in an Item to Signal

When Link is not initialized with Signal, call `/signal/prepare` to opt-in that Item to the Signal data collection process, developing a Signal score.  If you are using other Plaid products after Link, e.g. Identity or Assets, call `/signal/prepare` after those product calls are complete.  Example flow: Link is initialized with Auth, call `/auth/get` for the account and routing number, call `/identity/get` to retrieve bank ownership details, then call `/signal/prepare` to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call `/signal/evaluate` for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.signal_prepare_response import SignalPrepareResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.signal_prepare_request import SignalPrepareRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    signal_prepare_request = SignalPrepareRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
    ) # SignalPrepareRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Opt-in an Item to Signal
        api_response = api_instance.signal_prepare(signal_prepare_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->signal_prepare: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_prepare_request** | [**SignalPrepareRequest**](SignalPrepareRequest.md)|  |

### Return type

[**SignalPrepareResponse**](SignalPrepareResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_return_report**
> SignalReturnReportResponse signal_return_report(signal_return_report_request)

Report a return for an ACH transaction

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.signal_return_report_response import SignalReturnReportResponse
from plaid.model.signal_return_report_request import SignalReturnReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    signal_return_report_request = SignalReturnReportRequest(
        client_id="client_id_example",
        secret="secret_example",
        client_transaction_id="client_transaction_id_example",
        return_code="return_code_example",
        returned_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # SignalReturnReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Report a return for an ACH transaction
        api_response = api_instance.signal_return_report(signal_return_report_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->signal_return_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_return_report_request** | [**SignalReturnReportRequest**](SignalReturnReportRequest.md)|  |

### Return type

[**SignalReturnReportResponse**](SignalReturnReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statements_download**
> file_type statements_download(statements_download_request)

Retrieve a single statement.

The `/statements/download` endpoint retrieves a single statement.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.statements_download_request import StatementsDownloadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    statements_download_request = StatementsDownloadRequest(
        access_token="access_token_example",
        client_id="client_id_example",
        secret="secret_example",
        statement_id="statement_id_example",
    ) # StatementsDownloadRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single statement.
        api_response = api_instance.statements_download(statements_download_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->statements_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statements_download_request** | [**StatementsDownloadRequest**](StatementsDownloadRequest.md)|  |

### Return type

**file_type**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statements_list**
> StatementsListResponse statements_list(statements_list_request)

Retrieve a list of all statements associated with the provided item.

The `/statements/list` endpoint retrieves a list of all statements associated with the provided item.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.statements_list_request import StatementsListRequest
from plaid.model.statements_list_response import StatementsListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    statements_list_request = StatementsListRequest(
        access_token="access_token_example",
        client_id="client_id_example",
        secret="secret_example",
    ) # StatementsListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of all statements associated with the provided item.
        api_response = api_instance.statements_list(statements_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->statements_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statements_list_request** | [**StatementsListRequest**](StatementsListRequest.md)|  |

### Return type

[**StatementsListResponse**](StatementsListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_enhance**
> TransactionsEnhanceGetResponse transactions_enhance(transactions_enhance_get_request)

enhance locally-held transaction data

The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.  The product is currently in beta.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_enhance_get_response import TransactionsEnhanceGetResponse
from plaid.model.transactions_enhance_get_request import TransactionsEnhanceGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_enhance_get_request = TransactionsEnhanceGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        account_type="account_type_example",
        transactions=[
            ClientProvidedRawTransaction(),
        ],
    ) # TransactionsEnhanceGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # enhance locally-held transaction data
        api_response = api_instance.transactions_enhance(transactions_enhance_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_enhance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_enhance_get_request** | [**TransactionsEnhanceGetRequest**](TransactionsEnhanceGetRequest.md)|  |

### Return type

[**TransactionsEnhanceGetResponse**](TransactionsEnhanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_enrich**
> TransactionsEnrichGetResponse transactions_enrich(transactions_enrich_get_request)

Enrich locally-held transaction data

The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transactions_enrich_get_response import TransactionsEnrichGetResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_enrich_get_request import TransactionsEnrichGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_enrich_get_request = TransactionsEnrichGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        account_type="account_type_example",
        transactions=[
            ClientProvidedTransaction(),
        ],
        options=TransactionsEnrichRequestOptions(
            include_legacy_category=False,
        ),
    ) # TransactionsEnrichGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Enrich locally-held transaction data
        api_response = api_instance.transactions_enrich(transactions_enrich_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_enrich: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_enrich_get_request** | [**TransactionsEnrichGetRequest**](TransactionsEnrichGetRequest.md)|  |

### Return type

[**TransactionsEnrichGetResponse**](TransactionsEnrichGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> TransactionsGetResponse transactions_get(transactions_get_request)

Get transaction data

Note: All new implementations are encouraged to use `/transactions/sync` rather than `/transactions/get`. `/transactions/sync` provides the same functionality as `/transactions/get` and improves developer ease-of-use for handling transactions updates.  The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.  Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).  Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.  Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.  Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_response import TransactionsGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_get_request = TransactionsGetRequest(
        client_id="client_id_example",
        options=TransactionsGetRequestOptions(
            account_ids=[
                "account_ids_example",
            ],
            count=100,
            offset=0,
            include_original_description=False,
            include_personal_finance_category_beta=False,
            include_personal_finance_category=False,
            include_logo_and_counterparty_beta=False,
        ),
        access_token="access_token_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01').date(),
        end_date=dateutil_parser('1970-01-01').date(),
    ) # TransactionsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get transaction data
        api_response = api_instance.transactions_get(transactions_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_get_request** | [**TransactionsGetRequest**](TransactionsGetRequest.md)|  |

### Return type

[**TransactionsGetResponse**](TransactionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_recurring_get**
> TransactionsRecurringGetResponse transactions_recurring_get(transactions_recurring_get_request)

Fetch recurring transaction streams

The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.  This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.  This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`). Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.  After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_recurring_get_request import TransactionsRecurringGetRequest
from plaid.model.transactions_recurring_get_response import TransactionsRecurringGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_recurring_get_request = TransactionsRecurringGetRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
        options=TransactionsRecurringGetRequestOptions(
            include_personal_finance_category=False,
        ),
        account_ids=[
            "account_ids_example",
        ],
    ) # TransactionsRecurringGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch recurring transaction streams
        api_response = api_instance.transactions_recurring_get(transactions_recurring_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_recurring_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_recurring_get_request** | [**TransactionsRecurringGetRequest**](TransactionsRecurringGetRequest.md)|  |

### Return type

[**TransactionsRecurringGetResponse**](TransactionsRecurringGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_refresh**
> TransactionsRefreshResponse transactions_refresh(transactions_refresh_request)

Refresh transaction data

`/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`. Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.  `/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_refresh_response import TransactionsRefreshResponse
from plaid.model.transactions_refresh_request import TransactionsRefreshRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_refresh_request = TransactionsRefreshRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
    ) # TransactionsRefreshRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh transaction data
        api_response = api_instance.transactions_refresh(transactions_refresh_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_refresh_request** | [**TransactionsRefreshRequest**](TransactionsRefreshRequest.md)|  |

### Return type

[**TransactionsRefreshResponse**](TransactionsRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_rules_create**
> TransactionsRulesCreateResponse transactions_rules_create(transactions_rules_create_request)

Create transaction category rule

The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.  Rules will be applied on the Item's transactions returned in `/transactions/get` response.  The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transactions_rules_create_request import TransactionsRulesCreateRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_rules_create_response import TransactionsRulesCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_rules_create_request = TransactionsRulesCreateRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
        personal_finance_category="personal_finance_category_example",
        rule_details=TransactionsRuleDetails(
            field=TransactionsRuleField("TRANSACTION_ID"),
            type=TransactionsRuleType("EXACT_MATCH"),
            query="query_example",
        ),
    ) # TransactionsRulesCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create transaction category rule
        api_response = api_instance.transactions_rules_create(transactions_rules_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_rules_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_rules_create_request** | [**TransactionsRulesCreateRequest**](TransactionsRulesCreateRequest.md)|  |

### Return type

[**TransactionsRulesCreateResponse**](TransactionsRulesCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_rules_list**
> TransactionsRulesListResponse transactions_rules_list(transactions_rules_list_request)

Return a list of rules created for the Item associated with the access token.

The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_rules_list_request import TransactionsRulesListRequest
from plaid.model.transactions_rules_list_response import TransactionsRulesListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_rules_list_request = TransactionsRulesListRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
    ) # TransactionsRulesListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Return a list of rules created for the Item associated with the access token.
        api_response = api_instance.transactions_rules_list(transactions_rules_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_rules_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_rules_list_request** | [**TransactionsRulesListRequest**](TransactionsRulesListRequest.md)|  |

### Return type

[**TransactionsRulesListResponse**](TransactionsRulesListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_rules_remove**
> TransactionsRulesRemoveResponse transactions_rules_remove(transactions_rules_remove_request)

Remove transaction rule

The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_rules_remove_response import TransactionsRulesRemoveResponse
from plaid.model.transactions_rules_remove_request import TransactionsRulesRemoveRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_rules_remove_request = TransactionsRulesRemoveRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
        rule_id="rule_id_example",
    ) # TransactionsRulesRemoveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Remove transaction rule
        api_response = api_instance.transactions_rules_remove(transactions_rules_remove_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_rules_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_rules_remove_request** | [**TransactionsRulesRemoveRequest**](TransactionsRulesRemoveRequest.md)|  |

### Return type

[**TransactionsRulesRemoveResponse**](TransactionsRulesRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_sync**
> TransactionsSyncResponse transactions_sync(transactions_sync_request)

Get incremental transaction updates on an Item

This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.  The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.  This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.  Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.  In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as \"adds\"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.  Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.  When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails due to the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.  Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.  Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.  To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transactions_sync_response import TransactionsSyncResponse
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transactions_sync_request = TransactionsSyncRequest(
        client_id="client_id_example",
        access_token="access_token_example",
        secret="secret_example",
        cursor="cursor_example",
        count=100,
        options=TransactionsSyncRequestOptions(
            include_original_description=False,
            include_personal_finance_category=False,
            include_logo_and_counterparty_beta=False,
        ),
    ) # TransactionsSyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get incremental transaction updates on an Item
        api_response = api_instance.transactions_sync(transactions_sync_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transactions_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_sync_request** | [**TransactionsSyncRequest**](TransactionsSyncRequest.md)|  |

### Return type

[**TransactionsSyncResponse**](TransactionsSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_authorization_create**
> TransferAuthorizationCreateResponse transfer_authorization_create(transfer_authorization_create_request)

Create a transfer authorization

Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.  In Plaid's Sandbox environment the decisions will be returned as follows:    - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.    - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).    - To approve a transfer with the rationale code `ITEM_LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).    - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.    - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.  The fields `device.ip_address` and `device.user_agent` are required for all sessions where the end-user is present. For example, when a user is authorizing a one-time payment from their device.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_authorization_create_response import TransferAuthorizationCreateResponse
from plaid.model.transfer_authorization_create_request import TransferAuthorizationCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_authorization_create_request = TransferAuthorizationCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
        funding_account_id="funding_account_id_example",
        payment_profile_token="payment_profile_token_example",
        type=TransferType("debit"),
        network=TransferNetwork("ach"),
        amount="amount_example",
        ach_class=ACHClass("ccd"),
        user=TransferAuthorizationUserInRequest(
            legal_name="legal_name_example",
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=TransferUserAddressInRequest(
                street="street_example",
                city="city_example",
                region="region_example",
                postal_code="postal_code_example",
                country="country_example",
            ),
        ),
        device=TransferAuthorizationDevice(),
        origination_account_id="origination_account_id_example",
        iso_currency_code="iso_currency_code_example",
        idempotency_key=TransferAuthorizationIdempotencyKey("idempotency_key_example"),
        user_present=True,
        with_guarantee=True,
        beacon_session_id="beacon_session_id_example",
        originator_client_id="originator_client_id_example",
        credit_funds_source=TransferCreditFundsSource("sweep"),
        test_clock_id="test_clock_id_example",
    ) # TransferAuthorizationCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a transfer authorization
        api_response = api_instance.transfer_authorization_create(transfer_authorization_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_authorization_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_authorization_create_request** | [**TransferAuthorizationCreateRequest**](TransferAuthorizationCreateRequest.md)|  |

### Return type

[**TransferAuthorizationCreateResponse**](TransferAuthorizationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_balance_get**
> TransferBalanceGetResponse transfer_balance_get(transfer_balance_get_request)

Retrieve a balance held with Plaid

Use the `/transfer/balance/get` endpoint to view a balance held with Plaid.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_balance_get_request import TransferBalanceGetRequest
from plaid.model.transfer_balance_get_response import TransferBalanceGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_balance_get_request = TransferBalanceGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        type=TransferBalanceType("prefunded_rtp_credits"),
    ) # TransferBalanceGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a balance held with Plaid
        api_response = api_instance.transfer_balance_get(transfer_balance_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_balance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_balance_get_request** | [**TransferBalanceGetRequest**](TransferBalanceGetRequest.md)|  |

### Return type

[**TransferBalanceGetResponse**](TransferBalanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_cancel**
> TransferCancelResponse transfer_cancel(transfer_cancel_request)

Cancel a transfer

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_cancel_request import TransferCancelRequest
from plaid.model.transfer_cancel_response import TransferCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_cancel_request = TransferCancelRequest(
        client_id="client_id_example",
        secret="secret_example",
        transfer_id="transfer_id_example",
        originator_client_id="originator_client_id_example",
    ) # TransferCancelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a transfer
        api_response = api_instance.transfer_cancel(transfer_cancel_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_cancel_request** | [**TransferCancelRequest**](TransferCancelRequest.md)|  |

### Return type

[**TransferCancelResponse**](TransferCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_capabilities_get**
> TransferCapabilitiesGetResponse transfer_capabilities_get(transfer_capabilities_get_request)

Get RTP eligibility information of a transfer

Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of a transfer.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_capabilities_get_response import TransferCapabilitiesGetResponse
from plaid.model.transfer_capabilities_get_request import TransferCapabilitiesGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_capabilities_get_request = TransferCapabilitiesGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        account_id="account_id_example",
        payment_profile_token="payment_profile_token_example",
    ) # TransferCapabilitiesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get RTP eligibility information of a transfer
        api_response = api_instance.transfer_capabilities_get(transfer_capabilities_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_capabilities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_capabilities_get_request** | [**TransferCapabilitiesGetRequest**](TransferCapabilitiesGetRequest.md)|  |

### Return type

[**TransferCapabilitiesGetResponse**](TransferCapabilitiesGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_configuration_get**
> TransferConfigurationGetResponse transfer_configuration_get(transfer_configuration_get_request)

Get transfer product configuration

Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_configuration_get_request import TransferConfigurationGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_configuration_get_response import TransferConfigurationGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_configuration_get_request = TransferConfigurationGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        originator_client_id="originator_client_id_example",
    ) # TransferConfigurationGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get transfer product configuration
        api_response = api_instance.transfer_configuration_get(transfer_configuration_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_configuration_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_configuration_get_request** | [**TransferConfigurationGetRequest**](TransferConfigurationGetRequest.md)|  |

### Return type

[**TransferConfigurationGetResponse**](TransferConfigurationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_create**
> TransferCreateResponse transfer_create(transfer_create_request)

Create a transfer

Use the `/transfer/create` endpoint to initiate a new transfer.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_create_response import TransferCreateResponse
from plaid.model.transfer_create_request import TransferCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_create_request = TransferCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        idempotency_key=TransferCreateIdempotencyKey("idempotency_key_example"),
        access_token="access_token_example",
        account_id="account_id_example",
        payment_profile_token="payment_profile_token_example",
        authorization_id="authorization_id_example",
        type=None,
        network=None,
        amount="amount_example",
        description="description_example",
        ach_class=None,
        user=TransferUserInRequestDeprecated(
            legal_name="legal_name_example",
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=TransferUserAddressInRequest(
                street="street_example",
                city="city_example",
                region="region_example",
                postal_code="postal_code_example",
                country="country_example",
            ),
        ),
        metadata=TransferMetadata(
            key="key_example",
        ),
        origination_account_id="origination_account_id_example",
        iso_currency_code="iso_currency_code_example",
        test_clock_id="test_clock_id_example",
    ) # TransferCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a transfer
        api_response = api_instance.transfer_create(transfer_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_create_request** | [**TransferCreateRequest**](TransferCreateRequest.md)|  |

### Return type

[**TransferCreateResponse**](TransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_diligence_document_upload**
> TransferDiligenceDocumentUploadResponse transfer_diligence_document_upload(transfer_diligence_document_upload_request)

This endpoint allows third-party sender customers to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.

Third-party sender customers can use `/transfer/diligence/document/upload` endpoint to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data. You must provide the `client_id` in the `PLAID-CLIENT-ID` header and `secret` in the `PLAID-SECRET` header.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_diligence_document_upload_response import TransferDiligenceDocumentUploadResponse
from plaid.model.transfer_diligence_document_upload_request import TransferDiligenceDocumentUploadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_diligence_document_upload_request = TransferDiligenceDocumentUploadRequest(
        originator_client_id="originator_client_id_example",
        file=open('/path/to/file', 'rb'),
        purpose=TransferDocumentPurpose("DUE_DILIGENCE"),
    ) # TransferDiligenceDocumentUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        # This endpoint allows third-party sender customers to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.
        api_response = api_instance.transfer_diligence_document_upload(transfer_diligence_document_upload_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_diligence_document_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_diligence_document_upload_request** | [**TransferDiligenceDocumentUploadRequest**](TransferDiligenceDocumentUploadRequest.md)|  |

### Return type

[**TransferDiligenceDocumentUploadResponse**](TransferDiligenceDocumentUploadResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_diligence_submit**
> TransferDiligenceSubmitResponse transfer_diligence_submit(transfer_diligence_submit_request)

Submit transfer diligence on behalf of the end customer (i.e. the originator).

Use the `/transfer/diligence/submit` endpoint to submit transfer diligence on behalf of the originator.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_diligence_submit_request import TransferDiligenceSubmitRequest
from plaid.model.transfer_diligence_submit_response import TransferDiligenceSubmitResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_diligence_submit_request = TransferDiligenceSubmitRequest(
        client_id="client_id_example",
        secret="secret_example",
        originator_client_id="originator_client_id_example",
        originator_diligence=TransferOriginatorDiligence(
            dba="dba_example",
            tax_id="tax_id_example",
            credit_usage_configuration=TransferCreditUsageConfiguration(
                expected_frequency=OriginatorExpectedTransferFrequency("once_per_month"),
                expected_highest_amount="expected_highest_amount_example",
                expected_average_amount="expected_average_amount_example",
                expected_monthly_amount="expected_monthly_amount_example",
                sec_codes=[
                    CreditACHClass("ccd"),
                ],
            ),
            debit_usage_configuration=TransferDebitUsageConfiguration(
                expected_frequency=OriginatorExpectedTransferFrequency("once_per_month"),
                expected_highest_amount="expected_highest_amount_example",
                expected_average_amount="expected_average_amount_example",
                expected_monthly_amount="expected_monthly_amount_example",
                sec_codes=[
                    ACHClass("ccd"),
                ],
            ),
            address=TransferOriginatorAddress(
                city="city_example",
                street="street_example",
                region="region_example",
                postal_code="postal_code_example",
                country_code="country_code_example",
            ),
            website="website_example",
            naics_code="naics_code_example",
        ),
    ) # TransferDiligenceSubmitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Submit transfer diligence on behalf of the end customer (i.e. the originator).
        api_response = api_instance.transfer_diligence_submit(transfer_diligence_submit_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_diligence_submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_diligence_submit_request** | [**TransferDiligenceSubmitRequest**](TransferDiligenceSubmitRequest.md)|  |

### Return type

[**TransferDiligenceSubmitResponse**](TransferDiligenceSubmitResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_event_list**
> TransferEventListResponse transfer_event_list(transfer_event_list_request)

List transfer events

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_event_list_response import TransferEventListResponse
from plaid.model.transfer_event_list_request import TransferEventListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_event_list_request = TransferEventListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        transfer_id="transfer_id_example",
        account_id="account_id_example",
        transfer_type=TransferEventListTransferType("debit"),
        event_types=[
            TransferEventType("pending"),
        ],
        sweep_id="sweep_id_example",
        count=25,
        offset=0,
        origination_account_id="origination_account_id_example",
        originator_client_id="originator_client_id_example",
        funding_account_id="funding_account_id_example",
    ) # TransferEventListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List transfer events
        api_response = api_instance.transfer_event_list(transfer_event_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_event_list_request** | [**TransferEventListRequest**](TransferEventListRequest.md)|  |

### Return type

[**TransferEventListResponse**](TransferEventListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_event_sync**
> TransferEventSyncResponse transfer_event_sync(transfer_event_sync_request)

Sync transfer events

`/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_event_sync_request import TransferEventSyncRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_event_sync_response import TransferEventSyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_event_sync_request = TransferEventSyncRequest(
        client_id="client_id_example",
        secret="secret_example",
        after_id=0,
        count=25,
    ) # TransferEventSyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sync transfer events
        api_response = api_instance.transfer_event_sync(transfer_event_sync_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_event_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_event_sync_request** | [**TransferEventSyncRequest**](TransferEventSyncRequest.md)|  |

### Return type

[**TransferEventSyncResponse**](TransferEventSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_get**
> TransferGetResponse transfer_get(transfer_get_request)

Retrieve a transfer

The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_get_request import TransferGetRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_get_response import TransferGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_get_request = TransferGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        transfer_id="transfer_id_example",
        originator_client_id="originator_client_id_example",
    ) # TransferGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a transfer
        api_response = api_instance.transfer_get(transfer_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_get_request** | [**TransferGetRequest**](TransferGetRequest.md)|  |

### Return type

[**TransferGetResponse**](TransferGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_intent_create**
> TransferIntentCreateResponse transfer_intent_create(transfer_intent_create_request)

Create a transfer intent object to invoke the Transfer UI

Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_intent_create_request import TransferIntentCreateRequest
from plaid.model.transfer_intent_create_response import TransferIntentCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_intent_create_request = TransferIntentCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        account_id="account_id_example",
        funding_account_id="funding_account_id_example",
        mode=TransferIntentCreateMode("PAYMENT"),
        network=TransferIntentCreateNetwork("same-day-ach"),
        amount="amount_example",
        description="description_example",
        ach_class=ACHClass("ccd"),
        origination_account_id="origination_account_id_example",
        user=TransferUserInRequest(
            legal_name="legal_name_example",
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=TransferUserAddressInRequest(
                street="street_example",
                city="city_example",
                region="region_example",
                postal_code="postal_code_example",
                country="country_example",
            ),
        ),
        metadata=TransferMetadata(
            key="key_example",
        ),
        iso_currency_code="iso_currency_code_example",
        require_guarantee=False,
    ) # TransferIntentCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a transfer intent object to invoke the Transfer UI
        api_response = api_instance.transfer_intent_create(transfer_intent_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_intent_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_intent_create_request** | [**TransferIntentCreateRequest**](TransferIntentCreateRequest.md)|  |

### Return type

[**TransferIntentCreateResponse**](TransferIntentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_intent_get**
> TransferIntentGetResponse transfer_intent_get(transfer_intent_get_request)

Retrieve more information about a transfer intent

Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_intent_get_request import TransferIntentGetRequest
from plaid.model.transfer_intent_get_response import TransferIntentGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_intent_get_request = TransferIntentGetRequest() # TransferIntentGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve more information about a transfer intent
        api_response = api_instance.transfer_intent_get(transfer_intent_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_intent_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_intent_get_request** | [**TransferIntentGetRequest**](TransferIntentGetRequest.md)|  |

### Return type

[**TransferIntentGetResponse**](TransferIntentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_list**
> TransferListResponse transfer_list(transfer_list_request)

List transfers

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_list_response import TransferListResponse
from plaid.model.transfer_list_request import TransferListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_list_request = TransferListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
        origination_account_id="origination_account_id_example",
        originator_client_id="originator_client_id_example",
        funding_account_id="funding_account_id_example",
    ) # TransferListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List transfers
        api_response = api_instance.transfer_list(transfer_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_list_request** | [**TransferListRequest**](TransferListRequest.md)|  |

### Return type

[**TransferListResponse**](TransferListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_metrics_get**
> TransferMetricsGetResponse transfer_metrics_get(transfer_metrics_get_request)

Get transfer product usage metrics

Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_metrics_get_response import TransferMetricsGetResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_metrics_get_request import TransferMetricsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_metrics_get_request = TransferMetricsGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        originator_client_id="originator_client_id_example",
    ) # TransferMetricsGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get transfer product usage metrics
        api_response = api_instance.transfer_metrics_get(transfer_metrics_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_metrics_get_request** | [**TransferMetricsGetRequest**](TransferMetricsGetRequest.md)|  |

### Return type

[**TransferMetricsGetResponse**](TransferMetricsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_migrate_account**
> TransferMigrateAccountResponse transfer_migrate_account(transfer_migrate_account_request)

Migrate account into Transfers

As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_migrate_account_response import TransferMigrateAccountResponse
from plaid.model.transfer_migrate_account_request import TransferMigrateAccountRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_migrate_account_request = TransferMigrateAccountRequest(
        client_id="client_id_example",
        secret="secret_example",
        account_number="account_number_example",
        routing_number="routing_number_example",
        wire_routing_number="wire_routing_number_example",
        account_type="account_type_example",
    ) # TransferMigrateAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Migrate account into Transfers
        api_response = api_instance.transfer_migrate_account(transfer_migrate_account_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_migrate_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_migrate_account_request** | [**TransferMigrateAccountRequest**](TransferMigrateAccountRequest.md)|  |

### Return type

[**TransferMigrateAccountResponse**](TransferMigrateAccountResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_originator_create**
> TransferOriginatorCreateResponse transfer_originator_create(transfer_originator_create_request)

Create a new originator

Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_originator_create_request import TransferOriginatorCreateRequest
from plaid.model.transfer_originator_create_response import TransferOriginatorCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_originator_create_request = TransferOriginatorCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        company_name="company_name_example",
    ) # TransferOriginatorCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new originator
        api_response = api_instance.transfer_originator_create(transfer_originator_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_originator_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_originator_create_request** | [**TransferOriginatorCreateRequest**](TransferOriginatorCreateRequest.md)|  |

### Return type

[**TransferOriginatorCreateResponse**](TransferOriginatorCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_originator_get**
> TransferOriginatorGetResponse transfer_originator_get(transfer_originator_get_request)

Get status of an originator's onboarding

The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_originator_get_response import TransferOriginatorGetResponse
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_originator_get_request import TransferOriginatorGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_originator_get_request = TransferOriginatorGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        originator_client_id="originator_client_id_example",
    ) # TransferOriginatorGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get status of an originator's onboarding
        api_response = api_instance.transfer_originator_get(transfer_originator_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_originator_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_originator_get_request** | [**TransferOriginatorGetRequest**](TransferOriginatorGetRequest.md)|  |

### Return type

[**TransferOriginatorGetResponse**](TransferOriginatorGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json, examples
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_originator_list**
> TransferOriginatorListResponse transfer_originator_list(transfer_originator_list_request)

Get status of all originators' onboarding

The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_originator_list_request import TransferOriginatorListRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_originator_list_response import TransferOriginatorListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_originator_list_request = TransferOriginatorListRequest(
        client_id="client_id_example",
        secret="secret_example",
        count=25,
        offset=0,
    ) # TransferOriginatorListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get status of all originators' onboarding
        api_response = api_instance.transfer_originator_list(transfer_originator_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_originator_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_originator_list_request** | [**TransferOriginatorListRequest**](TransferOriginatorListRequest.md)|  |

### Return type

[**TransferOriginatorListResponse**](TransferOriginatorListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_questionnaire_create**
> TransferQuestionnaireCreateResponse transfer_questionnaire_create(transfer_questionnaire_create_request)

Generate a Plaid-hosted onboarding UI URL.

The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_questionnaire_create_request import TransferQuestionnaireCreateRequest
from plaid.model.transfer_questionnaire_create_response import TransferQuestionnaireCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_questionnaire_create_request = TransferQuestionnaireCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        originator_client_id="originator_client_id_example",
        redirect_uri="redirect_uri_example",
    ) # TransferQuestionnaireCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate a Plaid-hosted onboarding UI URL.
        api_response = api_instance.transfer_questionnaire_create(transfer_questionnaire_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_questionnaire_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_questionnaire_create_request** | [**TransferQuestionnaireCreateRequest**](TransferQuestionnaireCreateRequest.md)|  |

### Return type

[**TransferQuestionnaireCreateResponse**](TransferQuestionnaireCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_recurring_cancel**
> TransferRecurringCancelResponse transfer_recurring_cancel(transfer_recurring_cancel_request)

Cancel a recurring transfer.

Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  Scheduled transfer that hasn't been submitted to bank will be cancelled.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_recurring_cancel_request import TransferRecurringCancelRequest
from plaid.model.transfer_recurring_cancel_response import TransferRecurringCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_recurring_cancel_request = TransferRecurringCancelRequest(
        client_id="client_id_example",
        secret="secret_example",
        recurring_transfer_id="recurring_transfer_id_example",
    ) # TransferRecurringCancelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a recurring transfer.
        api_response = api_instance.transfer_recurring_cancel(transfer_recurring_cancel_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_recurring_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_recurring_cancel_request** | [**TransferRecurringCancelRequest**](TransferRecurringCancelRequest.md)|  |

### Return type

[**TransferRecurringCancelResponse**](TransferRecurringCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_recurring_create**
> TransferRecurringCreateResponse transfer_recurring_create(transfer_recurring_create_request)

Create a recurring transfer

Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_recurring_create_request import TransferRecurringCreateRequest
from plaid.model.transfer_recurring_create_response import TransferRecurringCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_recurring_create_request = TransferRecurringCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        access_token="access_token_example",
        idempotency_key=TransferRecurringIdempotencyKey("idempotency_key_example"),
        account_id="account_id_example",
        funding_account_id="funding_account_id_example",
        type=TransferType("debit"),
        network=TransferNetwork("ach"),
        ach_class=ACHClass("ccd"),
        amount="amount_example",
        user_present=True,
        iso_currency_code="iso_currency_code_example",
        description="description_example",
        test_clock_id="test_clock_id_example",
        schedule=TransferRecurringSchedule(
            interval_unit=TransferScheduleIntervalUnit("week"),
            interval_count=1,
            interval_execution_day=1,
            start_date=dateutil_parser('1970-01-01').date(),
            end_date=dateutil_parser('1970-01-01').date(),
        ),
        user=TransferUserInRequest(
            legal_name="legal_name_example",
            phone_number="phone_number_example",
            email_address="email_address_example",
            address=TransferUserAddressInRequest(
                street="street_example",
                city="city_example",
                region="region_example",
                postal_code="postal_code_example",
                country="country_example",
            ),
        ),
        device=TransferDevice(),
    ) # TransferRecurringCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a recurring transfer
        api_response = api_instance.transfer_recurring_create(transfer_recurring_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_recurring_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_recurring_create_request** | [**TransferRecurringCreateRequest**](TransferRecurringCreateRequest.md)|  |

### Return type

[**TransferRecurringCreateResponse**](TransferRecurringCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_recurring_get**
> TransferRecurringGetResponse transfer_recurring_get(transfer_recurring_get_request)

Retrieve a recurring transfer

The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_recurring_get_response import TransferRecurringGetResponse
from plaid.model.transfer_recurring_get_request import TransferRecurringGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_recurring_get_request = TransferRecurringGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        recurring_transfer_id="recurring_transfer_id_example",
    ) # TransferRecurringGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a recurring transfer
        api_response = api_instance.transfer_recurring_get(transfer_recurring_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_recurring_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_recurring_get_request** | [**TransferRecurringGetRequest**](TransferRecurringGetRequest.md)|  |

### Return type

[**TransferRecurringGetResponse**](TransferRecurringGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_recurring_list**
> TransferRecurringListResponse transfer_recurring_list(transfer_recurring_list_request)

List recurring transfers

Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers. 

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_recurring_list_request import TransferRecurringListRequest
from plaid.model.transfer_recurring_list_response import TransferRecurringListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_recurring_list_request = TransferRecurringListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
        funding_account_id="funding_account_id_example",
    ) # TransferRecurringListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List recurring transfers
        api_response = api_instance.transfer_recurring_list(transfer_recurring_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_recurring_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_recurring_list_request** | [**TransferRecurringListRequest**](TransferRecurringListRequest.md)|  |

### Return type

[**TransferRecurringListResponse**](TransferRecurringListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_refund_cancel**
> TransferRefundCancelResponse transfer_refund_cancel(transfer_refund_cancel_request)

Cancel a refund

Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_refund_cancel_request import TransferRefundCancelRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_refund_cancel_response import TransferRefundCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_refund_cancel_request = TransferRefundCancelRequest(
        client_id="client_id_example",
        secret="secret_example",
        refund_id="refund_id_example",
    ) # TransferRefundCancelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a refund
        api_response = api_instance.transfer_refund_cancel(transfer_refund_cancel_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_refund_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_refund_cancel_request** | [**TransferRefundCancelRequest**](TransferRefundCancelRequest.md)|  |

### Return type

[**TransferRefundCancelResponse**](TransferRefundCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_refund_create**
> TransferRefundCreateResponse transfer_refund_create(transfer_refund_create_request)

Create a refund

Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.  Processing of the refund will not occur until at least 3 business days following the transfer's settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_refund_create_request import TransferRefundCreateRequest
from plaid.model.transfer_refund_create_response import TransferRefundCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_refund_create_request = TransferRefundCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        transfer_id="transfer_id_example",
        amount="amount_example",
        idempotency_key=TransferRefundIdempotencyKey("idempotency_key_example"),
    ) # TransferRefundCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a refund
        api_response = api_instance.transfer_refund_create(transfer_refund_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_refund_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_refund_create_request** | [**TransferRefundCreateRequest**](TransferRefundCreateRequest.md)|  |

### Return type

[**TransferRefundCreateResponse**](TransferRefundCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_refund_get**
> TransferRefundGetResponse transfer_refund_get(transfer_refund_get_request)

Retrieve a refund

The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_refund_get_response import TransferRefundGetResponse
from plaid.model.transfer_refund_get_request import TransferRefundGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_refund_get_request = TransferRefundGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        refund_id="refund_id_example",
    ) # TransferRefundGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a refund
        api_response = api_instance.transfer_refund_get(transfer_refund_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_refund_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_refund_get_request** | [**TransferRefundGetRequest**](TransferRefundGetRequest.md)|  |

### Return type

[**TransferRefundGetResponse**](TransferRefundGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_repayment_list**
> TransferRepaymentListResponse transfer_repayment_list(transfer_repayment_list_request)

Lists historical repayments

The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_repayment_list_request import TransferRepaymentListRequest
from plaid.model.transfer_repayment_list_response import TransferRepaymentListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_repayment_list_request = TransferRepaymentListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
    ) # TransferRepaymentListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Lists historical repayments
        api_response = api_instance.transfer_repayment_list(transfer_repayment_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_repayment_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_repayment_list_request** | [**TransferRepaymentListRequest**](TransferRepaymentListRequest.md)|  |

### Return type

[**TransferRepaymentListResponse**](TransferRepaymentListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_repayment_return_list**
> TransferRepaymentReturnListResponse transfer_repayment_return_list(transfer_repayment_return_list_request)

List the returns included in a repayment

The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_repayment_return_list_request import TransferRepaymentReturnListRequest
from plaid.model.transfer_repayment_return_list_response import TransferRepaymentReturnListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_repayment_return_list_request = TransferRepaymentReturnListRequest(
        client_id="client_id_example",
        secret="secret_example",
        repayment_id="repayment_id_example",
        count=25,
        offset=0,
    ) # TransferRepaymentReturnListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List the returns included in a repayment
        api_response = api_instance.transfer_repayment_return_list(transfer_repayment_return_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_repayment_return_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_repayment_return_list_request** | [**TransferRepaymentReturnListRequest**](TransferRepaymentReturnListRequest.md)|  |

### Return type

[**TransferRepaymentReturnListResponse**](TransferRepaymentReturnListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_sweep_get**
> TransferSweepGetResponse transfer_sweep_get(transfer_sweep_get_request)

Retrieve a sweep

The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_sweep_get_request import TransferSweepGetRequest
from plaid.model.transfer_sweep_get_response import TransferSweepGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_sweep_get_request = TransferSweepGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        sweep_id="sweep_id_example",
    ) # TransferSweepGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a sweep
        api_response = api_instance.transfer_sweep_get(transfer_sweep_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_sweep_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_sweep_get_request** | [**TransferSweepGetRequest**](TransferSweepGetRequest.md)|  |

### Return type

[**TransferSweepGetResponse**](TransferSweepGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_sweep_list**
> TransferSweepListResponse transfer_sweep_list(transfer_sweep_list_request)

List sweeps

The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.transfer_sweep_list_request import TransferSweepListRequest
from plaid.model.plaid_error import PlaidError
from plaid.model.transfer_sweep_list_response import TransferSweepListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    transfer_sweep_list_request = TransferSweepListRequest(
        client_id="client_id_example",
        secret="secret_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        count=25,
        offset=0,
        amount="amount_example",
        status=SweepStatus("pending"),
        originator_client_id="originator_client_id_example",
        funding_account_id="funding_account_id_example",
        transfer_id="transfer_id_example",
    ) # TransferSweepListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List sweeps
        api_response = api_instance.transfer_sweep_list(transfer_sweep_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->transfer_sweep_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_sweep_list_request** | [**TransferSweepListRequest**](TransferSweepListRequest.md)|  |

### Return type

[**TransferSweepListResponse**](TransferSweepListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> UserCreateResponse user_create(user_create_request)

Create user

This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.  If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.  Ensure that you store the `user_token` along with your user's identifier in your database, as it is not possible to retrieve a previously created `user_token`.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.user_create_response import UserCreateResponse
from plaid.model.user_create_request import UserCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    user_create_request = UserCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        client_user_id="client_user_id_example",
    ) # UserCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create user
        api_response = api_instance.user_create(user_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->user_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  |

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_create**
> WalletCreateResponse wallet_create(wallet_create_request)

Create an e-wallet

Create an e-wallet. The response is the newly created e-wallet object.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_create_request import WalletCreateRequest
from plaid.model.wallet_create_response import WalletCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_create_request = WalletCreateRequest(
        client_id="client_id_example",
        secret="secret_example",
        iso_currency_code=WalletISOCurrencyCode("GBP"),
    ) # WalletCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an e-wallet
        api_response = api_instance.wallet_create(wallet_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_create_request** | [**WalletCreateRequest**](WalletCreateRequest.md)|  |

### Return type

[**WalletCreateResponse**](WalletCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_get**
> WalletGetResponse wallet_get(wallet_get_request)

Fetch an e-wallet

Fetch an e-wallet. The response includes the current balance.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_get_request import WalletGetRequest
from plaid.model.wallet_get_response import WalletGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_get_request = WalletGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        wallet_id="wallet_id_example",
    ) # WalletGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch an e-wallet
        api_response = api_instance.wallet_get(wallet_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_get_request** | [**WalletGetRequest**](WalletGetRequest.md)|  |

### Return type

[**WalletGetResponse**](WalletGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_list**
> WalletListResponse wallet_list(wallet_list_request)

Fetch a list of e-wallets

This endpoint lists all e-wallets in descending order of creation.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_list_request import WalletListRequest
from plaid.model.wallet_list_response import WalletListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_list_request = WalletListRequest(
        client_id="client_id_example",
        secret="secret_example",
        iso_currency_code=WalletISOCurrencyCode("GBP"),
        cursor="cursor_example",
        count=10,
    ) # WalletListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch a list of e-wallets
        api_response = api_instance.wallet_list(wallet_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_list_request** | [**WalletListRequest**](WalletListRequest.md)|  |

### Return type

[**WalletListResponse**](WalletListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transaction_execute**
> WalletTransactionExecuteResponse wallet_transaction_execute(wallet_transaction_execute_request)

Execute a transaction using an e-wallet

Execute a transaction using the specified e-wallet. Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction. Transactions will settle in seconds to several days, depending on the underlying payment rail.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_transaction_execute_request import WalletTransactionExecuteRequest
from plaid.model.wallet_transaction_execute_response import WalletTransactionExecuteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_transaction_execute_request = WalletTransactionExecuteRequest(
        client_id="client_id_example",
        secret="secret_example",
        idempotency_key=WalletTransactionIdempotencyKey("idempotency_key_example"),
        wallet_id="wallet_id_example",
        counterparty=WalletTransactionCounterparty(),
        amount=WalletTransactionAmount(),
        reference="reference_example",
    ) # WalletTransactionExecuteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Execute a transaction using an e-wallet
        api_response = api_instance.wallet_transaction_execute(wallet_transaction_execute_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_transaction_execute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_transaction_execute_request** | [**WalletTransactionExecuteRequest**](WalletTransactionExecuteRequest.md)|  |

### Return type

[**WalletTransactionExecuteResponse**](WalletTransactionExecuteResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transaction_get**
> WalletTransactionGetResponse wallet_transaction_get(wallet_transaction_get_request)

Fetch an e-wallet transaction

Fetch a specific e-wallet transaction

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_transaction_get_response import WalletTransactionGetResponse
from plaid.model.wallet_transaction_get_request import WalletTransactionGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_transaction_get_request = WalletTransactionGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        transaction_id="transaction_id_example",
    ) # WalletTransactionGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch an e-wallet transaction
        api_response = api_instance.wallet_transaction_get(wallet_transaction_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_transaction_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_transaction_get_request** | [**WalletTransactionGetRequest**](WalletTransactionGetRequest.md)|  |

### Return type

[**WalletTransactionGetResponse**](WalletTransactionGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transaction_list**
> WalletTransactionListResponse wallet_transaction_list(wallet_transaction_list_request)

List e-wallet transactions

This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.wallet_transaction_list_response import WalletTransactionListResponse
from plaid.model.wallet_transaction_list_request import WalletTransactionListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    wallet_transaction_list_request = WalletTransactionListRequest(
        client_id="client_id_example",
        secret="secret_example",
        wallet_id="wallet_id_example",
        cursor="cursor_example",
        count=10,
        options=WalletTransactionListRequestOptions(
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # WalletTransactionListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List e-wallet transactions
        api_response = api_instance.wallet_transaction_list(wallet_transaction_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->wallet_transaction_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_transaction_list_request** | [**WalletTransactionListRequest**](WalletTransactionListRequest.md)|  |

### Return type

[**WalletTransactionListResponse**](WalletTransactionListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_create**
> WatchlistScreeningEntityCreateResponse watchlist_screening_entity_create(watchlist_screening_entity_create_request)

Create a watchlist screening for an entity

Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_create_response import WatchlistScreeningEntityCreateResponse
from plaid.model.watchlist_screening_entity_create_request import WatchlistScreeningEntityCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_create_request = WatchlistScreeningEntityCreateRequest(
        search_terms=EntityWatchlistSearchTerms(
            entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
            legal_name=EntityWatchlistScreeningName("Al-Qaida"),
            document_number=WatchlistScreeningDocumentValueNullable("C31195855"),
            email_address="user@example.com",
            country=GenericCountryCodeNullable("US"),
            phone_number="+14025671234",
            url="https://example.com",
        ),
        client_user_id=ClientUserID("your-db-id-3b24110"),
        client_id="client_id_example",
        secret="secret_example",
    ) # WatchlistScreeningEntityCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a watchlist screening for an entity
        api_response = api_instance.watchlist_screening_entity_create(watchlist_screening_entity_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_create_request** | [**WatchlistScreeningEntityCreateRequest**](WatchlistScreeningEntityCreateRequest.md)|  |

### Return type

[**WatchlistScreeningEntityCreateResponse**](WatchlistScreeningEntityCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_get**
> WatchlistScreeningEntityGetResponse watchlist_screening_entity_get(watchlist_screening_entity_get_request)

Get an entity screening

Retrieve an entity watchlist screening.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_get_response import WatchlistScreeningEntityGetResponse
from plaid.model.watchlist_screening_entity_get_request import WatchlistScreeningEntityGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_get_request = WatchlistScreeningEntityGetRequest(
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        secret="secret_example",
        client_id="client_id_example",
    ) # WatchlistScreeningEntityGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get an entity screening
        api_response = api_instance.watchlist_screening_entity_get(watchlist_screening_entity_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_get_request** | [**WatchlistScreeningEntityGetRequest**](WatchlistScreeningEntityGetRequest.md)|  |

### Return type

[**WatchlistScreeningEntityGetResponse**](WatchlistScreeningEntityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_history_list**
> WatchlistScreeningEntityHistoryListResponse watchlist_screening_entity_history_list(watchlist_screening_entity_history_list_request)

List history for entity watchlist screenings

List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_history_list_response import WatchlistScreeningEntityHistoryListResponse
from plaid.model.watchlist_screening_entity_history_list_request import WatchlistScreeningEntityHistoryListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_history_list_request = WatchlistScreeningEntityHistoryListRequest(
        secret="secret_example",
        client_id="client_id_example",
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningEntityHistoryListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List history for entity watchlist screenings
        api_response = api_instance.watchlist_screening_entity_history_list(watchlist_screening_entity_history_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_history_list_request** | [**WatchlistScreeningEntityHistoryListRequest**](WatchlistScreeningEntityHistoryListRequest.md)|  |

### Return type

[**WatchlistScreeningEntityHistoryListResponse**](WatchlistScreeningEntityHistoryListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_hit_list**
> WatchlistScreeningEntityHitListResponse watchlist_screening_entity_hit_list(watchlist_screening_entity_hit_list_request)

List hits for entity watchlist screenings

List all hits for the entity watchlist screening.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_hit_list_request import WatchlistScreeningEntityHitListRequest
from plaid.model.watchlist_screening_entity_hit_list_response import WatchlistScreeningEntityHitListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_hit_list_request = WatchlistScreeningEntityHitListRequest(
        secret="secret_example",
        client_id="client_id_example",
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningEntityHitListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List hits for entity watchlist screenings
        api_response = api_instance.watchlist_screening_entity_hit_list(watchlist_screening_entity_hit_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_hit_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_hit_list_request** | [**WatchlistScreeningEntityHitListRequest**](WatchlistScreeningEntityHitListRequest.md)|  |

### Return type

[**WatchlistScreeningEntityHitListResponse**](WatchlistScreeningEntityHitListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_list**
> WatchlistScreeningEntityListResponse watchlist_screening_entity_list(watchlist_screening_entity_list_request)

List entity watchlist screenings

List all entity screenings.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_list_request import WatchlistScreeningEntityListRequest
from plaid.model.watchlist_screening_entity_list_response import WatchlistScreeningEntityListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_list_request = WatchlistScreeningEntityListRequest(
        secret="secret_example",
        client_id="client_id_example",
        entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
        client_user_id=ClientUserID("your-db-id-3b24110"),
        status=WatchlistScreeningStatus("cleared"),
        assignee="54350110fedcbaf01234ffee",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningEntityListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List entity watchlist screenings
        api_response = api_instance.watchlist_screening_entity_list(watchlist_screening_entity_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_list_request** | [**WatchlistScreeningEntityListRequest**](WatchlistScreeningEntityListRequest.md)|  |

### Return type

[**WatchlistScreeningEntityListResponse**](WatchlistScreeningEntityListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_program_get**
> WatchlistScreeningEntityProgramGetResponse watchlist_screening_entity_program_get(watchlist_screening_entity_program_get_request)

Get entity watchlist screening program

Get an entity watchlist screening program

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_program_get_request import WatchlistScreeningEntityProgramGetRequest
from plaid.model.watchlist_screening_entity_program_get_response import WatchlistScreeningEntityProgramGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_program_get_request = WatchlistScreeningEntityProgramGetRequest(
        entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
        secret="secret_example",
        client_id="client_id_example",
    ) # WatchlistScreeningEntityProgramGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get entity watchlist screening program
        api_response = api_instance.watchlist_screening_entity_program_get(watchlist_screening_entity_program_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_program_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_program_get_request** | [**WatchlistScreeningEntityProgramGetRequest**](WatchlistScreeningEntityProgramGetRequest.md)|  |

### Return type

[**WatchlistScreeningEntityProgramGetResponse**](WatchlistScreeningEntityProgramGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_program_list**
> WatchlistScreeningEntityProgramListResponse watchlist_screening_entity_program_list(watchlist_screening_entity_program_list_request)

List entity watchlist screening programs

List all entity watchlist screening programs

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_program_list_request import WatchlistScreeningEntityProgramListRequest
from plaid.model.watchlist_screening_entity_program_list_response import WatchlistScreeningEntityProgramListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_program_list_request = WatchlistScreeningEntityProgramListRequest(
        secret="secret_example",
        client_id="client_id_example",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningEntityProgramListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List entity watchlist screening programs
        api_response = api_instance.watchlist_screening_entity_program_list(watchlist_screening_entity_program_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_program_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_program_list_request** | [**WatchlistScreeningEntityProgramListRequest**](WatchlistScreeningEntityProgramListRequest.md)|  |

### Return type

[**WatchlistScreeningEntityProgramListResponse**](WatchlistScreeningEntityProgramListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_review_create**
> WatchlistScreeningEntityReviewCreateResponse watchlist_screening_entity_review_create(watchlist_screening_entity_review_create_request)

Create a review for an entity watchlist screening

Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_review_create_request import WatchlistScreeningEntityReviewCreateRequest
from plaid.model.watchlist_screening_entity_review_create_response import WatchlistScreeningEntityReviewCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_review_create_request = WatchlistScreeningEntityReviewCreateRequest(
        confirmed_hits=[
            "enthit_52xR9LKo77r1Np",
        ],
        dismissed_hits=[
            "enthit_52xR9LKo77r1Np",
        ],
        comment=ReviewComment("These look like legitimate matches, rejecting the customer."),
        client_id="client_id_example",
        secret="secret_example",
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
    ) # WatchlistScreeningEntityReviewCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a review for an entity watchlist screening
        api_response = api_instance.watchlist_screening_entity_review_create(watchlist_screening_entity_review_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_review_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_review_create_request** | [**WatchlistScreeningEntityReviewCreateRequest**](WatchlistScreeningEntityReviewCreateRequest.md)|  |

### Return type

[**WatchlistScreeningEntityReviewCreateResponse**](WatchlistScreeningEntityReviewCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_review_list**
> WatchlistScreeningEntityReviewListResponse watchlist_screening_entity_review_list(watchlist_screening_entity_review_list_request)

List reviews for entity watchlist screenings

List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_review_list_response import WatchlistScreeningEntityReviewListResponse
from plaid.model.watchlist_screening_entity_review_list_request import WatchlistScreeningEntityReviewListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_review_list_request = WatchlistScreeningEntityReviewListRequest(
        secret="secret_example",
        client_id="client_id_example",
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningEntityReviewListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List reviews for entity watchlist screenings
        api_response = api_instance.watchlist_screening_entity_review_list(watchlist_screening_entity_review_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_review_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_review_list_request** | [**WatchlistScreeningEntityReviewListRequest**](WatchlistScreeningEntityReviewListRequest.md)|  |

### Return type

[**WatchlistScreeningEntityReviewListResponse**](WatchlistScreeningEntityReviewListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_entity_update**
> WatchlistScreeningEntityUpdateResponse watchlist_screening_entity_update(watchlist_screening_entity_update_request)

Update an entity screening

Update an entity watchlist screening.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_entity_update_request import WatchlistScreeningEntityUpdateRequest
from plaid.model.watchlist_screening_entity_update_response import WatchlistScreeningEntityUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_entity_update_request = WatchlistScreeningEntityUpdateRequest(
        entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        search_terms=UpdateEntityScreeningRequestSearchTerms(
            entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
            legal_name=EntityWatchlistScreeningName("Al-Qaida"),
            document_number=WatchlistScreeningDocumentValue("C31195855"),
            email_address="user@example.com",
            country=GenericCountryCode("US"),
            phone_number="+14025671234",
            url="https://example.com",
        ),
        assignee="54350110fedcbaf01234ffee",
        status=WatchlistScreeningStatus("cleared"),
        client_user_id=ClientUserID("your-db-id-3b24110"),
        client_id="client_id_example",
        secret="secret_example",
        reset_fields=WatchlistScreeningEntityUpdateRequestResettableFieldList([
            WatchlistScreeningEntityUpdateRequestResettableField("assignee"),
        ]),
    ) # WatchlistScreeningEntityUpdateRequest | The entity screening was successfully updated.

    # example passing only required values which don't have defaults set
    try:
        # Update an entity screening
        api_response = api_instance.watchlist_screening_entity_update(watchlist_screening_entity_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_entity_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_entity_update_request** | [**WatchlistScreeningEntityUpdateRequest**](WatchlistScreeningEntityUpdateRequest.md)| The entity screening was successfully updated. |

### Return type

[**WatchlistScreeningEntityUpdateResponse**](WatchlistScreeningEntityUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_create**
> WatchlistScreeningIndividualCreateResponse watchlist_screening_individual_create(watchlist_screening_individual_create_request)

Create a watchlist screening for a person

Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_create_request import WatchlistScreeningIndividualCreateRequest
from plaid.model.watchlist_screening_individual_create_response import WatchlistScreeningIndividualCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_create_request = WatchlistScreeningIndividualCreateRequest(
        search_terms=WatchlistScreeningRequestSearchTerms(
            watchlist_program_id="prg_2eRPsDnL66rZ7H",
            legal_name=WatchlistScreeningIndividualName("Aleksey Potemkin"),
            date_of_birth=dateutil_parser('Mon May 28 17:00:00 PDT 1990').date(),
            document_number=WatchlistScreeningDocumentValue("C31195855"),
            country=GenericCountryCode("US"),
        ),
        client_user_id=ClientUserID("your-db-id-3b24110"),
        client_id="client_id_example",
        secret="secret_example",
    ) # WatchlistScreeningIndividualCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a watchlist screening for a person
        api_response = api_instance.watchlist_screening_individual_create(watchlist_screening_individual_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_create_request** | [**WatchlistScreeningIndividualCreateRequest**](WatchlistScreeningIndividualCreateRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualCreateResponse**](WatchlistScreeningIndividualCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_get**
> WatchlistScreeningIndividualGetResponse watchlist_screening_individual_get(watchlist_screening_individual_get_request)

Retrieve an individual watchlist screening

Retrieve a previously created individual watchlist screening

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_get_response import WatchlistScreeningIndividualGetResponse
from plaid.model.watchlist_screening_individual_get_request import WatchlistScreeningIndividualGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_get_request = WatchlistScreeningIndividualGetRequest(
        watchlist_screening_id="scr_52xR9LKo77r1Np",
        secret="secret_example",
        client_id="client_id_example",
    ) # WatchlistScreeningIndividualGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an individual watchlist screening
        api_response = api_instance.watchlist_screening_individual_get(watchlist_screening_individual_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_get_request** | [**WatchlistScreeningIndividualGetRequest**](WatchlistScreeningIndividualGetRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualGetResponse**](WatchlistScreeningIndividualGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_history_list**
> WatchlistScreeningIndividualHistoryListResponse watchlist_screening_individual_history_list(watchlist_screening_individual_history_list_request)

List history for individual watchlist screenings

List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_history_list_response import WatchlistScreeningIndividualHistoryListResponse
from plaid.model.watchlist_screening_individual_history_list_request import WatchlistScreeningIndividualHistoryListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_history_list_request = WatchlistScreeningIndividualHistoryListRequest(
        secret="secret_example",
        client_id="client_id_example",
        watchlist_screening_id="scr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningIndividualHistoryListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List history for individual watchlist screenings
        api_response = api_instance.watchlist_screening_individual_history_list(watchlist_screening_individual_history_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_history_list_request** | [**WatchlistScreeningIndividualHistoryListRequest**](WatchlistScreeningIndividualHistoryListRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualHistoryListResponse**](WatchlistScreeningIndividualHistoryListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_hit_list**
> WatchlistScreeningIndividualHitListResponse watchlist_screening_individual_hit_list(watchlist_screening_individual_hit_list_request)

List hits for individual watchlist screening

List all hits found by Plaid for a particular individual watchlist screening.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_hit_list_response import WatchlistScreeningIndividualHitListResponse
from plaid.model.watchlist_screening_individual_hit_list_request import WatchlistScreeningIndividualHitListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_hit_list_request = WatchlistScreeningIndividualHitListRequest(
        secret="secret_example",
        client_id="client_id_example",
        watchlist_screening_id="scr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningIndividualHitListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List hits for individual watchlist screening
        api_response = api_instance.watchlist_screening_individual_hit_list(watchlist_screening_individual_hit_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_hit_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_hit_list_request** | [**WatchlistScreeningIndividualHitListRequest**](WatchlistScreeningIndividualHitListRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualHitListResponse**](WatchlistScreeningIndividualHitListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_list**
> WatchlistScreeningIndividualListResponse watchlist_screening_individual_list(watchlist_screening_individual_list_request)

List Individual Watchlist Screenings

List previously created watchlist screenings for individuals

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_list_response import WatchlistScreeningIndividualListResponse
from plaid.model.watchlist_screening_individual_list_request import WatchlistScreeningIndividualListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_list_request = WatchlistScreeningIndividualListRequest(
        secret="secret_example",
        client_id="client_id_example",
        watchlist_program_id="prg_2eRPsDnL66rZ7H",
        client_user_id=ClientUserID("your-db-id-3b24110"),
        status=WatchlistScreeningStatus("cleared"),
        assignee="54350110fedcbaf01234ffee",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningIndividualListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List Individual Watchlist Screenings
        api_response = api_instance.watchlist_screening_individual_list(watchlist_screening_individual_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_list_request** | [**WatchlistScreeningIndividualListRequest**](WatchlistScreeningIndividualListRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualListResponse**](WatchlistScreeningIndividualListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_program_get**
> WatchlistScreeningIndividualProgramGetResponse watchlist_screening_individual_program_get(watchlist_screening_individual_program_get_request)

Get individual watchlist screening program

Get an individual watchlist screening program

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_program_get_request import WatchlistScreeningIndividualProgramGetRequest
from plaid.model.watchlist_screening_individual_program_get_response import WatchlistScreeningIndividualProgramGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_program_get_request = WatchlistScreeningIndividualProgramGetRequest(
        watchlist_program_id="prg_2eRPsDnL66rZ7H",
        secret="secret_example",
        client_id="client_id_example",
    ) # WatchlistScreeningIndividualProgramGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get individual watchlist screening program
        api_response = api_instance.watchlist_screening_individual_program_get(watchlist_screening_individual_program_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_program_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_program_get_request** | [**WatchlistScreeningIndividualProgramGetRequest**](WatchlistScreeningIndividualProgramGetRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualProgramGetResponse**](WatchlistScreeningIndividualProgramGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_program_list**
> WatchlistScreeningIndividualProgramListResponse watchlist_screening_individual_program_list(watchlist_screening_individual_program_list_request)

List individual watchlist screening programs

List all individual watchlist screening programs

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_program_list_request import WatchlistScreeningIndividualProgramListRequest
from plaid.model.watchlist_screening_individual_program_list_response import WatchlistScreeningIndividualProgramListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_program_list_request = WatchlistScreeningIndividualProgramListRequest(
        secret="secret_example",
        client_id="client_id_example",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningIndividualProgramListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List individual watchlist screening programs
        api_response = api_instance.watchlist_screening_individual_program_list(watchlist_screening_individual_program_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_program_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_program_list_request** | [**WatchlistScreeningIndividualProgramListRequest**](WatchlistScreeningIndividualProgramListRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualProgramListResponse**](WatchlistScreeningIndividualProgramListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_review_create**
> WatchlistScreeningIndividualReviewCreateResponse watchlist_screening_individual_review_create(watchlist_screening_individual_review_create_request)

Create a review for an individual watchlist screening

Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_review_create_request import WatchlistScreeningIndividualReviewCreateRequest
from plaid.model.watchlist_screening_individual_review_create_response import WatchlistScreeningIndividualReviewCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_review_create_request = WatchlistScreeningIndividualReviewCreateRequest(
        confirmed_hits=[
            "scrhit_52xR9LKo77r1Np",
        ],
        dismissed_hits=[
            "scrhit_52xR9LKo77r1Np",
        ],
        comment=ReviewComment("These look like legitimate matches, rejecting the customer."),
        client_id="client_id_example",
        secret="secret_example",
        watchlist_screening_id="scr_52xR9LKo77r1Np",
    ) # WatchlistScreeningIndividualReviewCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a review for an individual watchlist screening
        api_response = api_instance.watchlist_screening_individual_review_create(watchlist_screening_individual_review_create_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_review_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_review_create_request** | [**WatchlistScreeningIndividualReviewCreateRequest**](WatchlistScreeningIndividualReviewCreateRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualReviewCreateResponse**](WatchlistScreeningIndividualReviewCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_review_list**
> WatchlistScreeningIndividualReviewListResponse watchlist_screening_individual_review_list(watchlist_screening_individual_review_list_request)

List reviews for individual watchlist screenings

List all reviews for the individual watchlist screening.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_review_list_response import WatchlistScreeningIndividualReviewListResponse
from plaid.model.watchlist_screening_individual_review_list_request import WatchlistScreeningIndividualReviewListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_review_list_request = WatchlistScreeningIndividualReviewListRequest(
        secret="secret_example",
        client_id="client_id_example",
        watchlist_screening_id="scr_52xR9LKo77r1Np",
        cursor="eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM",
    ) # WatchlistScreeningIndividualReviewListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List reviews for individual watchlist screenings
        api_response = api_instance.watchlist_screening_individual_review_list(watchlist_screening_individual_review_list_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_review_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_review_list_request** | [**WatchlistScreeningIndividualReviewListRequest**](WatchlistScreeningIndividualReviewListRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualReviewListResponse**](WatchlistScreeningIndividualReviewListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_screening_individual_update**
> WatchlistScreeningIndividualUpdateResponse watchlist_screening_individual_update(watchlist_screening_individual_update_request)

Update individual watchlist screening

Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.watchlist_screening_individual_update_response import WatchlistScreeningIndividualUpdateResponse
from plaid.model.watchlist_screening_individual_update_request import WatchlistScreeningIndividualUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    watchlist_screening_individual_update_request = WatchlistScreeningIndividualUpdateRequest(
        watchlist_screening_id="scr_52xR9LKo77r1Np",
        search_terms=UpdateIndividualScreeningRequestSearchTerms(
            watchlist_program_id="prg_2eRPsDnL66rZ7H",
            legal_name=WatchlistScreeningIndividualName("Aleksey Potemkin"),
            date_of_birth=dateutil_parser('Mon May 28 17:00:00 PDT 1990').date(),
            document_number=WatchlistScreeningDocumentValue("C31195855"),
            country=GenericCountryCode("US"),
        ),
        assignee="54350110fedcbaf01234ffee",
        status=WatchlistScreeningStatus("cleared"),
        client_user_id=ClientUserID("your-db-id-3b24110"),
        client_id="client_id_example",
        secret="secret_example",
        reset_fields=WatchlistScreeningIndividualUpdateRequestResettableFieldList([
            WatchlistScreeningIndividualUpdateRequestResettableField("assignee"),
        ]),
    ) # WatchlistScreeningIndividualUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update individual watchlist screening
        api_response = api_instance.watchlist_screening_individual_update(watchlist_screening_individual_update_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->watchlist_screening_individual_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_screening_individual_update_request** | [**WatchlistScreeningIndividualUpdateRequest**](WatchlistScreeningIndividualUpdateRequest.md)|  |

### Return type

[**WatchlistScreeningIndividualUpdateResponse**](WatchlistScreeningIndividualUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_verification_key_get**
> WebhookVerificationKeyGetResponse webhook_verification_key_get(webhook_verification_key_get_request)

Get webhook verification key

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.  The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

### Example

* Api Key Authentication (clientId):
* Api Key Authentication (plaidVersion):
* Api Key Authentication (secret):

```python
import time
import plaid
from plaid.api import plaid_api
from plaid.model.webhook_verification_key_get_response import WebhookVerificationKeyGetResponse
from plaid.model.webhook_verification_key_get_request import WebhookVerificationKeyGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://production.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = plaid.Configuration(
    host = "https://production.plaid.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientId
configuration.api_key['clientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientId'] = 'Bearer'

# Configure API key authorization: plaidVersion
configuration.api_key['plaidVersion'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['plaidVersion'] = 'Bearer'

# Configure API key authorization: secret
configuration.api_key['secret'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secret'] = 'Bearer'

# Enter a context with an instance of the API client
with plaid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plaid_api.PlaidApi(api_client)
    webhook_verification_key_get_request = WebhookVerificationKeyGetRequest(
        client_id="client_id_example",
        secret="secret_example",
        key_id="key_id_example",
    ) # WebhookVerificationKeyGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get webhook verification key
        api_response = api_instance.webhook_verification_key_get(webhook_verification_key_get_request)
        pprint(api_response)
    except plaid.ApiException as e:
        print("Exception when calling PlaidApi->webhook_verification_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_verification_key_get_request** | [**WebhookVerificationKeyGetRequest**](WebhookVerificationKeyGetRequest.md)|  |

### Return type

[**WebhookVerificationKeyGetResponse**](WebhookVerificationKeyGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

