import re

def emoji_clean(text):
    emoji_pattern = re.compile(
    "["
    u"\U0001F600-\U0001F64F"  
    u"\U0001F300-\U0001F5FF"  
    u"\U0001F680-\U0001F6FF" 
    u"\U0001F1E0-\U0001F1FF" 
    u"\U00002500-\U00002BEF" 
    u"\U0001F900-\U0001F9FF"  
    u"\U0001FA70-\U0001FAFF" 
    "]+", flags=re.UNICODE)

    cleaned_chat_log = emoji_pattern.sub(r'', text)
    return cleaned_chat_log
