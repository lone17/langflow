import requests

base_url = "http://127.0.0.1:7860/api/v1"


def logged_in_headers():
    response = requests.get(url=base_url + "/auto_login")
    assert response.status_code == 200
    json_response = response.json()
    token = json_response["access_token"]
    return {"Authorization": f"Bearer {token}"}


headers = logged_in_headers()
response = requests.get(url=base_url + "/all", headers=headers)
json_response = response.json()

from langflow.interface.agents.base import agent_creator
from langflow.interface.chains.base import chain_creator
from langflow.interface.custom.base import custom_component_creator
from langflow.interface.document_loaders.base import documentloader_creator
from langflow.interface.embeddings.base import embedding_creator
from langflow.interface.llms.base import llm_creator
from langflow.interface.memories.base import memory_creator
from langflow.interface.output_parsers.base import output_parser_creator
from langflow.interface.prompts.base import prompt_creator
from langflow.interface.retrievers.base import retriever_creator
from langflow.interface.text_splitters.base import textsplitter_creator
from langflow.interface.toolkits.base import toolkits_creator
from langflow.interface.tools.base import tool_creator
from langflow.interface.utilities.base import utility_creator
from langflow.interface.vector_store.base import vectorstore_creator
from langflow.interface.wrappers.base import wrapper_creator

creators = [
    chain_creator,
    agent_creator,
    prompt_creator,
    llm_creator,
    memory_creator,
    tool_creator,
    toolkits_creator,
    wrapper_creator,
    embedding_creator,
    vectorstore_creator,
    documentloader_creator,
    textsplitter_creator,
    utility_creator,
    output_parser_creator,
    retriever_creator,
    custom_component_creator,
]
for creator in creators:
    created_types = creator.to_dict()
