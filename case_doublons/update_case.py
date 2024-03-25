import json
from packageFunction.recup_access import get_secret
import simple_salesforce

id_sfdc_full = json.loads(get_secret('identifiants_SF_Full'))


sf = simple_salesforce.Salesforce(
    username=id_sfdc_full["username"],
    password=id_sfdc_full["mdp"],
    security_token=id_sfdc_full["securityToken"],
    domain = 'test')



