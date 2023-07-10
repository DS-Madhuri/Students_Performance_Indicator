from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import StudentsScore
import config
import traceback

app = Flask(__name__)

@app.route('/students_scores')

def home1():
    return render_template('students.html')

@app.route('/predict', methods = ['GET', 'POST'])

def predict():
    if request.method == 'GET':
        print("+"*50)
        data = request.args.get
        print("Data :",data)

        gender=  data('gender')
        race_ethnicity = data('race_ethnicity')
        parental_level_of_education= data('parental_level_of_education')
        lunch = data('lunch')
        test_preparation_course = data('test_preparation_course')
        reading_score = int(data('reading_score'))
        writing_score = int(data('writing_score'))


        Obj = StudentsScore(gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score)
        pred_price = Obj.get_predicted_price()    

        return render_template('students.html', prediction = pred_price)


    elif request.method == 'POST':
        print("*"*40)
        data = request.form.get
        print("Data :",data)

        gender=  data('gender')
        race_ethnicity = data('race_ethnicity')
        parental_level_of_education= data('parental_level_of_education')
        lunch = data('lunch')
        test_preparation_course = data('test_preparation_course')
        reading_score = int(data('reading_score'))
        writing_score = int(data('writing_score'))


        Obj = StudentsScore(gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score)
        pred_price = Obj.get_predicted_price()    

        return render_template('students.html', prediction = pred_price)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= config.PORT_NUMBER, debug=False)
