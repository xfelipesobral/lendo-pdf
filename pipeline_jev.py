import os

import requests
import json
from pathlib import Path
import time
from dotenv import load_dotenv
import mdformat

import pymupdf4llm

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

load_dotenv()

# ==========================================
# CONFIGURAÇÕES
# ==========================================

NOME_ARQUIVO = "pdfs/teste5.pdf"
CAMINHO_MODELOS_DOCLING = Path("modelos-docling")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("A variável de ambiente OPENROUTER_API_KEY não está definida.")
    exit(1)

pipeline_options_docling = PdfPipelineOptions(artifacts_path=CAMINHO_MODELOS_DOCLING)

converter_docling = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options_docling)
    }
)


def processar_docling():
    print("Processando com DOCLING...")

    inicio = time.perf_counter()

    resultado = converter_docling.convert(NOME_ARQUIVO)

    markdown = resultado.document.export_to_markdown()

    fim = time.perf_counter()

    print(f"⏱️ Docling tempo: {fim - inicio:.4f} segundos")

    return markdown


def processar_pymupdf4llm():
    print("Processando com PYMUPDF4LLM...")

    inicio = time.perf_counter()

    markdown = pymupdf4llm.to_markdown(NOME_ARQUIVO)

    fim = time.perf_counter()

    print(f"⏱️ Pymupdf4llm tempo: {fim - inicio:.4f} segundos")

    return markdown


def juiz(representacao_a: str, representacao_b: str):
    print("Iniciando julgamento dos resultados...")

    response = requests.post(
        url="https://openrouter.ai/api/alpha/decisions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "X-OpenRouter-Title": "TESTES",
        },
        data=json.dumps(
            {
                "model": "typesafe/jev-1.13",
                "state": f"""Você está avaliando duas representações em Markdown do mesmo documento PDF.

REPRESENTAÇÃO A:
{representacao_a}

REPRESENTAÇÃO B:
{representacao_b}""",
                "questions": {
                    "estrutura": {
                        "type": "choice",
                        "instructions": "Qual representação está melhor estruturada? Considere a organização de títulos, seções, parágrafos, listas, tabelas, quebras de conteúdo e ordem das informações.",
                        "criteria": {
                            "a": "A apresenta uma estrutura mais clara e coerente.",
                            "b": "B apresenta uma estrutura mais clara e coerente.",
                        },
                    },
                    "legibilidade": {
                        "type": "choice",
                        "instructions": "Qual representação é mais legível e fácil de interpretar? Considere espaçamento, separação dos elementos, formatação Markdown, clareza visual e facilidade para compreender o conteúdo.",
                        "criteria": {
                            "a": "A é mais legível e fácil de interpretar.",
                            "b": "B é mais legível e fácil de interpretar.",
                        },
                    },
                    "integridade": {
                        "type": "choice",
                        "instructions": "Qual representação apresenta maior integridade textual? Procure por caracteres estranhos, palavras quebradas, números aparentemente corrompidos, símbolos inesperados, duplicações, truncamentos ou outros artefatos de extração.",
                        "criteria": {
                            "a": "A apresenta maior integridade textual.",
                            "b": "B apresenta maior integridade textual.",
                        },
                    },
                    "coerencia_semantica": {
                        "type": "choice",
                        "instructions": "Qual representação apresenta maior coerência semântica? Considere se as informações relacionadas permanecem próximas e se tabelas, rótulos, valores, datas, títulos e seus respectivos conteúdos estão organizados de maneira que suas relações sejam compreensíveis.",
                        "criteria": {
                            "a": "A apresenta maior coerência semântica.",
                            "b": "B apresenta maior coerência semântica.",
                        },
                    },
                    "melhor_para_llm": {
                        "type": "choice",
                        "instructions": "Qual representação é mais adequada para servir como contexto de entrada para um pipeline de LLM/RAG, minimizando alucinações e garantindo a correta extração de informações?",
                        "criteria": {
                            "a": "A é superior para consumo por LLM.",
                            "b": "B é superior para consumo por LLM.",
                        },
                    },
                },
            }
        ),
    )

    if response.status_code == 200:
        data = response.json()
        print("--- Resposta do JEV ---")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Erro {response.status_code}: {response.text}")


print(f"Iniciando processamento do PDF... {NOME_ARQUIVO}")

timer_inicio = time.perf_counter()

texto_docling = mdformat.text(processar_docling())
texto_pymupdf4llm = mdformat.text(processar_pymupdf4llm())

Path("resultados/resultado_pipeline_jev_a.txt").write_text(
    texto_docling, encoding="utf-8"
)
Path("resultados/resultado_pipeline_jev_b.txt").write_text(
    texto_pymupdf4llm, encoding="utf-8"
)

juiz(texto_docling, texto_pymupdf4llm)

timer_fim = time.perf_counter()

print(f"Processamento concluído em {timer_fim - timer_inicio:.2f} segundos.")

exit(0)
