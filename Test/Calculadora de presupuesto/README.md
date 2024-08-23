
---

### Proyecto: **Aplicación de Presupuesto**

#### Descripción

Como parte de su certificación, **Javiera Arteaga Moncado** desarrolló varios proyectos, logrando aprobar todas las pruebas automatizadas. Uno de estos proyectos es la **Aplicación de Presupuesto**, que permite gestionar diferentes categorías presupuestarias como alimentos, ropa, y entretenimiento.

#### Funcionalidad

1. **Clase `Categoría`**:
   - La clase `Categoría` permite crear instancias para diferentes categorías de presupuesto, como "Comida", "Ropa", etc.
   - Cada categoría tiene un **libro mayor**, que es una lista donde se registran todas las transacciones (depósitos y retiros).

   **Métodos Principales**:
   - **`deposito(cantidad, descripción='')`**:  
     Añade una cantidad al libro mayor con una descripción opcional.
   - **`retiro(cantidad, descripción='')`**:  
     Registra un retiro como un valor negativo en el libro mayor. Devuelve `True` si el retiro se realiza, y `False` si no hay fondos suficientes.
   - **`get_balance()`**:  
     Devuelve el saldo actual basado en los depósitos y retiros.
   - **`transferencia(cantidad, categoría_destino)`**:  
     Transfiere una cantidad de una categoría a otra. Registra un retiro en la categoría de origen y un depósito en la categoría de destino. Devuelve `True` si se realiza la transferencia, y `False` en caso contrario.
   - **`check_funds(cantidad)`**:  
     Verifica si hay fondos suficientes para realizar un retiro o transferencia. Devuelve `True` si hay suficientes fondos y `False` en caso contrario.

   **Ejemplo de Uso**:

   ```python
   comida = Categoría('Comida')
   comida.deposito(1000, 'depósito inicial')
   comida.retiro(10.15, 'comestibles')
   comida.retiro(15.89, 'restaurante y más comida')
   
   ropa = Categoría('Ropa')
   comida.transferencia(50, ropa)
   
   print(comida)
   ```

   **Resultado Ejemplo**:

   ```
   *************Comida*************
   depósito inicial          1000.00
   comestibles                -10.15
   restaurante y más comida   -15.89
   Transferencia a Ropa       -50.00
   Total: 923.96
   ```

2. **Función `create_spend_chart(categorías)`**:
   - **Objetivo**: Crear un gráfico de barras que muestre el porcentaje gastado en cada categoría.
   - **Cálculo**: El porcentaje se basa únicamente en los retiros.
   - **Formato**:
     - Las etiquetas de porcentaje van del 0 al 100.
     - Las barras del gráfico están formadas por el carácter `"o"`, y se redondean hacia abajo al múltiplo de 10 más cercano.
     - Debajo de las barras, los nombres de las categorías se muestran en formato vertical.
     - El gráfico incluye un título en la parte superior: **"Porcentaje gastado por categoría"**.

   **Ejemplo de Gráfico**:

   ```
   Porcentaje gastado por categoría
   100|          
    90|          
    80|          
    70|          
    60|          
    50|          
    40|          
    30|    o     
    20|    o  o  
    10|    o  o  
     0| o  o  o  
       ----------
        C  R  E  
        o  o  n  
        m  p  t  
        i  a  r  
        d  s  e  
        a     t  
              e  
              n  
              i  
              m  
              i  
              e
              n  
              t  
              o  
   ```

#### Consideraciones

- **Exactitud**: Asegúrese de que el espaciado y formato del gráfico coincida exactamente con el ejemplo proporcionado.
- **Uso de Métodos**: Los métodos deben interactuar correctamente para reflejar cambios en los saldos y transferencias entre categorías.
- **Versatilidad**: La función de gráfico debe manejar hasta cuatro categorías de manera efectiva.

Este proyecto proporciona una herramienta efectiva para gestionar y visualizar presupuestos, permitiendo a los usuarios controlar sus gastos en diferentes categorías.

---
