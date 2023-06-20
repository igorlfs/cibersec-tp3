ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEN_ALPHABET = len(ALPHABET)
ASCII_START = 65
KEY = "TESSOFTHEDURBERVILLES"
MESSAGE = "EUSOUMUITOCRIATIVOCOMEXEMPLOS"

# Exemplo da WIkipédia
# MESSAGE = "ATACARBASESUL"
# KEY = "LIMAO"

# |%%--%%| <dw3KNn7zEf|ENw5Sy6nTy>

if len(MESSAGE) < len(KEY):
    print(f"A mensagem '{MESSAGE}' deve ser maior que a chave '{KEY}'")
    exit()

# |%%--%%| <ENw5Sy6nTy|To2axeSBP6>

extended_key = ""
for i in range(len(MESSAGE)):
    extended_key += KEY[i % len(KEY)]
extended_key

# |%%--%%| <To2axeSBP6|t0FbLAs7Q3>

cipher = ""
for i in range(len(MESSAGE)):
    cipher += ALPHABET[
        (ord(MESSAGE[i]) - ASCII_START + ord(extended_key[i]) - ASCII_START)
        % LEN_ALPHABET
    ]
cipher

# |%%--%%| <t0FbLAs7Q3|wdcP0uJL57>

decipher = ""
for i in range(len(MESSAGE)):
    decipher += ALPHABET[
        (
            (ord(cipher[i]) - ASCII_START)
            - (ord(extended_key[i]) - ASCII_START)
            + LEN_ALPHABET
        )
        % LEN_ALPHABET
    ]
decipher

# |%%--%%| <wdcP0uJL57|qmqsVFVeAe>
