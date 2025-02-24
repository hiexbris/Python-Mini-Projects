import pandas as pd
def getDataByName(filepath,sheetname,key_heading,value_heading):
    self_brandwise_attritbuts = pd.read_excel(filepath,sheet_name=sheetname)
    key_col = -1
    value_col = -1
    first_row= -1
    last_row = -1
    for i in range(len(self_brandwise_attritbuts.index)):
        for j in self_brandwise_attritbuts.columns:
            if(self_brandwise_attritbuts.loc[i,j] == key_heading):
                key_col = self_brandwise_attritbuts.columns.get_loc(j)
                first_row = i
                break 
        if(key_col!=-1):
            break
    if(key_col==-1 or first_row<0):
        return Exception("Incorrect Column Name")
    else:
        last_row = first_row+1
        while True:
            ele = self_brandwise_attritbuts.iloc[last_row,key_col]
            if(type(ele) == float and str(ele) == "nan"):
                break
            elif(ele == "nan"):
                break
            else:
                last_row +=1
        if(value_heading is not None):
            for i in self_brandwise_attritbuts.columns:
                if(self_brandwise_attritbuts.loc[first_row,i] == value_heading):
                    value_col = self_brandwise_attritbuts.columns.get_loc(i)
                    break
            if(value_col==-1):
                return Exception("Incorrect Column Name")
        else:
            value_col = key_col+1
        tb = (self_brandwise_attritbuts.iloc[first_row:last_row,[key_col,value_col]])
        tb = tb.rename(columns = {self_brandwise_attritbuts.columns[key_col]:str(self_brandwise_attritbuts.iloc[first_row,key_col]),self_brandwise_attritbuts.columns[value_col]:str(self_brandwise_attritbuts.iloc[first_row,value_col])})
        tb = tb.drop(first_row)
        tb = pd.DataFrame(tb)
        tb = tb[tb[key_heading] != 'Grand Total']
        tb[value_heading] = tb[value_heading].apply(lambda x: round(x * 100, 0))
        result_dict = dict(zip(tb[key_heading], tb[value_heading]))
        return result_dict

t = getDataByName(r"C:\Users\A-Team\Desktop\‎\Python Programs\Marico Project\hair.xlsx",sheetname="Prices, Weights and Packaging",key_heading="MRP Band",value_heading="Share of Annual Revenue(USD)")
print(t)

