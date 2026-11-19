import re
# text = "Hello, World. This is a-- test"
with open ('the_verdict.txt', 'r', encoding='utf-8') as f:
    text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

preprocessed = [item.strip() for item in preprocessed if item.strip()]

print(len(preprocessed))
