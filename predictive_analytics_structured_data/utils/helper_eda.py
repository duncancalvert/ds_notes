import pandas as pd


def missing_unique_feature_counts(data):
    """_summary_
    Args:
        data (_type_): pandas dataframe import
    Returns:
        _type_: pandas dataframe with columns showing the value counts for missing and unique features for the dataframe
    """
    # missing values
    total_missing_values = data.isnull().sum().sort_values(ascending = False)
    percent_missing_values = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    missing_values = pd.concat([total_missing_values, percent_missing_values], axis=1, keys=['Total', 'Percent'])
    
    #unique values 
    total_data = data.count()
    total_unique_values = pd.DataFrame(total_data)
    total_unique_values.columns = ['Total']
    uniques = []
    for col in data.columns:
        unique = data[col].nunique()
        uniques.append(unique)
    total_unique_values['Uniques'] = uniques
    unique = total_unique_values
    return pd.concat([missing_values, unique], axis=1, keys=['Missing', 'UNIQUE'])