from typing import List

from weaverbird.backends.mongo_translator.steps.types import MongoStep
from weaverbird.pipeline.steps import TextStep


def translate_text(step: TextStep) -> List[MongoStep]:
    return [
        {
            '$addFields': {step.new_column: {'$literal': step.text}},
        }
    ]
