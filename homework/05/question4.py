import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv_file = 'dv.bin'

# Load the model and dv
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('subs_prob')


@app.route('/subs_predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    subscription_decision = (y_pred >= 0.5)
    y_pred_rounded = round(y_pred,3)
    print('Inside the web service')
    print('Subscription Probability:', round(y_pred, 3))
    print('Subscription Decision:', subscription_decision)

    result = {
        'subscription_probability' : float(y_pred_rounded),
        'subscription' : bool(subscription_decision)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)