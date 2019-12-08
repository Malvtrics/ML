import pandas as pd
import numpy as np
from scipy import stats

def analysis(df,name):
    
    print(name.center(30,'*'))
    
    #print("left side:")
    df_left = df[['l1','l2','l3']]
    #print(df_left)
    
    #print("right side:")
    df_right = df[['r1','r2','r3']]
    #print(df_right)
    
    N = df_left.size
    
    print('左侧列均值：')
    print(df_left.mean())
    print('左侧列方差:')
    print(df_left.std())
    print('左侧整体均值:',df_left.stack().mean())
    print('左侧整体方差:',df_left.stack().std())
    
    print('右侧列均值：')
    print(df_right.mean())
    print('右侧列方差：')
    print(df_right.std())
    print('右侧整体均值：',df_right.stack().mean())
    print('右侧整体方差：',df_right.stack().std())
    
    left_entire_mean = df_left.stack().mean()
    right_entire_mean = df_right.stack().mean()
    
    left_entire_std = df_left.stack().std()
    right_entire_std = df_right.stack().std()
    
    std_diff = np.sqrt(left_entire_std + right_entire_std)
    t = (left_entire_mean-right_entire_mean)/(std_diff*np.sqrt(2/N))
    
    freedom = 2*N-2
    p = 1-stats.t.cdf(t,df=freedom)
    
    print("t值 " + str(t))
    print("置信区间" + str(1-2*p))

def create():
    #first para is ndarray! that's the link
    df = pd.DataFrame(np.random.rand(20,3),index=[i+1 for i in range(20)],columns=list(['l1','l2','l3']))
    df = df*2+1
    return df

def main():
    df = pd.read_excel('data.xlsx')
    df = df[2:]
    
    df1 = df[['腰大肌','Unnamed: 10','Unnamed: 11','Unnamed: 13','Unnamed: 14','Unnamed: 15']]
    df2 = df[['竖脊肌','Unnamed: 18','Unnamed: 19','Unnamed: 21','Unnamed: 22','Unnamed: 23']]
    df3 = df[['多裂肌','Unnamed: 26','Unnamed: 27','Unnamed: 29','Unnamed: 30','Unnamed: 31']]
    df4 = df[['腰方肌','Unnamed: 34','Unnamed: 35','Unnamed: 37','Unnamed: 38','Unnamed: 39']]
    df5 = df[['压痛点','Unnamed: 42','Unnamed: 43','Unnamed: 45','Unnamed: 46','Unnamed: 47']]
    
    dfs = {'腰大肌':df1,'竖脊肌':df2,'多裂肌':df3,'腰方肌':df4,'压痛点':df5}
    
    i = 0
    for name,df in dfs.items():
        col_prefix = 'Unnamed: '
        
        arr = [10,11,13,14,15]
        arr = [str(arr[j]+8*i) for j in range(len(arr))]
        df.rename(columns = {name:'l1',col_prefix + arr[0]:'l2',col_prefix + arr[1]:'l3',
                             col_prefix + arr[2]:'r1',col_prefix + arr[3]:'r2',
                             col_prefix + arr[4]:'r3'},inplace=True) 
        df.index -= 1
        i += 1
        #analysis(df,name)

    df_new = create()
    print(df_new)
main()
