from pdfminer.high_level import extract_text

text = extract_text("./RESUME_.pdf")
print(text)