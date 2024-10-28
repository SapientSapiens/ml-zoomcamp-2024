import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

model_file = 'model1.bin'
dv_file = 'dv.bin'

# Client data
client = {"job": "management", "duration": 400, "poutcome": "success"}

# Load the model and dv
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

def predict():
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    subscription_decision = (y_pred >= 0.5)

    print('Subscription Probability:', round(y_pred, 3))
    print('Subscription Decision:', subscription_decision)
    return subscription_decision

# Call the predict function
predict()
