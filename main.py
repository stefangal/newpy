import click
from newpy.cli_builder import Builder


@click.command()
@click.option('--p',
              default='project',
              prompt='The project name: ',
              help='This will be the folder name & project name.')
def startnew(p):
    Builder(p)


# if __name__ == "__main__":
#     startnew()