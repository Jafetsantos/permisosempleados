 Proyecto: [Permisos de Empleados]

 ## Descripción
La necesidad de optimizar la gestión de solicitudes de permisos en la UNAH-Comayagua motivó el desarrollo de este proyecto.
A través de un sistema automatizado, se busca solucionar la problemática actual, caracterizada por trámites engorrosos y tiempos de respuesta prolongados. 
La herramienta, diseñada en el marco del curso de Análisis y Diseño de Sistemas, permite a los empleados realizar solicitudes de forma digital y facilita el seguimiento del proceso por parte de todas las partes involucradas.

### Tecnologías utilizadas
- Lenguaje de programación: [Python]
- Frameworks: [Odoo]
- Herramientas: [Github]

## Estructura del Proyecto
- `/_pycache_`: 
- `/controllers`: 
- `/demo`: 
- `/models`:
-     - _init_.py
-     - employees.py
-     - personalinfo.py
-     - seguimiento_empleado.py
-     - seguimiento_permiso.py
-     - Solicitud.py
- `/security`: 
- `/view`:
-     - employees.xml
-     - personalinfo.xml
-     - seguimiento_empleado.xml
-     - seguimiento_permiso.xml
-     - Solicitud.xml
- _init_.py
- _manifest_.py 

## Contribuciones

### Integrante 1: [Katie]
- **Rol:** [Frontend, Backend]
- **Tareas:**
  - Implementó el Modelo employees, personalinfo.
  - Implementó el Vista employees, personalinfo.
- **Imagen de Referencia:**
![1](https://github.com/user-attachments/assets/f132dac3-7757-4957-ba5d-1cc1c5732c11)
![2](https://github.com/user-attachments/assets/d7365984-85e4-460d-9dd6-6e03c5665b50)
![6](https://github.com/user-attachments/assets/a2e842e0-de60-4da3-b04f-c7299231ae0c)
![10](https://github.com/user-attachments/assets/2466e671-84da-401b-9d48-3d599cd601dd)


### Integrante 1: [Erick]
- **Rol:** [Frontend, Backend]
- **Tareas:** 
  - Implementó el Modelo employees, personalinfo.
  - Implementó el Vista employees, personalinfo.
- **Imagen de Referencia:**
  No colocamos imagenes porque son las mismas que Katie ya que se trabajo en parejas.
  
### Integrante 1: [Axel Santos]
- **Rol:** [Frontend, Backend]
- **Tareas:** 
  - Implementó el Modelo seguimiento_permiso.
  - Implementó el Vista seguimiento_permiso.
  - Implementó los grupos.
- **Imagen de Referencia:**
![3](https://github.com/user-attachments/assets/5b062ec1-725d-4b3b-9964-755cd188dfef)
![4](https://github.com/user-attachments/assets/05e7a314-6af2-48f8-b5ec-3e5e0d0fad64)
![5](https://github.com/user-attachments/assets/40d49bd0-470c-4afc-8f6f-372f80803019)

 ### Integrante 1: [Wendy]
- **Rol:** [Frontend]
- **Tareas:** 
  - Implementó el Modelo seguimiento_empleado.
  - Implementó el Vista seguimiento_empleado.
- **Imagen de Referencia:**
![7](https://github.com/user-attachments/assets/9629ceec-ddfa-4351-aece-554f73b955c5)
![8](https://github.com/user-attachments/assets/06dc57ca-bc31-40d9-bf93-6f9c331d4557)

### Integrante 1: [Mavet]
- **Rol:** [Backend]
- **Tareas:** 
  - Implementó el sistema de autenticación.
  - Diseñó la interfaz de usuario.
- **Imagen de Referencia:**


## Funcionamiento del Sistema

### Énfasis en la experiencia del usuario

"Una vez que el usuario inicia sesión, accede a un panel personal donde puede:

Gestionar su perfil: Editar sus datos y preferencias.
Realizar un seguimiento de sus solicitudes: Visualizar el estado de cada solicitud a través de una interfaz Kanban o una lista detallada.
Solicitar permisos: Completar un formulario intuitivo para realizar nuevas solicitudes."

### Énfasis en las funcionalidades del sistema

"El sistema ofrece a Recursos Humanos las siguientes funcionalidades:

Creación de usuarios: Permite agregar nuevos usuarios al sistema.
Panel de gestión de solicitudes: Ofrece una vista general de todas las solicitudes, con opciones de filtrado por estado (pendientes, aprobadas, rechazadas).
Flujo de aprobación: Facilita la toma de decisiones a través de botones de aprobación y rechazo para cada solicitud."
