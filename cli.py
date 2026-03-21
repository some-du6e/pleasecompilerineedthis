import click
import components.compiler as compilefr
import components.repl as replfr


def repl_loop(passthrough: str = ""):
    replfr.repl(passthrough)


@click.command()
@click.option('--repl', default=True, help='Make repl like thing idk how to name this')
@click.option('-c', help='File to compile')
@click.option('-o', default="output.py", help='Output file')
@click.option('--repl-passthrough', default="", help='Text to pass through to the REPL and run it (useful for llms)')
@click.option("--run", is_flag=True, help="Run the file after compiling it")
def cli(repl: bool, c: str, o: str, run: bool, repl_passthrough: str):
    if o and not c and not repl:
        print("U need to specify a file to compile if you want to specify an output file")
    if c:
        compilefr.compile(c, o, run)
        return
    if repl:
        repl_loop(repl_passthrough)
if __name__ == '__main__':
    cli()