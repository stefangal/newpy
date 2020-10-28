import click
from newpy.cli_builder import Builder


@click.command()
@click.option('--p',
              default='project',
              prompt='The project name: ',
              help='This will be the folder name & project name.')
@click.option('--license_type',
              default='mit',
              prompt='The license type: ',
              help="Choose license type")
def startnew(p, license_type):
    b = Builder(p, license_type)
    print(b.license_set)
    b.build_license(license_type)


# if __name__ == "__main__":
#     startnew()