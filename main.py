from brain import Fuffy
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.live import Live

fuffy = Fuffy()
console = Console()

console.print(Panel.fit("[bold green]🤖 Fuffy is running![/bold green] Type something or type [red]exit[/red] to quit.", title="Welcome", border_style="green"))

while True:
    try:
        user_input = Prompt.ask("[bold blue]🧑‍💻 You[/bold blue]")
        if user_input.lower() in ["exit", "quit"]:
            console.print(Panel.fit("[bold red]Goodbye![/bold red] 👋", border_style="red"))
            break

        with Live(Spinner("dots", text="Fuffy is thinking..."), refresh_per_second=10):
            reply = fuffy.think(user_input)

        assistant_text = Text("Fuffy: ", style="bold magenta") + Text(reply)
        console.print(Panel.fit(assistant_text, title="🤖 Assistant", border_style="magenta"))

    except KeyboardInterrupt:
        console.print("\n[bold red][!] Terminated by the user.[/bold red]")
        break