import re


def basic_tokenize(text):
    """
    Simple whitespace and punctuation-based tokenizer.
    """
    text = text.lower()
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens


def show_tokens(text):
    tokens = basic_tokenize(text)

    print("Original Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nToken Count:")
    print(len(tokens))


if __name__ == "__main__":
    sample_text = (
        "The statute drew legal influence from previous measures "
        "including those undertaken by the Holy Roman Empire."
    )

    show_tokens(sample_text)