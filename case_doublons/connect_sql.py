import json
from packageFunction.recup_access import get_secret
import simple_salesforce
from simple_salesforce.exceptions import SalesforceMalformedRequest
from databricks import sql

doublons_case = {}

with sql.connect(server_hostname = "dbc-ec350aea-e79c.cloud.databricks.com",
                 http_path       = "/sql/1.0/warehouses/ada8c6e6edcf5d3e",
                 access_token    = "dapia6693c950c1dd0b3b328efec79a8512d") as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
            select *
            from test_catalog.operation_maintenance.case_doublons
""" )
        result = cursor.fetchall()

        for row in result:
            doublons_case[row["doublons_case"]] = row['origin_case']



id_sfdc_full = json.loads(get_secret('identifiants_SF_Full'))

sf = simple_salesforce.Salesforce(
    username=id_sfdc_full["username"],
    password=id_sfdc_full["mdp"],
    security_token=id_sfdc_full["securityToken"],
    domain = 'test')

for key, value in doublons_case.items():
    try :
        get_value = sf.Case.update(key,{
            'OriginalCase__c': value, 
            'Duplicate_Detection_Status__c': 'Possible Duplicate Detected' })
    except SalesforceMalformedRequest:
        print(key)

        