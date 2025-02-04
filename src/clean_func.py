import re

def emoji_clean(text):
    emoji_pattern = re.compile(
    "["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002500-\U00002BEF"  # chinese char
    u"\U0001F900-\U0001F9FF"  # supplemental symbols and pictographs
    u"\U0001FA70-\U0001FAFF"  # additional symbols
    "]+", flags=re.UNICODE)

    cleaned_chat_log = emoji_pattern.sub(r'', text)
    return cleaned_chat_log
