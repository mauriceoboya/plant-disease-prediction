from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraingPipeline
from cnnClassifier.pipeline.stage_02_premodel import BaseModelPreparationPipeline
STAGE_NAME1='Data ingestion stage'

try:
    logger.info(f'>>>>>{STAGE_NAME1} started <<<<')
    data_ingestion=DataIngestionTraingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>{STAGE_NAME1} completed <<<<')
except Exception as e:
    logger.error(f'>>>>>{STAGE_NAME1} failed <<<<')
    logger.exception(e)



STAGE_NAME2='Base model preparation'

try:
    logger.info(f">>>> started {STAGE_NAME2}  <<<<<<<")
    obj=BaseModelPreparationPipeline()
    obj.main()
    logger.info(f">>>> completed {STAGE_NAME2}  <<<<<<<")
except Exception as e:
    logger.error(f">>>> failed {STAGE_NAME2}  <<<<<<<")
    logger.exception(e)