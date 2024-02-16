
from cnnClassifier.config.prepare_base_model_config import ConfigurationManager
from cnnClassifier.components.prepbasemodel import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME='base model ingestion stage'

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_model_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__=='__main__':
    try:
        logger.info(f'>>>>>stage{STAGE_NAME} started <<<<<<<')
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f'>>>>>stage{STAGE_NAME} completed <<<<<<<')
    except Exception as e:
        logger.error(f'>>>>>stage{STAGE_NAME} failed <<<<<<<')
        logger.error(e)

