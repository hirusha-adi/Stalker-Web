from .specific_sites import chess_com
from .specific_sites import deezer
from .specific_sites import duolingo
from .specific_sites import github
from .specific_sites import gravatar
from .specific_sites import imgur
from .specific_sites import instagram
from .specific_sites import pinterest
from .specific_sites import pornhub
from .specific_sites import spotify
from .specific_sites import strava
from .specific_sites import twitter
from . import holehe_

module_functions = {
    "specific/chess_com": chess_com.start,
    "specific/deezer": deezer.start,
    "specific/duolingo": duolingo.start,
    "specific/github": github.start,
    "specific/gravatar": gravatar.start,
    "specific/imgur": imgur.start,
    "specific/instagram": instagram.start,
    "specific/pinterest": pinterest.start,
    "specific/pornhub": pornhub.start,
    "specific/spotify": spotify.start,
    "specific/strava": strava.start,
    "specific/twitter": twitter.start,
    "holehe": holehe_.start
}

def handler(sub_modules, args, is_interactive=True):
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str in module_functions:
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        module_functions[sub_modules_str](email=email)
    
    elif sub_modules_str == "specific/all":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        for module_function in module_functions:
            if module_function.startswith("specific/"):
                module_functions[module_function](email=email)
    
    # Use this as a template to extent in the future if required.
    # -----
    # elif sub_modules_str == "specific/module":
    #     if is_interactive:
    #         email = input("[?] Email: ")
    #     else:
    #         email = args[0]
    #     print(f"[*] Using Email: {email}")
    #     module.start(email=email)
    # -----
    
    else:
        print("Invalid sub_module provided.")
