# Academia-ES
Sistema de academia da matéria de Engenharia de Software

Para ler as estórias de usuário, a metáfora do sistema, a descrição dos casos de uso e dos design patterns adotados, acesse a pasta "relatorio" e veja o PDF. Nesta pasta também é possível visualizar o tex do relatorio.

Para visualizar os casos de uso, entre na pasta "diagrama_caso_uso", haverá imagens com os 2 que cada integrante fez e a imagem que contém todos.

O sistema pode ser executado diretamente pelo arquivo "main.py". Para isso, é necessário ter o Python 3 instalado e as bibliotecas necessárias. Para instalá-las, execute o seguinte comando no terminal:

```
pip install -r requirements.txt
```

Após, será possível executar o sistema com o seguinte comando:

```
python src/main.py
```

Embora seja possível fazer login como qualquer um dos usuários presentes no arquivo "src/db/dml.sql", sugerimos os seguintes usuários:

- Usuário: 23456789016, Senha: testpass (Eve Smith - Aluno)
- Usuário: 12345678901, Senha: password123 (John Doe - Professor)