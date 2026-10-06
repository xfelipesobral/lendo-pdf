# Bibliotecas usadas no teste:

docling 2.134.0

pymupdf 1.28.2

pymupdf4llm 1.28.2

marker-pdf 2.0.0

## Baixar modelos do docling antes

docling-tools models download --all -o ./modelos-docling

## Usando o `.venv`

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 **Como confirmar que deu certo?** O prefixo `(.venv)` aparecerá logo no início da linha de comando do seu terminal, assim: `(.venv) ... %`.

Para sair do ambiente do .venv, use:

```bash
deactivate
```

# Testes 🏆

```text
============================================================
INFORMAÇÕES DO PDF
============================================================
Arquivo: pdfs/teste.pdf
Páginas: 13

Processando com PYMUPDF...
⏱️ Tempo: 0.1569 segundos
📄 Caracteres: 43,928
💾 Resultado: resultado_pymupdf.txt

Processando com PYMUPDF4LLM...
rapidocr_api using backend: rapidocr

=== Document parser messages ===
Using RapidOCR for OCR processing.

=== Document parser messages ===
Using RapidOCR for OCR processing.
📄 Caracteres markdown: 44,708; ⏱️ Tempo: 1.6726 segundos
📄 Caracteres texto: 42,224; ⏱️ Tempo: 1.5005 segundos
💾 Resultado: resultado_pymupdf4llm.md

Processando com DOCLING...
Loading weights: 100%|█████████████████████████████████████████████████████| 770/770 [00:00<00:00, 11538.33it/s]
⏱️ Tempo: 41.9609 segundos
📄 Caracteres markdown: 39,396 🏆
📄 Caracteres texto: 39,231
💾 Resultado: resultado_docling.md

============================================================
BENCHMARK FINALIZADO
============================================================
⏱️ Tempo total: 45.2922 segundos
```

```text
============================================================
INFORMAÇÕES DO PDF ESCANEADO
============================================================
Arquivo: pdfs/teste2.pdf
Páginas: 22

Processando com PYMUPDF...
⏱️ Tempo: 0.0041 segundos
📄 Caracteres: 0
💾 Resultado: resultado_pymupdf.txt

Processando com PYMUPDF4LLM...
rapidocr_api using backend: rapidocr
The text detection result is empty

=== Document parser messages ===
Using RapidOCR for OCR processing.
OCR on page.number=0/1.
OCR on page.number=1/2.
OCR on page.number=2/3.
OCR on page.number=3/4.
OCR on page.number=4/5.
OCR on page.number=5/6.
OCR on page.number=6/7.
OCR on page.number=7/8.
OCR on page.number=8/9.
OCR on page.number=9/10.
OCR on page.number=10/11.
OCR on page.number=11/12.
OCR on page.number=12/13.
OCR on page.number=13/14.
OCR on page.number=14/15.
OCR on page.number=15/16.
OCR on page.number=16/17.
OCR on page.number=17/18.
OCR on page.number=18/19.
OCR on page.number=19/20.
OCR on page.number=20/21.
OCR on page.number=21/22.
The text detection result is empty

=== Document parser messages ===
Using RapidOCR for OCR processing.
OCR on page.number=0/1.
OCR on page.number=1/2.
OCR on page.number=2/3.
OCR on page.number=3/4.
OCR on page.number=4/5.
OCR on page.number=5/6.
OCR on page.number=6/7.
OCR on page.number=7/8.
OCR on page.number=8/9.
OCR on page.number=9/10.
OCR on page.number=10/11.
OCR on page.number=11/12.
OCR on page.number=12/13.
OCR on page.number=13/14.
OCR on page.number=14/15.
OCR on page.number=15/16.
OCR on page.number=16/17.
OCR on page.number=17/18.
OCR on page.number=18/19.
OCR on page.number=19/20.
OCR on page.number=20/21.
OCR on page.number=21/22.
📄 Caracteres markdown: 38,214; ⏱️ Tempo: 49.5514 segundos
📄 Caracteres texto: 38,491; ⏱️ Tempo: 51.3679 segundos 🏆
💾 Resultado: resultado_pymupdf4llm.md

Processando com DOCLING...
Loading weights: 100%|█████████████████████████████████████████████████████| 770/770 [00:00<00:00, 13120.25it/s]
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
The text detection result is empty
RapidOCR returned empty result!
⏱️ Tempo: 61.9731 segundos
📄 Caracteres markdown: 38,091
📄 Caracteres texto: 37,646
💾 Resultado: resultado_docling.md

============================================================
BENCHMARK FINALIZADO
============================================================
⏱️ Tempo total: 162.8985 segundos
```

```text
============================================================
INFORMAÇÕES DO PDF
============================================================
Arquivo: pdfs/teste4.pdf
Páginas: 2

Processando com PYMUPDF...
⏱️ Tempo: 0.0104 segundos
📄 Caracteres: 4,240
💾 Resultado: resultado_pymupdf.txt

Processando com PYMUPDF4LLM...
rapidocr_api using backend: rapidocr

=== Document parser messages ===
Using RapidOCR for OCR processing.

=== Document parser messages ===
Using RapidOCR for OCR processing.
📄 Caracteres markdown: 2,582; ⏱️ Tempo: 0.8094 segundos
📄 Caracteres texto: 3,737; ⏱️ Tempo: 0.6643 segundos 🏆
💾 Resultado: resultado_pymupdf4llm.md

Processando com DOCLING...
Loading weights: 100%|█████████████████| 770/770 [00:00<00:00, 21789.62it/s]
RapidOCR returned empty result!
RapidOCR returned empty result!
⏱️ Tempo: 5.3830 segundos
📄 Caracteres markdown: 2,734
📄 Caracteres texto: 2,696
💾 Resultado: resultado_docling.md

Processando com MARKER...
2026-10-06 11:01:47,787 [INFO] marker: Table processing stats: {'tables_pdftext': 1, 'tables_total': 1}
⏱️ Tempo: 26.5527 segundos
📄 Caracteres markdown: 2,689
💾 Resultado: resultados/marker.md

============================================================
BENCHMARK FINALIZADO
============================================================
⏱️ Tempo total: 33.4229 segundos
```
