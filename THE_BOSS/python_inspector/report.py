from rich.console import Console
from rich.panel import Panel
from rich.table import Table
c= Console()
def generate_report(path,files,analysis=None,error=None,test=None):
    c.print(Panel(
            "Python INSPECTOR",
            title="PROJECT ANALYSIS",
            border_style="green")
    )
    #file ka info
    c.print("[bold] PATH :[/bold]", path)
    c.print(Panel("PYTHON FILES FOUND",
            title="FIle INFORMATION",
            border_style="blue")
            )
    for i in files:
        c.print(f"-> {i}")
    #identifiers 
    if analysis:
        c.print(Panel("identifiers",
                      title="identifiers analysis",
                      border_style="cyan")
                      )
        t=Table()
        t.add_column("category")
        t.add_column("count")
        t.add_column("names")
        t.add_row("Functions", str(len(analysis["functions"])),", ".join(analysis["functions"]))
        t.add_row("Classes", str(len(analysis["classes"])),", ".join(analysis["classes"]))
        t.add_row("Variables", str(len(analysis["variables"])),", ".join(analysis["variables"]))
        t.add_row("Parameters", str(len(analysis["parameters"])),", ".join(analysis["parameters"]))
        t.add_row("Imports", str(len(analysis["imports"])),", ".join(analysis["imports"]))
        t.add_row("Function / Method Calls", str(len(analysis["calls"])),", ".join(analysis["calls"]))
        c.print(t)
    if error:
        c.print(Panel("error",
              title="error analysis",
              border_style="red")
              )
        for k,v in error.items():
                    c.print(f"[bold]{k.title()}:[/bold]{v}")
    if test:
        c.print(Panel("code testing",
              title=" code testing",
              border_style="yellow")
              )
        for k,v in test.items():
            c.print(f"[bold]{k.title()}:[/bold]{v}")
    c.print(Panel("analysis completed",
              title="END OF REPORT",
              border_style="green")
              )
