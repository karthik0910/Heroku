from flask import Flask, render_template,request
from flask_cors import cross_origin
import pickle

app= Flask(__name__)

@app.route("/",methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI
@cross_origin()
def index():
    try:
        Intercept=1
        age = float(request.form['age'])
        yrs_married = float(request.form['yrs_married'])
        children = float(request.form['children'])
        marriage_rating = request.form['rate_marriage']
        if (marriage_rating == "very poor" ):
            rate_marriage = 1
        if (marriage_rating == "poor"):
            rate_marriage = 2

        if (marriage_rating == "fair"):
            rate_marriage = 3

        if (marriage_rating == "good"):
            rate_marriage = 4

        if (marriage_rating == "very good"):
            rate_marriage = 5

        how_religious = request.form['religious']
        if (how_religious == "not"):
            religious = 1
        if (how_religious == "mildly"):
            religious = 2
        if (how_religious == "fairly"):
            religious = 3

        if (how_religious == "strongly"):
            religious = 4
        Level_of_education = request.form["educ"]

        if (Level_of_education == "Grade School"):
            educ = 9
        if (Level_of_education == "High School"):
            educ = 12

        if (Level_of_education == "Some College"):
            educ = 14

        if (Level_of_education == "College Graduate"):
            educ = 16
        if (Level_of_education == "Some Graduate School"):
            educ = 17
        if (Level_of_education == "Advanced Degree"):
            educ = 20

        wife_occupation = request.form["occupation"]

        if (wife_occupation == "farming/semi-skilled/unskilled worker"):
            occ_2 = 1
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        if (wife_occupation == "white-collar"):
            occ_2 = 0
            occ_3 = 1
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        if (wife_occupation == "teacher/counselor/social worker/skilled worker"):
            occ_2 = 0
            occ_3 = 0
            occ_4 = 1
            occ_5 = 0
            occ_6 = 0
        if (wife_occupation == "managerial/administrative/business"):
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 1
            occ_6 = 0
        if (wife_occupation == "professional with advanced degree"):
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 1
        else:
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        husband_occupation = request.form["occupation_husb"]

        if (husband_occupation == "farming/semi-skilled/unskilled worker"):
            occ_husb_2 = 1
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        if (husband_occupation == "white-colloar"):
            occ_husb_2 = 0
            occ_husb_3 = 1
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        if (husband_occupation == "teacher/counselor/social worker/skilled worker"):
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 1
            occ_husb_5 = 0
            occ_husb_6 = 0
        if (husband_occupation == "managerial/administrative/business"):
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 1
            occ_husb_6 = 0
        if (husband_occupation == "professional with advanced degree"):
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 1
        else:
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0

        filename = 'modelForPrediction.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
        prediction = loaded_model.predict([[Intercept, age, yrs_married, children, rate_marriage, religious, educ,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6]])
            # showing the prediction results in a UI
        return render_template('results.html',prediction=round(prediction[0]))
    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'
        #return render_template('results.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True) # running the app



