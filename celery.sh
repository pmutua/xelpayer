#!/usr/bin/env bash
celery -A xelpayer worker -c 5 --loglevel=info -Q handle_lipa_na_mpesa_callback_task


# b2c_result,b2c_request,celery,c2b_confirmation,c2b_validation,online_checkout_request,online_checkout_callback