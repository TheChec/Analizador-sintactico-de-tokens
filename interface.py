import colorama
from colorama import Fore, Back, Style

def draw_broke_logo() -> None:
    colorama.init()
    text_color = Fore.BLUE
    bg_color = Back.BLACK
    text = 'Bienvenido a Broke, un identificador de tokens \npara aprender a reconocer e identificarlos'
    
    broke_logo = [
        f"                                                   {text_color}{bg_color}",
        f"  11111111   1111111    11111111  11   11  1111111 {text_color}{bg_color}",
        f"  111   111  11   111   11    11  11  11   11      {text_color}{bg_color}",
        f"  111   111  11   111   11    11  11  11   11      {text_color}{bg_color}",
        f"  1111111    1111111    11    11  1111     1111111 {text_color}{bg_color}",
        f"  111   111  11   111   11    11  11  11   11      {text_color}{bg_color}",
        f"  111   111  11   111   11    11  11  11   11      {text_color}{bg_color}",
        f"  11111111   11    111  11111111  11   11  111111  {text_color}{bg_color}",
        f"\n{text_color}{bg_color}{text}{Style.RESET_ALL}"
    ]
    print('\n'.join(broke_logo))