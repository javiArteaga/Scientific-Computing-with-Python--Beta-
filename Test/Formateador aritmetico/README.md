
---

### Proyecto: **Budget App**

#### Descripción:

Como parte de su certificación, **Javiera Arteaga Moncado** desarrolló una serie de proyectos que fueron evaluados exitosamente mediante pruebas automatizadas. Uno de estos proyectos es la **Budget App**.

#### Funcionalidad:

El objetivo de este proyecto fue crear una aplicación que permitiera a los usuarios organizar y resolver problemas aritméticos de manera vertical, siguiendo normas matemáticas estrictas. Si estas normas no se cumplen, la aplicación genera un mensaje de error adecuado para informar al usuario.

#### Errores y Validaciones:

La aplicación está diseñada para manejar las siguientes situaciones de error:

- **Demasiados Problemas**:  
  Si se suministran más de cinco problemas, la aplicación devolverá:  
  `"Error: Demasiados problemas."`

- **Operadores No Permitidos**:  
  Solo se permiten operadores de suma (`+`) y resta (`-`).  
  Si se usan multiplicación o división, la aplicación devolverá:  
  `"Error: el operador debe ser '+' o '-'."`

- **Formato Numérico Incorrecto**:  
  Los operandos deben contener únicamente dígitos. Si se detectan caracteres no numéricos, la aplicación devolverá:  
  `"Error: los números solo deben contener dígitos."`

- **Número de Dígitos Excedido**:  
  Cada operando puede tener un máximo de cuatro dígitos. Si se excede este límite, se devolverá:  
  `"Error: los números no pueden tener más de cuatro dígitos."`

#### Formato de Salida:

Si los problemas están correctamente formateados, la salida seguirá las siguientes reglas:

1. **Alineación**:  
   - Los números estarán alineados a la derecha.
   - El operador se colocará en la misma línea que el segundo operando.

2. **Espaciado**:  
   - Habrá un espacio entre el operador y el operando más largo.
   - Se deben dejar cuatro espacios entre cada problema.

3. **Subrayado**:  
   - Cada problema se subrayará con guiones que cubran toda su longitud.

#### Ejemplo de Código:

```plaintext
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

---

