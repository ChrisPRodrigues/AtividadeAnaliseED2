class HeapMaxima:

    def __init__(self):

        self.heap = []

        self.comparacoes = 0

    def vazia(self):
        return len(self.heap) == 0

    def inserir(self, paciente):

        self.heap.append(paciente)

        self.subir(len(self.heap) - 1)


    def subir(self, indice):

        pai = (indice - 1) // 2

        while indice > 0 and self.heap[indice].score > self.heap[pai].score:

            self.comparacoes += 1

            self.heap[indice], self.heap[pai] = (

                self.heap[pai],
                self.heap[indice]
            )

            indice = pai

            pai = (indice - 1) // 2


    def remover_maior(self):

        if len(self.heap) == 0:

            return None

        maior = self.heap[0]

        ultimo = self.heap.pop()

        if self.heap:

            self.heap[0] = ultimo

            self.descer(0)

        return maior


    def descer(self, indice):

        tamanho = len(self.heap)

        while True:

            maior = indice

            esquerda = 2 * indice + 1

            direita = 2 * indice + 2


            if esquerda < tamanho:

                self.comparacoes += 1

                if self.heap[esquerda].score > self.heap[maior].score:

                    maior = esquerda


            if direita < tamanho:

                self.comparacoes += 1

                if self.heap[direita].score > self.heap[maior].score:

                    maior = direita


            if maior == indice:

                break


            self.heap[indice], self.heap[maior] = (

                self.heap[maior],
                self.heap[indice]
            )

            indice = maior