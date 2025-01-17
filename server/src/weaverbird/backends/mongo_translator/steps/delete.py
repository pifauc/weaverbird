from typing import List

from weaverbird.backends.mongo_translator.steps.types import MongoStep
from weaverbird.pipeline.steps import DeleteStep


def translate_delete(step: DeleteStep) -> List[MongoStep]:
    return [{'$project': {c: 0 for c in step.columns}}]
