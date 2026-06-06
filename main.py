import os
import time
import csv
from tqdm import tqdm

from modelo import predict
from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL


# =========================
# GERAR PACIENTES
# =========================

pacientes = []

imagens = [
    img
    for img in os.listdir("images")
    if img.endswith(".jpg")
][:1000]

print("Gerando scores...\n")

for imagem in tqdm(imagens, desc="Processando imagens"):

    caminho = os.path.join("images", imagem)

    pred = predict(caminho)

    score = float(pred[0])

    paciente = Paciente(
        imagem,
        score
    )

    pacientes.append(paciente)

print(f"\nPacientes carregados: {len(pacientes)}")

# =========================
# PACIENTES.CSV
# =========================

with open(
    "pacientes.csv",
    "w",
    newline="",
    encoding="utf-8"
) as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "ID_Imagem",
        "Score"
    ])

    for paciente in pacientes:

        escritor.writerow([
            paciente.id_imagem,
            paciente.score
        ])

print("pacientes.csv gerado")

# =========================
# HEAP
# =========================

heap = HeapMaxima()

inicio = time.perf_counter()

for paciente in tqdm(
    pacientes,
    desc="Inserindo Heap"
):
    heap.inserir(paciente)

fim = time.perf_counter()

tempo_heap_insercao = (
    fim - inicio
) * 1000


inicio = time.perf_counter()

ordem_heap = []

while not heap.vazia():

    ordem_heap.append(
        heap.remover_maior()
    )

fim = time.perf_counter()

tempo_heap_ordem = (
    fim - inicio
) * 1000


# =========================
# ABB
# =========================

abb = ABB()

inicio = time.perf_counter()

for paciente in tqdm(
    pacientes,
    desc="Inserindo ABB"
):
    abb.inserir(paciente)

fim = time.perf_counter()

tempo_abb_insercao = (
    fim - inicio
) * 1000


inicio = time.perf_counter()

ordem_abb = abb.em_ordem_inversa()

fim = time.perf_counter()

tempo_abb_ordem = (
    fim - inicio
) * 1000


# =========================
# AVL
# =========================

avl = AVL()

inicio = time.perf_counter()

for paciente in tqdm(
    pacientes,
    desc="Inserindo AVL"
):
    avl.inserir(paciente)

fim = time.perf_counter()

tempo_avl_insercao = (
    fim - inicio
) * 1000


inicio = time.perf_counter()

ordem_avl = avl.em_ordem_inversa()

fim = time.perf_counter()

tempo_avl_ordem = (
    fim - inicio
) * 1000

# =========================
# PACIENTE PRIORITÁRIO
# =========================

# Heap
inicio = time.perf_counter()

paciente_heap = ordem_heap[0]

fim = time.perf_counter()

tempo_heap_prioritario = (
    fim - inicio
) * 1000


# ABB
inicio = time.perf_counter()

paciente_abb = abb.maior()

fim = time.perf_counter()

tempo_abb_prioritario = (
    fim - inicio
) * 1000


# AVL
inicio = time.perf_counter()

paciente_avl = avl.maior()

fim = time.perf_counter()

tempo_avl_prioritario = (
    fim - inicio
) * 1000

# =========================
# GERAR ORDEM_ATENDIMENTO.TXT
# =========================

with open(
    "ordem_atendimento.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write(
        "Posicao,ID_Imagem,Score\n"
    )

    for posicao, paciente in enumerate(
        ordem_heap,
        start=1
    ):

        arquivo.write(
            f"{posicao},"
            f"{paciente.id_imagem},"
            f"{paciente.score:.6f}\n"
        )


# =========================
# RESULTADOS.TXT
# =========================

with open(
    "resultados.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write("===== HEAP =====\n")
    arquivo.write(
        f"Insercao: {tempo_heap_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_heap_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritario: {tempo_heap_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Comparacoes: {heap.comparacoes}\n\n"
    )

    arquivo.write("===== ABB =====\n")
    arquivo.write(
        f"Insercao: {tempo_abb_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_abb_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritario: {tempo_abb_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Comparacoes: {abb.comparacoes}\n"
    )
    arquivo.write(
        f"Altura: {abb.altura()}\n\n"
    )

    arquivo.write("===== AVL =====\n")
    arquivo.write(
        f"Insercao: {tempo_avl_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_avl_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritario: {tempo_avl_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Comparacoes: {avl.comparacoes}\n"
    )
    arquivo.write(
        f"Altura: {avl.altura()}\n"
    )
    arquivo.write(
        f"Rotacoes: {avl.rotacoes}\n"
    )


# =========================
# MOSTRAR RESULTADOS
# =========================

print("\n===== RESULTADOS =====\n")

print("HEAP")
print(f"Inserção: {tempo_heap_insercao:.4f} ms")
print(f"Ordem: {tempo_heap_ordem:.4f} ms")
print(f"Prioritário: {tempo_heap_prioritario:.6f} ms")
print(f"Comparações: {heap.comparacoes}")

print()

print("ABB")
print(f"Inserção: {tempo_abb_insercao:.4f} ms")
print(f"Ordem: {tempo_abb_ordem:.4f} ms")
print(f"Prioritário: {tempo_abb_prioritario:.6f} ms")
print(f"Comparações: {abb.comparacoes}")
print(f"Altura: {abb.altura()}")

print()

print("AVL")
print(f"Inserção: {tempo_avl_insercao:.4f} ms")
print(f"Ordem: {tempo_avl_ordem:.4f} ms")
print(f"Prioritário: {tempo_avl_prioritario:.6f} ms")
print(f"Comparações: {avl.comparacoes}")
print(f"Altura: {avl.altura()}")
print(f"Rotações: {avl.rotacoes}")

print("\nArquivos gerados:")
print("- ordem_atendimento.txt")
print("- resultados.txt")