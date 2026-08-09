# create-gentilpedro-python

Scaffold de um novo projeto Python de CLI/automação (estilo PyInvest), com a estrutura que o [Gentil Pedro](https://github.com/gentilpedro) usa nos próprios projetos.

## Uso

```
pipx run create-gentilpedro-python minha-app
cd minha-app
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
python main.py --hello Mundo
```

(ou `uvx create-gentilpedro-python minha-app` se você usa [uv](https://docs.astral.sh/uv/))

## O que vem incluído

- `app/` — lógica de negócio (domain + use cases)
- `ui/` — reservado para GUI (ttkbootstrap)
- `infra/` — reservado para integrações externas (selenium, APIs, etc.)
- Logging configurado (console + arquivo rotativo)
- `build_app.py` + `template.spec` — build de executável standalone via PyInstaller
- Testes com pytest

## Código-fonte

Publicado automaticamente a partir de [gentilpedro/template-python-cli](https://github.com/gentilpedro/template-python-cli) — o mesmo repositório pode ser usado direto como GitHub template ("Use this template"), sem passar pelo CLI.

## Licença

MIT
