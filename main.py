import re
with open ('the_verdict.txt', 'r', encoding='utf-8') as f:
    text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
all_words.extend(["<|endoftext|>", "<|unk|>"])

#Create a vocabulary
vocab = {token: integer for integer, token in enumerate(all_words)}
class SimpleTokenizerV2:
    #Store vocab as a class to use in encode and decode methods
    def __init__(self, vocab):
        #Convet token to token id
        self.str_to_int = vocab
        #Convert token id to token
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        #Remove spaces and convert into tokens
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        preprocessed = [
            item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed
        ]
        #Call str to int to get token ids for each token
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text

tokenizer = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terrace of the palace"
text = " <|endoftext|> ".join((text1, text2))
print(text)
print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))