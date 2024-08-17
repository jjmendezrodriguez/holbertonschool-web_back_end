# Python - Variable Annotations

This project covers the use of type annotations in Python, a feature that allows you to specify and document the types of variables, parameters, and return values in your code. Type annotations do not affect the execution of the code, but they are extremely useful for improving readability and for using static analysis tools like `mypy`.

## Content

The project includes several practical examples and exercises that cover the following topics:

1. **Variable Declaration**:
   - Annotating variables with specific types such as integers, floats, strings, and booleans.

2. **Functions with Annotations**:
   - How to annotate functions to clearly define the types of their parameters and return values.
   - Examples include functions that sum lists, concatenate strings, convert numbers to strings, and more.

3. **Duck Typing and Using `TypeVar`**:
   - Implementing functions that operate on more general types using `TypeVar` and duck typing.
   - Examples like `safely_get_value` that safely retrieve values from dictionaries.

4. **Validation with `mypy`**:
   - Using the `mypy` tool to validate type annotations and ensure that the code meets the expected type specifications.
   - Corrections and adjustments based on `mypy` output.

5. **Documentation and Best Practices**:
   - The importance of documenting modules, classes, and functions adequately.
   - Example of a fully documented module and how annotations were adjusted to meet best practices.

## Main Files

- **0-add.py**: Function that adds two floating-point numbers.
- **1-concat.py**: Function that concatenates two strings.
- **2-floor.py**: Function that returns the floor of a floating-point number.
- **3-to_str.py**: Function that converts a floating-point number to its string representation.
- **4-define_variables.py**: Example of variable declaration with type annotations.
- **5-sum_list.py**: Function that sums the elements of a list of floats.
- **6-sum_mixed_list.py**: Function that sums the elements of a list of integers and floats.
- **7-to_kv.py**: Function that returns a tuple with a string and the square of a number.
- **8-make_multiplier.py**: Function that returns another function to multiply by a factor.
- **9-element_length.py**: Function that returns a list of tuples with the length of elements in a sequence.

## Advances 

- **100-safe_first_element.py**: Function that safely retrieves the first element of a sequence.
- **101-safely_get_value.py**: Function that retrieves a value from a dictionary with a default value.
- **102-type_checking.py**: Function that repeats the elements of a tuple a specified number of times.

## Using `mypy`

To verify the type annotations in this project, use `mypy`:

bash

    `mypy 102-type_checking.py`

# Python - Variable Annotations

Este proyecto abarca el uso de anotaciones de tipo en Python, una característica que permite especificar y documentar los tipos de variables, parámetros y valores de retorno en tu código. Las anotaciones de tipo no afectan la ejecución del código, pero son extremadamente útiles para mejorar la legibilidad y para utilizar herramientas de análisis estático como `mypy`.

## Contenido

El proyecto incluye varios ejemplos prácticos y ejercicios que cubren los siguientes temas:

1. **Declaración de Variables**:
   - Anotación de variables con tipos específicos, como enteros, flotantes, cadenas, y booleanos.

2. **Funciones con Anotaciones**:
   - Cómo anotar funciones para definir claramente los tipos de sus parámetros y valores de retorno.
   - Ejemplos incluyen funciones que suman listas, concatenan cadenas, convierten números a cadenas, y más.

3. **Duck Typing y Uso de `TypeVar`**:
   - Implementación de funciones que operan sobre tipos más generales, utilizando `TypeVar` y duck typing.
   - Ejemplos como `safely_get_value` que recupera valores de diccionarios de manera segura.

4. **Validación con `mypy`**:
   - Uso de la herramienta `mypy` para validar las anotaciones de tipo y asegurar que el código cumpla con las especificaciones de tipo esperadas.
   - Correcciones y ajustes realizados basados en la salida de `mypy`.

5. **Documentación y Buenas Prácticas**:
   - Importancia de documentar módulos, clases y funciones adecuadamente.
   - Ejemplo de un módulo completamente documentado y cómo se ajustaron las anotaciones para cumplir con las mejores prácticas.

## Archivos Principales

- **0-add.py**: Función que suma dos números flotantes.
- **1-concat.py**: Función que concatena dos cadenas.
- **2-floor.py**: Función que devuelve el piso de un número flotante.
- **3-to_str.py**: Función que convierte un número flotante a su representación en cadena.
- **4-define_variables.py**: Ejemplo de declaración de variables con anotaciones de tipo.
- **5-sum_list.py**: Función que suma los elementos de una lista de flotantes.
- **6-sum_mixed_list.py**: Función que suma los elementos de una lista de enteros y flotantes.
- **7-to_kv.py**: Función que devuelve una tupla con una cadena y el cuadrado de un número.
- **8-make_multiplier.py**: Función que devuelve otra función para multiplicar por un factor.
- **9-element_length.py**: Función que devuelve una lista de tuplas con la longitud de los elementos de una secuencia.
- **100-safe_first_element.py**: Función que obtiene de manera segura el primer elemento de una secuencia.
- **101-safely_get_value.py**: Función que recupera un valor de un diccionario con un valor por defecto.
- **102-type_checking.py**: Función que repite los elementos de una tupla un número determinado de veces.

## Uso de `mypy`

Para verificar las anotaciones de tipo en este proyecto, utiliza `mypy`:

bash

    mypy 102-type_checking.py
