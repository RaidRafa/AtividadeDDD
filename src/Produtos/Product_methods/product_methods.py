from src.Produtos.product_catalog import Produtos

listProducts = list()

pd1 = Produtos("Batom", "Passa na boca", 49.99, "LuizVitor")
pd2 = Produtos("Base", "Passa na cara", 149.90, "VitoriaSecredos")
pd3 = Produtos("Sombra", "Passa na cara", 180.90, "Abravanel")
pd4 = Produtos("Gloss", "Passa na cara", 25.90, "Channel")

listProducts.append(pd1)
listProducts.append(pd2)
listProducts.append(pd3)
listProducts.append(pd4)


def catalogo():
    print("---------- Lista de produtos ----------")
    for p in listProducts:
        print(f"""
            Produto: {p.name}
            Descrição: {p.descricao}
            Preço: {p.preco}
            Código: {p._token}""")
