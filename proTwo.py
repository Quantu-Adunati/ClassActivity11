import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def importCSV():
    tips = pd.read_csv("./tips.csv",index_col=0)
    #Add a new calculated column
    tips["tip_percent"] = (tips['tip']/tips.index)*100
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(tips)
    createSubset(tips)

def createSubset(tips):
    subset =tips[['sex','tip_percent']].query('sex=="Male" and tip_percent>10.00')
    print("=======SUBSET=======")
    print(subset)
    #calculating the correlation coeffiecient
    correlation = (tips['tip_percent']).corr(tips['tip'])
    print("=======Correlation=======")
    print(correlation)
    createDataVis(tips)

def createDataVis(tips):
    fig, ax = plt.subplots() 
    # count the occurrence of each class 
    data=tips["tip_percent"].value_counts()
    points = tips.index
    frequency =tips["tip_percent"]
    ax.bar(points,frequency) 
    ax.set_title('Tips % per total bill') 
    ax.set_xlabel('Total bill') 
    ax.set_ylabel('%')
    plt.show()
    # columns = tips.drop(['size','smoker','day','time','sex','tip_percent'],axis=1)
    
    # # create x data
    # x_data = range(0, tips.shape[0])
   
    # # plot each column
    # for column in columns:
    #     ax.plot(x_data,tips[column])
    # # set title and legend
    # ax.set_title('Yeah')
    # plt.show()

importCSV()