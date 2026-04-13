"""
This is a stub for COMP16321 Python Skills.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here" and before the pass for that method.

Each method is documented to explain what work is to be placed within it.

NOTE: You can create as many more methods as you need. However, you need to add 
self as a parameter of the new method and  to call it with the prefix self.name 

"""

class Basics:#(s)
    # ---Section 1 --- #

    #(Task 1.1)
    def read_file(self) -> str:#(s)    
        """
            Read the contents of the text file paragraph.txt and return it as a single string.

            Returns: 
                str: The content of the text file as a single string
        """
        #Your code here
        file = open("paragraph.txt", "r")
        content = file.read()
        file.close()
        return content
        pass#(s)
    
    # ---Section 2 --- #

    #(Task 2.1)
    def length_of_file(self, file_string) -> int:#(s)
        """
            Calculates the total number of characters in the provided text string, including letters, numbers, symbols, and whitespace.
        
            Parameters:
                file_string (str): The text string from Task 1.1

            Returns:
                int: The total number of characters in the text string, counting all letters, numbers, symbols, and spaces.
        """
        #Your code here
        return len(file_string)
        pass#(s)

    #(Task 2.2)
    def lower_case_count(self, file_string) -> int:#(s)
        """
            Calculates the total number of lowercase letters (a-z) in the provided text string.

            Parameters:
                file_string (str): The text string from Task 1.1.

            Returns:
                int: The number of lowercase letters in the text string.
        """
        count = 0
        for char in file_string:
            if char.islower():
                count += 1

        return count
        pass#(s)
                

    #(Task 2.3)
    def upper_case_merge(self, file_string) -> str:#(s)
        """
            Finds all uppercase letters (A-Z) in the provided text string and merges them into a single string.

            For example, "thIs Sentence OF a feW wordS" will return "ISOFWS".

            Parameters:
                file_string (str): The text string from Task 1.1.

            Returns:
                str: A string containing all uppercase letters from the input text, merged together.
        """
        result = ""
        for char in file_string:
            if char.isupper():
                result += char
        return result
        pass#(s)

    #(Task 2.4)
    def digits_sum(self, file_string) -> int:#(s)
        """
            Sums all individual digits found in the provided text string.

            This method identifies all digits in the text string and treats each digit as an individual value. 
            For example, if the text contains '1' and '23', the sum will be 1 + 2 + 3, not 1 + 23.

            Parameters:
                file_string (str): The text string from Task 1.1.

            Returns:
                int: The sum of all individual digits in the text string.
        """
        #Your code here
        total = 0
        for char in file_string:
            if char.isdigit():
                total += int(char)
        return total
        pass#(s)

    # ---Section 3 --- #

    def load_dictionary(self):
        file = open("dictionary.txt", "r")
        words = file.read().split()
        file.close()

        dictionary_words = []
        for w in words:
            dictionary_words.append(w.lower())
        
        return dictionary_words

    def clean_word(self, word):
        cleaned = ""

        for char in word:
            if char.isalpha():
                cleaned += char
        
        return cleaned

    #(Task 3.1)
    def specific_character(self, file_string, word, letter) -> str|bool:#(s)
        """
            Returns the n'th letter of the m'th chunk of text in the paragraph if the chunk of text is found in the dictionary file.

            A word is considered valid if it exists in the dictionary.txt file, with a case-insensitive comparison. 
            Any punctuation (such as apostrophes or commas) should be removed before checking the word against the dictionary. 
            For example, "python's" would be treated as "pythons".

            Parameters:
                file_string (str): The text string from Task 1.1.
                word (int): The position of the word in the paragraph.
                letter (int): The position of the letter in the word.

            Returns:
                str: The letter at position 'letter' in the m'th word, if the word is valid and the input is correct.
                bool: False if the m'th word is not found in the dictionary or the input is invalid.
        """
        #Your code here
        chunks = file_string.split()
        dictionary_words = self.load_dictionary()

        if word < 1 or word > len(chunks):
            return False
        
        target_chunk = chunks[word - 1]
        cleaned = self.clean_word(target_chunk)

        if cleaned == "":
            return False
        
        if cleaned.lower() not in dictionary_words:
            return False
        
        return cleaned[letter - 1]

        pass#(s)

    #(Task 3.2)
    def word_display(self, file_string, length) -> list[str]:#(s)
        """
            Returns a list of all words in the text string that are of the specified length or longer.

            A word is considered valid if it exists in the dictionary.txt file, with a case-insensitive comparison. 
            Any punctuation (such as apostrophes or commas) should be removed before checking the word against the dictionary. 
            For example, "python's" would be treated as "pythons".

            Parameters:
                file_string (str): The text string from Task 1.1.
                length (int): The minimum length of words to include in the result.

            Returns:
                list[str]: A list of words that are of the specified length or longer, each word as an individual string.
        """
        # Your code here
        # 
        chunks = file_string.split()
        dictionary_words = self.load_dictionary()
        result = []

        for chunk in chunks:
            cleaned = self.clean_word(chunk)
        
            if cleaned != "" and cleaned.lower() in dictionary_words:
                if len(cleaned) >= length:
                    result.append(cleaned)

        return result

        pass#(s)

    #(Task 3.3)
    def letter_count(self, file_string, letters) -> int:#(s)
        """
            Returns the count of all letters (a-z), irrespective of case, excluding the specified letters.

            The specified letters, provided in the 'letters' parameter with a case-insensitive comparison, are ignored in the count.

            Parameters:
                file_string (str): The text string from Task 1.1.
                letters (list[str]): A list of letters (as strings) to exclude from the count.

            Returns:
                int: The count of all letters (a-z), excluding those specified in the 'letters' parameter.
        """
        #Your code here

        excluded_letters = []

        for item in letters:
            excluded_letters.append(item.lower())

        count = 0

        for char in file_string:
            if char.isalpha() and char.lower() not in excluded_letters:
                count += 1

        return count

        pass#(s)

    #(Task 3.4)
    def find_replace(self, file_string, old_substring, new_substring) -> str:#(s)
        """
            Finds all occurrences of a specified substring and replaces them with a new substring.

            This method directly replaces each occurrence of the old substring with the new one, with no additional changes to the text. If the old substring is not found, the text remains unchanged.

            Parameters:
                file_string (str): The text string from Task 1.1.
                old_substring (str): The substring to be replaced.
                new_substring (str): The substring that will replace the old one.

            Returns:
                str: The modified text with all occurrences of the old substring replaced by the new substring.
        """
        #Your code here
        return file_string.replace(old_substring, new_substring)
        pass#(s)


if __name__ == '__main__':#(s)
    #You can place any ad-hoc testing here, below are examples of how to do this.
    my_instance = Basics()
    
    text = my_instance.read_file()

    print("Length:", my_instance.length_of_file(text))
    print("Lowercase:", my_instance.lower_case_count(text))
    print("Uppercase:", my_instance.upper_case_merge(text))
    print("Digits sum:", my_instance.digits_sum(text))

    print("Specific char:", my_instance.specific_character(text, 1, 2))
    print("Words >= length:", my_instance.word_display(text, 5))
    print("Letter count (exclude a,b):", my_instance.letter_count(text, ["a", "b"]))
    print("Replace:", my_instance.find_replace(text, "Python", "Java"))

    pass#(s)