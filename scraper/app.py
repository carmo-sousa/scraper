import typer
from rich import print
from rich.console import Console
from rich.table import Table

cli = typer.Typer()
console = Console()

# response = requests.post("https://argosscan.com/graphql", json=query, headers=header)
# project = response.json()["data"]["project"]

# project_orm = ProjectORM(
#     project_id=project["id"],
#     name=project["name"],
#     adult=project["adult"],
#     description=project["description"],
#     cover=project["cover"],
#     create_at=project["createAt"],
#     update_at=project["updateAt"],
# )

# project_model = ProjectModel.from_orm(project_orm)

# # print(project_model.dict())


@cli.command()
def obj(confirm: bool = typer.Option(True, prompt="Confirmar ação?")):
    if confirm:
        table = Table("Name", "Item")
        table.add_row("Rick", "Portal Gun")
        table.add_row("Morty", "Plumbus")
        console.print(table)
    else:
        print("Ação cancelada!")


if __name__ == "__main__":
    cli()
