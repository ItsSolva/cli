def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    
    color_code = colors.get(color.lower(), colors["reset"])
    print(f"{color_code}{text}{colors['reset']}")


def get_coverage_percentage(branch_coverage):
    total_branches = len(branch_coverage)
    executed_branches = sum([1 for value in branch_coverage.values() if value])
    return (executed_branches / total_branches) * 100