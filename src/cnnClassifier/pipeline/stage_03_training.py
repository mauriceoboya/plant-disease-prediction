from cnnClassifier.config.configurations import ConfigurationManager
from cnnClassifier.components.preparecallback import PrepareCallbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logger
STAGE_NAME3='training pipeline'

class TrainingPipeline:
    def main(self):
        config=ConfigurationManager()
        prepare_callbacks_config=config.get_prepare_callbacks_config()
        prepare_callbacks=PrepareCallbacks(config=prepare_callbacks_config)
        callbacks_list=prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callbacks_list)



if __name__=='__main__':
    try:
        logger.info(f">>>>>  {STAGE_NAME3} started <<<<<<<<<")
        obj=TrainingPipeline()
        obj.main()
        logger.info(f">>>>>  {STAGE_NAME3} completed <<<<<<<<<")
    except Exception as e:
        logger.error(f">>>>> {STAGE_NAME3} failed  <<<<<<<<<")
        logger.error(e)