import settings

from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.prompts import PromptTemplate

custom_prompt_template_str = """
You are a helpful assistant answering user questions based on the provided context.

Context:
{context_str}

Question:
{query_str}

Answer the question only using the context above.
If the context does not contain relevant information, say:
"I don't know based on the provided documentation."
Do not attempt to make up an answer.
"""

custom_prompt = PromptTemplate(custom_prompt_template_str)

def handle_query(query):
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(text_qa_template=custom_prompt)
    response = query_engine.query(query)
    return response