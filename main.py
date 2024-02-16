from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraingPipeline
from cnnClassifier.pipeline.stage_02_premodel import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline



STAGE_NAME='Data ingestion stage'

try:
    logger.info(f'>>>>>{STAGE_NAME} started <<<<')
    data_ingestion=DataIngestionTraingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>{STAGE_NAME} completed <<<<')
except Exception as e:
    logger.error(f'>>>>>{STAGE_NAME} failed <<<<')
    logger.exception(e)



STAGE_NAME1='Base model preparation'

try:
    logger.info(f">>>>>>>{STAGE_NAME1} started <<<<<<")
    prepare_model_ingestion=PrepareBaseModelPipeline()
    prepare_model_ingestion.main()
    logger.info(f">>>>>>>{STAGE_NAME1} completed <<<<<<")

except Exception as e:
    logger.error(f">>>>>>>{STAGE_NAME1} failed <<<<<<")
    logger.error(e)
    raise e

STAGE_NAME3='model training pipeline'

try:
    logger.info(f">>>>>  {STAGE_NAME3}  started<<<<<<<<<")
    obj=TrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME3} completed  <<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>  {STAGE_NAME3}  failed <<<<<<<<<")
    logger.error(e)