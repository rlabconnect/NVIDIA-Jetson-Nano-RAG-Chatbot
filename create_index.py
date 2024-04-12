import os
from secret_key import OPENAI_API_KEY
from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

data_path = Path('data')
index_path = Path('index')

documents = SimpleDirectoryReader(data_path).load_data()
index = VectorStoreIndex.from_documents(documents)
print(documents)

# Save the index
index.storage_context.persist(index_path)
