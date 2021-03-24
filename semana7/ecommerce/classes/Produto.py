class Produto:
    def __init__(self, **kwargs):
        if kwargs.get('preco', 0) < 0:
            raise ValueError('Preço negativo')
        self.ean = kwargs.get('ean', '')
        self.preco = kwargs.get('preco', 0)

    def __str__(self):
        return self.ean

    def __repr__(self):
        return 'Produto:' + self.ean
