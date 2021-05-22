import pandas as pd
from user.models import DummyCitizenInfo


df = pd.read_csv('DummyCitizenData.csv')
    

for i in range(len(df)):
        
    citizen = DummyCitizenInfo(name = df['Name'][i],
                          father_name=df['father name'][i],
                          mother_name=df['mother name'][i],
                          email = df['Email'][i],
                          nid = df['NID'][i],
                          phone = df['Phone Number'][i],
                          area_name = df['AreaCode'][i],
                          ward_number = df['Ward'][i],
                          dob = df['dob'][i],
                          )
    
    citizen.save()

