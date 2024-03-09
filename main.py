from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains.llm import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.mapreduce import MapReduceChain
from pdfminer.high_level import extract_text





text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)


llm = HuggingFacePipeline.from_model_id(
    model_id="deepset/roberta-base-squad2",
    task="text-generation"
)

prompt_template = """"
The following is the context: {text} 

Now answer the following question: {question}
"""
prompt = PromptTemplate.from_template(prompt_template)

llm_chain = LLMChain(llm=llm,prompt=prompt)

# chain = MapReduceChain(llm_chain)

text = extract_text("./RESUME_.pdf")

# documents = text_splitter.split_documents(prompt.format(text=text,question="what are the titles of the project?"))
question = "What the are the titles of the project?"
prompt.template = prompt.template.format(text = text, question = "What the are the titles of the project?")
prompt.input_variables = []
# print(prompt)
res = llm_chain.invoke(text, )


