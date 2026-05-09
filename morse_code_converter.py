MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-','@': '.--.-.',
}

# Reverse mapping for Morse → Text
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    """Convert plain text to Morse code."""
    text = text.upper()
    words = text.split(' ')
    morse_words = []

    for word in words:
        morse_chars = []
        for char in word:
            if char in MORSE_CODE:
                morse_chars.append(MORSE_CODE[char])
            else:
                morse_chars.append(f'[?{char}]')  # unknown character
        morse_words.append(' '.join(morse_chars))

    # Words separated by ' / ', letters by ' '
    return ' / '.join(morse_words)


def morse_to_text(morse: str) -> str:
    """Convert Morse code back to plain text."""
    words = morse.strip().split(' / ')
    decoded_words = []

    for word in words:
        letters = word.split(' ')
        decoded_chars = []
        for symbol in letters:
            symbol = symbol.strip()
            if symbol in REVERSE_MORSE:
                decoded_chars.append(REVERSE_MORSE[symbol])
            elif symbol:
                decoded_chars.append(f'[?{symbol}]')
        decoded_words.append(''.join(decoded_chars))

    return ' '.join(decoded_words)


def print_char_breakdown(text: str) -> None:
    """Show character-by-character Morse breakdown."""
    print(f"\n{'CHAR':<6} {'MORSE'}")
    print('-' * 20)
    for char in text.upper():
        if char == ' ':
            print(f"{'[SPC]':<6} /")
        elif char in MORSE_CODE:
            print(f"{char:<6} {MORSE_CODE[char]}")
        else:
            print(f"{char:<6} [unsupported]")


def main():
    print("=" * 50)
    print("       TEXT ↔ MORSE CODE CONVERTER")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Text  →  Morse Code")
        print("  2. Morse →  Text")
        print("  3. Exit")
        choice = input("\nChoose (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter text: ")
            if not text.strip():
                print("Input cannot be empty.")
                continue
            morse = text_to_morse(text)
            print(f"\nMorse Code : {morse}")
            show = input("Show character breakdown? (y/n): ").strip().lower()
            if show == 'y':
                print_char_breakdown(text)

        elif choice == '2':
            print("Enter Morse code (separate letters with space, words with ' / '):")
            morse = input("> ")
            if not morse.strip():
                print("Input cannot be empty.")
                continue
            decoded = morse_to_text(morse)
            print(f"\nDecoded Text : {decoded}")

        elif choice == '3':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
