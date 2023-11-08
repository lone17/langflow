from langflow import CustomComponent


class TextInput(CustomComponent):
    display_name: str = "Text Input"

    def build_config(self):
        return {"text": {"display_name": "Text"}, "code": {"advanced": True}}

    def build(self, text: str) -> str:
        return text
