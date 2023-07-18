#!/usr/bin/env python
# coding: utf-8

# # Q.1  What is the name of the feature responsible for generating Regex objects?

# In most programming languages, the feature responsible for generating regular expression objects is commonly referred to as the "regular expression compiler" or the "regular expression engine." This feature is responsible for taking a regular expression pattern as input and generating a regex object or data structure that can be used for pattern matching operations.
# 
# The specific implementation and naming of this feature can vary depending on the programming language or library being used. For example:
# 
# In Python, the 're' module provides the regular expression functionality, and the 're.compile()' function is used to compile a regular expression pattern into a regex object.
# 
# While the naming and usage may vary, the underlying purpose of this feature remains the same: to generate regex objects from regular expression patterns for matching and manipulating text.

# # Q.2  Why do raw strings often appear in Regex objects?

# Raw strings, denoted by adding an 'r' prefix to a string literal (e.g., r"pattern"), are often used in regular expression (regex) objects for several reasons:
# 
# Escaping backslashes: In regex patterns, backslashes \ are often used to escape special characters or represent special sequences. However, in regular Python strings, backslashes are also used for escape sequences, such as \n for a newline. Using a raw string allows backslashes to be treated as literal characters, preventing unintended escape sequences and reducing the need for excessive escaping.
# 
# Readability and maintainability: Regex patterns can include many special characters and sequences, which can be visually cluttered and hard to read. Raw strings help improve readability by making the pattern more self-explanatory, as escape sequences and special characters are treated as literal text.
# 
# Consistency: Raw strings ensure consistency between the regex pattern as written and the actual regex engine interpretation. Without raw strings, additional backslashes would be required for escape sequences, leading to potential discrepancies between the pattern's appearance and its intended meaning.
# 
# For example, consider the regex pattern '\d{3}\s+\w+.' In a raw string, it would be represented as 'r"\d{3}\s+\w+".' Here, the raw string prevents accidental interpretation of the backslash and enhances readability.
# 
# It's worth noting that using raw strings in regex objects is not always necessary, especially when the pattern doesn't contain backslashes or special characters. However, it has become a common practice to use raw strings by default in regex patterns to minimize potential issues and improve code clarity.

# # Q3. What is the return value of the search() method?

# The search() method, commonly available in regular expression (regex) libraries or modules, is used to search for a pattern match within a given string. The return value of the search() method depends on the specific implementation and programming language being used. However, in most cases, the search() method returns an object or data structure that represents the result of the search.
# 
# In Python's re module, for example, the search() method returns a match object if a match is found, or None if no match is found. The match object contains information about the first occurrence of the pattern within the string, including the matched text, the start and end positions of the match, and any captured groups.

# In[1]:


import re

text = "Hello, World!"
pattern = r"World"

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match.")


# In this example, the search() method searches for the pattern "World" within the string "Hello, World!". If a match is found, the search() method returns a match object, and the "Match found!" message is printed. If no match is found, the search() method returns None, and the "No match." message is printed.
# 
# The specific properties and methods of the match object can vary between different regex implementations and programming languages. However, common properties include group(), start(), end(), and span() to retrieve information about the matched text and its position within the original string.

# # Q4. From a Match item, how do you get the actual strings that match the pattern?

# To retrieve the actual strings that match the pattern from a match object, you can use the group() method. The group() method is typically available in regular expression libraries or modules and allows you to access the matched text.
# 
# The group() method can be called without any arguments or with an optional argument specifying the group number. By default, calling group() without an argument returns the entire matched text. If you provide a group number as an argument, it returns the text matched by that specific capturing group.
# 
# Here's an example using Python's re module:

# In[2]:


import re

text = "Hello, World!"
pattern = r"(\w+), (\w+)"

match = re.search(pattern, text)
if match:
    full_match = match.group()  # Retrieves the entire match
    first_word = match.group(1)  # Retrieves the text matched by the first capturing group
    second_word = match.group(2)  # Retrieves the text matched by the second capturing group

    print("Full match:", full_match)
    print("First word:", first_word)
    print("Second word:", second_word)
else:
    print("No match.")


# In this example, the pattern (\w+), (\w+) captures two words separated by a comma and a space. The search() method is used to find the pattern within the string "Hello, World!". The group() method is then called to retrieve the matched text.

# You can access the matched text by calling group() on the match object and provide the appropriate group number for capturing groups if needed.

# # Q5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d), what does group zero cover? Group 2? Group 1?

# In the regex pattern r'(\d\d\d)-(\d\d\d-\d\d\d\d)', the groups are defined by the parentheses () in the pattern. Each set of parentheses creates a capturing group, and the groups are numbered starting from 1. The groups can be accessed using the group() method on a match object.
# 
# In this specific regex pattern:
# 
# Group 0 (or match.group(0)) represents the entire match of the pattern.
# 
# Group 1 (or match.group(1)) corresponds to the first capturing group (\d\d\d).
# 
# Group 2 (or match.group(2)) corresponds to the second capturing group (\d\d\d-\d\d\d\d).
# 
# Here's an example using Python to illustrate how these groups work:

# In[4]:


import re

text = "Phone: 123-456-7890"
pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'

match = re.search(pattern, text)
if match:
    print("Group 0 (Entire match):", match.group(0))
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
else:
    print("No match.")


# Group 0 (match.group(0)) represents the entire match of the pattern, which is the string "123-456-7890". Group 1 (match.group(1)) captures the first three digits "123", and Group 2 (match.group(2)) captures the remaining digits "456-7890".
# 
# By accessing different groups, you can extract specific parts of the matched text based on the defined capturing groups in the regex pattern.

# # Q6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell ,a regex that you want it to fit real parentheses and periods?

# To match literal parentheses and periods in a regex pattern, you need to escape them with a backslash (\). This tells the regex engine to interpret them as literal characters rather than special characters with their respective meanings.
# 
# Here's how you can indicate that you want to match real parentheses and periods in a regex pattern:
# 
# Matching parentheses: To match literal parentheses, use \( to match a left parenthesis and \) to match a right parenthesis.
# 
# For example:
# 
# To match the string "(example)", you can use the pattern \( followed by the pattern example and then \).
# Matching periods: To match a literal period, use \. in the regex pattern.
# 
# For example:
# 
# To match the string "example.com", you can use the pattern example\. followed by the pattern com.
# By escaping parentheses and periods with a backslash, you specify that you want to match the actual characters rather than using their special meaning in regular expressions.
# 
# Here's an example of using escaped parentheses and periods in Python:

# In[5]:


import re

text = "(example.com)"
pattern = r'\(example\.com\)'  # Escaping parentheses and period

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match.")


# In this example, the pattern \(example\.com\) is used to match the string "(example.com)". The backslashes escape the parentheses and period, ensuring they are treated as literal characters. If a match is found, the "Match found!" message is printed.
# 
# Remember to escape any special characters that you want to be treated as literals within your regex pattern to match them exactly as intended.

# # Q7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?

# The findall() method, available in regular expression (regex) libraries or modules, returns a list of matching strings or a list of string tuples based on the regex pattern and the presence of capturing groups in the pattern.
# 
# The return value of findall() depends on whether the regex pattern contains capturing groups:
# 
# If the pattern does not contain any capturing groups, findall() returns a list of matching strings. Each element in the list represents a separate match found in the input string.
# 
# If the pattern contains one or more capturing groups, findall() returns a list of string tuples. Each tuple represents a match, and each element within the tuple corresponds to a capturing group in the pattern.
# 
# To clarify, here's a breakdown of the return values:
# 
# List of Matching Strings (No Capturing Groups):
# 
# If the regex pattern does not contain any capturing groups, findall() returns a list of matching strings.
# 
# Each element in the list represents a separate match found in the input string.
# 
# The returned list contains the matched strings in the order they were found.
# 
# List of String Tuples (With Capturing Groups):
# 
# If the regex pattern contains one or more capturing groups (defined by parentheses ()), findall() returns a list of string tuples.
# 
# Each tuple represents a match found in the input string.
# 
# Each element within the tuple corresponds to a capturing group in the pattern.
# 
# The order of the tuples in the list corresponds to the order in which the matches were found.
# 
# Each tuple contains the captured strings for each capturing group in the pattern.
# Here's an example to illustrate the two cases:

# In[7]:


import re

text = "Hello, Alice and Bob! Nice to meet you both."
pattern_no_groups = r"\b[A-Z]\w+\b"  # Pattern without capturing groups
pattern_with_groups = r"\b([A-Z]\w+)\b"  # Pattern with capturing group

matches_no_groups = re.findall(pattern_no_groups, text)
matches_with_groups = re.findall(pattern_with_groups, text)

print("Matches without capturing groups:", matches_no_groups)
print("Matches with capturing groups:", matches_with_groups)


# In this example, the findall() method is used to find matches of two different regex patterns (pattern_no_groups and pattern_with_groups) in the given input text.
# 
# The first pattern (pattern_no_groups) does not contain capturing groups. Hence, findall() returns a list of matching strings: ['Hello', 'Alice', 'Bob', 'Nice'].
# The second pattern (pattern_with_groups) contains a capturing group. Therefore, findall() returns a list of string tuples, where each tuple contains the captured strings for the capturing group: ['Hello', 'Alice', 'Bob', 'Nice'].
# To summarize, the presence or absence of capturing groups in the regex pattern determines the structure of the return value from the findall() method.

# # Q8. In standard expressions, what does the | character mean?

# In regular expressions (regex), the | character, known as the pipe or alternation operator, is used to specify alternative matches. It allows you to create a pattern that matches either one expression or another.
# 
# The | character separates multiple expressions, and it matches either the expression on the left side or the expression on the right side. It behaves like a logical OR operator.
# 
# Here are a few examples to illustrate the usage of the | character:
# 
# Matching multiple words: Suppose you want to match either "apple" or "banana". The regex pattern would be apple|banana. This pattern will match either "apple" or "banana" wherever they appear in the text.
# 
# Matching variations of a word: If you want to match variations of a word, such as "color" or "colour", you can use the pattern colou?r. The ? quantifier makes the preceding character (u) optional, so it will match both "color" and "colour".
# 
# Matching multiple patterns within a larger expression: You can use the | character to specify alternative patterns within a larger regex. For example, the pattern (cat|dog) house will match either "cat house" or "dog house".
# 
# It's important to note that the | character has a precedence lower than most other regex operators. If you need to apply the alternation operator to a larger group of expressions, you may need to use parentheses to group them together. For example, (apple|banana) juice matches either "apple juice" or "banana juice".
# 
# In summary, the | character in regex allows you to create patterns with alternative matches, where the expression on the left or right side of the | character can be matched.

# # Q9. In regular expressions, what does the character stand for?

# In regular expressions, the | character, known as the pipe or alternation operator, represents logical OR. It is used to specify alternative matches between multiple expressions.
# 
# The | character allows you to create a pattern that matches either one expression or another. It separates multiple expressions and matches the pattern on the left side or the pattern on the right side.
# 
# Here are a few examples to illustrate the usage of the | character:
# 
# Matching multiple words: For example, the pattern apple|banana will match either "apple" or "banana". It looks for either "apple" or "banana" in the text being matched.
# 
# Matching variations of a word: You can use the | character to match variations of a word. For instance, the pattern colo(u|ur) matches either "color" or "colour". The (u|ur) part represents the choice between "u" and "ur".
# 
# Matching multiple patterns within a larger expression: The | character can be used to specify alternative patterns within a larger regular expression. For example, (cat|dog) house matches either "cat house" or "dog house". It looks for the pattern "cat" or "dog" followed by the word "house".
# 
# It's important to note that the | character has lower precedence than most other regex operators. If you need to apply the alternation operator to a larger group of expressions, you may need to use parentheses to group them together.
# 
# In summary, the | character in regular expressions represents logical OR, allowing you to specify alternative matches between expressions.

# # Q10.In regular expressions, what is the difference between the + and * characters?

# In regular expressions, the + and * characters are quantifiers used to specify the number of occurrences of the preceding element in a pattern. Here's the difference between the two:
# 
# + (Plus Quantifier): The + character specifies that the preceding element must occur one or more times in the input string. It matches one or more occurrences of the preceding element.
# 
# Example: The pattern a+ matches one or more occurrences of the letter "a". It would match strings like "a", "aa", "aaa", and so on.
# 
# * (Asterisk Quantifier): The * character specifies that the preceding element can occur zero or more times in the input string. It matches zero or more occurrences of the preceding element.
# 
# Example: The pattern a* matches zero or more occurrences of the letter "a". It would match strings like "", "a", "aa", "aaa", and so on.
# 
# To summarize:
# 
# + matches one or more occurrences of the preceding element.
# * matches zero or more occurrences of the preceding element.
# 
# It's important to note that the + and * quantifiers are greedy by default, meaning they match as many occurrences as possible. If you want to make them non-greedy and match as few occurrences as possible, you can append a ? after them. For example, +? and *? are non-greedy versions of + and * respectively.
# 
# Here's an example to illustrate the difference:

# In[8]:


import re

text = "abcaaa"

pattern_plus = r"a+"  # Matches one or more "a"
pattern_asterisk = r"a*"  # Matches zero or more "a"

matches_plus = re.findall(pattern_plus, text)
matches_asterisk = re.findall(pattern_asterisk, text)

print("Matches with '+':", matches_plus)
print("Matches with '*':", matches_asterisk)


# In this example, the input string is "abcaaa". The pattern a+ matches one or more occurrences of "a" and returns the matches "a" and "aaa". The pattern a* matches zero or more occurrences of "a" and returns all possible matches including empty strings and individual "a" characters.

# # Q11. What is the difference between {4} and {4,5} in regular expression?

# In regular expressions, {4} and {4,5} are quantifiers used to specify the exact number of occurrences of the preceding element in a pattern. Here's the difference between the two:
# 
# {4}: This quantifier specifies that the preceding element must occur exactly 4 times in the input string. It matches only if the preceding element is repeated exactly 4 times.
# 
# Example: The pattern a{4} matches strings where the letter "a" occurs exactly 4 times consecutively. It would match strings like "aaaa", but not "aa" or "aaaaa".
# 
# {4,5}: This quantifier specifies a range for the number of occurrences of the preceding element. It matches if the preceding element occurs between 4 and 5 times (inclusive) in the input string.
# 
# Example: The pattern a{4,5} matches strings where the letter "a" occurs between 4 and 5 times consecutively. It would match strings like "aaaa" and "aaaaa", but not "aa" or "aaaaaa".
# 
# To summarize:
# 
# {4} matches exactly 4 occurrences of the preceding element.
# {4,5} matches between 4 and 5 occurrences (inclusive) of the preceding element.
# These quantifiers allow you to specify precise repetition requirements for the preceding element in a regular expression pattern.

# In[9]:


import re

text = "aa aaa aaaa aaaaa"

pattern_exact = r"a{4}"  # Matches exactly 4 consecutive "a"
pattern_range = r"a{4,5}"  # Matches between 4 and 5 consecutive "a"

matches_exact = re.findall(pattern_exact, text)
matches_range = re.findall(pattern_range, text)

print("Matches with '{4}':", matches_exact)
print("Matches with '{4,5}':", matches_range)


# In this example, the input string is "aa aaa aaaa aaaaa". The pattern a{4} matches exactly 4 consecutive "a" and returns the match "aaaa". The pattern a{4,5} matches between 4 and 5 consecutive "a" and returns the matches "aaaa" and "aaaaa".

# # Q12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?

# In regular expressions, the shorthand character classes \d, \w, and \s are predefined character classes that represent common character categories. Here's what each of them signifies:
# 
# \d: This shorthand character class represents any digit character. It is equivalent to the character range [0-9]. It matches a single digit from 0 to 9.
# 
# Example: The pattern \d{3} matches any three consecutive digits.
# 
# \w: This shorthand character class represents any word character. It includes alphanumeric characters (letters and digits) and underscores. It is equivalent to the character range [a-zA-Z0-9_].
# 
# Example: The pattern \w+ matches one or more word characters, such as letters, digits, and underscores.
# 
# \s: This shorthand character class represents any whitespace character. It includes spaces, tabs, newlines, and other whitespace characters.
# 
# Example: The pattern \s+ matches one or more whitespace characters, such as spaces or tabs.
# 
# It's important to note that these shorthand character classes are based on ASCII characters by default. If you're working with Unicode text or need to match characters from specific Unicode categories, you may need to use additional flags or modifiers depending on the regex implementation.

# In[10]:


import re

text = "abc 123 _+."
pattern_digits = r"\d+"  # Matches one or more digits
pattern_word = r"\w+"  # Matches one or more word characters
pattern_whitespace = r"\s+"  # Matches one or more whitespace characters

matches_digits = re.findall(pattern_digits, text)
matches_word = re.findall(pattern_word, text)
matches_whitespace = re.findall(pattern_whitespace, text)

print("Matches with '\\d+':", matches_digits)
print("Matches with '\\w+':", matches_word)
print("Matches with '\\s+':", matches_whitespace)


# In this example, the input string is "abc 123 +.". The pattern \d+ matches the digits "123". The pattern \w+ matches the word characters "abc", "123", and "". The pattern \s+ matches the whitespace character (a space) between "abc" and "123".

# # Q13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

# In regular expressions, the shorthand character classes \D, \W, and \S are negated versions of their counterparts \d, \w, and \s. They represent character classes that are the negation or complement of the corresponding classes. Here's what each of them signifies:
# 
# \D: This shorthand character class represents any character that is not a digit. It is the negation of \d. It matches any character that is not in the range [0-9].
# 
# Example: The pattern \D+ matches one or more consecutive non-digit characters.
# 
# \W: This shorthand character class represents any character that is not a word character. It is the negation of \w. It matches any character that is not in the range [a-zA-Z0-9_].
# 
# Example: The pattern \W+ matches one or more consecutive non-word characters.
# 
# \S: This shorthand character class represents any character that is not a whitespace character. It is the negation of \s. It matches any character that is not a space, tab, newline, or other whitespace character.
# 
# Example: The pattern \S+ matches one or more consecutive non-whitespace characters.
# 
# The negated shorthand character classes \D, \W, and \S provide a convenient way to match characters that do not belong to specific character categories.
# 
# Here's an example to illustrate the usage of these negated shorthand character classes in Python:

# In[11]:


import re

text = "abc 123 _+."
pattern_non_digits = r"\D+"  # Matches one or more non-digit characters
pattern_non_word = r"\W+"  # Matches one or more non-word characters
pattern_non_whitespace = r"\S+"  # Matches one or more non-whitespace characters

matches_non_digits = re.findall(pattern_non_digits, text)
matches_non_word = re.findall(pattern_non_word, text)
matches_non_whitespace = re.findall(pattern_non_whitespace, text)

print("Matches with '\\D+':", matches_non_digits)
print("Matches with '\\W+':", matches_non_word)
print("Matches with '\\S+':", matches_non_whitespace)


# In this example, the input string is "abc 123 _+.". The pattern \D+ matches the consecutive non-digit characters "abc " and " +.". The pattern \W+ matches the consecutive non-word characters " ", " ", " ", and ".". The pattern \S+ matches the consecutive non-whitespace characters "abc", "123", and "+.".

# # Q14. What is the difference between .*? and .*?

# The difference between .*? and .* lies in their behavior as quantifiers in regular expressions. Both .*? and .* are used to match any character (except newline characters) in a non-greedy and greedy manner, respectively.
# 
# .*? (Non-greedy or lazy quantifier): The .*? quantifier matches any character (except newline) in a non-greedy manner. It matches as few characters as possible to allow the rest of the pattern to match.
# 
# Example: In the pattern a.*?b, if applied to the string "aababb", it will match "aab" since it matches as few characters as possible until it encounters the first "b".
# 
# .* (Greedy quantifier): The .* quantifier matches any character (except newline) in a greedy manner. It matches as many characters as possible while still allowing the rest of the pattern to match.
# 
# Example: In the pattern a.*b, if applied to the string "aababb", it will match "aababb" since it matches as many characters as possible until it reaches the last "b".
# 
# The primary distinction between .*? and .* is the greedy or non-greedy behavior when it comes to the number of characters matched. .*? matches the fewest possible characters, while .* matches the most possible characters.
# 
# It's important to note that the behavior of .*? and .* can vary depending on the specific regex engine or programming language being used. In some regex flavors, the behavior may be slightly different or require additional flags or modifiers to achieve non-greedy or greedy matching.

# # Q15. What is the syntax for matching both numbers and lowercase letters with a character class?

# To match both numbers and lowercase letters using a character class in regular expressions, you can use the range operator - within the character class to specify the desired range of characters. The syntax for matching numbers (0-9) and lowercase letters (a-z) in a character class is:

# [0-9a-z]
# 

# In this syntax:
# 
# 0-9 represents the range of numbers from 0 to 9.
# a-z represents the range of lowercase letters from a to z.
# By combining these ranges within square brackets, you create a character class that matches any character that is either a number or a lowercase letter.
# 
# Here are a few examples of how you can use this syntax:

# In[13]:


import re

text = "a1b2c3x4y5z"
pattern = r"[0-9a-z]+"

matches = re.findall(pattern, text)
print(matches)


# In this example, the input string is "a1b2c3x4y5z". The pattern [0-9a-z]+ matches one or more consecutive characters that are either numbers (0-9) or lowercase letters (a-z). The findall() function returns a list containing the matched string "a1b2c3x4y5z".
# 
# By using the range operator - within a character class, you can easily create a pattern that matches both numbers and lowercase letters.

# # Q16. What is the procedure for making a normal expression in regax case insensitive?

# To make a regular expression case-insensitive, you can use the appropriate flag or modifier depending on the regex implementation or programming language you are using. Here are the general procedures for making a regular expression case-insensitive:
# 
# Using Flags/Modifiers:
# 
# In most regex implementations, you can use a flag or modifier to indicate case insensitivity.
# 
# The specific flag or modifier may vary depending on the programming language or regex library being used.
# 
# Common flags/modifiers include i, x, or (?i).
# 
# Inline Modifiers:
# 
# Some regex implementations allow you to specify modifiers directly within the pattern using inline modifiers.
# 
# The specific syntax for inline modifiers may vary depending on the regex implementation.
# 
# Common inline modifiers include (?i) or (?i:pattern).
# 
# Here are examples using Python's re module to demonstrate the procedures:
# 
# 1.Using Flags/Modifiers:

# In[14]:


import re

text = "Hello, World!"
pattern = r"world"
flags = re.IGNORECASE  # or re.I

matches = re.findall(pattern, text, flags=flags)
print(matches)


# In this example, the re.IGNORECASE flag (or re.I) is passed as an argument to the flags parameter in the findall() method. It makes the pattern case-insensitive, allowing it to match "world" in a case-insensitive manner.
# 
# 2.Inline Modifiers:

# In[15]:


import re

text = "Hello, World!"
pattern = r"(?i)world"

matches = re.findall(pattern, text)
print(matches)


# In this example, the (?i) inline modifier is used within the pattern itself to specify case insensitivity. It makes the pattern "world" case-insensitive, allowing it to match "World" in the input string.
# 
# These are general procedures, but the specific syntax and usage may vary depending on the regex implementation or programming language you are using. Refer to the documentation of your specific regex library or language for more precise details on making regular expressions case-insensitive.

# # Q17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?

# In regular expressions, the . character (dot) normally matches any character except a newline character (\n). It matches a single character of any kind, except for newline characters.
# 
# However, if the re.DOTALL (or re.S) flag is passed as the second argument when compiling a regular expression using re.compile(), the behavior of the . character changes. In this case, the . character will match any character, including newline characters.
# 
# Let's illustrate this with an example using Python's re module:

# In[16]:


import re

text = "Hello\nWorld"

pattern_without_dotall = r".+"
pattern_with_dotall = r".+"
compiled_pattern_without_dotall = re.compile(pattern_without_dotall)
compiled_pattern_with_dotall = re.compile(pattern_with_dotall, re.DOTALL)

match_without_dotall = compiled_pattern_without_dotall.findall(text)
match_with_dotall = compiled_pattern_with_dotall.findall(text)

print("Match without DOTALL:", match_without_dotall)
print("Match with DOTALL:", match_with_dotall)


# In this example, the input text is "Hello\nWorld", which contains a newline character \n.
# 
# When using the pattern ".+" without the DOTALL flag, the . character matches any character except a newline. Thus, the match is limited to "Hello" since it stops at the newline character.
# 
# When using the pattern ".+" with the DOTALL flag, the . character matches any character, including a newline. As a result, the match includes the entire string "Hello\nWorld".
# 
# By passing the DOTALL flag to re.compile(), you can modify the behavior of the . character to match any character, including newline characters.

# # Q18. If numReg = re.compile('r\d+'), what will numRegex.sub('X','11 drummers, 10 pipers, five rings, 4) return?

# If numReg = re.compile(r'\d+'), the expression numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hens') will return the string 'X drummers, X pipers, five rings, X hens'.
# 
# Explanation:
# 
# re.compile(r'\d+') creates a regular expression pattern that matches one or more consecutive digits.
# 
# numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hens') replaces all occurrences of the digit sequences in the input string with the string 'X'.
# 
# In the given input string '11 drummers, 10 pipers, five rings, 4 hens', there are four digit sequences: "11", "10", "4".
# 
# Each of these digit sequences is replaced with the letter 'X', resulting in the string 'X drummers, X pipers, five rings, X hens'.

# # Q19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

# Passing re.VERBOSE as the second argument to re.compile() allows you to create regular expressions with increased readability by ignoring whitespace and adding comments within the pattern.
# 
# Here's what re.VERBOSE allows you to do:
# 
# Ignore Whitespace: The re.VERBOSE flag enables you to include whitespace within the regular expression pattern, which is then ignored when matching. This allows you to format and structure the pattern in a more readable manner.
# 
# Add Comments: With re.VERBOSE, you can add comments within the regular expression pattern using the # symbol. These comments are ignored during pattern matching and serve as explanatory notes for the pattern.
# 
# By using re.VERBOSE, you can make complex regular expressions more understandable by organizing them into multiple lines, adding indentation, and providing comments to explain the purpose of different parts of the pattern.
# 
# Here's an example to illustrate the usage of re.VERBOSE:

# In[17]:


import re

pattern = re.compile(r"""
    \d{3}     # Match three digits
    -         # Match a hyphen
    \d{3}     # Match three digits
    -         # Match a hyphen
    \d{4}     # Match four digits
""", re.VERBOSE)

text = "Phone: 123-456-7890"

match = pattern.search(text)
if match:
    print("Match found:", match.group())
else:
    print("No match.")


# In this example, the pattern re.compile(r"\d{3}-\d{3}-\d{4}", re.VERBOSE) matches a phone number in the format "123-456-7890". By using re.VERBOSE, the pattern is spread across multiple lines with comments explaining each part of the pattern.
# 
# The whitespace and comments are ignored during pattern matching, allowing for better readability and understanding of the pattern.
# 
# Using re.VERBOSE is particularly useful when working with complex regular expressions that may be difficult to comprehend in a single line.

# # Q20. How would you write a regex that match a number with comma for every three digits? 
# It must match the given following:
# 
# '42'
# 
# '1,234'
# 
# '6,368,745'
# 
# but not the following:
# '12,34,567' (which has only two digits between the commas)
# 
# '1234' (which lacks commas)

# To match a number with commas for every three digits, you can use the following regular expression:

# In[18]:


import re

pattern = r'^\d{1,3}(,\d{3})*$'

numbers = ['42', '1,234', '6,368,745', '12,34,567', '1234']

for number in numbers:
    match = re.match(pattern, number)
    if match:
        print(f"Match found: {number}")
    else:
        print(f"No match: {number}")


# Explanation:
# 
# ^\d{1,3} matches one to three digits at the beginning of the string.
# 
# (,\d{3})* matches zero or more occurrences of a comma followed by exactly three digits.
# 
# $ asserts the end of the string.
# 
# With this pattern, the regular expression matches numbers that start with one to three digits, followed by zero or more occurrences of a comma and exactly three digits. The pattern ensures that there are commas for every three digits in the number.
# 
# The example code demonstrates how the pattern matches the given numbers correctly while excluding the numbers that don't meet the comma pattern.
# 

# # Q21. How would you write a regex that matches the full name of someone whose last name is
# Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter.
# 
# The regex must match the following:
# 
# 'Haruto Watanabe'
# 
# 'Alice Watanabe'
# 
# 'RoboCop Watanabe'
# 
# but not the following:
# 
# 'haruto Watanabe' (where the first name is not capitalized)
# 
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 
# 'Watanabe' (which has no first name)
# 
# 'Haruto watanabe' (where Watanabe is not capitalized)

# # ANS
# To match the full name of someone whose last name is "Watanabe" and the first name is one word that begins with a capital letter, you can use the following regex pattern:

# ^[A-Z][a-zA-Z]*\sWatanabe$
# 

# Here's how the regex pattern breaks down:
# 
# ^: Matches the start of the string.
# [A-Z]: Matches an uppercase letter (the first letter of the first name).
#     
# [a-zA-Z]*: Matches zero or more lowercase or uppercase letters (the remaining letters of the first name).
#     
# \s: Matches a whitespace character (space).
#     
# Watanabe: Matches the last name "Watanabe".
#     
# $: Matches the end of the string.
#     
# This pattern ensures that the first name starts with a capital letter and is followed by only letters (uppercase or lowercase). The last name is fixed as "Watanabe".
# 
# Here's an example of how you could use this regex pattern in Python:

# In[20]:


import re

full_name = "Haruto Watanabe"
pattern = r"^[A-Z][a-zA-Z]*\sWatanabe$"

match = re.match(pattern, full_name)
if match:
    print("Match found!")
else:
    print("No match.")


# You can modify the full_name variable to test other names and see if they match the specified pattern.
# 
# 
# 
# 
# 

# # Q22. How would you write a regex that matches 
# a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# 
# 'Alice eats apples.'
# 
# 'Bob pets cats.'
# 
# 'Carol throws baseballs.'
# 
# 'Alice throws Apples.'
# 
# 'BOB EATS CATS.'
# 
# but not the following:
# 
# 'RoboCop eats apples.'
# 
# 'ALICE THROWS FOOTBALLS.'
# 
# 'Carol eats 7 cats.'

# # ANS

# To match the specified pattern using a regular expression (regex) with case-insensitivity, you can use the following pattern:

# "^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$ "

# Here's how the regex pattern breaks down:
# 
# ^: Matches the start of the sentence.
# 
# (Alice|Bob|Carol): Matches either "Alice", "Bob", or "Carol".
# 
# \s+: Matches one or more whitespace characters.
# 
# (eats|pets|throws): Matches either "eats", "pets", or "throws".
# 
# \s+: Matches one or more whitespace characters.
# 
# (apples|cats|baseballs): Matches either "apples", "cats", or "baseballs".
# 
# \.: Matches a period (escaped with a backslash).
# 
# $: Matches the end of the sentence.
# 
# To perform a case-insensitive match, you would use the appropriate flag or option provided by your programming language or regex engine.
# 
# Here's an example of how you could use this regex pattern in Python:

# In[21]:


import re

sentence = "Alice eats apples."
pattern = r"^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$"

match = re.match(pattern, sentence, re.IGNORECASE)
if match:
    print("Match found!")
else:
    print("No match.")


# 
# 
# You can modify the sentence variable to test other sentences and see if they match the specified pattern.

# In[ ]:




