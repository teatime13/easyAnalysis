from pandas import Series,DataFrame
import pandas as pd
import sys
import seaborn as sns
import matplotlib as matplotlib
import matplotlib.pyplot as plt

def main():
    print("input the CSV file name: ",end="")
    fileName = input()
    print("\n")

    #左から2つデータを読み取る
    dframe = pd.read_table(fileName, sep=',')
    data1 = dframe.iloc[:,0]
    data2 = dframe.iloc[:,1]

    sns.set()    #snsを使う時に必要
    fig, (ax1, ax2) = plt.subplots(1, 2)

    sns.distplot(data1, ax=ax1)
    sns.distplot(data2, ax=ax2)
    sns.jointplot(data1, data2)

    plt.show()  #plt(sns)を表示


if __name__ == "__main__":
    main()