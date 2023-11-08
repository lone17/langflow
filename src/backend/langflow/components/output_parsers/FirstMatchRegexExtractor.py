import re
from typing import Callable, Dict, List, Optional, Union

from langflow import CustomComponent
from langflow.field_typing import BaseOutputParser


class FirstMatchRegexExtractorComponent(CustomComponent, BaseOutputParser):
    display_name: str = "FirstMatchRegexExtractor"
    beta = True

    def build_config(self):
        return {
            "patterns": {"display_name": "Regex Patterns", "options": []},
            "output_map": {"display_name": "Output Map Dict"},
            "output_map_func": {"display_name": "Output Map Func"},
            "code": {"advanced": True},
        }

    @classmethod
    def build(
        self,
        patterns: list[str],
        output_map: Optional[dict] = None,
        output_map_func: Optional[str] = None,
    ) -> BaseOutputParser:
        if not output_map:
            if output_map_func:
                output_map = eval(output_map_func)
            else:
                output_map = None

        # return __FirstMatchRegexExtractor(patterns=patterns, output_map=output_map)
        return self(patterns=patterns, output_map=output_map)

    # class __FirstMatchRegexExtractor(BaseOutputParser):
    """Parse the output of an LLM call using a regex."""

    @classmethod
    def is_lc_serializable(cls) -> bool:
        return True

    patterns: List[str] = "."
    output_map: Union[Dict, Callable] = None

    @property
    def _type(self) -> str:
        return "first_match_regex_extractor"

    @staticmethod
    def map_output(text, output_map) -> str:
        """
        Maps the given `text` to its corresponding value in the `output_map` dictionary.

        Parameters:
            text (str): The input text to be mapped.
            output_map (dict): A dictionary containing mapping of input text to output
                values.

        Returns:
            str: The corresponding value from the `output_map` if `text` is found in the
                dictionary, otherwise returns the original `text`.
        """
        if not output_map:
            return text

        if isinstance(output_map, dict):
            return output_map.get(text, text)

        return output_map(text)

    def parse(self, text: str) -> str:
        answer = None
        for each_pattern in self.patterns:
            print(each_pattern)
            output = re.findall(each_pattern, text)
            if output:
                output = [self.map_output(text, self.output_map) for text in output]
                answer = output[0]
                break

        return answer
