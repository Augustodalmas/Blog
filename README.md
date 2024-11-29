Este é um aplicativo web de blog desenvolvido com Django.</br>
O sistema permite que os usuários gerenciem postagens por meio de um CRUD completo (Criar, Ler, Atualizar e Deletar). Além disso, os leitores podem interagir deixando comentários nas postagens. O projeto é ideal para aprendizado e implementação de funcionalidades essenciais de um sistema de blog.

<b>Funcionalidades</b></br>
CRUD de Postagens</br>
Criar novas postagens com título, conteúdo e tags.</br>
Listar todas as postagens com exibição de título e resumo.</br>
Editar o conteúdo de postagens existentes.</br>
Excluir postagens.</br>

<b>Sistema de Comentários</b></br>
Leitores podem comentar nas postagens.</br>
Moderação: comentários podem ser aprovados/rejeitados pelo administrador.</br>
Sistema de Autenticação</br>
Usuários autenticados podem criar e editar postagens.</br>
Apenas usuários logados podem comentar.</br>

<b>Tecnologias Utilizadas</b></br>
Linguagem de programação: Python</br>
Framework backend: Django</br>
Banco de Dados: SQLite (pode ser facilmente substituído por PostgreSQL ou MySQL)</br>
Frontend: HTML, CSS, e Bootstrap para estilização</br>
Outros: Django Admin para gerenciamento</br>

Como Utilizar 🚀<br>
Clone o Repositório:<br>
```git clone https://github.com/seu-usuario/django-genres-api.git```

Certifique-se de ter o Python e Django instalados. Em seguida, instale as dependências:<br>
```pip install -r requirements.txt```

Execute as Migrações:<br>
```python manage.py migrate```

Inicie o Servidor Django:<br>
```python manage.py runserver```
