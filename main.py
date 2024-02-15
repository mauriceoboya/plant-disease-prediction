from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraingPipeline

STAGE_NAME1='Data ingestion stage'

try:
    logger.info(f'>>>>>{STAGE_NAME1} started <<<<')
    data_ingestion=DataIngestionTraingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>{STAGE_NAME1} completed <<<<')
except Exception as e:
    logger.error(f'>>>>>{STAGE_NAME1} failed <<<<')
    logger.exception(e)