import spacy
import random
from spacy.util import minibatch, compounding
from spacy.tokens import DocBin
from spacy.training import Example
from pathlib import Path
from train_data import TRAIN_DATA


# training function
def train_ner_model(train_data, iterations=20, model=None, output_dir=None):
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

    # prepare the training data
    examples = []
    for text, annots in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annots)
        examples.append(example)

    # train the model
    optimizer = nlp.initialize(lambda: examples)
    for itn in range(iterations):
        random.shuffle(examples)
        losses = {}
        for batch in spacy.util.minibatch(examples, size=2):
            nlp.update(batch, sgd=optimizer, losses=losses)
        print(f"Iteration {itn}, Losses: {losses}")

    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

# load model to be updated
my_model = "outputmodels/model1"

# train the model using data defined above
train_ner_model(TRAIN_DATA, iterations=20, model=my_model, output_dir="outputmodels/model1")