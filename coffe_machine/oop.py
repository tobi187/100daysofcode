from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Charmander", "Machamp"])
table.add_column("types", ["electric", "fire", "fighting"])

table.align = "l"

print(table)