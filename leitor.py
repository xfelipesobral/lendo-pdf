from pathlib import Path
import time
import unicodedata

import pymupdf
import pymupdf4llm

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from unstructured.partition.pdf import partition_pdf

# ==========================================
# CONFIGURAÇÕES
# ==========================================

NOME_ARQUIVO = "pdfs/teste4.pdf"
CAMINHO_MODELOS_DOCLING = Path("modelos-docling")

pipeline_options_docling = PdfPipelineOptions(artifacts_path=CAMINHO_MODELOS_DOCLING)

converter_docling = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options_docling)
    }
)

converter_marker = PdfConverter(artifact_dict=create_model_dict())


# ==========================================
# INFORMAÇÕES DO PDF
# ==========================================

documento = pymupdf.open(NOME_ARQUIVO)

print("=" * 60)
print("INFORMAÇÕES DO PDF")
print("=" * 60)
print(f"Arquivo: {NOME_ARQUIVO}")
print(f"Páginas: {len(documento)}")
print()

documento.close()

# ==========================================
# PYMUPDF
# ==========================================


def processar_pymupdf():
    print("Processando com PYMUPDF...")

    inicio = time.perf_counter()

    texto = ""

    documento = pymupdf.open(NOME_ARQUIVO)

    for numero_pagina, pagina in enumerate(documento, start=1):
        texto_cru = pagina.get_text("text", sort=True)

        texto_corrigido = unicodedata.normalize("NFC", texto_cru)

        texto_final = texto_corrigido.strip()

        if texto_final:
            texto += texto_final + "\n\n"

    documento.close()

    Path("resultados/pymupdf.txt").write_text(texto, encoding="utf-8")

    fim = time.perf_counter()

    print(f"⏱️ Tempo: {fim - inicio:.4f} segundos")
    print(f"📄 Caracteres: {len(texto):,}")
    print("💾 Resultado: resultado_pymupdf.txt")
    print()


# ==========================================
# PYMUPDF4LLM
# ==========================================


def processar_pymupdf4llm():
    print("Processando com PYMUPDF4LLM...")

    inicio = time.perf_counter()

    markdown = pymupdf4llm.to_markdown(NOME_ARQUIVO)

    fim = time.perf_counter()
    tempo_markdown = fim - inicio

    inicio = time.perf_counter()

    texto = pymupdf4llm.to_text(NOME_ARQUIVO)

    fim = time.perf_counter()
    tempo_texto = fim - inicio

    Path("resultados/pymupdf4llm.md").write_text(markdown, encoding="utf-8")
    Path("resultados/pymupdf4llm.txt").write_text(texto, encoding="utf-8")

    print(
        f"📄 Caracteres markdown: {len(markdown):,}; ⏱️ Tempo: {tempo_markdown:.4f} segundos"
    )
    print(f"📄 Caracteres texto: {len(texto):,}; ⏱️ Tempo: {tempo_texto:.4f} segundos")
    print("💾 Resultado: resultado_pymupdf4llm.md")
    print()


# ==========================================
# DOCLING
# ==========================================


def processar_docling():
    print("Processando com DOCLING...")

    inicio = time.perf_counter()

    resultado = converter_docling.convert(NOME_ARQUIVO)

    markdown = resultado.document.export_to_markdown()
    texto = resultado.document.export_to_text()

    fim = time.perf_counter()

    Path("resultados/resultado_docling.md").write_text(markdown, encoding="utf-8")
    Path("resultados/resultado_docling.txt").write_text(texto, encoding="utf-8")

    print(f"⏱️ Tempo: {fim - inicio:.4f} segundos")
    print(f"📄 Caracteres markdown: {len(markdown):,}")
    print(f"📄 Caracteres texto: {len(texto):,}")
    print("💾 Resultado: resultado_docling.md")
    print()


# ==========================================
# MARKER
# ==========================================


def processar_marker():
    print("Processando com MARKER...")

    inicio = time.perf_counter()

    resultado = converter_marker(NOME_ARQUIVO)

    markdown, _, _ = text_from_rendered(resultado)

    fim = time.perf_counter()

    Path("resultados/marker.md").write_text(markdown, encoding="utf-8")

    print(f"⏱️ Tempo: {fim - inicio:.4f} segundos")
    print(f"📄 Caracteres markdown: {len(markdown):,}")
    print("💾 Resultado: resultados/marker.md")
    print()


# ==========================================
# UNSTRUCTURED
# ==========================================


def processar_unstructured():
    print("Processando com UNSTRUCTURED...")

    inicio = time.perf_counter()

    elementos = partition_pdf(
        filename=NOME_ARQUIVO, strategy="hi_res", languages=["por"]
    )

    fim = time.perf_counter()

    texto = "\n\n".join(elemento.text for elemento in elementos if elemento.text)

    Path("resultados/unstructured.txt").write_text(texto, encoding="utf-8")

    print(f"⏱️ Tempo: {fim - inicio:.4f} segundos")
    print(f"📄 Elementos: {len(elementos):,}")
    print(f"📄 Caracteres: {len(texto):,}")

    tipos = {}

    for elemento in elementos:
        tipo = elemento.category
        tipos[tipo] = tipos.get(tipo, 0) + 1

    print("📊 Tipos encontrados:")

    for tipo, quantidade in sorted(tipos.items()):
        print(f"   {tipo}: {quantidade}")

    print("💾 Resultado: resultados/unstructured.txt")
    print()


# ==========================================
# EXECUÇÃO
# ==========================================

inicio_total = time.perf_counter()

processar_pymupdf()

processar_pymupdf4llm()

processar_docling()

processar_marker()

processar_unstructured()

fim_total = time.perf_counter()

print("=" * 60)
print("BENCHMARK FINALIZADO")
print("=" * 60)
print(f"⏱️ Tempo total: {fim_total - inicio_total:.4f} segundos")

exit(0)
