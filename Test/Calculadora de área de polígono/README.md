
---

### Proyecto: **Calculadora de Área de Polígono**

#### Descripción

Como parte de su certificación, **Javiera Arteaga Moncado** desarrolló un proyecto de **Calculadora de Área de Polígono** utilizando programación orientada a objetos. Este proyecto involucra la creación de dos clases: **Rectángulo** y **Cuadrado**. La clase **Cuadrado** es una subclase de **Rectángulo**, heredando todos sus métodos y atributos.

#### Funcionalidad

1. **Clase `Rectángulo`**:
   - **Atributos**:
     - `ancho`: Almacena el ancho del rectángulo.
     - `alto`: Almacena la altura del rectángulo.
   - **Métodos**:
     - **`set_ancho(ancho)`**: Establece el valor del ancho.
     - **`set_alto(alto)`**: Establece el valor de la altura.
     - **`get_area()`**: Calcula y devuelve el área del rectángulo (`ancho * alto`).
     - **`get_perimeter()`**: Calcula y devuelve el perímetro del rectángulo (`2 * ancho + 2 * alto`).
     - **`get_diagonal()`**: Calcula y devuelve la diagonal del rectángulo usando el teorema de Pitágoras (`(ancho² + alto²) ** 0.5`).
     - **`get_picture()`**: Devuelve una representación en cadena del rectángulo utilizando el carácter `*`. Cada línea tendrá una longitud igual al ancho y habrá un número de líneas igual a la altura. Si el ancho o la altura es mayor que 50, el método devolverá `"Demasiado grande para la imagen"`.
     - **`get_amount_inside(otra_forma)`**: Acepta como argumento otra instancia de `Rectángulo` o `Cuadrado` y devuelve cuántas veces esa forma puede caber dentro del rectángulo sin rotaciones.

   - **Representación en Cadena**:
     - La representación en cadena de una instancia de `Rectángulo` tiene el formato `Rectángulo(ancho=x, alto=y)`.

   **Ejemplo de Uso**:
   ```python
   rect = Rectángulo(10, 5)
   print(rect.get_area())         # Salida: 50
   rect.set_alto(3)
   print(rect.get_perimeter())    # Salida: 26
   print(rect)                    # Salida: Rectángulo(ancho=10, alto=3)
   print(rect.get_picture())      # Salida: **********
                                  #          **********
                                  #          **********
   ```

2. **Clase `Cuadrado`**:
   - **Herencia**: La clase `Cuadrado` hereda de `Rectángulo`.
   - **Atributos**:
     - `lado`: Almacena la longitud de un solo lado del cuadrado.
   - **Métodos**:
     - **`__init__(lado)`**: Inicializa el cuadrado, estableciendo tanto el `ancho` como el `alto` de la clase `Rectángulo` con el valor de `lado`.
     - **`set_lado(lado)`**: Establece tanto el `ancho` como el `alto` con el valor de `lado`.
     - **`set_ancho(ancho)`** y **`set_alto(alto)`**: Ambos métodos actualizan tanto el `ancho` como el `alto` para mantener la propiedad de un cuadrado.

   - **Representación en Cadena**:
     - La representación en cadena de una instancia de `Cuadrado` tiene el formato `Cuadrado(lado=x)`.

   **Ejemplo de Uso**:
   ```python
   sq = Cuadrado(9)
   print(sq.get_area())           # Salida: 81
   sq.set_lado(4)
   print(sq.get_diagonal())       # Salida: 5.656854249492381
   print(sq)                      # Salida: Cuadrado(lado=4)
   print(sq.get_picture())        # Salida: ****
                                  #          ****
                                  #          ****
                                  #          ****
   ```

3. **Ejemplo Completo**:
   ```python
   rect.set_alto(8)
   rect.set_ancho(16)
   print(rect.get_amount_inside(sq))  # Salida: 8
   ```

   **Resultados Esperados**:
   ```plaintext
   50
   26
   Rectángulo(ancho=10, alto=3)
   **********
   **********
   **********

   81
   5.656854249492381
   Cuadrado(lado=4)
   ****
   ****
   ****
   ****

   8
   ```

#### Consideraciones
- **Herencia**: La clase `Cuadrado` utiliza la herencia de manera efectiva para evitar la duplicación de código.
- **Encapsulamiento**: Los métodos y atributos están encapsulados para proporcionar una interfaz clara y mantener la coherencia de los objetos.
- **Flexibilidad**: El método `get_amount_inside` permite calcular cuántas veces una forma puede caber dentro de otra, lo que añade versatilidad a la funcionalidad de estas clases.

Este proyecto demuestra una comprensión sólida de la programación orientada a objetos, incluyendo la creación de clases, la herencia, y la implementación de métodos específicos para realizar cálculos geométricos.

---
