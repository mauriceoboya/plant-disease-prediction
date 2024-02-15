from cnnClassifier  import logger
from cnnClassifier.components.prepare_basemodel import PrepareBaseModel
from cnnClassifier.config.configurations import ConfigurationManager


STAGE_NAME2='Base model preparation'

class BaseModelPreparationPipeline:
    def main():
            config=ConfigurationManager()
            prepare_base_model_config=config.get_prepare_model_config()
            prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()


if __name__=='__main__':
    try:
        logger.info(f">>>> started {STAGE_NAME2}  <<<<<<<")
        obj=BaseModelPreparationPipeline()
        obj.main()
        logger.info(f">>>> completed {STAGE_NAME2}  <<<<<<<")
    except Exception as e:
        logger.error(f">>>> failed {STAGE_NAME2}  <<<<<<<")
        logger.exception(e)