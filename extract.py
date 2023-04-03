import spacy

def extract_information(text, model_path="outputmodels/model1"):
    nlp = spacy.load(model_path)
    doc = nlp(text)
    result = {}

    for ent in doc.ents:
        result[ent.label_] = ent.text

    return result

text = "Date Notice Posted: 2019/11/12 | Company: Mitsubishi Electric Power Products, Inc. | County: Shelby | Affected Workers: 160 | Closure/Layoff Date: January 3, 2020 through January 31, 2020 | Notice/Type: #201900060"
print(extract_information(text))
