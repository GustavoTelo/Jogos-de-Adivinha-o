
# Jogo da Adivinhação

## Descrição
**Jogo da Adivinhação** é um jogo simples feito em Python onde o jogador tenta adivinhar um número secreto gerado aleatoriamente pela máquina. O número está entre 1 e 15, e o jogador tem um número limitado de tentativas para descobrir o valor correto. Caso o jogador acerte o número, ele será parabenizado. Se errar, o jogo informa se o número correto é maior ou menor e quantas tentativas restam.

## Regras do Jogo
1. O jogo sorteará um número aleatório entre 1 e 15.
2. O jogador deve fazer tentativas para adivinhar o número.
3. O jogo dirá se a tentativa foi correta ou não:
   - Se acertar, o jogador será parabenizado.
   - Se errar, o jogo indicará se o número secreto é maior ou menor.
4. O jogador tem um total de 5 tentativas para acertar o número.

## Como Jogar
1. Ao iniciar o jogo, o jogador verá uma mensagem de boas-vindas e será informado sobre o intervalo do número e o limite de tentativas.
2. O jogador insere um número dentro do intervalo (1 a 15) como palpite.
3. O jogo verifica o palpite e responde:
   - Se o palpite for correto, o jogo exibe uma mensagem de parabéns e encerra.
   - Se estiver incorreto, o jogo informa se o número secreto é maior ou menor e diminui o número de tentativas restantes.
4. Caso o jogador use todas as tentativas sem acertar, uma mensagem de derrota é exibida.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação para lógica do jogo
- **Biblioteca Random**: Para geração aleatória do número secreto

## Como Executar
1. Certifique-se de que você tem o Python instalado.
2. Salve o código em um arquivo `.py`.
3. Abra um terminal e execute o comando:
   ```bash
   python nome_do_arquivo.py
   ```

---
