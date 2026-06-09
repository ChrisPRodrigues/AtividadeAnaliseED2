import os
import time
import csv
from tqdm import tqdm

from modelo import predict
from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL

import matplotlib.pyplot as plt

# Gera os pacientes.

pacientes = []

imagens = [
    img
    for img in os.listdir("images")
    if img.endswith(".jpg")
]

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

# PACIENTES.CSV.

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

# HEAP.

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

# Gera o arquivo com a ordem de atendimento usando a heap.

with open(
    "ordem_heap.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write("Posicao,ID_Imagem,Score\n")

    for posicao, paciente in enumerate(
        ordem_heap,
        start=1
    ):

        arquivo.write(
            f"{posicao},"
            f"{paciente.id_imagem},"
            f"{paciente.score:.6f}\n"
        )

# ABB.

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

# Gera o arquivo com a ordem de atendimento usando a ABB.

with open(
    "ordem_abb.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write("Posicao,ID_Imagem,Score\n")

    for posicao, paciente in enumerate(
        ordem_abb,
        start=1
    ):

        arquivo.write(
            f"{posicao},"
            f"{paciente.id_imagem},"
            f"{paciente.score:.6f}\n"
        )

# AVL.

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

# Gera o arquivo com a ordem de atendimento usando a AVL.

with open(
    "ordem_avl.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write("Posicao,ID_Imagem,Score\n")

    for posicao, paciente in enumerate(
        ordem_avl,
        start=1
    ):

        arquivo.write(
            f"{posicao},"
            f"{paciente.id_imagem},"
            f"{paciente.score:.6f}\n"
        )

# PACIENTE PRIORITÁRIO.
# Heap.
inicio = time.perf_counter()

paciente_heap = ordem_heap[0]

fim = time.perf_counter()

tempo_heap_prioritario = (
    fim - inicio
) * 1000

# ABB.
inicio = time.perf_counter()

paciente_abb = abb.maior()

fim = time.perf_counter()

tempo_abb_prioritario = (
    fim - inicio
) * 1000

# AVL.
inicio = time.perf_counter()

paciente_avl = avl.maior()

fim = time.perf_counter()

tempo_avl_prioritario = (
    fim - inicio
) * 1000

# REMOÇÃO DO PRIORITÁRIO.
# Heap.
heap_remocao = HeapMaxima()

for paciente in pacientes:
    heap_remocao.inserir(paciente)

inicio = time.perf_counter()

heap_remocao.remover_maior()

fim = time.perf_counter()

tempo_heap_remocao = (
    fim - inicio
) * 1000

# ABB.
abb_remocao = ABB()

for paciente in pacientes:
    abb_remocao.inserir(paciente)

maior_abb = abb_remocao.maior()

inicio = time.perf_counter()

abb_remocao.remover(maior_abb.score)

fim = time.perf_counter()

tempo_abb_remocao = (
    fim - inicio
) * 1000

# AVL.
avl_remocao = AVL()

for paciente in pacientes:
    avl_remocao.inserir(paciente)

maior_avl = avl_remocao.maior()

inicio = time.perf_counter()

avl_remocao.remover(maior_avl.score)

fim = time.perf_counter()

tempo_avl_remocao = (
    fim - inicio
) * 1000

# Gera o arquivo com a ordem de atendimento.

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


# Gera o arquivo com os resultados.

with open(
    "resultados.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write("===== HEAP =====\n")
    arquivo.write(
        f"Inserção: {tempo_heap_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_heap_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritário: {tempo_heap_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Remoção: {tempo_heap_remocao:.6f} ms\n"
    )
    arquivo.write(
        f"Comparações: {heap.comparacoes}\n\n"
    )

    arquivo.write("===== ABB =====\n")
    arquivo.write(
        f"Inserção: {tempo_abb_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_abb_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritário: {tempo_abb_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Remoção: {tempo_abb_remocao:.6f} ms\n"
    )
    arquivo.write(
        f"Comparações: {abb.comparacoes}\n"
    )
    arquivo.write(
        f"Altura: {abb.altura()}\n\n"
    )

    arquivo.write("===== AVL =====\n")
    arquivo.write(
        f"Inserção: {tempo_avl_insercao:.4f} ms\n"
    )
    arquivo.write(
        f"Ordem: {tempo_avl_ordem:.4f} ms\n"
    )
    arquivo.write(
        f"Prioritário: {tempo_avl_prioritario:.6f} ms\n"
    )
    arquivo.write(
        f"Remoção: {tempo_avl_remocao:.6f} ms\n"
    )
    arquivo.write(
        f"Comparações: {avl.comparacoes}\n"
    )
    arquivo.write(
        f"Altura: {avl.altura()}\n"
    )
    arquivo.write(
        f"Rotações: {avl.rotacoes}\n"
    )

# GRÁFICO - Tempo de Inserção.

estruturas = ["Heap", "ABB", "AVL"]

tempos_insercao = [
    tempo_heap_insercao,
    tempo_abb_insercao,
    tempo_avl_insercao
]

plt.figure(figsize=(8,5))

barras = plt.bar(
    estruturas,
    tempos_insercao
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{altura:.2f}",
        ha="center"
    )

plt.title("Tempo de Inserção")
plt.ylabel("Milissegundos")
plt.grid(axis="y", linestyle="--")

plt.savefig("grafico_insercao.png")
plt.close()

# GRÁFICO - Tempo para Gerar Ordem de Atendimento.

tempos_ordem = [
    tempo_heap_ordem,
    tempo_abb_ordem,
    tempo_avl_ordem
]

plt.figure(figsize=(8,5))

barras = plt.bar(
    estruturas,
    tempos_ordem
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{altura:.3f}",
        ha="center"
    )

plt.title("Tempo para Gerar Ordem de Atendimento")
plt.ylabel("Milissegundos")
plt.grid(axis="y", linestyle="--")

plt.savefig("grafico_ordem.png")
plt.close()

# GRÁFICO - Tempo para Encontrar Paciente Prioritário.

tempos_prioritario = [
    tempo_heap_prioritario,
    tempo_abb_prioritario,
    tempo_avl_prioritario
]

plt.figure(figsize=(8,5))

barras = plt.bar(
    estruturas,
    tempos_prioritario
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{altura:.6f}",
        ha="center"
    )

plt.title("Tempo para Encontrar o Paciente Prioritário")
plt.ylabel("Milissegundos")
plt.grid(axis="y", linestyle="--")

plt.savefig("grafico_prioritario.png")
plt.close()

# GRÁFICO - Comparações.

comparacoes = [
    heap.comparacoes,
    abb.comparacoes,
    avl.comparacoes
]

plt.figure(figsize=(8,5))

barras = plt.bar(
    estruturas,
    comparacoes
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{int(altura)}",
        ha="center"
    )

plt.title("Quantidade de Comparações")
plt.ylabel("Comparações")
plt.grid(axis="y", linestyle="--")

plt.savefig("grafico_comparacoes.png")
plt.close()

# GRÁFICO - Altura das Árvores.

estruturas_arvore = [
    "ABB",
    "AVL"
]

alturas = [
    abb.altura(),
    avl.altura()
]

plt.figure(figsize=(8,5))

barras = plt.bar(
    estruturas_arvore,
    alturas
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{int(altura)}",
        ha="center"
    )

plt.title("Altura das Árvores")
plt.ylabel("Níveis")
plt.grid(axis="y", linestyle="--")

plt.savefig("grafico_altura.png")
plt.close()

# Mostra os resultados no console.

print("\n===== RESULTADOS =====\n")

print("HEAP")
print(f"Inserção: {tempo_heap_insercao:.4f} ms")
print(f"Ordem: {tempo_heap_ordem:.4f} ms")
print(f"Prioritário: {tempo_heap_prioritario:.6f} ms")
print(f"Remoção: {tempo_heap_remocao:.6f} ms")
print(f"Comparações: {heap.comparacoes}")

print()

print("ABB")
print(f"Inserção: {tempo_abb_insercao:.4f} ms")
print(f"Ordem: {tempo_abb_ordem:.4f} ms")
print(f"Prioritário: {tempo_abb_prioritario:.6f} ms")
print(f"Remoção: {tempo_abb_remocao:.6f} ms")
print(f"Comparações: {abb.comparacoes}")
print(f"Altura: {abb.altura()}")

print()

print("AVL")
print(f"Inserção: {tempo_avl_insercao:.4f} ms")
print(f"Ordem: {tempo_avl_ordem:.4f} ms")
print(f"Prioritário: {tempo_avl_prioritario:.6f} ms")
print(f"Remoção: {tempo_avl_remocao:.6f} ms")
print(f"Comparações: {avl.comparacoes}")
print(f"Altura: {avl.altura()}")
print(f"Rotações: {avl.rotacoes}")

print("\nArquivos gerados:")
print("- ordem_atendimento.txt")
print("- resultados.txt")
print("- ordem_heap.txt")
print("- ordem_abb.txt")
print("- ordem_avl.txt")