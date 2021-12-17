class Trimmer():

    def __init__(self, string) -> None:
        self.ignored_characters = ['\n', '\t']

        # Add a space to the end of each line
        # Makes the trimming process easier
        string = string.split('\n')
        string = [line + ' ' for line in string]
        string = ''.join(string)

        self.line = list(string)
        self.characters = []

        self.last_character = None
        self.current_character = None
        self.current_index = 0

        self.in_string = False

    def trim_character(self):
        self.last_character = self.current_character
        char = self.line[self.current_index] # Get the current character
        self.current_character = char # Set the current character
        self.current_index += 1 # Increment the current index

        if self.in_string: # If trimmer is in a string
            self.characters.append(char)
            if char == '"': # Exiting the string
                self.in_string = False
            return

        if char == '"': # Entering a string
            self.in_string = True
            self.characters.append(char)
            return

        if char in self.ignored_characters: # Skip if character is ignored
            return
        
        if char == ' ' and self.last_character == ' ':
            return

        self.characters.append(char)

    def trim(self):
        for i in range(0, len(self.line)):
            self.trim_character()
        return self.characters

    def __str__(self):
        return ''.join(self.characters)