import re 
import spacy

#Εισαγωγή μοντέλου ελληνικής γλώσσας
nlp = spacy.load('el_core_news_sm')


def primary_preprocess(text):
    """
    Βασικό module για preprocessing των ομιλιών ώστε να μπορούν να επεξεργασθούν από τις πιο προηγμένες τεχνικές αργότερα 
    """
    #Βήμα 1ο μετατροπή σε lower case για ομοιογένεια
    cleaned_text = text.lower()

    #Bήμα 2ο απαλοιφή μη αλφαβητικών χαρακτήρων, δεν θεωρούνται χρήσιμοι
    cleaned_text = re.sub(r'[^άέήίόύώα-ω\s]', '', cleaned_text)
    doc=nlp(cleaned_text)

    #Απαλοιφή stop words μέσω tokenization
    tokens = [token.text for token in doc if not token.is_stop]
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text