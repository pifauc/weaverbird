from typing import Any, Dict, List, Union

from weaverbird.pipeline import Pipeline
from weaverbird.pipeline.steps import BaseStep
from weaverbird.pipeline.steps.utils.combination import Reference


def _get_pipeline_for_domain(
    reference: Union[Any, List[Dict[Any, Any]], str, Reference], pipelines: Dict[str, List[BaseStep]]
) -> Any:
    if isinstance(reference, str) and reference in pipelines:
        return dereference_pipelines(pipelines[reference], pipelines)
    elif isinstance(reference, list) and 'domain' in reference[0]:
        return reference[0]['domain']
    else:
        return [{'domain': reference, 'name': 'domain'}]


def dereference_pipelines(
    pipeline: List[BaseStep], pipelines: Dict[str, List[BaseStep]]
) -> List[Dict[str, List[Reference]]]:
    dereferenced_pipeline = []  # type: ignore
    for pipeline_step in pipeline:
        if pipeline_step.name == 'domain':
            dereferenced_pipeline.append(*_get_pipeline_for_domain(pipeline_step.domain, pipelines))  # type: ignore
        elif pipeline_step.name == 'append':
            dereferenced_pipeline.append(
                {
                    **pipeline_step.dict(),
                    'pipelines': list(
                        map(
                            lambda x: _get_pipeline_for_domain(x, pipelines),
                            pipeline_step.pipelines,  # type:ignore
                        )
                    ),
                }
            )
        elif pipeline_step.name == 'join':
            dereferenced_pipeline.append(
                {
                    **pipeline_step.dict(),
                    'right_pipeline': _get_pipeline_for_domain(
                        pipeline_step.right_pipeline, pipelines  # type:ignore
                    ),
                }
            )
        else:
            dereferenced_pipeline.append(pipeline_step)  # type: ignore

    return dereferenced_pipeline
