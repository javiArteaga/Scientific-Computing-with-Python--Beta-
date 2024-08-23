
---

### Proyecto: **Calculadora de Tiempo**

#### Descripción

Como parte de su certificación, **Javiera Arteaga Moncado** desarrolló varios proyectos, logrando aprobar todas las pruebas automatizadas. Uno de estos proyectos es la **Calculadora de Tiempo**.

#### Funcionalidad

La **Calculadora de Tiempo** es una aplicación diseñada para sumar un tiempo de duración a una hora de inicio dada en formato de 12 horas. La función principal, llamada `add_time`, acepta los siguientes parámetros:

1. **Hora de Inicio**:  
   Formato de reloj de 12 horas (terminando en AM o PM).

2. **Tiempo de Duración**:  
   El número de horas y minutos que se deben sumar a la hora de inicio.

3. **Día Inicial (Opcional)**:  
   El día de la semana, sin distinción entre mayúsculas y minúsculas.

#### Comportamiento de la Función

- La función `add_time` suma el tiempo de duración a la hora de inicio y devuelve el resultado en el formato de 12 horas.
- Si el resultado ocurre al día siguiente, se indicará como **"(día siguiente)"**.
- Si el resultado es más de un día después, se mostrará como **"(n días después)"**, donde `n` es el número de días transcurridos.
- Si se proporciona un día de inicio, el resultado incluirá el día de la semana.

#### Ejemplos de Uso

```python
# Ejemplo 1: Sumar 3 horas y 10 minutos a las 3:00 p.m.
add_time('3:00 p.m.', '3:10')
# Resultado: 6:10 p.m.

# Ejemplo 2: Sumar 2 horas y 32 minutos a las 11:30 a.m. en un lunes
add_time('11:30 a. m.', '2:32', 'lunes')
# Resultado: 2:02 p.m., lunes

# Ejemplo 3: Sumar 20 minutos a las 11:43 a.m.
add_time('11:43 a.m.', '00:20')
# Resultado: 12:03 p.m.

# Ejemplo 4: Sumar 3 horas y 30 minutos a las 10:10 p.m.
add_time('10:10 p.m.', '3:30')
# Resultado: 1:40 AM (día siguiente)

# Ejemplo 5: Sumar 24 horas y 20 minutos a las 11:43 p.m. en un martes
add_time('11:43 p.m.', '24:20', 'martes')
# Resultado: 00:03, jueves (2 días después)

# Ejemplo 6: Sumar 205 horas y 12 minutos a las 6:30 p.m.
add_time('6:30 p.m.', '205:12')
# Resultado: 7:42 a. m. (9 días después)
```

#### Consideraciones

- **Formato de Entrada**: Las horas de inicio deben ser válidas en formato de 12 horas.
- **Duración**: Los minutos en la duración son un número entero menor que 60; las horas pueden ser cualquier número entero.
- **Salida**: La salida debe seguir un formato preciso de espaciado y puntuación.

Este proyecto permite calcular la hora futura de manera precisa, considerando posibles cambios de día y días de la semana, sin necesidad de importar bibliotecas adicionales de Python.

---