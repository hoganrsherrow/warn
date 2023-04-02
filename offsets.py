import spacy
from spacy.training import offsets_to_biluo_tags

model = "outputmodels/model1"

def find_misalignment(train_data, model):
    if model is not None:
        nlp = spacy.load(model)
        print("Loaded model:", model)
    else:
        nlp = spacy.blank("en")
        print("Created blank 'en' model")

    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        biluo_tags = offsets_to_biluo_tags(doc, annotations['entities'])
        print(text)
        print(biluo_tags)

# training data
TRAIN_DATA = [
    (
        "Date Notice Posted: 2018/10/19 | Company: Goodman Manufacturing Company L.P. | County: Lincoln | Affected Workers: 81 | Closure/Layoff Date: December 21, 2018",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 76, "COMPANY"),
                (87, 94, "COUNTY"),
                (115, 117, "AFFECTED_WORKERS"),
                (141, 158, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2018/10/11 | Company: GSK Consumer Health - Global manufacturing & Supply | County: Shelby | Affected Workers: 99 | Closure/Layoff Date: December 10, 2018",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 93, "COMPANY"),
                (104, 110, "COUNTY"),
                (131, 133, "AFFECTED_WORKERS"),
                (157, 174, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2018/9/28 | Company: Youth Villages | County: Perry | Affected Workers: 87 | Closure/Layoff Date: November 25, 2018 | Notice/Type: #20180030",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 55, "COMPANY"),
                (66, 71, "COUNTY"),
                (92, 94, "AFFECTED_WORKERS"),
                (118, 135, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/3/2 | Company: National Seating & Mobility, Inc. | County: Hamilton | Affected Workers: 108 | Closure/Layoff Date: March 23, 2023 – July 28, 2023 | Notice/Type: #202300012",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 73, "COMPANY"),
                (84, 92, "COUNTY"),
                (113, 116, "AFFECTED_WORKERS"),
                (140, 154, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/27 | Company: American Car Center | County: Shelby | Affected Workers: 288 | Closure/Layoff Date: February 24, 2023 | Notice/Type: #02300011",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 60, "COMPANY"),
                (71, 77, "COUNTY"),
                (98, 101, "AFFECTED_WORKERS"),
                (125, 142, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/22 | Company: CEVA Logistics | County: Wilson | Affected Workers: 142 | Closure/Layoff Date: April 22, 2023 | Notice/Type: #202300010",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 55, "COMPANY"),
                (66, 72, "COUNTY"),
                (93, 96, "AFFECTED_WORKERS"),
                (120, 134, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/10 | Company: Befesa Zinc US Inc. | County: Roane | Affected Workers: 50 | Closure/Layoff Date: April 8, 2023 | Notice/Type: #202300009",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 60, "COMPANY"),
                (71, 76, "COUNTY"),
                (97, 99, "AFFECTED_WORKERS"),
                (123, 136, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/9 | Company: American Snuff Company, LLC | County: Shelby | Affected Workers: 132 | Closure/Layoff Date: December 1, 2023 | Notice/Type: #202300008",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 67, "COMPANY"),
                (78, 84, "COUNTY"),
                (105, 108, "AFFECTED_WORKERS"),
                (132, 148, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/8 | Company: ThyssenKrupp | County: Hamilton | Affected Workers: 156 | Closure/Layoff Date: May 6, 2023 – May 20, 2023 | Notice/Type: #202300007",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 52, "COMPANY"),
                (63, 71, "COUNTY"),
                (92, 95, "AFFECTED_WORKERS"),
                (119, 145, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/8 | Company: National Pen | County: Bedford| Affected Workers: 67 | Closure/Layoff Date: March 30, 2023 – May 31, 2023 | Notice/Type: #202300006",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 52, "COMPANY"),
                (63, 70, "COUNTY"),
                (90, 92, "AFFECTED_WORKERS"),
                (116, 145, "CLOSURE_LAYOFF_DATE")
            ]
        }
    )
]

find_misalignment(TRAIN_DATA, model)