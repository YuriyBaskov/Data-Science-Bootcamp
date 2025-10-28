import sys

def caesar_cipher(text, shift, encode=True):
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            if encode:
                new_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                new_char = chr((ord(char) - start - shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")

# Извлекаются аргументы ком строки
    action = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])

    if any(char.isalpha() and not char.isascii() for char in text):
        raise Exception("Script does not support your language yet")

    if action == 'encode':
        print(caesar_cipher(text, shift, encode=True))
    elif action == 'decode':
        print(caesar_cipher(text, shift, encode=False))
    else:
        raise Exception("Invalid action. Use 'encode' or 'decode'.")

if __name__ == '__main__':
    main()