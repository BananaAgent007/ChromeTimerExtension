from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Load dataset
def predictTimes(data, sample):
  #print(data)
  print(sample)
  names = ['time', 'avg word size', 'word count', 'readability']
  X=[]
  y=[]
  for array in data:
    X.append(array[1:])
    y.append(array[0])
  #print(X)
  #print(y)
  X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
  # Make predictions on validation dataset
  print(Y_validation)
  model = SVC(gamma='auto')
  model.fit(X_train, Y_train)
  X_validation = [sample]
  predictions = model.predict(X_validation)
  print("prediction", predictions[0])
  return predictions[0]