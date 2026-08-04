#!/usr/bin/env python3
"""
Extrator do dump de capítulo para a estrutura correta do projeto.
"""
import re
import os

INPUT_FILE = "/home/user/uploads/codigo_completo (3).txt"
OUTPUT_DIR = "/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_03"
SEP = "=" * 42

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Padrão: "Conteúdo de NOME (caminho: PATH) [enc: utf-8]:"
    header_re = re.compile(
        r'^Conteúdo de (\S+) \(caminho: ([^\)]+)\) \[enc: utf-8\]:$',
        re.MULTILINE
    )
    sep_re = re.compile(r'^' + re.escape(SEP) + r'$', re.MULTILINE)

    matches = list(header_re.finditer(content))
    print(f"Cabeçalhos encontrados: {len(matches)}")

    files = {}
    for m in matches:
        nome = m.group(1)
        path = m.group(2).strip()

        # Pula o \n após o cabeçalho, o separador, e o \n após o separador
        content_start = m.end() + 1 + len(SEP) + 1

        # Acha o próximo separador (42 '=' em linha sozinha)
        sep_iter = sep_re.finditer(content, pos=content_start)
        try:
            next_sep = next(sep_iter)
            content_end = next_sep.start()
        except StopIteration:
            content_end = len(content)

        body = content[content_start:content_end]
        # Remove newline final se existir
        if body.endswith('\n'):
            body = body[:-1]

        files[path] = body

    print(f"Arquivos parseados: {len(files)}")
    total_chars = 0
    for path in sorted(files.keys()):
        size = len(files[path])
        total_chars += size
        print(f"  - {path} ({size} chars)")
    print(f"\nTotal de caracteres: {total_chars}")

    # Cria os arquivos
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = 0
    for rel_path, body in files.items():
        if rel_path.startswith("capitulo_03/"):
            rel_path = rel_path[len("capitulo_03/"):]

        full_path = os.path.join(OUTPUT_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(body)
        created += 1

    print(f"\nTotal criado: {created} arquivos em {OUTPUT_DIR}")
    print(f"\nPor cena:")
    cenas = {}
    for path in files:
        m = re.search(r'cena_(\d+)', path)
        if m:
            cena = m.group(1)
            cenas.setdefault(cena, []).append(path)
    for cena in sorted(cenas.keys()):
        print(f"  cena_{cena}: {len(cenas[cena])} arquivos")

if __name__ == "__main__":
    main()
