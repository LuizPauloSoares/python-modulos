# 🐍 Estudos Python — Módulos e Bibliotecas

Repositório dedicado ao estudo prático de **módulos em Python**: criação de módulos próprios, uso de módulos nativos e integração com bibliotecas externas.

---

## 📁 Estrutura do Projeto

```
📦 estudos-python-modulos
 ┣ 📄 minha_calculadora.py      # Módulo personalizado com operações matemáticas
 ┣ 📄 teste_calculadora.py      # Importação e teste do módulo calculadora
 ┣ 📄 explorandoModuloOs.py     # Exploração do módulo nativo `os`
 ┗ 📄 moduloExterno.py          # Requisição HTTP com a biblioteca `requests`
```

---

## 📌 Descrição dos Arquivos

### `minha_calculadora.py`
Módulo criado do zero com as seguintes funções matemáticas:

| Função | Descrição |
|---|---|
| `adicao(n1, n2)` | Retorna a soma de dois números |
| `subtracao(n1, n2)` | Retorna a subtração de dois números |
| `multiplicacao(n1, n2)` | Retorna a multiplicação de dois números |
| `divizao(n1, n2)` | Retorna a divisão de dois números |
| `restDivizao(n1, n2)` | Retorna o resto da divisão (módulo `%`) |
| `divizaopor0(n1)` | Demonstra erro de divisão por zero |

---

### `teste_calculadora.py`
Arquivo que importa e utiliza o módulo `minha_calculadora`, testando as funções definidas nele.

```python
import minha_calculadora

print(minha_calculadora.multiplicacao(7, 10))  # Saída: 70
```

---

### `explorandoModuloOs.py`
Exploração do módulo nativo `os` do Python para interagir com o sistema operacional:

- `os.getcwd()` — obtém o diretório atual
- `os.listdir()` — lista os arquivos e pastas do diretório
- `os.mkdir()` — cria novos diretórios
- `os.environ` — acessa variáveis de ambiente do sistema

---

### `moduloExterno.py`
Uso da biblioteca externa `requests` para realizar uma requisição HTTP à API pública do GitHub.

- Faz uma chamada `GET` para `https://api.github.com`
- Trata os status codes `200`, `404` e outros
- Utiliza bloco `try/except` para capturar exceções

---

## 🚀 Como executar

**Pré-requisito:** Python 3 instalado.

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale a dependência externa:
```bash
pip install requests
```

3. Execute os scripts individualmente:
```bash
python teste_calculadora.py
python explorandoModuloOs.py
python moduloExterno.py
```

---

## 🧠 Conceitos Praticados

- Criação e importação de módulos personalizados
- Uso de módulos nativos do Python (`os`)
- Instalação e uso de bibliotecas externas (`requests`)
- Tratamento de exceções com `try/except`
- Requisições HTTP e consumo de APIs REST

---

## 👨‍💻 Autor

**Luiz Paulo Soares**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-luiz--paulo--soares-blue?logo=linkedin)](https://linkedin.com/in/luiz-paulo-soares)
[![Instagram](https://img.shields.io/badge/Instagram-lu1z__st-E4405F?logo=instagram&logoColor=white)](https://instagram.com/lu1z_st)

---

> Projeto desenvolvido como parte dos estudos de lógica de programação e Python. 🚀
