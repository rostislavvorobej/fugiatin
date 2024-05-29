from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "cyan",
    "warning": "magenta",
    "error": "red",
    "success": "green",
})
console = Console(theme=custom_theme)

console.print(f'\n============================================= example =============================================', style="info")
