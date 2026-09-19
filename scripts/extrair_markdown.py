#!/usr/bin/env python3
"""Extrai células markdown de um notebook para revisão."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("uso: extrair_markdown.py NOTEBOOK.ipynb")
    path = Path(sys.argv[1])
    nb = json.loads(path.read_text(encoding="utf-8"))
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") != "markdown":
            continue
        src = "".join(cell.get("source", []))
        print(f"\n===== CELL {i} =====")
        print(src)


if __name__ == "__main__":
    main()
