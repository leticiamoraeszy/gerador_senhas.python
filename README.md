# 🔐 Gerador de Senhas

Gerador e verificador de senhas em Python, feito com programação orientada a objetos. As senhas são geradas com o módulo `secrets`, que usa uma fonte de aleatoriedade criptograficamente segura, ao contrário do `random`, que não é indicado para esse fim.

## ✨ Funcionalidades

- Geração de senhas aleatórias e seguras
- Escolha dos tipos de caractere: números, letras maiúsculas, letras minúsculas e símbolos
- Validação do tamanho da senha (de 7 a 16 caracteres)
- Verificação de força com sistema de pontuação
- Saída colorida e formatada no terminal com a biblioteca `rich`

## 🛠️ Tecnologias

| Recurso | Para que serve |
|---|---|
| `secrets` | Escolha aleatória segura dos caracteres |
| `string` | Conjuntos prontos de caracteres (dígitos, letras, pontuação) |
| `rich` | Impressão formatada no terminal |

## 📦 Instalação

Requer **Python 3.8+**.

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd <nome-da-pasta>

# 2. Instale a dependência
pip install rich
```

## 🚀 Como usar

```python
senha = GeradorSenhas(
    tamanho=12,
    usar_numeros=True,
    usar_maiusculas=True,
    usar_minusculas=True,
    usar_simbolos=True,
)

senha.verificar_forca()  # mostra a pontuação e a classificação
senha.ver_senha()        # gera e exibe uma senha
```

Para rodar:

```bash
python gerador_senhas.py
```

### Exemplo de saída

```
--- VERIFICAÇÃO DA SENHA---
pontuação - 6
--GERADOR DE SENHAS--
aB3$kL9#mQ2!
```

## ⚙️ Parâmetros

| Parâmetro | Tipo | Padrão | Descrição |
|---|---|---|---|
| `tamanho` | `int` | — (obrigatório) | Quantidade de caracteres (de 7 a 16) |
| `usar_numeros` | `bool` | `True` | Inclui dígitos (`0-9`) |
| `usar_maiusculas` | `bool` | `False` | Inclui letras de `A-Z` |
| `usar_minusculas` | `bool` | `True` | Inclui letras de `a-z` |
| `usar_simbolos` | `bool` | `False` | Inclui símbolos (`!@#$%...`) |

> ⚠️ Um `tamanho` fora do intervalo de 7 a 16 levanta `ValueError`.

## 🧩 Estrutura da classe

| Método | O que faz |
|---|---|
| `tamanho` (property) | Getter e setter com validação do tamanho |
| `montar()` | Monta o alfabeto de caracteres conforme as opções escolhidas |
| `gerar()` | Sorteia caractere por caractere com `secrets.choice` e devolve a senha |
| `verificar_forca()` | Calcula a pontuação e classifica a senha |
| `ver_senha()` | Gera uma senha e a exibe no terminal |

## 📊 Como a força é calculada

| Critério | Pontos |
|---|---|
| Tamanho entre 8 e 12 caracteres | +2 |
| Usa minúsculas | +1 |
| Usa maiúsculas | +1 |
| Usa símbolos | +2 |

- **Pontuação ≤ 5** → senha **FRACA**
- **Pontuação > 7** → senha **FORTE**

## 🔧 Melhorias futuras

Pontos que ainda podem evoluir no projeto:

- [ ] Ajustar os limites da pontuação: hoje o máximo possível é 6, então a classificação "FORTE" nunca aparece, e uma pontuação 6 não mostra nenhuma classificação
- [ ] Incluir números e o tamanho da senha de forma mais completa no cálculo de força
- [ ] Validar o tipo (`int`) **antes** de comparar o tamanho
- [ ] Mostrar mensagens de erro claras nos `ValueError`
- [ ] Impedir que todas as opções de caractere sejam desativadas (alfabeto vazio causa erro)
- [ ] Garantir ao menos um caractere de cada tipo escolhido na senha final
- [ ] Verificar a força da senha **gerada**, não só das configurações
- [ ] Criar interface de linha de comando com `argparse` ou interface gráfica
- [ ] Adicionar testes automatizados

## 📚 Conceitos praticados

Programação orientada a objetos, `@property` e setters, validação de dados, tratamento de exceções, uso de bibliotecas externas e geração segura de dados aleatórios.

## 👩‍💻 Autora

Feito por **Letícia** como projeto de estudo em Python e desenvolvimento backend.
