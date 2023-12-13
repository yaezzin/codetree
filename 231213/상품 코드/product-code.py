class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
# 1번 생성
product1 = Product("codetree", 50)

# 2번 생성
name, code = tuple(input().split())
product2 = Product(name, int(code))

# 출력
print('product', product1.code, 'is', product1.name)
print('product', product2.code, 'is', product2.name)