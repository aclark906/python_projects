# def findAndReplace(text, oldText, newText):
#     return text.replace(oldText.lower(), newText)
    
def findAndReplace(text, oldText, newText):
    replacedText = ''
    i = 0

    while i in range(0, len(text)):
        if text[i:i + len(oldText)] == oldText:
            i = i + len(oldText)
            replacedText += newText
        else:
            replacedText += text[i]
            i = i + 1
    return replacedText

 



assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
