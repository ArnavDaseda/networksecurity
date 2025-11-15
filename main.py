from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TraningPipelineConfig

import sys

if __name__ =="__main__":
    try:
        traning_pipelineconfig = TraningPipelineConfig()
        data_ingestionconfig = DataIngestionConfig(traning_pipelineconfig)
        data_ingestion = DataIngestion(data_ingestionconfig)
        data_ingestionArtifacts = data_ingestion.initiate_data_ingestion()
        print(data_ingestionArtifacts)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)