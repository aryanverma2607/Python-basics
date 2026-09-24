from rich import print
print("[red]Aryan[/red]")
print("[bold yellow][italic][underline]Student Information[/italic][/bold yellow][/underline]")

from rich.console import Console   #we can call print using object

console = Console()

console.print("[bold red]Hello Aryan[bold red]")
console.print()
console.print("aryan is a :PILE_OF_POO:")
console.log("Program started")

from rich.panel import Panel

console.print(Panel("Hello",title="Student Details",subtitle="Info",title_align="left",subtitle_align="center",style="Bold yellow",border_style="Bold green"))
console.rule("python")

from rich.table import Table
table=Table(title="student data")
table.add_column("name")
table.add_column("age")
table.add_column("class_of_student")

table.add_row("Aryan verma","20","7")
table.add_row("Niteen mandloi","21","11")
#print(table)
console.print(table)

from rich.progress import track
for i in track(range(1000),description="Processing...!"):   #by default description is working
    pass

from rich.traceback import install

install()