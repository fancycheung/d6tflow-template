import sklearn
import tasks
import pandas as pd

def accuracy(do_preprocess=False):
    model = tasks.TaskTrain(do_preprocess).output().load()
    df_train = tasks.TaskPreprocess().output().load()
    print(sklearn.metrics.accuracy_score(df_train['y'],model.predict(df_train.iloc[:,:-1])))

def plot_importances():
    model = tasks.TaskTrain().output().load()
    df_train = tasks.TaskPreprocess().output().load()
    df_importance = pd.Series(model.feature_importances_, index=df_train.iloc[:,:-1].columns)
    import matplotlib.pyplot as plt
    df_importance.sort_values(ascending=False).plot.bar()
    plt.savefig('reports/plot.png')

