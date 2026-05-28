class NoAVL:

    def __init__(self, paciente):

        self.paciente = paciente

        self.esquerda = None

        self.direita = None

        self.altura = 1


class AVL:

    def __init__(self):

        self.raiz = None

        self.comparacoes = 0

        self.rotacoes = 0


    def altura_no(self, no):

        if not no:

            return 0

        return no.altura


    def fator_balanceamento(self, no):

        if not no:

            return 0

        return (

            self.altura_no(no.esquerda)
            -
            self.altura_no(no.direita)
        )


    def rotacao_direita(self, y):

        self.rotacoes += 1

        x = y.esquerda

        t2 = x.direita

        x.direita = y

        y.esquerda = t2

        y.altura = 1 + max(

            self.altura_no(y.esquerda),

            self.altura_no(y.direita)
        )

        x.altura = 1 + max(

            self.altura_no(x.esquerda),

            self.altura_no(x.direita)
        )

        return x


    def rotacao_esquerda(self, x):

        self.rotacoes += 1

        y = x.direita

        t2 = y.esquerda

        y.esquerda = x

        x.direita = t2

        x.altura = 1 + max(

            self.altura_no(x.esquerda),

            self.altura_no(x.direita)
        )

        y.altura = 1 + max(

            self.altura_no(y.esquerda),

            self.altura_no(y.direita)
        )

        return y


    def inserir(self, paciente):

        self.raiz = self._inserir(

            self.raiz,
            paciente
        )


    def _inserir(self, no, paciente):

        if not no:

            return NoAVL(paciente)


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


        no.altura = 1 + max(

            self.altura_no(no.esquerda),

            self.altura_no(no.direita)
        )


        balanceamento = self.fator_balanceamento(no)


        if balanceamento > 1 and paciente.score < no.esquerda.paciente.score:

            return self.rotacao_direita(no)


        if balanceamento < -1 and paciente.score > no.direita.paciente.score:

            return self.rotacao_esquerda(no)


        if balanceamento > 1 and paciente.score > no.esquerda.paciente.score:

            no.esquerda = self.rotacao_esquerda(no.esquerda)

            return self.rotacao_direita(no)


        if balanceamento < -1 and paciente.score < no.direita.paciente.score:

            no.direita = self.rotacao_direita(no.direita)

            return self.rotacao_esquerda(no)


        return no


    def altura(self):

        return self.altura_no(self.raiz)