import pandas as pd
import numpy as np # linear algebra
import pickle
class Modelpredict:
    def __init__(self) -> None:
        self.model=[]
        filenamemodel = 'RFT_model.pkl'
        with open(filenamemodel, 'rb') as f:
            self.loaded_model = pickle.load(f)
    def difference(self,list1, list2):
        """
        Lấy ra những phần tử khác nhau giữa hai mảng.

        Args:
            list1 (list): Mảng thứ nhất.
            list2 (list): Mảng thứ hai.

        Returns:
            list: Danh sách chứa các phần tử khác nhau giữa hai mảng.
            """
        set1 = set(list1)
        set2 = set(list2)
        return (set1 - set2).union(set2 - set1)
    def cleandata(self,df):
        df['DAYS_EMPLOYED']=np.where(df['DAYS_EMPLOYED']>0,df['DAYS_EMPLOYED'].median(),df['DAYS_EMPLOYED'])
        
        df['Ratio_Ann_Inc']=df['AMT_ANNUITY']/df['AMT_INCOME_TOTAL']
        df['Ratio_Goods_Credit']=df['AMT_GOODS_PRICE']/df['AMT_CREDIT']
        df['Ratio_Credit_Inc']=df['AMT_CREDIT']/df['AMT_INCOME_TOTAL']
        df['CREDIT_TERM']=df['AMT_ANNUITY']/df['AMT_CREDIT']
        df['DAYS_EMPLOYED_PERCENT'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
        columns=pd.read_csv('column.csv')
        columns=list(columns['0'])
        remove_column=pd.read_csv('column_remove.csv')
        remove_column=list(remove_column['0'])
        remove_column.append("SK_ID_CURR")
        
        df=df[df.columns[~df.columns.isin(remove_column)]]

        cat_col=df.columns[df.dtypes=='object']
        df=pd.get_dummies(df,columns=cat_col,dtype=int)

    

        addnewcl=self.difference(columns,list(df.columns))
        for ncl in addnewcl:
            df[ncl]=0
        

        df.fillna(df.mean(),inplace=True)
        df = df.sort_index(axis=1)

        return df
    def predict(self,data):
        cldata=self.cleandata(data)
        kq=self.loaded_model.predict(cldata)
        submission=pd.DataFrame({'SK_ID_CURR':data["SK_ID_CURR"],'TARGET':kq})
        return submission