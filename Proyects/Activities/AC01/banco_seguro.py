from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        Cliente.__init__(self, id_cliente, nombre, contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.saldo

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.saldo = nuevo_saldo
        else:
            self.tiene_fraude = True

    def deposito_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            self.depositar(dinero)
            archivo.write(self.id_cliente + ", deposita, " + str(dinero))
        archivo.close()

    def retiro_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            if not self.tiene_fraude:
                self.retirar(dinero)
                archivo.write(self.id_cliente +", retira, " + str(dinero))


class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        BancoDCC.__init__(self)

    def cargar_clientes(self, ruta):
        with open(ruta, 'rt', encoding='utf-8') as archivo:
            for linea in archivo:
                lista_cliente = linea.strip().split(", ")
                if lista_cliente[2].isdigit():
                    cliente = ClienteSeguro(lista_cliente[0], lista_cliente[1], lista_cliente[3])
                    cliente.saldo_actual = float(lista_cliente[2])
                    self.clientes.append(cliente)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        for cliente in self.clientes:
            if (cliente.id_cliente == id_cliente) and (accion == "retira"):
                cliente.retiro_seguro(int(dinero))
            elif (cliente.id_cliente == id_cliente) and (accion == "deposito"):
                cliente.deposito_seguro(int(dinero))

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        # completar
        pass

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        # completar
        pass
