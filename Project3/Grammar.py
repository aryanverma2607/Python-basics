import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

def grammar_check(text):
    matches=tool.check(text)
    results=[]
    for match in matches:
        result={
            "message":match.message,
            "replacements":match.replacements,
            "context":match.context,
            "category":match.category
        }
        results.append(result)
    correct=tool.correct(text)
    return results,correct
