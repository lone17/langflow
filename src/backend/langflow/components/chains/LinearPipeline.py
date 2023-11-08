from typing import Optional, Union

from langchain.chains import LLMChain

from langflow import CustomComponent
from langflow.field_typing import BaseLLM, BaseOutputParser, Chain, PromptTemplate


class LinearPipeline(CustomComponent):
    display_name: str = "LinearPipeline"
    description: str = "A Linear pipeline."
    beta = True

    def build_config(self):
        return {
            "prompt": {
                "display_name": "Prompt",
                "info": "Make sure the prompt has all variables filled.",
            },
            "llm": {"display_name": "LLM"},
            "output_parser": {"display_name": "Output Parser", "advanced": False},
            "condition_func": {
                "display_name": "Condition function",
                "info": "A python function to validate the condition_text.",
                "advanced": False,
            },
            "code": {"advanced": False},
        }

    def build(
        self,
        prompt: PromptTemplate,
        llm: BaseLLM,
        output_parser: Optional[BaseOutputParser] = None,
        condition_func: Optional[str] = "",
    ) -> Union[Chain, None]:
        chain = LLMChain(llm=llm, prompt=prompt, output_parser=output_parser)

        if condition_func:
            chain.__dict__["condition_func"] = eval(condition_func)

        return chain
