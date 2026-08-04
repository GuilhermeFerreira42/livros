#!/usr/bin/env python3
"""Recalcula o checksum do livro_capitulo_05.md de forma estável."""
import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira")
LIVRO = BASE / "capitulos/capitulo_05/livro_capitulo_05.md"

content = LIVRO.read_text(encoding="utf-8")
# Substitui qualquer checksum atual por placeholder
content = re.sub(
    r"\*\*Checksum SHA256 \(8 chars\):\*\* `[a-f0-9]{8}`",
    "**Checksum SHA256 (8 chars):** `PENDENTE`",
    content,
)
LIVRO.write_text(content, encoding="utf-8")

# Recalcula com placeholder
checksum = hashlib.sha256(content.encode("utf-8")).hexdigest()[:8]

# Substitui placeholder pelo checksum real
content = content.replace(
    "**Checksum SHA256 (8 chars):** `PENDENTE`",
    f"**Checksum SHA256 (8 chars):** `{checksum}`",
)
LIVRO.write_text(content, encoding="utf-8")

# Round-trip
final = LIVRO.read_text(encoding="utf-8")
final_checksum = hashlib.sha256(final.encode("utf-8")).hexdigest()[:8]
print(f"Checksum: {final_checksum}")
print(f"Match: {'OK' if final_checksum == checksum else 'MISMATCH'}")
print(f"Bytes: {len(final)}")
print(f"Palavras: {len(final.split())}")
