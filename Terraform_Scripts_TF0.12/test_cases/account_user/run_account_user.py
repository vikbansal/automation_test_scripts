"""
run_account_user.py

Test case for account_user Terraform resource/ use-case

- note various placeholders that must be updated:
    - filepath for terraform_fx.py
    - create/ import/ update/ destroy test functions and respective arguments
    - update "#" in "avx_ip_#", "avx_user_#", "avx_pass_#" accordingly
- place xxx.py in respective test_cases/xxx/ directory
"""

import os

import sys
sys.path.insert(1, '/file_path/aviatrix_terraform_regression/py_libs')
import terraform_fx as tf

import logging
import logging.handlers
import time

TIMESTR = time.strftime("%Y-%m-%d")
LOGLEVEL = logging.DEBUG
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATEFORMAT = "%d-%b-%y %H:%M:%S"
logging.basicConfig(level=LOGLEVEL,
                    format=FORMAT,
                    datefmt=DATEFORMAT,
                    handlers=[
                        logging.FileHandler(filename=TIMESTR + "_regression_result.log"),
                        logging.StreamHandler()
                    ])
log = logging.getLogger()

log.info("\n")
log.info("============================================================")
log.debug("RUNNING STAGE: " + str(os.path.split(os.getcwd())[1]).upper())
log.info("============================================================")
log.info("Steps to perform:")
log.info("      1. Set up environment variables/ credentials")
log.info("      2. Create account user based on AWS access account")
log.info("      3. Run import test to identify deltas")
log.info("      4. Tear down infrastructure\n")

try:
    log.info("Setting environment...")
    log.debug("     placeholder_ip: %s", str(os.environ["AVIATRIX_CONTROLLER_IP"]))
    log.debug("     placeholder_user: %s", str(os.environ["AVIATRIX_USERNAME"]))
    log.debug("     placeholder_pass: %s", str(os.environ["AVIATRIX_PASSWORD"]))
    avx_controller_ip = os.environ["avx_ip_1"]
    avx_controller_user = os.environ["avx_user_1"]
    avx_controller_pass = os.environ["avx_pass_1"]
    log.info("Setting new variable values as follows...")
    log.debug("     avx_controller_ip: %s", avx_controller_ip)
    log.debug("     avx_controller_user: %s", avx_controller_user)
    log.debug("     avx_controller_pass: %s", avx_controller_pass)
    os.environ["AVIATRIX_CONTROLLER_IP"] = avx_controller_ip
    os.environ["AVIATRIX_USERNAME"] = avx_controller_user
    os.environ["AVIATRIX_PASSWORD"] = avx_controller_pass
except:
    log.info("-------------------- RESULT --------------------")
    log.error("     Failed to properly set environment credentials!")
    sys.exit()
log.info("-------------------- RESULT --------------------")
log.info("      Set environment credentials: PASS\n")


try:
    log.info("Creating infrastructure...")
    tf.create_verify("acc_user_cred")
except:
    log.info("-------------------- RESULT --------------------")
    log.error("     create_verify(): FAIL\n")
    sys.exit()
log.info("-------------------- RESULT --------------------")
log.info("      create_verify(): PASS\n")


try:
    log.info("Verifying import functionality...")
    tf.import_test("account_user", "test_accountuser", "acc_user_cred")
except:
    log.info("-------------------- RESULT --------------------")
    log.error("     import_test: FAIL\n")
    sys.exit()
log.info("-------------------- RESULT --------------------")
log.info("      import_test(): PASS\n")


log.info(str(os.path.split(os.getcwd())[1]).upper() + " does not support update functionality...")
log.info("-------------------- RESULT --------------------")
log.info("     update_test(): SKIPPED\n")


try:
    log.info("Verifying destroy functionality...")
    tf.destroy_test("acc_user_cred")
except:
    log.info("-------------------- RESULT --------------------")
    log.error("     destroy_test(): FAIL\n")
    sys.exit()
log.info("-------------------- RESULT --------------------")
log.info("      destroy_test(): PASS\n")
