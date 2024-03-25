import json
from packageFunction.recup_access import get_secret
import simple_salesforce
import pandas as pd

id_sfdc_full = json.loads(get_secret('identifiants_SF_Full'))



sf = simple_salesforce.Salesforce(
    username=id_sfdc_full["username"],
    password=id_sfdc_full["mdp"],
    security_token=id_sfdc_full["securityToken"],
    domain = 'test')


request = """
select 
    id, 
    CaseNumber, 
    AccountId, 
    Client_Name__c, 
    Opportunity__c, 
    SuppliedEmail, 
    description, 
    InternalDescription__c, 
    Reason, 
    Preciser_votre_demande__c, 
    Status, 
    CreatedDate, 
    ClosedDate
from case
order by CreatedDate
"""

df_case = pd.DataFrame(sf.query_all(request)['records'])

# Delete columns not needed   
df_case.drop(columns=['attributes'], inplace=True)


df_case.Description = df_case.Description.str.replace('\r\n', ' ')
df_case.InternalDescription__c = df_case.InternalDescription__c.str.replace('\r\n', ' ')
df_case.Reason = df_case.Reason.str.replace('\r\n', ' ')
df_case.Preciser_votre_demande__c = df_case.Preciser_votre_demande__c.str.replace('\r\n', ' ')

df_case.to_csv('salesforces_full_case.csv', sep=';', index=False)


