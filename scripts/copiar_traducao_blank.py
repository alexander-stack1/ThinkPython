#!/usr/bin/env python3
"""Copia células markdown traduzidas de chapters/ para blank/ quando o inglês era idêntico.

Uso (depois de traduzir chapters/):
  1. Manter um snapshot inglês não é necessário se blank/ ainda estiver em inglês.
  2. Para cada célula de blank em inglês, procura a mesma célula (texto idêntico)
     na versão traduzida? Isso não funciona depois que chapters/ já foi traduzido.

Estratégia correta:
  - Se blank ainda está em inglês e chapters já está em português, não há âncora.
  - Por isso este script só deve rodar se você passar um mapa:
      scripts/mapas/chapXX.json = lista de pares {\"blank_index\": n, \"chapters_index\": m}
    gerada ANTES da tradução, quando os textos ainda coincidiam.

Gera o mapa agora, se ambos ainda tiverem o mesmo texto em alguma célula.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cells_md(nb_path: Path) -> list[tuple[int, str]]:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    out = []
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "markdown":
            out.append((i, "".join(cell.get("source", []))))
    return out


def build_map(name: str) -> list[dict]:
    ch = ROOT / "chapters" / name
    bl = ROOT / "blank" / name
    md_ch = cells_md(ch)
    md_bl = cells_md(bl)
    by_text = {}
    for idx, text in md_ch:
        by_text.setdefault(text, []).append(idx)
    mapping = []
    used = set()
    for b_idx, text in md_bl:
        candidates = [i for i in by_text.get(text, []) if i not in used]
        if candidates:
            mapping.append({"blank_index": b_idx, "chapters_index": candidates[0]})
            used.add(candidates[0])
    return mapping


def apply_map(name: str, mapping: list[dict]) -> int:
    ch_nb = json.loads((ROOT / "chapters" / name).read_text(encoding="utf-8"))
    bl_path = ROOT / "blank" / name
    bl_nb = json.loads(bl_path.read_text(encoding="utf-8"))
    copied = 0
    for item in mapping:
        src = ch_nb["cells"][item["chapters_index"]].get("source", [])
        dest = bl_nb["cells"][item["blank_index"]]
        if dest.get("cell_type") != "markdown":
            continue
        dest["source"] = src
        copied += 1
    bl_path.write_text(json.dumps(bl_nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return copied


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "map"
    maps_dir = ROOT / "scripts" / "mapas"
    maps_dir.mkdir(parents=True, exist_ok=True)
    names = [p.name for p in sorted((ROOT / "blank").glob("chap*.ipynb"))]
    if cmd == "map":
        for name in names:
            mapping = build_map(name)
            (maps_dir / f"{name}.json").write_text(
                json.dumps(mapping, indent=2), encoding="utf-8"
            )
            print(f"{name}: {len(mapping)} células mapeadas")
    elif cmd == "apply":
        for name in names:
            path = maps_dir / f"{name}.json"
            if not path.exists():
                print(f"{name}: sem mapa")
                continue
            mapping = json.loads(path.read_text(encoding="utf-8"))
            n = apply_map(name, mapping)
            print(f"{name}: {n} células copiadas")
    else:
        raise SystemExit("uso: copiar_traducao_blank.py [map|apply]")


if __name__ == "__main__":
    main()
