
---

### Proyecto: **Calculadora de Probabilidades**

#### Descripción

Como parte de su certificación, **Javiera Arteaga Moncado** desarrolló varios proyectos, logrando aprobar todas las pruebas automatizadas. Uno de estos proyectos es la **Calculadora de Probabilidades**.

#### Objetivo

El objetivo de este proyecto es escribir un programa que determine la probabilidad aproximada de extraer ciertas combinaciones de bolas al azar de un sombrero. Este cálculo se realizará mediante la simulación de un gran número de experimentos.

#### Funcionalidad

1. **Clase `Hat`**:
   - La clase `Hat` se encarga de gestionar el contenido del sombrero. Se construye a partir de un número variable de argumentos que especifican la cantidad de bolas de cada color.
   - Cada bola se representa como una cadena que indica su color.
   - La clase incluye un método de `draw` que permite extraer una cantidad específica de bolas al azar, sin reemplazo.

   **Ejemplos de Instanciación:**

   ```python
   sombrero1 = Hat(amarillo=3, azul=2, verde=6)
   sombrero2 = Hat(rojo=5, naranja=4)
   sombrero3 = Hat(rojo=5, naranja=4, negro=1, azul=0, rosa=2, rayado=9)
   ```

   - **Contenido del Sombrero**: Si se crea un sombrero con `{'rojo': 2, 'azul': 1}`, el contenido será `['rojo', 'rojo', 'azul']`.

2. **Método `draw`**:
   - Este método acepta un argumento que indica el número de bolas a extraer del sombrero.
   - Las bolas se extraen al azar y no se devuelven al sombrero.
   - Si se solicita más bolas de las que hay disponibles, se devuelven todas las bolas.

3. **Función `experimento`**:
   - Esta función realiza una serie de experimentos para estimar la probabilidad de obtener una combinación específica de bolas al extraer un conjunto de bolas de un sombrero.
   - **Argumentos**:
     - `hat`: Un objeto de la clase `Hat`.
     - `expected_balls`: Un diccionario que define la combinación de bolas que se intenta extraer.
     - `num_balls_drawn`: El número de bolas a extraer en cada experimento.
     - `num_experiments`: El número de experimentos a realizar para la estimación.

   - **Comportamiento**:
     - Realiza `num_experiments` experimentos.
     - Cuenta cuántas veces se obtiene la combinación deseada.
     - Devuelve la probabilidad estimada como la relación entre los éxitos y el número total de experimentos.

#### Ejemplo de Uso

```python
# Ejemplo de simulación de probabilidad
sombrero = Hat(negro=6, rojo=4, verde=3)
probabilidad = experimento(
    sombrero=sombrero,
    expected_balls={'rojo': 2, 'verde': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probabilidad)
# Resultado: 0.356 (El valor exacto puede variar debido a la naturaleza aleatoria de los sorteos)
```

#### Consideraciones

- **Precisión**: Cuantos más experimentos se realicen (`num_experiments`), más precisa será la probabilidad estimada.
- **Aleatoriedad**: La probabilidad variará ligeramente en cada ejecución debido a la aleatoriedad inherente al proceso de extracción de bolas.
- **Sin Inicialización de Semillas Aleatorias**: No se debe inicializar ninguna semilla aleatoria en el archivo.

Este proyecto demuestra la aplicación de simulaciones para resolver problemas de probabilidad que serían complejos de calcular mediante fórmulas matemáticas tradicionales.

---
