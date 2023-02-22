Sistema de Adoção de Animais
Este é um sistema de adoção de animais desenvolvido em Django. Ele permite que os usuários se cadastrem, cadastrem animais para adoção e solicitem a adoção de animais.

Funcionalidades
Cadastro de usuário: os usuários podem criar contas e fazer login para acessar o sistema.
Cadastro de animais para adoção: os usuários podem cadastrar animais que estão disponíveis para adoção, incluindo informações como nome, idade, raça, sexo, se já foi vacinado, entre outras.
Listagem de animais disponíveis: os usuários podem ver todos os animais disponíveis para adoção.
Visualização detalhada de animais: quando um usuário clica em um animal na lista de animais disponíveis, uma janela é aberta com informações detalhadas sobre o animal, como se é vacinado, docil, etc.
Solicitação de adoção: os usuários podem solicitar a adoção de um animal clicando em um botão na página de detalhes do animal.
E-mail automático de solicitação de adoção: quando um usuário solicita a adoção de um animal, um e-mail é enviado automaticamente para o responsável pelo animal.
Aprovação de adoção: os responsáveis pelos animais podem acessar o sistema para ver quantas pessoas estão solicitando a adoção do seu animal e aprovar a adoção para uma pessoa.
E-mail automático de confirmação de adoção: quando uma adoção é aprovada pelo responsável do animal, um e-mail é enviado para o adotante informando que a adoção foi confirmada e passando os contatos do dono para concretizarem a adoção.
Dashboard de estatísticas: o sistema apresenta um dashboard com gráficos que mostram quais raças foram mais adotadas.
Instalação
1. Clone o repositório:
git clone https://github.com/seu-usuario/sistema-adocao-animais.git

2. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Crie o arquivo .env na raiz do projeto e cole o texto abaixo configurando com seu email:
DEFAULT_FROM_EMAIL = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
EMAIL_USE_TLS = True
EMAIL_PORT = 
EMAIL_HOST 

5. Configure o banco de dados no arquivo settings.py.

6. Crie as tabelas do banco de dados:
python manage.py migrate

7- Inicie o servidor:
python manage.py runserver

8. Acesse o sistema no navegador em http://localhost:8000/

Contribuição
Contribuições são sempre bem-vindas! Se você quiser contribuir para este projeto, siga as instruções abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (git checkout -b feature/minha-feature).
3. Faça o commit das suas mudanças (git commit -am 'Adicionando minha feature').
4. Faça o push para a branch (git push origin feature/minha-feature).
5. Abra um Pull Request.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Autor
Vinicios Matheus 




