from datetime import datetime
import os
from networksecurity.constant import traning_pipeline

print(traning_pipeline.Pipeline_name)

class TraningPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
        self.pipeline_name = traning_pipeline.Pipeline_name
        self.artifact_name = traning_pipeline.Artifacts
        self.artifact_dir  = os.path.join(self.artifact_name,timestamp)
        self.timpestamp:str = timestamp
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TraningPipelineConfig):
        self.data_ingestion_dir: str = os.path.join( training_pipeline_config.artifact_dir,
            traning_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, traning_pipeline.Data_ingestion_feature_store_name, traning_pipeline.File_name
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, traning_pipeline.Data_ingestion_ingested_dir, traning_pipeline.train_file_name
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, traning_pipeline.Data_ingestion_ingested_dir, traning_pipeline.test_file_name
            )
        self.train_test_split_ratio: float = traning_pipeline.Data_ingestion_train_test_split
        self.collection_name: str = traning_pipeline.Data_ingestion_collection_name
        self.database_name: str = traning_pipeline.Data_ingestion_database_name

