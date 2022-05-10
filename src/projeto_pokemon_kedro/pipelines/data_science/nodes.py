"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.0
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

def split_data(df, test_size = 0.3, random_state=9999):
    """Splits data into train and test dataset"""
    
    # Split train and test
    X = df.drop('type1', axis=1)
    y = df['type1']

    X_train, X_test, y_train, y_test =  train_test_split(
    X, y, test_size = test_size, random_state=random_state, stratify = y
    )
    
    return X_train, X_test, y_train, y_test
    
    

def fit_model(X_train, X_test, y_train, y_test):
    """ Fits a classifier model using a training dataset """
   
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X_train,y_train)
    
    # Predict test set
    y_pred = classifier.predict(X_test)

    #Reports Score
    score = accuracy_score(y_test, y_pred)
    print(score)

    return classifier