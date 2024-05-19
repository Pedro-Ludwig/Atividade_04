class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item, preco):
        self.itens.append({"item": item, "preco": preco})

    def remover_item(self):
        if self.itens:
            self.itens.pop()

    def total(self):
        return sum(item['preco'] for item in self.itens)

    def esta_vazio(self):
        return len(self.itens) == 0