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


    def altura(self):

        return self._altura(self.raiz)


    def _altura(self, no):

        if no is None:

            return 0

        esquerda = self._altura(no.esquerda)

        direita = self._altura(no.direita)

        return max(esquerda, direita) + 1