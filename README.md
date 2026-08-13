# 🔐 Gerador de Senhas

Um gerador de senhas simples e interativo, feito em Python, que permite personalizar o tamanho e os tipos de caracteres da senha.

## ✨ Funcionalidades

- Gera senhas de qualquer tamanho, definido por você
- Permite escolher se a senha deve conter:
  - 🔢 Números
  - 🔤 Letras (maiúsculas e minúsculas)
  - ⚡ Símbolos especiais
- Gera quantas senhas você quiser, sem precisar reiniciar o programa
- Interface no terminal com cores para facilitar a leitura

## 🛠️ Tecnologias utilizadas

- Python 3
- Bibliotecas nativas: `random`, `string`, `time`

Não precisa instalar nenhuma biblioteca externa — só ter o Python instalado no computador.

## ▶️ Como executar

1. Baixe (ou clone) este repositório.
2. Abra o terminal na pasta do projeto.
3. Rode o comando:

```bash
python gerador_senhas.py
```

## 💻 Exemplo de uso

```
------------------------------
GERADOR DE SENHAS
------------------------------
Tamanho da senha: 12
Você quer números na sua senha?[S/N]: S
Você quer letras na sua senha?[S/N]: S
Você quer simbolos na sua senha?[S/N]: N
==================================================
SENHA GERADA: aB3fT9mZpQ7x
==================================================
Deseja continuar?[S/N]: N
Encerrando...
Até a próxima!
```

## 🔧 Possíveis melhorias futuras

- Hoje, a opção "números" usa só os dígitos de **um único número sorteado**, o que limita a variedade. Trocar por `string.digits` deixaria o pool de números completo (0 a 9).
- Adicionar uma opção para copiar a senha gerada direto para a área de transferência.
- Tratar o caso em que o usuário responde "N" para todas as opções (hoje a senha sai vazia).

## 📄 Licença

Projeto de estudo, livre para uso e modificação.
