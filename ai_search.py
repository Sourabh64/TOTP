import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Prepare the text data
text_data = ["This is the first document",
             "This document is the second document",
             "And this is the third one",
             "Is this the first document?"]

# Tokenize the text data
text_data = [word_tokenize(doc) for doc in text_data]

# Remove stopwords
stop_words = set(stopwords.words("english"))
text_data = [[word for word in doc if word.lower() not in stop_words] for doc in text_data]

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(text_data)

# Create a function for searching the text data
def search(query):
    query = word_tokenize(query)
    query = [word for word in query if word.lower() not in stop_words]
    query_vector = vectorizer.transform(query)
    scores = cosine_similarity(query_vector, vectors)
    return scores

# Test the search function
print(search("first document"))
