import language_tool_python

tool=language_tool_python.LanguageTool("en-US")

matches = tool.check("He is going to school.")
corrected=tool.correct("He go to school.")
print("Before correction: he go to school")
print("After correction:",corrected)
print(matches)

match=tool.check("I am a student")
if match==[]:
    print("no error found")
else:
    print(match)
