import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample Text
text = "Apple Inc. is one of the biggest companies in the world, founded by Steve Jobs in 1976."

# Process Text
doc = nlp(text)

# Extract Named Entities
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
