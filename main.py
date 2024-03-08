from langchain.llms.huggingface_pipeline import HuggingFacePipeline

nlp = HuggingFacePipeline.from_model_id(
    model_id="impira/layoutlm-document-qa",
    task="text2text-generation"
)


