#!/usr/bin/env python3
"""Substitui células markdown de um notebook a partir de um JSON.

O JSON é uma lista de objetos {\"index\": int, \"source\": str}.
Não altera células de código. Gera o source no formato Jupyter (linhas com \\n).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def to_jupyter_source(text: str) -> list[str]:
    if text == "":
        return []
    parts = text.split("\n")
    source = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            source.append(part + "\n")
        elif part:
            source.append(part)
    return source


def apply(nb_path: Path, updates_path: Path) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    updates = json.loads(updates_path.read_text(encoding="utf-8"))
    cells = nb["cells"]
    for item in updates:
        idx = int(item["index"])
        cell = cells[idx]
        if cell.get("cell_type") != "markdown":
            raise SystemExit(f"{nb_path}: célula {idx} não é markdown")
        cell["source"] = to_jupyter_source(item["source"])
    nb_path.write_text(
        json.dumps(nb, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Atualizado {nb_path} ({len(updates)} células)")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("uso: aplicar_markdown.py NOTEBOOK.ipynb TRADUCOES.json")
    apply(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
