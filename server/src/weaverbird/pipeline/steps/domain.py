from typing import Literal, Union

from weaverbird.pipeline.steps.utils.base import BaseStep
from weaverbird.pipeline.steps.utils.combination import Reference


class DomainStep(BaseStep):
    name: Literal['domain'] = 'domain'
    domain: Union[str, Reference]
