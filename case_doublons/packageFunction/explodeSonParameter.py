
import pandas as pd
def explodeSonParameters(stringParameter , dfToModify ) :
    
    dfToReturn = pd.DataFrame(dfToModify)
    listDataToInsert = []
    listParam = stringParameter.split('.')
    for index, row in dfToReturn.iterrows():
        value = row
        for param in listParam:
            try:
                value = value[param]
            except:
                value = ''    
        listDataToInsert.append(value)
    dfToReturn[stringParameter] = listDataToInsert
    return dfToReturn


# list_sofactoapp__Opportunite__r_Billed_to__r_Name = []
# for index, row in dfBills.iterrows():
#     list_sofactoapp__Opportunite__r_Billed_to__r_Name.append(row['sofactoapp__Opportunite__r']['Billed_to__r']['Name'])
# dfBills['sofactoapp__Opportunite__r.Billed_to__r.Name'] = list_sofactoapp__Opportunite__r_Billed_to__r_Name


if __name__ == 'main':
    dfToModify = pd.DataFrame(dfBills)

