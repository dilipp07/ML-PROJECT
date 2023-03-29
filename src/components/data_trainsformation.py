import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
import sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):
         '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_column=["writing_score","reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_column}")



            num_pipeline= Pipeline(steps=[("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())])
            logging.info("Numerical pipeline is done")
            cat_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy="most_frequent")),("one_hot_encoder",OneHotEncode()),("scaler",StandardScaler(with_mean=False))])
            logging.info("Categorical pipeline is done")
            
            


            preprocessor=ColumnTransformer([("num_pipeline",num_pipeline,numerical_columns),("cat_pipelines",cat_pipeline,categorical_columns)])

            logging.info("column transformation is done")

            return preprocessor
        
        
       
        except Exception as e:
            raise CustomException(e,sys)

    def           
