
## 6. Unidad VI. Seguridad Informática

La seguridad informática,es el conjunto de prácticas, procesos, técnicas y tecnologías diseñadas para
proteger los sistemas informáticos, redes, programas, datos y dispositivos contra amenazas, ataques y
accesos no autorizados.

### 6.1. Objetivos de la seguridad informática

El objetivo principal de la seguridad informática es garantizar la confidencialidad, integridad y disponibilidad
 de la información almacenada y procesada en entornos digitales.

> **Confidencialidad:**
> Los datos solo pueden ser legibles y modificados por personas autorizadas, tanto en el acceso a datos
> almacenados como también durante la transferencia de ellos.
>
>**Integridad:**
>Los datos están completos, sin modificar y todos los cambios son reproducibles (se conoce el autor y el
>momento del cambio). Solo quienes tengan la debida autorización podrán eliminar, descargar o modificar
>datos.
>
>**Disponibilidad:**
>El acceso a los datos debe ser garantizado en el momento necesario. Hay que evitar fallos del sistema y
>proveer el acceso adecuado.

### 6.2. Antivirus

Un antivirus es un programa diseñado para detectar, prevenir y eliminar software malicioso (malware) 
de los sistemas informáticos.El término “antivirus” a menudo se utiliza de manera más general para
referirse a programas de seguridad que abordan no solo virus tradicionales, sino también otras formas de
malware, como gusanos, troyanos, spyware, ransomware y más.



#### 6.2.1. Modos de detección que emplean los antivirus


**Modos de detección que emplean los antivirus**
**Escaneo:** Un antivirus analiza archivos y programas en busca de patrones o comportamientos
sospechosos que puedan indicar la presencia de malware. Utiliza bases de datos de firmas y
técnicas de análisis heurístico para identificar amenazas conocidas y nuevas.


**Detección de Firmas (Signature-Based):** Este método se basa en el uso de firmas o patrones
específicos conocidos de malware. Las firmas son características únicas de fragmentos de
código de malware identificados previamente

**Detección de Comportamiento:** Al observar el comportamiento de programas y procesos en
tiempo real, los antivirus pueden detectar actividades maliciosas. Por ejemplo, si un programa
intenta modificar archivos de sistema sin autorización, el antivirus podría identificarlo como
una amenaza.

### 6.3. Firewall

Un firewall es un componente de seguridad informática que actúa como una barrera entre una red privada
y redes externas, como Internet. Su función principal es controlar y monitorear el tráfico de red, permitiendo
o bloqueando la comunicación basándose en un conjunto de reglas predefinidas.

#### 6.3.1. Tipos de firewall

**Firewalls de hardware**

> Son dispositivos físicos independientes que se colocan entre la red interna y la externa. Pueden ser
> dispositivos dedicados o integrados en enrutadores y otros dispositivos de red.


**Firewalls de software:** 

> Son programas o aplicaciones que se ejecutan en sistemas operativos y proporcionan funciones de firewall. 
> Pueden ser instalados en servidores, computadoras personales o incluso dispositivos móviles.



#### 6.3.2. Funciones principales de un firewall


**Funcionamiento básico de un firewall**

> **Filtrado de Paquetes (Packet Filtering):** Examina la información de encabezado de los paquetes
> de datos y decide si permitir o bloquear el paso según reglas específicas. Las reglas
> pueden basarse en direcciones de IP, puertos, protocolos, y otros atributos del paquete.
>
> **Inspección de Estado (Stateful Inspection):** Realiza un seguimiento del estado de las conexiones
> y toma decisiones basadas en el contexto, permitiendo o bloqueando el tráfico en función
> del estado de la conexión. Si un paquete pertenece a una conexión establecida y permitida, es
>más probable que se le permita.
>
>**Logging y Auditoría:** Los firewalls registran eventos y actividades, como conexiones exitosas
> o bloqueadas. Estos registros son esenciales para la auditoría de seguridad, la resolución de
> problemas y la identificación de patrones de tráfico anómalos.


