# Enviador Automático de Currículos

Uma ferramenta de linha de comando em Python que automatiza o envio de currículos por e-mail, passando o destinatário manualmente ou buscando o e-mail de RH da empresa via pesquisa no Google.

## Funcionalidades  
- Interação via terminal para inserir:
  - Nome da vaga  
  - Plataforma de origem da vaga  
  - Assunto do e-mail  
  - Nome da empresa  
- Busca automática no Google por e-mails de RH usando palavras‑chave 
- Tratamento de strings para remoção de pontuação extra dos e-mails (ex: `email@exemplo.com.` → `email@exemplo.com`)
- Opção de envio ao usuário  
- Suporte a templates de e-mail em HTML e anexos em PDF  

## Pré‑requisitos  
- Python 3.10+  
- Google Chrome instalado  
- `chromedriver` 
- Conexão à internet  

## Instalação  
```bash
git clone https://github.com/luis-otavio-dias/resume-submitter.git
cd resume-submitter
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuração

- chromedriver: baixe a versão compatível com seu Chrome e coloque em drivers/chrome.
- Configure as veriáveis de ambiente criando um arquivo .env com base em .env-example.
- Cofigure o template HTML em templates/.
- Adicione seu currícule no formato pdf em assets/.
- Em main.py, configure as varíaveis html_file e pdf_file de acordo com os nomes do arquivos que adicionar.

##  Uso

```bash
python main.py
```

 - Informe o nome da vaga.

 - Informe a plataforma onde encontrou a vaga.

 - Insira o assunto do e-mail.

 - Digite o nome da empresa.

 - Confirme o (ou os) e-mail(s) de RH encontrados.
