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



**Caso de Uso: Transferir Datos**

| **ID:** | MHC-PMS-01 |
|---------|-------------|
| **Nombre:** | Transferir Datos |
| **Descripción:** | Un recepcionista médico puede transferir datos desde el sistema Mentcase a una base de datos de registros de pacientes generales mantenida por una autoridad de salud. La información transferida puede ser información personal actualizada (dirección, número de teléfono, etc.) o un resumen del diagnóstico y tratamiento del paciente. |
| **Actores:** | Recepcionista médico, Sistema de Registros de Pacientes (PRS) |
| **Datos:** | Información personal del paciente, resumen del tratamiento |
| **Estímulo:** | Comando del usuario emitido por el recepcionista médico |
| **Respuesta:** | Confirmación de que el PRS ha sido actualizado |
| **Comentarios:** | El recepcionista debe tener permisos de seguridad apropiados para acceder a la información del paciente y al PRS. |

**Caso de Uso: Actualizar Información Personal del Paciente**

| **ID:** | MHC-PMS-02 |
|---------|-------------|
| **Nombre:** | Actualizar Información Personal del Paciente |
| **Descripción:** | Un recepcionista médico puede actualizar la información personal del paciente, como la dirección y el número de teléfono, en el sistema Mentcase. |
| **Actores:** | Recepcionista médico |
| **Datos:** | Información personal del paciente |
| **Estímulo:** | Comando del usuario emitido por el recepcionista médico |
| **Respuesta:** | Confirmación de que la información personal del paciente ha sido actualizada |
| **Comentarios:** | El recepcionista debe tener permisos de seguridad apropiados para acceder y actualizar la información del paciente en el sistema Mentcase. |

**Caso de Uso: Transferir Resumen de Diagnóstico y Tratamiento del Paciente**

| **ID:** | MHC-PMS-03 |
|---------|-------------|
| **Nombre:** | Transferir Resumen de Diagnóstico y Tratamiento del Paciente |
| **Descripción:** | Un recepcionista médico puede transferir un resumen del diagnóstico y tratamiento del paciente desde el sistema Mentcase a la base de datos de registros de pacientes generales mantenida por una autoridad de salud. |
| **Actores:** | Recepcionista médico, Sistema de Registros de Pacientes (PRS) |
| **Datos:** | Resumen del diagnóstico y tratamiento del paciente |
| **Estímulo:** | Comando del usuario emitido por el recepcionista médico |
| **Respuesta:** | Confirmación de que el PRS ha sido actualizado con el resumen del diagnóstico y tratamiento del paciente |
| **Comentarios:** | El recepcionista debe tener permisos de seguridad apropiados para acceder a la información del paciente en el sistema Mentcase y para transferir datos al PRS. |

