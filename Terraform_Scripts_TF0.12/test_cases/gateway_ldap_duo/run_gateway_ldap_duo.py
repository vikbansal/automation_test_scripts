"""
run_gateway_ldap_duo.py

Test case for AWS Gateway (LDAP, Duo) Terraform resource/ use-case

- note various placeholders that must be updated:
    - filepath for terraform_fx.py
    - create/ import/ update/ destroy test functions and respective arguments
    - update "#" in "avx_ip_#", "avx_user_#", "avx_pass_#" accordingly
- place xxx.py in respective test_cases/xxx/ directory
"""

import os

import sys
sys.path.insert(1, '/var/lib/jenkins/workspace/Terraform-Regression/py_libs')
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
                        logging.FileHandler(filename=os.getcwd() + "/logs/" + TIMESTR + "_regression_result.log"),
                        logging.StreamHandler()
                    ])
log = logging.getLogger()

log.info("\n")
log.info("============================================================")
log.debug("RUNNING STAGE: " + str(os.path.split(os.getcwd())[1]).upper())
log.info("============================================================")
log.info("Steps to perform:")
log.info("      1. Set up environment variables/ credentials")
log.info("      2. Create AWS gateway (LDAP, Duo)")
log.info("      3. Perform terraform import to identify deltas")
log.info("      4. Perform update tests")
log.info("      5. Tear down infrastructure\n")

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
except Exception as err:
    log.exception(str(err))
    log.info("-------------------- RESULT --------------------")
    log.error("     Failed to properly set environment credentials!")
    sys.exit(1)
else:
    log.info("-------------------- RESULT --------------------")
    log.info("      Set environment credentials: PASS\n")


try:
    log.info("Creating infrastructure...")
    tf.create_verify()
except tf.subprocess.CalledProcessError as err:
    log.exception(err.stderr.decode())
    log.info("-------------------- RESULT --------------------")
    log.error("     create_verify(): FAIL\n")
    sys.exit(1)
else:
    log.info("-------------------- RESULT --------------------")
    log.info("      create_verify(): PASS\n")


try:
    log.info("Verifying import functionality...")
    log.debug("     Importing the AWS (LDAP, Duo) gateway...")
    tf.import_test("gateway", "aws_ldap_duo_gw")
except tf.subprocess.CalledProcessError as err:
    log.exception(err.stderr.decode())
    log.info("-------------------- RESULT --------------------")
    log.error("     import_test(): FAIL\n")
    sys.exit(1)
else:
    log.info("-------------------- RESULT --------------------")
    log.info("      import_test(): PASS\n")


try:
    log.info("Verifying update functionality...")
    log.debug("     duoUpdateIntKey: Updating the Duo Integration Key...")
    tf.update_test("duoUpdateIntKey")
    log.debug("     duoUpdateSecretKey: Updating the Duo Secret Key...")
    tf.update_test("duoUpdateSecretKey")
    log.debug("     duoUpdatePushMode: Updating the Duo Push Mode...")
    tf.update_test("duoUpdatePushMode")
    log.debug("     ldapUpdateServer: Updating the LDAP Server...")
    tf.update_test("ldapUpdateServer")
    log.debug("     ldapUpdateBindDN: Updating the LDAP Bind DN...")
    tf.update_test("ldapUpdateBindDN")
    log.debug("     ldapUpdatePassword: Updating the LDAP Password...")
    tf.update_test("ldapUpdatePassword")
    log.debug("     ldapUpdateBaseDN: Updating the LDAP Base DN...")
    tf.update_test("ldapUpdateBaseDN")
    log.debug("     ldapUpdateUsername: Updating the LDAP Username...")
    tf.update_test("ldapUpdateUsername")
except tf.subprocess.CalledProcessError as err:
    log.exception(err.stderr.decode())
    log.info("-------------------- RESULT --------------------")
    log.error("     update_test(): FAIL\n")
    sys.exit(1)
else:
    log.info("-------------------- RESULT --------------------")
    log.info("      update_test(): PASS\n")


for i in range(3):
    try:
        log.info("Verifying destroy functionality...")
        log.debug("     destroy_target() the ELB gateway first...") # Mantis (13255)
        tf.destroy_target("gateway", "aws_ldap_duo_gw")
        log.debug("Sleeping for 3 minutes to wait for gateway clean-up...")
        time.sleep(180)
        log.debug("     Now running destroy_test() to finish clean-up...")
        tf.destroy_test()
    except tf.subprocess.CalledProcessError as err:
        log.exception(err.stderr.decode())
        if i == 2:
            log.info("-------------------- RESULT --------------------")
            log.error("     destroy_test(): FAIL\n")
            sys.exit(1)
    else:
        log.info("-------------------- RESULT --------------------")
        log.info("      destroy_test(): PASS\n")
        sys.exit(0)
