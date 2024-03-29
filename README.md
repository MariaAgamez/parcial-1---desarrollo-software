# parcial-1---desarrollo-software
**Requerimientos Funcionales:**

1. **Reserva de Herramienta:**
   - Debe haber un sistema de reserva que indique la disponibilidad de la herramienta deseada(computador/bicicleta).
   - Los estudiantes pueden reservar la herramienta para proyectos/desplazarse.

2. **Alquiler de Herramienta:**
   - Los estudiantes pueden alquilar la herramienta deseada(computador/bicicleta).
   - Deben poder seleccionar la herramienta y el período de alquiler.

3. **Pago de Servicios:**
   - Los estudiantes pueden pagar por servicios como comida en la cafetería y materiales de papelería.
   - Se debe proporcionar un método seguro de pago digital, como escaneo de códigos QR.

4. **Acceso a Biblioteca virtual:**
   - Los estudiantes pueden acceder a recursos académicos virtuales.
   - Deben poder buscar, acceder y descargar materiales académicos según sus necesidades.

5. **Gestión de Usuarios:**
   - El sistema debe permitir a los administradores iniciar sesion, agregar, modificar y eliminar cuentas de usuario según sea necesario.
   - Los administradores deben poder asignar roles y permisos a las cuentas de usuario, incluyendo roles específicos para otros administradores.

6. **Gestión de Elementos:**
   - Los administradores deben poder agregar nuevos elementos al inventario de la plataforma, incluyendo equipos tecnológicos, recursos físicos, etc.
   - Deben poder actualizar la disponibilidad y el estado de los elementos en el inventario.
   - Los administradores deben poder eliminar elementos del inventario si es necesario.

**Requerimientos No Funcionales:**

1. **Seguridad:**
   - El sistema debe cumplir con estándares de seguridad para proteger la información confidencial de los usuarios.
   - Debe haber controles de acceso apropiados para garantizar que solo los administradores autorizados puedan realizar ciertas acciones.

2. **Rendimiento:**
   - El sistema debe ser capaz de manejar un alto volumen de usuarios y transacciones simultáneas sin experimentar una degradación significativa del rendimiento.
   - Debe tener tiempos de respuesta rápidos para garantizar una experiencia de usuario fluida.

3. **Escalabilidad:**
   - El sistema debe ser escalable para permitir futuras expansiones y adiciones de características sin requerir cambios significativos en la arquitectura subyacente.

4. **Usabilidad:**
   - La interfaz de usuario para los administradores debe ser intuitiva y fácil de usar, con funciones claramente etiquetadas y accesibles.

5. **Disponibilidad:**
   - El sistema debe estar disponible la mayor parte del tiempo posible, con tiempos de inactividad planificados mínimos para mantenimiento y actualizaciones.

**Requerimientos No Funcionales:**

1. **Seguridad:**
   - La plataforma debe garantizar la seguridad de las transacciones financieras y la privacidad de los datos del usuario.
   - Debe cumplir con estándares de seguridad de la industria y regulaciones de protección de datos.

2. **Usabilidad:**
   - La interfaz de usuario debe ser intuitiva y fácil de usar para los estudiantes.
   - Debe estar optimizada para dispositivos móviles y ofrecer una experiencia fluida de navegación.

3. **Disponibilidad:**
   - La plataforma debe estar disponible las 24 horas del día, los 7 días de la semana para garantizar el acceso constante a los servicios.
   - Deben minimizarse los tiempos de inactividad planificados para mantenimiento.

**Requerimientos de Usuario (Características de UX):**

1. **Interfaz Intuitiva:**
   - La interfaz de usuario debe ser intuitiva y fácil de entender para los estudiantes, independientemente de su nivel de habilidad tecnológica.
   - Debe haber un flujo de navegación claro y coherente.

2. **Personalización:**
   - Los estudiantes deben poder personalizar su experiencia según sus preferencias y necesidades individuales.
   - Deben poder guardar elementos como favoritos o configurar preferencias de pago.

3. **Retroalimentación Instantánea:**
   - La plataforma debe proporcionar retroalimentación instantánea para confirmar acciones, como la finalización de una reserva o un pago exitoso.
   - Deben proporcionarse mensajes de error claros y orientados a la solución en caso de problemas.

**Requerimientos del Sistema:**

1. **Arquitectura escalable:**
   - El sistema debe ser capaz de escalar para manejar un aumento en el número de usuarios y transacciones sin comprometer el rendimiento.
   - Debe haber una arquitectura robusta que pueda adaptarse a futuras expansiones y actualizaciones.

2. **Integración de Datos:**
   - La plataforma debe integrarse con sistemas existentes en el campus, como la base de datos de estudiantes y los sistemas de gestión de recursos.
   - Debe permitir el intercambio seguro de datos entre diferentes componentes del sistema.

3. **Mantenibilidad:**
   - El sistema debe ser fácilmente mantenible, con capacidad para realizar actualizaciones y correcciones de errores de manera eficiente.
   - Debe haber una documentación clara y detallada para facilitar el mantenimiento del sistema.


**Descripcion con plantilla**
1. **Requerimentos funcionales:**

| ID | 0 |
|----------------------|--------------------|
| Nombre        | Reserva de Herramienta       |
| Descripción         | La funcionalidad permite a los estudiantes reservar herramientas tecnológicas para proyectos académicos.       |
| Entrada         | Solicitud de reserva de herramienta por parte del estudiante.       |
| Salida         | Confirmación de la reserva de la herramienta.       |
| Excepciones         | La herramienta solicitada no está disponible en el momento de la reserva.       |
| Autor         | Equipo de desarrollo de la Plataforma Universitaria de Servicios y Préstamos (PUSP).       |
| Prioridad         | Alta       |


| ID | 1 |
|----------------------|--------------------|
| Nombre        | Alquiler de Herramienta       |
| Descripción         | Esta funcionalidad permite a los estudiantes alquilar herramientas tecnológicas para proyectos académicos o personales.       |
| Entrada         | Solicitud de alquiler de herramienta por parte del estudiante.       |
| Salida         | Confirmación del alquiler de la herramienta.       |
| Excepciones         | La herramienta solicitada no está disponible en el momento del alquiler.       |
| Autor         | Equipo de desarrollo de la Plataforma Universitaria de Servicios y Préstamos (PUSP).       |
| Prioridad         | Alta       |


| ID | 2 |
|----------------------|--------------------|
| Nombre        | Pago de Servicios       |
| Descripción         | Esta funcionalidad permite a los estudiantes pagar servicios como comida en la cafetería y materiales de papelería de forma digital.       |
| Entrada         | Solicitud de pago por parte del estudiante.       |
| Salida         | Confirmación del pago realizado.       |
| Excepciones         | Fondos insuficientes en la cuenta del estudiante para completar el pago.       |
| Autor         | Equipo de desarrollo de la Plataforma Universitaria de Servicios y Préstamos (PUSP).       |
| Prioridad         | Alta       |



**Caso de Uso: Reservar Equipo Tecnológico**

| **Nombre:** Reservar Equipo Tecnológico |
|-----------------------------------------|
| **Descripción:** Un estudiante puede reservar equipo tecnológico, como computadoras portátiles o cámaras, a través de la PUSP para su uso en proyectos académicos o actividades relacionadas. |
| **Actores:** Estudiante |
| **Datos:** Equipo tecnológico a reservar |
| **Estímulo:** Solicitud de reserva emitida por el estudiante |
| **Respuesta:** Confirmación de la reserva y detalles del equipo tecnológico reservado |
| **Comentarios:** El estudiante debe proporcionar detalles como la fecha, la hora y la duración de la reserva. La disponibilidad del equipo se verifica antes de confirmar la reserva.|

**Caso de Uso: Realizar Pago de Servicios**

| **Nombre:** Realizar Pago de Servicios |
|----------------------------------------|
| **Descripción:** Un estudiante puede realizar pagos por servicios ofrecidos por la universidad, como comidas en la cafetería, materiales de papelería, etc., a través de la PUSP. |
| **Actores:** Estudiante |
| **Datos:** Detalles del servicio a pagar, método de pago |
| **Estímulo:** Solicitud de pago emitida por el estudiante |
| **Respuesta:** Confirmación del pago realizado |
| **Comentarios:** El estudiante selecciona el servicio que desea pagar, proporciona detalles del pago y luego recibe una confirmación de que el pago ha sido procesado correctamente.|

**Caso de Uso: Consultar Disponibilidad de Recursos**

| **Nombre:** Consultar Disponibilidad de Recursos |
|--------------------------------------------------|
| **Descripción:** Un estudiante puede consultar la disponibilidad de recursos, como computadoras, bicicletas u otros equipos, a través de la PUSP antes de realizar una reserva o alquiler. |
| **Actores:** Estudiante |
| **Datos:** Tipo de recurso deseado |
| **Estímulo:** Solicitud de consulta de disponibilidad de recursos emitida por el estudiante |
| **Respuesta:** Despliegue de la disponibilidad de recursos solicitados |
| **Comentarios:** El estudiante puede verificar la disponibilidad de recursos específicos y planificar sus actividades en consecuencia, evitando conflictos de reserva.|

