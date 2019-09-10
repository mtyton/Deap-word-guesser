import random

AVAILABLE_CHARS = [chr(a) for a in range(65, 90)]


class Word:

    @staticmethod
    def randomize(length):
        content = []
        for i in range(0, length):
            number = random.randint(0,24)
            content += AVAILABLE_CHARS[number]
        return content
