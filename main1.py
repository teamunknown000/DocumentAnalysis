from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from pdfminer.high_level import extract_text

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': "Give me the titles of all the projects of the candidate?",
    'context': extract_text("./RESUME_.pdf")

}
res = nlp(QA_input)

print(res)