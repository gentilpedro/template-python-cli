# ui/

Reservado para interface gráfica (ex: `ttkbootstrap`, como no PyInvest).

Se o projeto for puramente CLI, esta pasta pode ficar vazia/ser removida.
Ao adicionar uma GUI, mantenha a mesma separação: `ui/` só monta janelas e
delega toda lógica para `app/use_cases`, nunca chama `infra/` diretamente.
