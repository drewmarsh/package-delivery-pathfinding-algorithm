import random

class Style:
    # Colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    PINK = "\033[1;95m"
    ORANGE = "\033[38;5;208m"
    COLORS = [RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, PINK, ORANGE] # Array of all the colors

    # Formats
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    # Takes any text and desired effect and colors or formats it accordingly
    def set_style(text, effect):
        return f"{effect}{text}{Style.RESET}"
    
    # Takes any text and returns it with each character being randomly colored
    def generate_raindow_style(text):
        colored_asterisks = [random.choice(Style.COLORS) + char + Style.RESET for char in text]
        return ''.join(colored_asterisks)
    
    # Prints a seperator made up of randomly colored asterisks. Improves readability of the CLI by seperating different sections
    def print_seperator():
        asterisks = '*' * 120
        print("\n" + Style.generate_raindow_style(asterisks) + "\n")

    # Takes a datetime value and returns it in HH:MM:SS format and with a cyan color
    def format_time_string(time):
        time = time.strftime('%H:%M:%S')
        return Style.set_style(time, Style.CYAN)