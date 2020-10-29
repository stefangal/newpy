import click
from newpy.cli_builder import Builder


@click.command()
@click.option('--p',
              default='project',
              prompt='The project name: ',
              help='This will be the folder name & project name.')
@click.option('--l',
              default='mit',
              prompt='The license type: ',
              help="Choose license type")
def startnew(p, l):
    build = Builder(p, l)
    build.build_license(l)


# if __name__ == "__main__":
#     startnew()
