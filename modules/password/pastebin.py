from utils import search_google
from utils import errors


@errors.handle_errors
def start(password: str):
    search_google(f'site:pastebin.com "{password}"')
    