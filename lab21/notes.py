class Invoice:
    def __init__(self,vat):
        self.vat = vat

    def print_item(self, name, price):
        print(f'{name}: {self.with_vat(price)}')

    def with_vat(self, price):
        return price * (1 + self.vat)


i = Invoice(0.17)

i.print_item('iPhone',3000)
i.print_item('Samsung', 3120)

