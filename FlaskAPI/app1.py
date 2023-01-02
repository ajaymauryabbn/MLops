import pickle
from flask import Flask ,request

#loading the model
model_pickle=open("./classifier.pkl",'rb')
clf=pickle.load(model_pickle)

app=Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    return{"message":"Hello World!"}

@app.route("/predict",methods=['POST'])
def renderprediction():
    load_application=request.get_json()

    if load_application['Gender']=="Male":
        gender=0
    else:
        gender=1
    if load_application['Married']=="Unmarried":
        married=0
    else:
        married=1
    if load_application['Credit_History']=="Unclear Debts":
        credit_history=0
    else:
        credit_history=1
    applicant_income=load_application['ApplicantIncome']
    loan_amt=load_application['LoanAmount']/1000

    ## making prediction
    prediction=clf.predict(
        [[gender,
        married,
        applicant_income,
        loan_amt,
        credit_history]]
    )

    if prediction==0:
        pred="Rejected"
    else:
        pred="Approved"
    result={'Loan_approval_status':pred}

    return result