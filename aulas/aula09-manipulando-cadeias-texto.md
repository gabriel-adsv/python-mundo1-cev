## **Aula 9 - Manipulando Texto**

- No python, para incluir todas as funcionalidades de um módulo, utiliza-se o comando **import**
- Para incluir apenas algumas funcionalidades, utiliza-se **from nomeDoModulo import itemUnico**
- **Importação otimizada**, é quando se importa uma única funcionalidade da biblioteca
 
### Fatiamento
- Pega pedaços de uma string
- Quando se trabalha com fatiamento de string, o último valor não entra na contagem

### Análise
- **len(XXX)**: conta o comprimento de um texto
- **.count()**: conta quantas vezes aparece um caractere em um texto  
- **.find()**: encontra um conjunto de letras e indica em que posição este conjunto começa
    - Se colocar uma string que não existe no testo, o find retorna -1

### Transformação
- **.replace()**: substitui uma cadeia de strings
- **.upper()**: coloca todas as letras em maiúsculas
- **.lower()**: coloca todas as letras em minúsculas
- **.capitalize()**: joga todos os caracteres de uma string para minúsculos e mantém apenas a primeira letra em maiúscula
- **.title()**: tem a mesma função do capitalize, mas palavra por palavra
- **.strip()**: remove todos os espaços inúteis no início e no final de uma string
- **.rstrip()**: remove os espaços inúteis do lado direito da string
- **.rstrip()**: remove os espaços inúteis do lado esquerdo da string

### Divisão e Junção
- **.split()**: tecnicamente, gera uma lista com todas as palavras de uma cadeia de caracteres
- **.join()**: junta uma coisa na outra


