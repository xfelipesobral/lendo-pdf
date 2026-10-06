```text
Iniciando processamento do PDF... pdfs/teste.pdf
Processando com DOCLING...
[INFO] 2026-10-06 14:38:30,242 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:38:30,243 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/PP-OCRv6_det_small.onnx
[INFO] 2026-10-06 14:38:30,258 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:38:30,259 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/ch_ppocr_mobile_v2.0_cls_mobile.onnx
[INFO] 2026-10-06 14:38:30,270 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:38:30,270 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/PP-OCRv6_rec_small.onnx
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████| 770/770 [00:00<00:00, 12903.85it/s]
⏱️ Docling tempo: 45.3684 segundos
Processando com PYMUPDF4LLM...
rapidocr_api using backend: rapidocr

=== Document parser messages ===
Using RapidOCR for OCR processing.
⏱️ Pymupdf4llm tempo: 1.5966 segundos
Iniciando julgamento dos resultados...

--- Resposta do JEV ---
{
  "model": "typesafe/jev-1.13-20260917",
  "answers": {
    "estrutura": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "empate": 0,
        "a": 0.94,
        "b": 0.06
      },
      "confidence": 0.91
    },
    "legibilidade": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "b": 0.03,
        "a": 0.97,
        "empate": 0
      },
      "confidence": 0.95
    },
    "integridade": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "empate": 0,
        "a": 0.95,
        "b": 0.05
      },
      "confidence": 0.92
    },
    "coerencia_semantica": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "empate": 0,
        "a": 0.98,
        "b": 0.02
      },
      "confidence": 0.97
    },
    "melhor_para_llm": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "empate": 0,
        "a": 0.99,
        "b": 0.01
      },
      "confidence": 0.99
    }
  },
  "usage": {
    "input_tokens": 29458,
    "output_tokens": 197,
    "cost": 0.001237236
  },
  "id": "gen-dec-1791308357-g9MEDxZO4oxET8u7mnt4",
  "provider": "TypeSafe"
}
Processamento concluído em 47.84 segundos.
```

```text
Iniciando processamento do PDF... pdfs/teste4.pdf
Processando com DOCLING...
[INFO] 2026-10-06 14:43:15,169 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:43:15,170 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/PP-OCRv6_det_small.onnx
[INFO] 2026-10-06 14:43:15,186 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:43:15,186 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/ch_ppocr_mobile_v2.0_cls_mobile.onnx
[INFO] 2026-10-06 14:43:15,199 [RapidOCR] base.py:23: Using engine_name: onnxruntime
[INFO] 2026-10-06 14:43:15,199 [RapidOCR] main.py:63: Using modelos-docling/RapidOcr/PP-OCRv6_rec_small.onnx
Loading weights: 100%|███████████████████████████████████████████████████████| 770/770 [00:00<00:00, 9324.42it/s]
RapidOCR returned empty result!
RapidOCR returned empty result!
⏱️ Docling tempo: 6.3951 segundos
Processando com PYMUPDF4LLM...
rapidocr_api using backend: rapidocr

=== Document parser messages ===
Using RapidOCR for OCR processing.
⏱️ Pymupdf4llm tempo: 0.7082 segundos
Iniciando julgamento dos resultados...
--- Resposta do JEV ---
{
  "model": "typesafe/jev-1.13-20260917",
  "answers": {
    "estrutura": {
      "type": "choice",
      "choice": "b",
      "probabilities": {
        "a": 0.35,
        "b": 0.64,
        "empate": 0.01
      },
      "confidence": 0.46
    },
    "legibilidade": {
      "type": "choice",
      "choice": "b",
      "probabilities": {
        "a": 0.4,
        "b": 0.59,
        "empate": 0.01
      },
      "confidence": 0.39
    },
    "integridade": {
      "type": "choice",
      "choice": "a",
      "probabilities": {
        "a": 0.83,
        "b": 0.17,
        "empate": 0
      },
      "confidence": 0.74
    },
    "coerencia_semantica": {
      "type": "choice",
      "choice": "b",
      "probabilities": {
        "a": 0.4,
        "b": 0.57,
        "empate": 0.03
      },
      "confidence": 0.36
    },
    "melhor_para_llm": {
      "type": "choice",
      "choice": "b",
      "probabilities": {
        "a": 0.4,
        "b": 0.59,
        "empate": 0.01
      },
      "confidence": 0.39
    }
  },
  "usage": {
    "input_tokens": 3481,
    "output_tokens": 197,
    "cost": 0.000146202
  },
  "id": "gen-dec-1791308602-Bhao0oLXcYKQQgMZTjaV",
  "provider": "TypeSafe"
}
Processamento concluído em 7.71 segundos.
```
