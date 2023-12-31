import sys

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
except ImportError:
    print("NLTK module not found. Installing NLTK...")
    try:
        import pip
        pip.main(['install', 'nltk'])
        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
    except ImportError:
        print("Failed to install NLTK. Please make sure you have pip installed.")
        sys.exit(1)

def calculate_similarity(text1, text2):
    stop_words = set(stopwords.words('english'))

    # Tokenize the texts
    tokens1 = [token.lower() for token in word_tokenize(text1) if token.lower() not in stop_words and token.isalnum()]
    tokens2 = [token.lower() for token in word_tokenize(text2) if token.lower() not in stop_words and token.isalnum()]

    # Calculate Jaccard similarity
    similarity = nltk.jaccard_distance(set(tokens1), set(tokens2))

    return 1 - similarity

def check_plagiarism(text1, text2, threshold=0.8):
    similarity_score = calculate_similarity(text1, text2)

    if similarity_score >= threshold:
        print("Potential plagiarism detected!")
        print(f"Similarity score: {similarity_score}")
    else:
        print("No plagiarism detected.")
        print(f"Similarity score: {similarity_score}")

# Example usage
text1 = "What is the step by step guide to invest in share market in india?"
text2 = "What is the step by step guide to invest in share market?"

check_plagiarism(text1, text2)
