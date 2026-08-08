# infra/

Integrações externas: scraping (selenium/undetected-chromedriver), chamadas de API,
leitura/escrita de arquivos (`storage/`), clientes de terceiros (`external/`).

Nada aqui deve conter regra de negócio — só I/O e adapters que o `app/use_cases`
consome através de uma interface simples (função ou classe pequena).

Sugestão de subpastas, conforme a necessidade do projeto:
- `external/` — clientes HTTP, scraping, APIs de terceiros
- `storage/` — leitura/escrita em disco, planilhas, banco local
- `writers/` — geração de saída (Excel, CSV, PDF, etc.)
