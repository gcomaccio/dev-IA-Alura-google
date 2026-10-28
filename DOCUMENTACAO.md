# Documentação Técnica: `teste.py`

Documentação da análise estrutural, lógica de execução e saídas do script [teste.py](teste.py).

---

## 1. Visão Geral

O arquivo [teste.py](teste.py) é um script desenvolvido em Python para realizar sorteios pseudoaleatórios de números inteiros dentro de um intervalo pré-determinado (de 13 a 22). Conforme o número sorteado, o script avalia condições específicas e exibe mensagens correspondentes no terminal.

---

## 2. Código Fonte

```python
from random import randint

sorteio = randint(13, 22)
print(sorteio)

if sorteio == 13:
    print("ladrao")

elif sorteio == 22:
    print("HAHAHAHAH Eh o mito po 22, neles")
```

---

## 3. Funcionamento Passo a Passo

1. **Importação da Biblioteca (`Linha 1`)**:
   - `from random import randint`
   - Importa a função `randint` do módulo nativo `random`, responsável por gerar números inteiros pseudoaleatórios.

2. **Geração do Sorteio (`Linha 3`)**:
   - `sorteio = randint(13, 22)`
   - Define a variável `sorteio` com um valor inteiro aleatório no intervalo fechado de **13 a 22** ($13 \le x \le 22$).

3. **Exibição do Valor Gerado (`Linha 4`)**:
   - `print(sorteio)`
   - Imprime imediatamente no terminal o número obtido.

4. **Estrutura Condicional (`Linhas 5 a 9`)**:
   - **Caso `sorteio == 13`**: Imprime a string `"ladrao"`.
   - **Caso `sorteio == 22`**: Imprime a string `"HAHAHAHAH Eh o mito po 22, neles"`.
   - **Caso qualquer outro número (14 a 21)**: Nenhuma mensagem adicional é exibida.

---

## 4. Tabela de Possíveis Saídas

| Número Sorteado | Mensagem Condicional | Saída no Console |
| :---: | :--- | :--- |
| **`13`** | `"ladrao"` | `13`<br>`ladrao` |
| **`14` a `21`** | *(nenhuma)* | `<número>` |
| **`22`** | `"HAHAHAHAH Eh o mito po 22, neles"` | `22`<br>`HAHAHAHAH Eh o mito po 22, neles` |

---

## 5. Requisitos e Como Executar

- **Requisitos**: Python 3 instalado (não requer bibliotecas externas).
- **Comando para executar**:
  ```bash
  python teste.py
  ```
