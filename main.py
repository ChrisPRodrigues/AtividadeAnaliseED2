import os
import time

from modelo import predict

from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL


# =========================
# gerar pacientes
# =========================

pacientes = []

for imagem in os.listdir("images") [:100]:

    if imagem.endswith(".jpg"):

        caminho = f"images/{imagem}"

        pred = predict(caminho)

        score = float(pred[0])

        paciente = Paciente(

            imagem,
            score
    )

        pacientes.append(paciente)


print(f"Pacientes carregados: {len(pacientes)}")


# =========================
# HEAP
# =========================

heap = HeapMaxima()

inicio = time.time()

for paciente in pacientes:

    heap.inserir(paciente)

fim = time.time()

tempo_heap = fim - inicio


# =========================
# ABB
# =========================

abb = ABB()

inicio = time.time()

for paciente in pacientes:

    abb.inserir(paciente)

fim = time.time()

tempo_abb = fim - inicio


# =========================
# AVL
# =========================

avl = AVL()

inicio = time.time()

for paciente in pacientes:

    avl.inserir(paciente)

fim = time.time()

tempo_avl = fim - inicio


# =========================
# resultados
# =========================

print("\n===== RESULTADOS =====\n")


print("HEAP")

print(f"Tempo: {tempo_heap:.6f}")

print(f"Comparações: {heap.comparacoes}")

print()


print("ABB")

print(f"Tempo: {tempo_abb:.6f}")

print(f"Comparações: {abb.comparacoes}")

print(f"Altura: {abb.altura()}")

print()


print("AVL")

print(f"Tempo: {tempo_avl:.6f}")

print(f"Comparações: {avl.comparacoes}")

print(f"Altura: {avl.altura()}")

print(f"Rotações: {avl.rotacoes}")