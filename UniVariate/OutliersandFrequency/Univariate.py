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
    
    def FrequencyTable(columnName,dataset):
        freqtable=pd.DataFrame(columns=['UniqueValues','Frequency','RelativeFrequency','Cumsum'])
        freqtable['UniqueValues']=dataset[columnName].value_counts().index
        freqtable['Frequency']=dataset[columnName].value_counts().values
        freqtable['RelativeFrequency']=freqtable['Frequency']/103
        freqtable['Cumsum']=freqtable['RelativeFrequency'].cumsum()
        return freqtable
    def outliers(dataset,quan):
        descriptive=pd.DataFrame(index=['Mean','Median','Mode','Q1:25th','Q2:50th','Q3:75th','99th','Q4:100th','IQR','1.5IQRrule',
                                           'Lesser','Greater','Min','Max','kurtosis','skew','variance','stddev'],columns=quan)
        for columnName in quan:
            descriptive[columnName]['Mean']=dataset[columnName].mean()
            descriptive[columnName]['Median']=dataset[columnName].median()
            descriptive[columnName]['Mode']=dataset[columnName].mode()[0]
            descriptive[columnName]['Q1:25th']=dataset.describe()[columnName]['25%']
            descriptive[columnName]['Q2:50th']=dataset.describe()[columnName]['50%']
            descriptive[columnName]['Q3:75th']=dataset.describe()[columnName]['75%']
            descriptive[columnName]['99th']=np.percentile(dataset[columnName],99)
            descriptive[columnName]['Q4:100th']=dataset.describe()[columnName]['max']
            descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75th']-descriptive[columnName]['Q1:25th']
            descriptive[columnName]['1.5IQRrule']=1.5*descriptive[columnName]['IQR']
            descriptive[columnName]['Lesser']=descriptive[columnName]['Q1:25th']-descriptive[columnName]['1.5IQRrule']
            descriptive[columnName]['Greater']=descriptive[columnName]['Q3:75th']+descriptive[columnName]['1.5IQRrule']
            descriptive[columnName]['Min']=dataset[columnName].min()
            descriptive[columnName]['Max']=dataset[columnName].max()
            descriptive[columnName]['kurtosis']=dataset[columnName].kurtosis()
            descriptive[columnName]['skew']=dataset[columnName].skew()
            descriptive[columnName]['variance']=dataset[columnName].var()
            descriptive[columnName]['stddev']=dataset[columnName].std()
        return descriptive