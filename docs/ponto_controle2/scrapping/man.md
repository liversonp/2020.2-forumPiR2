# Manual para execucao das ferramentas

Esteja ciente de que a elaboracao destas funcionalidades foi projetada para um ambiente linux.

- Instale e configure o mysql

Segue um site com um tutorial para tal passo:<https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-pt>

- Instale a dependencia que auxilia na conexao entre o python( e outros programas ) e o mysql

apt install libmysqlclient-dev

- Instale o python3 e o pip3

apt install python3

apt install python3-pip

- Istale as dependencias do python

pip3 install -r requirements

- Execute o script de criacao da base de dados
  
mysql -u <seu_usuario> -p < pir2.sql

- Configurando acesso entre o python e o Mysql

Para nao expor o seu usuario e senha do mysql foi configurado para o git nao rastear o arquivo
"credenciais.txt", portanto:

+ - crie um arquivo com nome "credenciais.txt" 

+ - siga exatamente o seguinte padrao:
```
user:<seu_usuario>
password:<sua_senha>
```
Nota: Sim, os sinais'<' e '>' sao obrigatorios.
