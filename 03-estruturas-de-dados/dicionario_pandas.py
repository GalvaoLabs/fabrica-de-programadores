import pandas as pd
import openpyxl
pessoa = {"nome": ["Carla", "Vanessa", "Enzo", "Luiz", "Maria", "Pedro", "Marianna", "Alice", "Aline", "Saulo"],
            "idade": [19, 31, 15, 15, 15, 16, 21, 13, 14, 41],
            "tamanho": [1.58, 1.81, 1.50, 1.56, 1.78, 1.80, 1.40, 1.79, 1.90, 1.93, 1.82]
            }

df = pd.DataFrame(pessoa)

df.to_excel("tabela.Excelxlsx", sheet_name="Aula Hebert", engine="openpyxl")

print("O arquivo foi salvo com sucesso")