SIMPLE = {
    # "stopping_strings": [
    "stop": [
        "\nUSER:",
        "\nASSISTANT:",
        "\nFUNCTION RETURN:",
        "\nUSER",
        "\nASSISTANT",
        "\nFUNCTION RETURN",
        "\nFUNCTION",
        "\nFUNC",
        "<|im_start|>",
        "<|im_end|>",
        "<|im_sep|>",
        # '\n' +
        # '</s>',
        # '<|',
        # '\n#',
        # '\n\n\n',
    ],
    # "max_tokens": 3072,
    # "truncation_length": 4096,  # assuming llama2 models
    # "truncation_length": LLM_MAX_TOKENS,  # assuming mistral 7b
}
