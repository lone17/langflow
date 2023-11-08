from typing import Optional

from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate

from langflow import CustomComponent
from langflow.field_typing import BaseOutputParser, Document


class PromptRunner(CustomComponent):
    display_name: str = "PromptRunner"
    description: str = "Run a Chain with the given PromptTemplate"
    beta = True
    field_config = {
        "llm": {"display_name": "LLM", "required": True},
        "prompt": {
            "display_name": "Prompt Template",
            "info": "Make sure the prompt has all variables filled.",
            "required": True,
        },
        "output_parser": {
            "display_name": "Output Parser",
            "advanced": False,
            "name": "output_parser",
        },
        "inputs": {"displaye_name": "Additional inputs", "advanced": True},
        "code": {"advanced": True},
    }

    def build(
        self,
        llm: BaseLLM,
        prompt: PromptTemplate,
        output_parser: Optional[BaseOutputParser] = None,
        inputs: Optional[dict] = {},
    ) -> Document:
        if output_parser:
            chain = prompt | llm | output_parser
        else:
            chain = prompt | llm

        # The input is an empty dict because the prompt is already filled
        result = chain.invoke(input=inputs)

        if hasattr(result, "content"):
            result = result.content

        self.repr_value = result

        return Document(page_content=str(result))
