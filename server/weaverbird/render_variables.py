from typing import Any, Dict

from toucan_connectors.common import nosql_apply_parameters_to_query

from weaverbird.steps.base import BaseStep


class StepWithVariablesMixin:
    def render(self, variables: Dict[str, Any]) -> BaseStep:
        RenderedClass = self.__class__.__bases__[0]
        step_as_dict = self.dict()  # type: ignore
        rendered_dict = nosql_apply_parameters_to_query(step_as_dict, variables)
        return RenderedClass(**rendered_dict)
