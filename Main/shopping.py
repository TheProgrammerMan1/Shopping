language = input('PT-BR, EN-US, ES-AR: ').upper()

if language == 'PT-BR' or language == 'PT':
    product_list = [
        {'name': 'Arroz', 'price': 20.00, 'id': 1, 'amount': 1},
        {'name': 'Feijão', 'price': 10.00, 'id': 2, 'amount': 1},
        {'name': 'Batata', 'price': 0.5, 'id': 3, 'amount': 1},
        {'name': 'Bolacha', 'price': 3.30, 'id': 4, 'amount': 1}
    ]

    print('Produtos Disponiveis:')
    for product in product_list:
        price = product['price']
        name = product['name']
        print(f'{name}, {price:.2f}')


    def shopping_cart():
        global value1, value2, value3, value4

        cart = []
        item1 = input('Primeiro item: ').title()
        if item1 == 'Sair':
            print('Saiu')
            return
        amount1 = int(input('Quantidade: '))
        item2 = input('Segundo item: ').title()
        if item2 == 'Sair':
            print('Saiu')
            return
        amount2 = int(input('Quantidade: '))
        item3 = input('Terceiro item: ').title()
        if item3 == 'Sair':
            print('Saiu')
            return
        amount3 = int(input('Quantidade: '))
        item4 = input('Quarto item: ').title()
        if item4 == 'Sair':
            print('Saiu')
            return
        amount4 = int(input('Quantidade: '))

        if item1 == 'Arroz':
            item1 = product_list[0]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Feijão' or item1 == 'Feijao':
            item1 = product_list[1]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Batata':
            item1 = product_list[2]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Bolacha':
            item1 = product_list[3]
            cart.append(item1)
            value1 = item1['price'] * amount1

        else:
            print(f'{item1} não encontrado!')
            value1 = 0

        if item2 == 'Arroz':
            item2 = product_list[0]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Feijão' or item2 == 'Feijao':
            item2 = product_list[1]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Batata':
            item2 = product_list[2]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Bolacha':
            item2 = product_list[3]
            cart.append(item2)
            value2 = item2['price'] * amount2

        else:
            print(f'{item2} não encontrado!')
            value2 = 0

        if item3 == 'Arroz':
            item3 = product_list[0]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Feijão' or item3 == 'Feijao':
            item3 = product_list[1]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Batata':
            item3 = product_list[2]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Bolacha':
            item3 = product_list[3]
            cart.append(item3)
            value3 = item3['price'] * amount3

        else:
            print(f'{item3} não encontrado!')
            value3 = 0

        if item4 == 'Arroz':
            item4 = product_list[0]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Feijão' or item4 == 'Feijao':
            item4 = product_list[1]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Batata':
            item4 = product_list[2]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Bolacha':
            item4 = product_list[3]
            cart.append(item4)
            value4 = item4['price'] * amount4

        else:
            print(f'{item4} não encontrado!')
            value4 = 0

        def calc(product1, product2, product3, product4):
            the_total = product1 + product2 + product3 + product4
            if len(cart) > 1:
                print('Produtos escolhidos:')
                print([p['name'] for p in cart])
            print(f'O total da sua compra é R${the_total:.2f}')

        calc(value1, value2, value3, value4)


    shopping_cart()

elif language == 'EN-US' or language == 'EN':
    product_list = [
        {'name': 'Rice', 'price': 20 / 5.4, 'id': 1, 'amount': 1},
        {'name': 'Beans', 'price': 10 / 5.4, 'id': 2, 'amount': 1},
        {'name': 'Potato', 'price': 0.5 / 5.4, 'id': 3, 'amount': 1},
        {'name': 'Biscuit', 'price': 3.30 / 5.4, 'id': 4, 'amount': 1}
    ]

    print('Available products:')
    for product in product_list:
        price = product['price']
        name = product['name']
        print(f'{name}, {price:.2f}')


    def shopping_cart():
        global value1
        global value2
        global value3
        global value4

        cart = []
        item1 = input('First item: ').title()
        if item1 == 'exit':
            print('exited')
            return
        amount1 = int(input('First item amount: '))
        item2 = input('Second item: ').title()
        if item2 == 'exit':
            print('exited')
            return
        amount2 = int(input('Second item amount: '))
        item3 = input('Third item: ').title()
        if item3 == 'exit':
            print('exited')
            return
        amount3 = int(input('Third item amount: '))
        item4 = input('Fourth item: ').title()
        if item4 == 'exit':
            print('exited')
            return
        amount4 = int(input('Fourth item amount: '))

        if item1 == 'Rice':
            item1 = product_list[0]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Beans':
            item1 = product_list[1]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Potato':
            item1 = product_list[2]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Biscuit':
            item1 = product_list[3]
            cart.append(item1)
            value1 = item1['price'] * amount1

        else:
            print(f'{item1} not found!')
            value1 = 0

        if item2 == 'Rice':
            item2 = product_list[0]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Beans':
            item2 = product_list[1]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Potato':
            item2 = product_list[2]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Biscuit':
            item2 = product_list[3]
            cart.append(item2)
            value2 = item2['price'] * amount2

        else:
            print(f'{item2} not found!')
            value2 = 0

        if item3 == 'Rice':
            item3 = product_list[0]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Beans':
            item3 = product_list[1]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Potato':
            item3 = product_list[2]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Biscuit':
            item3 = product_list[3]
            cart.append(item3)
            value3 = item3['price'] * amount3

        else:
            print(f'{item3} not found!')
            value3 = 0

        if item4 == 'Rice':
            item4 = product_list[0]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Beans':
            item4 = product_list[1]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Potato':
            item4 = product_list[2]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Biscuit':
            item4 = product_list[3]
            cart.append(item4)
            value4 = item4['price'] * amount4

        else:
            print(f'{item4} not found!')
            value4 = 0

        def calc(product1, product2, product3, product4):
            the_total = product1 + product2 + product3 + product4
            if len(cart) > 1:
                print('Chosen products:')
                print([p['name'] for p in cart])
            print(f'Your total purchase is ${the_total:.2f}')

        calc(value1, value2, value3, value4)


    shopping_cart()

elif language == 'ES-AR' or language == 'ES':
    product_list = [
        {'name': 'Arroz', 'price': 20 * 15.99, 'id': 1, 'amount': 1},
        {'name': 'Frijol', 'price': 10 * 15.99, 'id': 2, 'amount': 1},
        {'name': 'Patata', 'price': 0.5 * 15.99, 'id': 3, 'amount': 1},
        {'name': 'Galleta', 'price': 3.30 * 15.99, 'id': 4, 'amount': 1}
    ]

    print('Productos disponibles:')
    for product in product_list:
        price = product['price']
        name = product['name']
        print(f'{name}, {price:.2f}')


    def shopping_cart():
        global value1
        global value2
        global value3
        global value4
        cart = []
        item1 = input('Primer elemento: ').title()
        if item1 == 'Salir':
            print('Salido')
            return
        amount1 = int(input('Cantidad del primer elemento: '))
        item2 = input('Segundo elemento: ').title()
        if item2 == 'Salir':
            print('Salido')
            return
        amount2 = int(input('Cantidad del segundo elemento: '))
        item3 = input('Tercer elemento: ').title()
        if item3 == 'Salir':
            print('Salido')
            return
        amount3 = int(input('Cantidad del tercer elemento: '))
        item4 = input('Cuarto elemento: ').title()
        if item4 == 'Salir':
            print('Salido')
            return
        amount4 = int(input('Cantidad del cuarto elemento: '))

        if item1 == 'Arroz':
            item1 = product_list[0]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Frijol':
            item1 = product_list[1]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Patata':
            item1 = product_list[2]
            cart.append(item1)
            value1 = item1['price'] * amount1

        elif item1 == 'Galleta':
            item1 = product_list[3]
            cart.append(item1)
            value1 = item1['price'] * amount1

        else:
            print(f'{item1} no encontrado!')
            value1 = 0

        if item2 == 'Arroz':
            item2 = product_list[0]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Frijol':
            item2 = product_list[1]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Patata':
            item2 = product_list[2]
            cart.append(item2)
            value2 = item2['price'] * amount2

        elif item2 == 'Galleta':
            item2 = product_list[3]
            cart.append(item2)
            value2 = item2['price'] * amount2

        else:
            print(f'{item2} no encontrado!')
            value2 = 0

        if item3 == 'Arroz':
            item3 = product_list[0]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Frijol':
            item3 = product_list[1]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Patata':
            item3 = product_list[2]
            cart.append(item3)
            value3 = item3['price'] * amount3

        elif item3 == 'Galleta':
            item3 = product_list[3]
            cart.append(item3)
            value3 = item3['price'] * amount3

        else:
            print(f'{item3} no encontrado!')
            value3 = 0

        if item4 == 'Arroz':
            item4 = product_list[0]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Frijol':
            item4 = product_list[1]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Patata':
            item4 = product_list[2]
            cart.append(item4)
            value4 = item4['price'] * amount4

        elif item4 == 'Galleta':
            item4 = product_list[3]
            cart.append(item4)
            value4 = item4['price'] * amount4

        else:
            print(f'{item4} no encontrado!')
            value4 = 0

        def calc(product1, product2, product3, product4):
            the_total = product1 + product2 + product3 + product4
            if len(cart) > 1:
                print('Productos elegidos:')
                print([p['name'] for p in cart])
            print(f'El total de su compra es AR${the_total:.2f}')

        calc(value1, value2, value3, value4)


    shopping_cart()
