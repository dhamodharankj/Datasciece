class UnivariateClass():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtypes=='O'):
                Qual.append(columnName)
                #print('Qual')
            else:
                Quan.append(columnName)
                #print('Quan')
        return Quan,Qual