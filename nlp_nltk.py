import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required datasets (Only needed once)
nltk.download("punkt")
nltk.download("stopwords")

# Sample Text
text = "Natural Language Processing (NLP) allows AI to understand human language easily!"

# Tokenization (Splitting text into words)
tokens = word_tokenize(text)

# Removing Stopwords (Common words like "the", "is", "to")
filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words("english")]

print("Original Text:", text)
print("Tokenized Words:", tokens)
print("Filtered Words (Without Stopwords):", filtered_tokens)
