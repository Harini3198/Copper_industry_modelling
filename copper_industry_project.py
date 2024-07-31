import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import copper_streamlit
copper=pd.read_csv("copper_industry_project\Copper_Set.xlsx - Result 1.csv")
copper_copy=pd.read_csv("copper_industry_project\Copper_Set.xlsx - Result 1.csv")
copper_copy['material_ref'] = copper_copy['material_ref'].astype(str)
copper_copy['material_ref']=copper_copy['material_ref'].apply(lambda x: np.nan if x.startswith('00000') else x)
copper_copy.dropna()
copper.drop(['id','item_date','country','material_ref','product_ref','delivery date'],axis=1,inplace=True)
copper['quantity tons']=pd.to_numeric(copper['quantity tons'], errors='coerce')
copper.dropna(how="any",subset=['customer','status','application','thickness','selling_price',
                                'quantity tons'],inplace=True)
encoded=LabelEncoder()
for i in copper.select_dtypes(include=['object']).columns:
    copper[i]=encoded.fit_transform(copper[i])
copper1=copper
x=copper.drop('status',axis=1)
y=copper['status']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
result=DecisionTreeClassifier().fit(x_train,y_train)
for i in copper1.columns:
    if i=='quantity tons':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'customer':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'status':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'item type':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'application':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'thickness':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'width':
        copper1[i]=copper1[i]**(1/3)
    elif i == 'selling_price':
        copper1[i]=copper1[i]**(1/3)

copper1.dropna(how="any",subset=copper1.columns,inplace=True)
x1=copper1.drop('selling_price',axis=1)
y1=copper1['selling_price']
x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.2)
result1=RandomForestRegressor().fit(x1_train,y1_train)

def regression_model(quantityTons,customer,status,itemtype,application,thickness,width):
    status_type={
        'Won': 7,
        'Draft': 0,
        'To be approved': 6,
        'Lost': 1,
        'Not lost for AM': 2,
        'Wonderful': 8,
        'Revised': 5,
        'Offered': 4,
        'Offerable': 3
    }
    status=status_type.get(status)

    item_type={
        'W': 5,
        'WI': 6,
        'S': 3,
        'Others': 1,
        'PL': 2,
        'IPL': 0,
        'SLAWR': 4
    }

    itemType=item_type.get(itemType)
    price = np.array([quantityTons, customer, status, itemType, application, thickness, width]).reshape(1, -1)
    price_pred=result1.predict(price)

    return price_pred


def classification_model(quantityTons,customer,itemType,application,thickness,width,selling_price):
    status_type={
        7: 'Won',
        0: 'Draft',
        6: 'To be approved',
        1: 'Lost',
        2: 'Not lost for AM',
        8: 'Wonderful',
        5: 'Revised',
        4: 'Offered',
        3: 'Offerable'
    }
    
    item_type={
        'W': 5,
        'WI': 6,
        'S': 3,
        'Others': 1,
        'PL': 2,
        'IPL': 0,
        'SLAWR': 4
    }
    itemType=item_type.get(itemType)
    
    product=np.array([quantityTons,customer,itemType,application,thickness,width,selling_price]).reshape(1,-1)
    product_pred=result.predict(product)
    pred_value=product_pred[0]
    predicted_status=status_type.get(pred_value)
    return predicted_status





    



