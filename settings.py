from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openrouter import OpenRouter

openrouter_api_key = 'Your api key'

llm = OpenRouter(
    model="meta-llama/llama-3.3-70b-instruct:free",
    api_key=openrouter_api_key,
)

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

Settings.llm = llm
Settings.embed_model = embed_model
# splitter = SentenceSplitter(chunk_size=512, chunk_overlap=20)
# Settings.transformations = [splitter]
# Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
# Settings.num_output = 512
# Settings.context_window = 3900

print(Settings.embed_model)