import logging

from dify_plugin import ModelProvider
from dify_plugin.entities.model import ModelType
from dify_plugin.errors.model import CredentialsValidateFailedError

logger = logging.getLogger(__name__)

VALIDATION_MODEL = "openai/gpt-5.4-mini"


class LlmtrProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        try:
            model_instance = self.get_model_instance(ModelType.LLM)
            model_instance.validate_credentials(model=VALIDATION_MODEL, credentials=credentials)
        except CredentialsValidateFailedError:
            raise
        except Exception:
            logger.exception("%s credentials validate failed", self.get_provider_schema().provider)
            raise
