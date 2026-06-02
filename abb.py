class NoABB:

    def __init__(self, paciente):

        self.paciente = paciente

        self.esquerda = None

        self.direita = None


class ABB:

    def __init__(self):

        self.raiz = None

        self.comparacoes = 0


    def inserir(self, paciente):

        self.raiz = self._inserir(

            self.raiz,
            paciente
        )

    def buscar(self, score):
        return self._buscar(self.raiz, score)


    def _buscar(self, no, score):

        if no is None:
            return None

        self.comparacoes += 1

        if score == no.paciente.score:
            return no.paciente

        if score < no.paciente.score:
            return self._buscar(no.esquerda, score)

        return self._buscar(no.direita, score)

    def _inserir(self, no, paciente):

        if no is None:
            return NoABB(paciente)

        self.comparacoes += 1

        if paciente.score < no.paciente.score:
            no.esquerda = self._inserir(
                no.esquerda,
                paciente
            )

        else:
            no.direita = self._inserir(
                no.direita,
                paciente
            )
        return no

    def remover(self, score):
        self.raiz = self._remover(self.raiz, score)


    def _remover(self, no, score):

        if no is None:
            return None

        if score < no.paciente.score:

            no.esquerda = self._remover(
                no.esquerda,
                score
            )

        elif score > no.paciente.score:

            no.direita = self._remover(
                no.direita,
                score
            )

        else:

            if no.esquerda is None:
                return no.direita

            if no.direita is None:
                return no.esquerda

            sucessor = self._menor(no.direita)

            no.paciente = sucessor.paciente

            no.direita = self._remover(
                no.direita,
                sucessor.paciente.score
            )

        return no


    def _menor(self, no):

        while no.esquerda:
            no = no.esquerda
        return no

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0
        
        esquerda = self._altura(no.esquerda)
        direita = self._altura(no.direita)

        return max(esquerda, direita) + 1

    def em_ordem_inversa(self):

        resultado = []

        self._em_ordem_inversa(
            self.raiz,
            resultado
        )

        return resultado


    def _em_ordem_inversa(self, no, resultado):

        if no is None:
            return

        self._em_ordem_inversa(
            no.direita,
            resultado
        )

        resultado.append(no.paciente)

        self._em_ordem_inversa(
            no.esquerda,
            resultado
        )