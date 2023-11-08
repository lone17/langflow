from typing import Optional, Union

from langflow import CustomComponent
from langflow.field_typing import Chain, Document


class GatedBranchingPipeline(CustomComponent):
    display_name: str = "GatedBranchingPipeline"
    description: str = "Create any custom component you want!"
    beta = True

    def build_config(self):
        return {
            "chains": {"display_name": "Chains"},
            "default_chain": {"display_name": "Default Chain"},
            "condition_text": {"display_name": "Condition Text", "advanced": False},
            "condition_text_from": {
                "display_name": "Condition Text from",
                "advanced": False,
            },
            "code": {"advanced": True},
        }

    def build(
        self,
        chains: list[Chain],
        condition_text: Optional[Document],
        condition_text_from: Optional[Chain] = None,
        default_chain: Optional[Chain] = None,
    ) -> Union[Chain, None]:
        if condition_text:
            if isinstance(condition_text, Document):
                condition_text = condition_text.page_content
        elif condition_text_from:
            condition_text = condition_text_from.invoke({})
        for each_chain in chains:
            if (
                "condition_func" not in each_chain.__dict__
                or each_chain.condition_func(condition_text)
            ):
                return each_chain

        return default_chain
