class Tokenizer():

    def __init__(self, string):
        self.string = string

        self.current_index = 0
        self.current_character = None

    def tokenize(self):
        char = self.string[self.current_index]
        self.current_character = char
        self.current_index += 1

        if char == '"':
            
            token = Token('STRING', )



# Token class
class Token():

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type} {self.value}"