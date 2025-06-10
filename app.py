from modelos.OOP import Restaurante

restaurante_hamburgueria = Restaurante('Burguer King', 'Hamburgueria')
restaurante_hamburgueria.receber_avaliacao('Mateus', 8)

restaurante_hamburgueria.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
