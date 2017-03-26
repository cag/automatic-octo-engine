import pandas as pd
from sklearn import metrics # check out metrics.log_loss

training_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
