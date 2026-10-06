from pathlib import Path
import time

import pymupdf

NOME_ARQUIVO = "pdfs/teste.pdf"

print("Iniciando processamento do PDF...")

timer_inicio = time.perf_counter()

documento = pymupdf.open(NOME_ARQUIVO)


for numero_pagina, pagina in enumerate(documento, start=1):
    texto_arquivo += f"{"-" * 10} Página {numero_pagina} {"-" * 10}\n\n"

    texto_cru = pagina.get_text("text", sort=True)
    texto_final = texto_cru.strip()

    blocos = pagina.get_text("blocks")
    imagens = pagina.get_images(full=True)
    tabelas = pagina.find_tables()
    largura = pagina.rect.width
    altura = pagina.rect.height
    area_pagina = largura * altura
    area_blocos = 0

    for bloco in blocos:
        x0, y0, x1, y1 = bloco[:4]

        largura_bloco = max(0, x1 - x0)
        altura_bloco = max(0, y1 - y0)

        area_blocos += largura_bloco * altura_bloco

    # Calculando a densidade de texto na página
    densidade_texto = area_blocos / area_pagina if area_pagina > 0 else 0

    complexidade = 0
    tem_imagens = len(imagens) > 0
    quantidade_caracteres = len(texto_final)
    sem_texto_nativo = not bool(texto_final)
    pouco_texto_na_pagina = densidade_texto < 0.2
    tem_tabelas = len(tabelas.tables) > 0

    if tem_tabelas:
        complexidade += 4

    if tem_imagens:
        complexidade += 1

    if pouco_texto_na_pagina:
        complexidade += 2

    if len(blocos) > 50:
        complexidade += 1

    if sem_texto_nativo and tem_imagens:
        complexidade += 5

    if complexidade >= 6:
        print("Usa docling")
    elif complexidade >= 3:
        print("Usa marker")
    else:
        print("Usa pymupdf4llm")

    print(f"Finalizou análise da página {numero_pagina} - Complexidade: {complexidade}")

Path("resultados/resultado_pipeline_complexidade.txt").write_text(
    texto_arquivo, encoding="utf-8"
)

timer_fim = time.perf_counter()

print(f"Processamento concluído em {timer_fim - timer_inicio:.2f} segundos.")
