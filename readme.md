# Estudo de caso: leitura de PDFs

Comparação de bibliotecas de extração de PDF e de duas formas de decidir qual resultado usar: uma heurística de complexidade por página e um juiz (JEV) que compara duas extrações em Markdown.

Os PDFs de entrada ficam em `pdfs/`. Os textos extraídos vão para `resultados/`. O caminho do arquivo está em `NOME_ARQUIVO` no topo de cada script.

## Scripts

| Script | O que faz |
| --- | --- |
| `leitor.py` | Extrai o mesmo PDF com cada biblioteca e grava tempo, tamanho e o texto em `resultados/`. |
| `pipeline_calculando_complexidade.py` | Mede a complexidade de cada página e sugere qual biblioteca usar. |
| `pipeline_jev.py` | Extrai com Docling e PyMuPDF4LLM e pede ao JEV para dizer qual parse ficou melhor. |

## Preparação

```bash
python3 -m venv .venv
source .venv/bin/activate
```

O prefixo `(.venv)` no início da linha do terminal confirma que o ambiente está ativo. Para sair:

```bash
deactivate
```

Bibliotecas usadas nos testes:

```bash
pip install docling==2.134.0 pymupdf==1.28.2 pymupdf4llm==1.28.2 marker-pdf==2.0.0 "unstructured[pdf]==0.27.16" "unstructured[local-inference]" python-dotenv mdformat
```

O Docling precisa dos modelos locais antes da primeira execução:

```bash
docling-tools models download --all -o ./modelos-docling
```

O `pipeline_jev.py` chama a API do OpenRouter. Copie `exemplo.env` para `.env` e preencha a chave:

```bash
cp exemplo.env .env
```

```text
OPENROUTER_API_KEY=sua_chave_secreta_aqui
```

## `leitor.py`

Lê o PDF configurado em `NOME_ARQUIVO` e roda, em sequência:

- **PyMuPDF** — texto nativo, página a página, normalizado em NFC. Saída: `resultados/pymupdf.txt`.
- **PyMuPDF4LLM** — Markdown e texto plano. Saídas: `resultados/pymupdf4llm.md` e `resultados/pymupdf4llm.txt`.
- **Docling** — usa os modelos em `modelos-docling`. Saídas: `resultados/resultado_docling.md` e `resultados/resultado_docling.txt`.
- **Marker** — Markdown. Saída: `resultados/marker.md`.
- **Unstructured** — partição `hi_res` em português, com contagem dos tipos de elemento. Saída: `resultados/unstructured.txt`.

```bash
python leitor.py
```

No fim, o script imprime o tempo total do benchmark.

## `pipeline_calculando_complexidade.py`

Abre o PDF com PyMuPDF e, em cada página, calcula um score a partir do layout:

| Sinal | Pontos |
| --- | --- |
| Tem tabelas | +4 |
| Tem imagens | +1 |
| Densidade de texto abaixo de 0,2 | +2 |
| Mais de 50 blocos | +1 |
| Sem texto nativo e com imagens | +5 |

A densidade é a área ocupada pelos blocos de texto dividida pela área da página.

A sugestão por página é:

- **6 ou mais** — Docling
- **3 a 5** — Marker
- **abaixo de 3** — PyMuPDF4LLM

```bash
python pipeline_calculando_complexidade.py
```

## `pipeline_jev.py`

Extrai o mesmo PDF duas vezes, formata os dois Markdowns com `mdformat` e envia ao juiz.

- **Representação A** — Docling (`resultados/resultado_pipeline_jev_a.txt`)
- **Representação B** — PyMuPDF4LLM (`resultados/resultado_pipeline_jev_b.txt`)

O juiz é o modelo `typesafe/jev-1.13`, via `POST https://openrouter.ai/api/alpha/decisions`. Ele escolhe A ou B em cinco critérios:

- **estrutura** — títulos, seções, listas, tabelas e ordem do conteúdo
- **legibilidade** — espaçamento, formatação Markdown e clareza
- **integridade** — caracteres estranhos, palavras quebradas, duplicações e truncamentos
- **coerência semântica** — rótulos, valores, datas e trechos relacionados permanecem juntos
- **melhor para LLM** — qual texto serve melhor de contexto para um pipeline de LLM/RAG

A resposta traz a escolha, as probabilidades e a confiança de cada critério. Um registro de execuções está em `resultados_pipeline_jev.md`.

```bash
python pipeline_jev.py
```
