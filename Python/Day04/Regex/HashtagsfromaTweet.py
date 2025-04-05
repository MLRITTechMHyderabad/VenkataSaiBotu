import re
tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"
pattern = r'#[a-zA-Z0-9_]+'
matches = re.findall(pattern,tweet)
print(matches)