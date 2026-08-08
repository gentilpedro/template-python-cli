# template-python-cli

Template base para projetos Python de automação/CLI/desktop (estilo [PyInvest](../PyInvest)).
Sem libs pesadas por padrão — adicione selenium, pandas, ttkbootstrap etc. conforme a necessidade
de cada projeto novo.

## Estrutura

```
main.py            # entrypoint fino: parse de args, delega para app/
app/
  config.py         # Settings carregado de .env
  logger.py          # logging configurado (console + arquivo rotativo em output/app.log)
  domain/            # regras de negócio puras, sem I/O
  use_cases/          # orquestra domain + infra
ui/                 # reservado para GUI (ex: ttkbootstrap) — ver ui/README.md
infra/              # integrações externas: scraping, APIs, storage — ver infra/README.md
tests/              # testes pytest
build_app.py        # gera executável via PyInstaller
template.spec        # spec do PyInstaller (edite ao crescer o projeto)
```

A separação `domain/` → `use_cases/` → `infra/`/`ui/` é a mesma usada no PyInvest real: regra de
negócio não conhece I/O, e I/O (arquivo, rede, GUI) nunca contém regra de negócio.

## Como usar este template

1. No GitHub, clique em **Use this template** neste repositório.
2. Clone o repositório novo e ajuste o nome do projeto em `build_app.py`, `template.spec` e neste README.
3. Crie o ambiente virtual e instale as dependências:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements-dev.txt
```

4. Copie `.env.example` para `.env` e ajuste as variáveis.
5. Rode o exemplo:

```bash
python main.py --hello Mundo
```

6. Rode os testes:

```bash
python -m pytest
```

7. Gere o executável (opcional):

```bash
python build_app.py
```

## Adicionando dependências pesadas

`requirements.txt` fica enxuto de propósito. Ao integrar scraping, planilhas, GUI etc.,
adicione a lib em `requirements.txt` (ex: `selenium`, `pandas`, `ttkbootstrap`) e, se for gerar
executável, inclua `--collect-all=<lib>` ou `--hidden-import=<lib>` em `build_app.py`/`template.spec`
— veja `PyInvest/build_app.py` como referência de um caso real com selenium + pandas + ttkbootstrap.
