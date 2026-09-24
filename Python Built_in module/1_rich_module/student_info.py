'''from rich import print'''
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console=Console()
console.print("[bold White]STUDENT INFORMATION SYSTEM[/bold white]")
console.rule("Student Details")

table=Table(title="[bold][italic][underline]Student Info[/underline][/bold][/italic]")
table.add_column("[bold white]Field[/bold white]")
table.add_column("[bold white]Information[/bold white]")
table.add_row("Name","[blue]Arjun Singh[/blue]")
table.add_row("Age","[blue]20[/blue]")
table.add_row("Course","[blue]B.tech CSE[/blue]")
table.add_row("Semester","[blue]7th[/blue]")
table.add_row("CGPA","[blue]6.93[/blue]")
console.print(table)

console.rule("[bold yellow]After using Panel[/bold yellow]")

console.print(Panel(table,title="[bold][underline]Student data[/underline][/bold]",title_align="center"))
console.rule(":cross_mark: Program ended :cross_mark:")