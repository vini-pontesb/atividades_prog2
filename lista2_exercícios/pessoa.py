class Pessoa:
    def __init__(self, nome, documento):
        self._nome = nome
        self._documento = documento


class Cliente(Pessoa):
    def __init__(self, codigo_cliente, nome_cliente, documento_cliente):
        self.codigo_cliente = codigo_cliente
        super().__init__(nome_cliente, documento_cliente)


class Vendedor(Pessoa):
    def __init__(self, comissao, nome_vendedor, documento_vendedor):
        self.comissao = comissao
        super().__init__(nome_vendedor, documento_vendedor)
