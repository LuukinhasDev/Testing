
import random


class SimuladorDeDado:
    def _init_(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um valor para o dado?"

    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!😁')
            else:
                print('Por favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao gerar sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()

simulador.iniciar()
