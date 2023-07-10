import pickle
import json
import numpy as np
import config


class StudentsScore():
    def __init__(self, gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        print("****** INIT Function *********")
        self.gender=gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()

        gender = self.json_data['gender'][self.gender]
        race_ethnicity = self.json_data['race_ethnicity'][self.race_ethnicity]
        parental_level_of_education = self.json_data['parental_level_of_education'][self.parental_level_of_education]
        lunch = self.json_data['lunch'][self.lunch]
        test_preparation_course = self.json_data['test_preparation_course'][self.test_preparation_course]
        
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = gender
        test_array[0,1] = race_ethnicity
        test_array[0,2] = parental_level_of_education
        test_array[0,3] = lunch
        test_array[0,4] = test_preparation_course
        test_array[0,5] = self.reading_score
        test_array[0,6] = self.writing_score
  
        predicted_score = np.around(self.model.predict(test_array)[0],3)
        return predicted_score


