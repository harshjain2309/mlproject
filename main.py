from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    
    transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(train_path, test_path)

    print("Data Transformation Completed.")
    print("Train shape:", train_arr.shape)
    print("Test shape:", test_arr.shape)
    print("Preprocessor file:", preprocessor_path)
