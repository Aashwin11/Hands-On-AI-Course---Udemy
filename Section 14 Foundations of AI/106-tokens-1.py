import tiktoken 

#Tokenize
encoder=tiktoken.encoding_for_model("gpt-4o")
text="Hey There ! My name is Aniket"
token=encoder.encode(text)
print(f"Tokens: {token}")

#Reversre Tokenize

decoded=encoder.decode([25216, 3274, 1073, 3673, 1308, 382, 1689, 74367])
print(f"Decoded value:{decoded}")