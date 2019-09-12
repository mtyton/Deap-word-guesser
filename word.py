import random


def get_available_chars():
    chars = []
    for a in range(65, 91):
        chars.append(chr(a))
    for a in range(97,123):
        chars.append(chr(a))
    chars.append("_")
    return chars


AVAILABLE_CHARS = get_available_chars()


class Word:

    @staticmethod
    def randomize(length):
        content = []
        for i in range(0, length):
            number = random.randint(0, len(AVAILABLE_CHARS)-1)
            content += AVAILABLE_CHARS[number]
        return content
