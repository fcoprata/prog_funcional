# README

## Requisitos Funcionais

Os requisitos funcionais descrevem as funções específicas que o sistema deve realizar. Estes requisitos estão diretamente relacionados às funcionalidades que o sistema oferece aos usuários.

### Cálculo de Soma de Dois Números

O sistema deve ser capaz de calcular a soma de dois números fornecidos como entrada. Este requisito está implementado na função lambda `add` dentro do arquivo `lambda.py`.

```python
add = lambda x, y: x + y
```

### Elevar ao Quadrado uma Lista de Números

O sistema deve permitir elevar ao quadrado cada elemento de uma lista de números. Este requisito está implementado na list comprehension `squared_numbers` dentro do arquivo `list_comprehension.py`.

```python
squared_numbers = [x**2 for x in numbers]
```

### Uso de Closure para Manter Estado

O sistema deve permitir a criação de uma função que capture e mantenha um estado para ser usado posteriormente. Este requisito está implementado nas funções `outer_function` e `inner_function` dentro do arquivo `closure.py`.

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
```

### Aplicação de Funções de Alta Ordem

O sistema deve suportar a aplicação de funções de alta ordem, permitindo passar funções como argumentos para outras funções. Este requisito está implementado na função `apply_operation` dentro do arquivo `alta_ordem.py`.

```python
def apply_operation(operation, x, y):
    return operation(x, y)
```

## Requisitos Não Funcionais

Os requisitos não funcionais descrevem as propriedades do sistema, como desempenho, segurança e usabilidade, mas que não estão relacionadas diretamente às funcionalidades específicas.

### Testabilidade

O sistema deve ser facilmente testável para garantir que todas as funcionalidades funcionem conforme o esperado. Este requisito está implementado no arquivo `unittest.py`, onde diferentes testes unitários são realizados para cada funcionalidade.

```python
import unittest
```

Os testes estão organizados em métodos como `test_lambda_function`, `test_list_comprehension`, `test_closure` e `test_higher_order_function`, verificando a corretude de cada funcionalidade do sistema.
