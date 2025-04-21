from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformation = DataTransformation()
    train_arr, test_arr, _ = transformation.initiate_data_transformation(train_path, test_path)

    trainer = ModelTrainer()
    r2 = trainer.initiate_model_trainer(train_arr, test_arr)

    print("✅ Pipeline completed successfully.")
    print("🎯 Final R2 Score:", r2)