# Sistema Software FJ

Sistema integral de gestión de clientes, servicios y reservas desarrollado en Python mediante programación orientada a objetos.

## Descripción del proyecto

El sistema Software FJ permite administrar clientes, registrar servicios y gestionar reservas de manera organizada. Está diseñado para controlar las operaciones de una empresa que ofrece reserva de salas, alquiler de equipos y asesorías especializadas.

## Funcionalidades principales

- Registro y validación de clientes.
- Gestión de diferentes tipos de servicios.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con descuentos e impuestos mediante parámetros opcionales.
- Manejo de excepciones personalizadas.
- Validación de datos y control de errores.
- Registro de eventos y errores en un archivo de log.
- Aplicación de abstracción, herencia, encapsulamiento y polimorfismo.

## Servicios disponibles

1. Reserva de salas.
2. Alquiler de equipos.
3. Asesoría especializada.

## Tecnologías utilizadas

- Python.
- Programación orientada a objetos (POO).
- Git y GitHub.
- Visual Studio Code.

## Estructura del proyecto

- `main.py`: ejecución del sistema y operaciones de prueba.
- `entidades.py`: clases de entidades y clientes.
- `servicios.py`: clase abstracta de servicios y sus clases derivadas.
- `reservas.py`: gestión y control de reservas.
- `excepciones.py`: definición de excepciones personalizadas.
- `gestor_logs.py`: configuración del registro de eventos y errores.
- `software_fj.log`: archivo generado durante la ejecución para almacenar eventos y errores.

## Ejecución

Para ejecutar el sistema desde la terminal, utiliza el siguiente comando:

```bash
python main.py
```

## Pruebas

El sistema incluye 16 operaciones de prueba que permiten verificar el registro y validación de clientes, la creación de servicios, la gestión de reservas, los cálculos de costos y el manejo de errores. También se comprueba que la aplicación continúe funcionando cuando se presentan datos inválidos o excepciones controladas.

## Objetivo académico

Aplicar los principios de programación orientada a objetos y el manejo de excepciones en el desarrollo de una solución funcional para la gestión de clientes, servicios y reservas.