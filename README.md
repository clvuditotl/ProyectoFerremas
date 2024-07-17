# Proyecto Ferremas

### Descripción del Proyecto
El proyecto Ferremas tiene como objetivo principal la integración de una nueva API/Webservice 
con el sistema de pagos WEBPAY y la funcionalidad de conversión de divisas. Este sistema está diseñado 
para mejorar y automatizar el proceso de consulta de productos, procesamiento de pagos en línea y 
conversión de divisas en tiempo real. La finalidad es asegurar que todas las funcionalidades desarrolladas 
cumplan con los requisitos especificados y se integren de manera eficiente con los sistemas existentes, 
garantizando una experiencia de usuario segura y sin problemas​

## Lenguajes de Programación
- JavaScript
- Python
- SQL

## Tecnologías Utilizadas
- Java: Principal lenguaje de programación utilizado para desarrollar la lógica de negocio y las APIs.
- Node.js: Entorno de ejecución para JavaScript en el servidor.
- MySQL: Sistemas de gestión de bases de datos relacionales utilizados para almacenar información de productos, usuarios y transacciones.
- HTTPS: Protocolo de transferencia de hipertexto seguro utilizado para cifrar la comunicación entre el cliente y el servidor.
- WEBPAY: Plataforma de pagos en línea utilizada para procesar transacciones con tarjetas de crédito y débito.
- API del Banco Central de Chile: Servicio utilizado para la conversión de divisas y obtener tasas de cambio actualizadas.
- GitHub/GitLab/Bitbucket: Plataformas para la colaboración en el desarrollo y gestión de repositorios de código.

## Base de Datos
- La base de datos utilizada en el proyecto es Microsoft SQL Server

## Arquitectura
1. API/Webservice 
2. Sistema de Pagos WEBPAY
3. API de Conversión de Divisas

#### Interacción entre Componentes
- Consulta de Productos:
El cliente envía una solicitud a la API de FERREMAS para obtener información sobre un producto específico.
La API responde con los detalles del producto, incluyendo el nombre, marca, código y precio.

- Actualización de Inventarios:
El administrador o el sistema interno envía una solicitud a la API para actualizar el stock de un producto.
La API procesa la solicitud y actualiza la información en la base de datos, devolviendo un mensaje de confirmación.

- Procesamiento de Pagos:
El cliente realiza una compra y selecciona el método de pago.
La solicitud de pago se envía al módulo de integración de pagos WEBPAY.
WEBPAY procesa la transacción y devuelve el estado de la misma (aprobada o rechazada) junto con un ID de transacción.

- Conversión de Divisas:
El cliente selecciona la opción de convertir divisas para saber el valor de su compra en otra moneda.
La solicitud se envía a la API de Conversión de Divisas, que consulta al Banco Central de Chile.
La API devuelve el monto convertido y la tasa de cambio utilizada.

![Untitled](https://github.com/user-attachments/assets/1ee15a2f-687e-4a12-b599-57311e5e13b3)

##Frameworks Utilizados

- Node.js: Utilizado para construir servicios backend y manejar solicitudes asincrónicas.
- Spring Boot: Utilizado para construir las APIs del sistema, manejando la lógica de negocio y la comunicación con la base de datos.
- Hibernate: Empleado para la interacción con la base de datos relacional, gestionando operaciones CRUD (crear, leer, actualizar y eliminar) de manera eficiente.
- Angular: Utilizado para desarrollar la interfaz de usuario, permitiendo una experiencia interactiva y responsiva para los usuarios.
- Express.js: Empleado junto con Node.js para construir y manejar la lógica del servidor y las rutas de la aplicación.
