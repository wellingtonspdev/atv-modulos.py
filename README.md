# Resolução de Exercícios

Este repositório contém soluções para três atividades de programação em Python. Os exercícios abordam conceitos fundamentais, como manipulação de strings, estrutura de dados, funções e recursividade.

## Estrutura do Repositório

```
ATV-MODULOS.PY/
│── modulos/
│   │── contador_de_palavras.py
│   │── media_alunos.py
│   │── num_primos.py
│   │── registrador.py
│   │── soma_lista.py
│   │── soma_notas.py
│── main.atv1.py
│── main.atv2.py
│── main.atv3.py
│── README.md
```

## Atividades Resolvidas

### **Atividade 1 - Contagem de Palavras**

Crie um módulo `contador_de_palavras.py` dentro da pasta `modulos/`, contendo a função `contar_palavras`:

1. **Converter para Minúsculas:** Utiliza `lower()` para padronizar o texto.
2. **Dividir em Palavras:** Usa `split()` para separar o texto em uma lista de palavras.
3. **Contar Palavras:**
   - Inicializa um dicionário vazio para armazenar a contagem.
   - Percorre a lista e incrementa a contagem de cada palavra.
4. **Retornar o Dicionário:** Retorna um dicionário contendo palavras e suas frequências.

O arquivo `main.atv1.py` será responsável por chamar essa função e exibir os resultados.

### **Atividade 2 - Cálculo da Média das Notas**

1. Criar uma lista com as notas de cinco alunos.
2. Utilizar um loop `foreach` para calcular a soma das notas.
3. Criar uma função que receba a soma das notas e o número de alunos e retorne a média.
4. Exibir a média das notas na tela.

A implementação está no arquivo `main.atv2.py`, utilizando o módulo `media_alunos.py` e `soma_notas.py`.

### **Atividade 3 - Funções Diversas**

1. **Função de Verificação de Número Primo**  
   Criar uma função no módulo `num_primos.py` que receba um número e retorne `True` se for primo e `False` caso contrário.

2. **Função Recursiva para Somar uma Lista**  
   Criar uma função recursiva no módulo `soma_lista.py` que calcule a soma de todos os elementos de uma lista.

3. **Função para Contagem de Palavras**  
   Escrever uma função no módulo `contador_de_palavras.py` que receba uma string e conte o número de palavras nela.

4. **Função com *args e **kwargs para Registrar Várias Informações**  
   Criar uma função no módulo `registrador.py` que aceite um número indeterminado de argumentos e informações extras nomeadas, exibindo-os.

Essas implementações estão contidas no arquivo `main.atv3.py`.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/wellingtonspdev/atv-modulos.py.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd ATV-MODULOS.PY
   ```
3. Execute os arquivos Python conforme necessário:
   ```bash
   python main.atv1.py
   python main.atv2.py
   python main.atv3.py
   ```

## Tecnologias Utilizadas
- Python 3

## Autor
[Wellington Siqueira Porto](https://github.com/wellingtonspdev)

