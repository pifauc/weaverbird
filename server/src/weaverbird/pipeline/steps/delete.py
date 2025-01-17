from typing import List, Literal

from weaverbird.pipeline.steps.utils.base import BaseStep
from weaverbird.pipeline.types import ColumnName


class DeleteStep(BaseStep):
    name: Literal['delete'] = 'delete'
    columns: List[ColumnName]
