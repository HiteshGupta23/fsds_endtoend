from src.DiamondPricePrediction.components.data_ingestion import DataIngestion

from src.DiamondPricePrediction.components.data_transformation import DataTransformation

from src.DiamondPricePrediction.components.model_trainer import ModelTrainer



import os
import sys
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()


