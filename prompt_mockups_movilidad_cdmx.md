# Prompt maestro unificado para mockups de una plataforma de movilidad inteligente en CDMX

## 1. Rol de la IA de diseño

Actúa como un equipo sénior de Product Design, UX Research, Service Design, diseño de información, accesibilidad y movilidad urbana. Diseña una aplicación móvil de alta fidelidad, coherente y navegable para planear, monitorear y optimizar viajes en transporte público dentro de la Zona Metropolitana del Valle de México.

El resultado debe priorizar la experiencia cotidiana del pasajero. La tecnología, las métricas urbanas y la infraestructura inteligente deben aparecer como capacidades de soporte, no desplazar el flujo principal de viaje.

---

## 2. Nombre provisional

Usar temporalmente:

**Movilidad CDMX**

El nombre debe permanecer editable. No crear una identidad definitiva ni un logotipo complejo, ya que el naming todavía está por definirse.

---

## 3. Visión del producto

Crear una experiencia unificada para consultar, comparar y seguir rutas multimodales. La aplicación debe acompañar al usuario antes, durante y al finalizar su viaje, actualizando las recomendaciones cuando cambien las condiciones de movilidad.

Debe ayudar al usuario a responder rápidamente:

- ¿Cuál es la mejor ruta para mí en este momento?
- ¿Cuánto tardaré y cuánto costará?
- ¿Cuánto tendré que caminar y cuántos transbordos haré?
- ¿La ruta es accesible para mis necesidades?
- ¿Qué tan ocupada está o estará la unidad?
- ¿Cuándo llegará el siguiente servicio?
- ¿Existe algún incidente que afecte mi trayecto?
- ¿Debo cambiar de ruta y cuánto tiempo tengo para hacerlo?

---

## 4. Público objetivo y contexto de uso

Diseñar para personas que utilizan diariamente el transporte público, especialmente quienes combinan varias modalidades.

La aplicación se consultará frecuentemente:

- Caminando o dentro de una unidad en movimiento.
- Con una sola mano.
- Bajo luz solar intensa o durante la noche.
- En espacios saturados y ruidosos.
- Con poco tiempo para decidir.
- Con conexión limitada o intermitente.
- En situaciones de estrés, retrasos o interrupciones.
- Con necesidades visuales, auditivas, cognitivas o de movilidad diferentes.

La siguiente acción útil debe poder identificarse en menos de tres segundos.

---

## 5. Sistemas de transporte contemplados

Representar dentro de un ecosistema visual unificado:

- STC Metro.
- Metrobús.
- Trolebús y otros servicios de Transportes Eléctricos.
- Cablebús.
- RTP.
- Tren Ligero.
- Ecobici.
- Corredores concesionados.
- Tren Interurbano El Insurgente.
- Tren Suburbano.
- Segmentos caminando para conectar servicios.

Usar colores, iconografía y capas diferenciadas. Cuando una línea o sistema tenga una identidad cromática reconocible, conservarla para facilitar el reconocimiento. El color principal de la app no debe reemplazar los colores funcionales de las rutas.

Distinguir visualmente servicios locales, metropolitanos e interurbanos sin fragmentar la experiencia del usuario.

---

## 6. Objetivo principal de optimización

Permitir que el usuario indique un origen y un destino para recibir alternativas personalizadas considerando, cuando los datos estén disponibles:

- Tiempo total estimado.
- Tiempo de espera.
- Hora de llegada.
- Costo estimado y desglose por modalidad.
- Número de transbordos.
- Tiempo y distancia caminando.
- Nivel actual o previsto de ocupación.
- Accesibilidad de estaciones, unidades y conexiones.
- Disponibilidad de bicicletas o anclajes.
- Incidentes confirmados y reportes en revisión.
- Cierres, inundaciones, bloqueos, manifestaciones o fallas.
- Preferencias personales.
- Impacto ambiental estimado, presentado como información secundaria y con metodología aclarada.

La aplicación puede recomendar una alternativa principal, pero debe explicar por qué fue elegida y permitir comparar otras opciones.

---

## 7. Principios de experiencia

1. **Decisiones rápidas:** destacar la siguiente acción y la información que cambia la decisión.
2. **Comparación clara:** permitir comparar rutas sin abrir cada opción.
3. **Información progresiva:** mostrar primero lo esencial y ampliar detalles bajo demanda.
4. **Mapa legible:** agrupar unidades y marcadores según el zoom para evitar saturación.
5. **Recomendaciones explicables:** indicar por qué una opción es más rápida, económica, accesible o menos saturada.
6. **Alertas accionables:** incluir impacto, alternativa y tiempo disponible para reaccionar.
7. **Continuidad:** conservar el contexto al recalcular una ruta.
8. **Accesibilidad real:** no limitarse a una pantalla informativa; integrar accesibilidad en todo el flujo.
9. **Confianza:** mostrar procedencia, precisión y última actualización de los datos.
10. **Realismo:** incluir carga, ausencia de datos, conectividad limitada, permisos denegados y GPS impreciso.
11. **Privacidad:** explicar el uso de ubicación, fotografías y reportes ciudadanos.
12. **Seguridad contextual:** evitar interacciones complejas mientras la persona camina o realiza un transbordo.

---

## 8. Arquitectura de información

Usar navegación inferior con un máximo de cinco destinos:

1. **Mapa:** búsqueda, exploración y planeación.
2. **Viajes:** trayecto activo, rutas frecuentes y viajes recientes.
3. **Estado:** operación de líneas e incidentes.
4. **Reportar:** creación y seguimiento de reportes ciudadanos.
5. **Perfil:** preferencias, accesibilidad, privacidad y configuración.

Durante un trayecto activo, minimizar la navegación para dar prioridad al mapa, la siguiente acción y las alertas.

El **Centro de métricas urbanas** debe tratarse como una vista conceptual secundaria, administrativa o de demostración, no como una sección principal para el pasajero cotidiano.

---

## 9. Dirección visual

### Estética

- Moderna, premium y minimalista.
- Urbana, confiable y cercana.
- Mapas interactivos con jerarquía clara.
- Tarjetas flotantes y bottom sheets.
- Bordes redondeados y elevación moderada.
- Microinteracciones funcionales, no decorativas.
- Modo oscuro prioritario y variante en modo claro.

### Paleta propuesta

Mantener la dirección original basada en morado, complementándola con colores funcionales:

- Fondo oscuro: negro azulado o gris carbón.
- Superficies: gris oscuro.
- Acento de marca: morado eléctrico o violeta.
- Acento secundario: lavanda.
- Información: azul accesible.
- Movilidad sostenible o impacto positivo: verde accesible.
- Advertencia: ámbar o naranja.
- Incidente crítico: rojo o coral.
- Texto principal: blanco cálido o gris muy claro.
- Modo claro: blanco roto, gris claro y superficies limpias.

No usar verde, amarillo y rojo como único medio para indicar ocupación. Añadir siempre texto, ícono o patrón.

### Tipografía

- Sans serif altamente legible.
- Números de tiempo y distancia prominentes.
- Títulos breves.
- Texto adaptable sin romper componentes.
- Áreas táctiles amplias.

### Referencias de categoría

Tomar como referencia conceptual la claridad cartográfica, comparación multimodal y seguimiento de viaje de productos modernos de mapas y movilidad. No copiar directamente interfaces, componentes, iconografía ni identidad visual de terceros.

---

## 10. Sistema de datos y confianza

Cada dato dinámico debe poder mostrarse en uno de estos estados:

- **Confirmado:** dato verificado o procedente de una fuente identificada.
- **Estimado:** cálculo o inferencia con nivel de confianza.
- **Predictivo:** pronóstico futuro generado por un modelo.
- **Reportado:** información ciudadana todavía no confirmada.
- **No disponible:** no se cuenta con información suficiente.

Incluir:

- Hora de última actualización.
- Fuente o tipo de fuente cuando sea relevante.
- Indicador de confianza para predicciones.
- Mensaje “Datos de demostración” en los mockups.

No asumir que todas las modalidades entregan posición, capacidad o llegada en tiempo real. Diseñar alternativas cuando estos datos no existan.

---

## 11. Pantallas prioritarias

### 11.1 Splash y onboarding breve

Crear un splash sobrio y un onboarding de máximo tres pasos:

1. Planea rutas multimodales.
2. Recibe alertas y alternativas durante el viaje.
3. Personaliza accesibilidad y preferencias.

Solicitar ubicación después de explicar su beneficio. Permitir elegir el origen manualmente.

### 11.2 Home y mapa principal

Mostrar:

- Mapa de CDMX y zona metropolitana en modo oscuro.
- Ubicación actual y orientación.
- Búsqueda “¿A dónde vas?”.
- Estaciones y servicios cercanos.
- Estado resumido de la red.
- Rutas frecuentes o destinos guardados.
- Botón para recentrar.
- Hora de última actualización.
- Chips desplazables: Todos, Metro, Metrobús, Trolebús, Cablebús, RTP, Tren Ligero, Ecobici, Corredores y Trenes.
- Bottom sheet con servicios cercanos.

Agrupar vehículos y marcadores según el zoom. La ubicación, el destino y la ruta seleccionada deben tener prioridad visual.

### 11.3 Búsqueda y selección de destino

Incluir:

- Origen actual o editable.
- Destino por nombre, dirección, estación o punto en el mapa.
- Historial y destinos frecuentes.
- Opción “Salir ahora” o seleccionar horario.
- Inversión de origen y destino.
- Preferencias rápidas.

### 11.4 Resultados y comparación de rutas

Mostrar de tres a cinco alternativas. Cada tarjeta debe incluir:

- Tiempo total y hora de llegada.
- Costo estimado.
- Secuencia de modalidades.
- Número de transbordos.
- Tiempo y distancia caminando.
- Próxima llegada o frecuencia estimada.
- Ocupación actual o prevista.
- Estado de accesibilidad.
- Incidentes relevantes.
- Impacto ambiental estimado como dato secundario.

Etiquetas posibles:

- Más rápida.
- Más económica.
- Menos saturada.
- Menos transbordos.
- Menos caminata.
- Accesible.
- Menor impacto estimado.

Acciones:

- **Iniciar viaje**.
- **Ver pasos**.
- Guardar.
- Compartir.

### 11.5 Detalle paso a paso

Mostrar una línea de tiempo con:

- Caminatas y conexiones.
- Estación de ascenso y descenso.
- Dirección o terminal que debe buscarse.
- Paradas restantes.
- Tiempo de espera.
- Ocupación.
- Costo por segmento.
- Elevadores, rampas, accesos adaptados y posibles interrupciones.
- Alertas conocidas.
- Botón fijo “Iniciar viaje”.

### 11.6 Trayecto en tiempo real

Jerarquía:

1. Siguiente acción.
2. Tiempo o distancia para realizarla.
3. Posición y progreso actual.
4. Próxima estación o transbordo.
5. Llegada actualizada.

Mostrar:

- Mapa centrado en el usuario.
- Trayecto activo resaltado.
- Vehículo o progreso de la unidad cuando el dato exista.
- Próxima estación.
- Paradas restantes.
- Tiempo restante.
- Ocupación actual o estimada.
- Tiempo para alcanzar la siguiente conexión.
- Lista expandible de pasos.
- Botones para reportar un problema, recentrar y finalizar.

Ejemplos:

- “Baja en 3 estaciones: Hidalgo”.
- “Camina 4 min hacia la parada de Trolebús”.
- “Tu unidad llega en aproximadamente 6 min”.
- “Tienes 5 min para realizar el transbordo”.

### 11.7 Incidente y recálculo

Ante un bloqueo, inundación, manifestación, accidente, falla eléctrica, cierre o interrupción, mostrar:

- Tipo de incidente.
- Ubicación aproximada.
- Estado: confirmado o en revisión.
- Impacto estimado.
- Última actualización.
- Alternativa recomendada.
- Diferencia de tiempo y costo.
- Tiempo disponible para alcanzar la conexión.

Acciones:

- **Cambiar a esta ruta**.
- **Ver otras opciones**.
- **Mantener ruta actual**.

No cambiar silenciosamente el viaje cuando implique otra modalidad, mayor costo, caminata considerable o una diferencia importante de tiempo.

### 11.8 Estado de la red

Diseñar una vista escaneable con:

- Estado general.
- Sistemas y líneas agrupados.
- Operación normal, demoras, servicio parcial o interrupción.
- Incidentes, inundaciones, fallas eléctricas y cierres.
- Filtros por modalidad, cercanía y severidad.
- Hora de actualización.
- Detalle de incidencia y servicios alternativos.

Evitar un dashboard excesivamente técnico para el usuario final.

### 11.9 Reportes ciudadanos

Crear un flujo breve y seguro para reportar:

- Manifestación o bloqueo.
- Accidente.
- Inundación.
- Estación cerrada.
- Falla de unidad o infraestructura.
- Problema de accesibilidad.
- Problema general de seguridad, sin solicitar detalles que expongan a la persona.

Formulario:

- Categoría.
- Ubicación automática editable.
- Descripción breve opcional.
- Fotografía opcional.
- Hora del evento.
- Envío anónimo o identificado según preferencias.

Después de enviar, mostrar estado:

- Recibido.
- En revisión.
- Confirmado.
- Resuelto.

La “validación comunitaria” debe evitar concursos de popularidad. Diseñar confirmaciones contextuales como “¿Esto sigue ocurriendo?” y combinar señales comunitarias con moderación y fuentes confiables. Incluir advertencias de privacidad antes de cargar fotografías y no incentivar reportar mientras se conduce o en una situación riesgosa.

### 11.10 Perfil y preferencias

Permitir configurar:

- Más rápida.
- Más económica.
- Menos caminata.
- Menos transbordos.
- Evitar saturación.
- Preferir Ecobici.
- Requerir rutas accesibles.
- Umbral máximo de caminata.
- Preferencias de alertas, vibración y sonido.
- Tamaño de texto, contraste y navegación simplificada.
- Privacidad y uso de ubicación.
- Rutas frecuentes.

### 11.11 Llegada al destino

Mostrar:

- Confirmación de llegada.
- Tiempo planeado frente al tiempo real.
- Incidentes evitados o cambios realizados.
- Costo estimado final.
- Opción de calificar la precisión.
- Guardar destino.
- Finalizar viaje.

---

## 12. Accesibilidad universal integrada

No diseñar la accesibilidad como una función aislada. Aplicarla a todas las pantallas.

### Discapacidad visual

- Alto contraste.
- Compatibilidad conceptual con lectores de pantalla.
- Orden lógico de enfoque.
- Botones grandes.
- Texto escalable.
- Instrucciones breves y auditivas opcionales.
- No colocar texto directamente sobre zonas complejas del mapa.

### Discapacidad auditiva

- Instrucciones completamente visuales.
- Vibraciones configurables para próximas acciones y alertas.
- Iconos y texto para toda señal sonora.

### Movilidad reducida

- Filtro de rutas accesibles.
- Elevadores, rampas y accesos adaptados.
- Estado operativo de infraestructura accesible cuando esté disponible.
- Mayor tiempo de conexión configurable.
- Alternativas cuando un elevador o acceso esté fuera de servicio.

### Accesibilidad cognitiva

- Lenguaje directo.
- Una acción principal por estado.
- Navegación simplificada opcional.
- Consistencia en iconografía y posición de controles.

---

## 13. Ocupación e Índice de Saturación Predictiva

### Ocupación actual o estimada

Combinar porcentaje, etiqueta e ícono:

- Baja: 0% a 35%.
- Media: 36% a 70%.
- Alta: 71% a 90%.
- Muy alta: 91% a 100%.
- Sin información.

Los rangos son demostrativos y deben validarse posteriormente.

### Índice de Saturación Predictiva

Añadir una función diferenciadora que pronostique ocupación futura y sugiera momentos alternativos de salida.

Ejemplo:

> “Si sales en 15 min, se estima una ocupación 25% menor. Tu llegada podría cambiar 8 min.”

Siempre mostrar:

- Que se trata de una predicción.
- Horizonte temporal.
- Nivel de confianza.
- Última actualización.
- Opción de comparar “Salir ahora” frente a “Salir después”.

No presentar predicciones como garantías ni prometer ahorro de tiempo sin indicar incertidumbre.

---

## 14. Centro conceptual de métricas urbanas

Crear una vista independiente, secundaria y claramente diferenciada de la app del pasajero. Puede representar una consola para operadores, autoridades o una demostración de ciudad inteligente.

Mostrar de forma agregada:

- Estado de la red.
- Flujo estimado de pasajeros.
- Saturación por zona o sistema.
- Incidentes del día.
- Tendencias y predicciones.
- Cobertura y calidad de datos.

No mostrar ubicaciones individuales ni datos personales. Evitar métricas decorativas sin propósito operativo.

---

## 15. Capa tecnológica conceptual

Comunicar en una lámina explicativa, no necesariamente dentro de la interfaz principal, que la plataforma podría apoyarse en:

- GPS o telemetría de unidades.
- Sensores de conteo de pasajeros.
- Dispositivos de cómputo a bordo, sin depender de una marca o modelo específico.
- Datos abiertos y fuentes gubernamentales.
- Información de operadores.
- Reportes ciudadanos moderados.
- Analítica en tiempo real.
- Modelos predictivos de saturación y tiempos de llegada.
- Conectividad pública o móvil disponible.

Presentar estos elementos como arquitectura conceptual o fuentes potenciales. No afirmar que toda la infraestructura ya existe, está desplegada o alimenta el producto.

---

## 16. Estados complementarios

Diseñar variantes para:

- Permiso de ubicación.
- Permiso de notificaciones.
- GPS impreciso.
- Carga y skeletons.
- Conectividad limitada.
- Modo sin conexión con ruta precargada.
- Sin rutas disponibles.
- Sin datos en tiempo real.
- Ocupación desconocida.
- Servicio saturado.
- Incidente en revisión.
- Predicción con baja confianza.
- Elevador fuera de servicio.
- Fotografía rechazada por privacidad o moderación.
- Reporte enviado y confirmado.

---

## 17. Componentes reutilizables

Crear un mini sistema de diseño con:

- Barra de búsqueda.
- Selector origen-destino.
- Chips por modalidad.
- Tarjetas de ruta.
- Tarjeta de siguiente acción.
- Timeline de viaje.
- Marcadores de usuario, estación, unidad e incidente.
- Indicador de ocupación.
- Indicador predictivo con confianza.
- Etiqueta de fuente y actualización.
- Bottom sheets colapsado, medio y expandido.
- Alertas de severidad variable.
- Navegación inferior.
- Botones primario, secundario, terciario e iconográfico.
- Controles de accesibilidad.
- Tarjetas de estado de línea.
- Formulario de reporte.
- Skeleton, estado vacío, snackbar y modal.

---

## 18. Microinteracciones

- Transición suave entre ruta anterior y recalculada.
- Pulso discreto de ubicación actual.
- Actualización de tiempos sin saltos bruscos.
- Estado “Recalculando ruta…”.
- Confirmación al activar filtros.
- Expansión accesible de bottom sheets.
- Vibración configurable para próximas acciones y alertas críticas.
- Evitar animaciones decorativas durante el trayecto.
- Respetar preferencias de movimiento reducido.

---

## 19. Datos de demostración

Usar datos ficticios pero verosímiles:

- Origen: Tu ubicación.
- Destino: Centro Histórico.
- Viaje: 47 min.
- Llegada: 08:42.
- Costo estimado: $15 MXN.
- Próximo servicio: 4 min.
- Ocupación estimada: media, 62%.
- Caminata: 8 min.
- Transbordos: 1.
- Última actualización: hace 20 s.
- Predicción: ocupación 25% menor saliendo en 15 min, confianza media.

Marcar el prototipo como **Datos de demostración**.

---

## 20. Flujo navegable principal

Conectar el siguiente recorrido:

1. Abrir la aplicación.
2. Completar onboarding breve o saltarlo.
3. Autorizar ubicación o elegir origen manual.
4. Ver mapa y estado resumido.
5. Buscar destino.
6. Comparar rutas.
7. Aplicar una preferencia de accesibilidad o saturación.
8. Abrir detalle paso a paso.
9. Iniciar viaje.
10. Recibir alerta por incidente.
11. Comparar y aceptar una ruta alternativa.
12. Completar un transbordo.
13. Llegar al destino.
14. Calificar precisión.

Crear un flujo secundario para consultar el estado de la red y enviar un reporte ciudadano.

---

## 21. Entregables

Generar:

1. Mockups móviles de alta fidelidad para todas las pantallas prioritarias.
2. Frames base cercanos a 390 × 844 px y diseño adaptable.
3. Modo oscuro completo y una muestra significativa en modo claro.
4. Sistema de diseño con componentes, variantes y estados.
5. Bottom sheets en estados colapsado, medio y expandido.
6. Flujo principal navegable.
7. Flujo secundario de reporte ciudadano.
8. Estados de carga, error, falta de datos y conectividad limitada.
9. Vista conceptual del Centro de métricas urbanas.
10. Lámina conceptual de arquitectura tecnológica.
11. Anotaciones breves de UX para decisiones clave.

---

## 22. Restricciones y cosas que se deben evitar

- No saturar el mapa con todas las unidades simultáneamente.
- No copiar interfaces de productos existentes.
- No usar el color como único indicador.
- No inventar disponibilidad de datos operativos.
- No representar predicciones como certezas.
- No cambiar rutas importantes sin explicar y pedir acción.
- No ocultar costo, caminata o accesibilidad en niveles profundos.
- No convertir la app del pasajero en un dashboard técnico.
- No exponer datos personales o ubicaciones individuales en métricas.
- No incentivar reportes en situaciones peligrosas.
- No usar una Raspberry Pi u otra marca concreta como requisito visual del producto.
- No mostrar impacto ambiental sin aclarar que es una estimación.
- No generar textos demasiado pequeños ni tarjetas excesivamente densas.

---

## 23. Prompt condensado listo para pegar

Diseña una aplicación móvil de alta fidelidad llamada provisionalmente **Movilidad CDMX** para planear, comparar y seguir viajes multimodales en la Ciudad de México y su zona metropolitana. Integra conceptualmente Metro, Metrobús, Trolebús, Cablebús, RTP, Tren Ligero, Ecobici, corredores concesionados, Tren Interurbano El Insurgente, Tren Suburbano y segmentos caminando.

La experiencia debe ayudar al usuario a elegir rutas considerando tiempo total, espera, costo, transbordos, caminata, ocupación actual o prevista, accesibilidad, incidentes y preferencias personales. Recomienda una opción principal, explica por qué y permite comparar entre tres y cinco alternativas con etiquetas como “Más rápida”, “Más económica”, “Menos saturada” y “Accesible”.

Crea un flujo conectado con splash, onboarding breve, permiso de ubicación, Home con mapa, búsqueda de destino, resultados, detalle paso a paso, trayecto en tiempo real, incidente con recálculo, llegada al destino, estado de la red, reportes ciudadanos y perfil. Agrega una función de Índice de Saturación Predictiva que compare salir ahora frente a salir después, mostrando siempre que es una predicción, su nivel de confianza y la última actualización.

Usa una estética moderna, premium y minimalista. Prioriza modo oscuro con fondos carbón, superficies oscuras y acentos morados; usa verde para movilidad sostenible, azul para información, naranja para advertencias y rojo para incidencias críticas. Conserva colores funcionales de líneas y modalidades. Incluye una muestra en modo claro. Utiliza tarjetas flotantes, bottom sheets, bordes redondeados, mapas legibles y microinteracciones funcionales.

Integra accesibilidad en todas las pantallas: alto contraste, texto escalable, botones grandes, lector de pantalla, vibraciones configurables, navegación visual, rutas con elevadores y rampas, mayor tiempo de conexión y navegación simplificada. No dependas únicamente del color.

Diferencia datos confirmados, estimados, predictivos, reportados y no disponibles. Muestra fuente, confianza y última actualización cuando corresponda. No asumas que todas las modalidades ofrecen GPS, ocupación o tiempos en vivo. Usa datos ficticios marcados como “Datos de demostración”.

Diseña reportes ciudadanos con categoría, ubicación editable, descripción y fotografía opcionales, protección de privacidad, moderación y estados Recibido, En revisión, Confirmado y Resuelto. No incentivas reportar en situaciones riesgosas.

Crea una vista secundaria de métricas urbanas, claramente separada de la experiencia del pasajero, con información agregada y sin datos personales. Incluye una lámina conceptual sobre posibles fuentes tecnológicas como telemetría, sensores, cómputo a bordo, datos abiertos, reportes moderados y modelos predictivos, sin afirmar que ya están desplegados.

Genera frames cercanos a 390 × 844 px, componentes reutilizables, variantes de bottom sheets, estados de carga y error, un flujo navegable principal y un flujo secundario de reporte. La siguiente acción debe identificarse en menos de tres segundos. Evita mapas saturados, precisión ficticia, predicciones presentadas como garantías y dashboards técnicos dentro del recorrido cotidiano.

---

## 24. Criterios de evaluación

- La siguiente acción se identifica rápidamente.
- Las rutas se comparan sin abrir cada tarjeta.
- Tiempo, costo, ocupación, caminata, transbordos y accesibilidad tienen jerarquía clara.
- La recomendación explica su criterio.
- Los incidentes ofrecen una alternativa accionable.
- El recálculo conserva el contexto.
- Se diferencia entre dato confirmado, estimado, predictivo y reportado.
- La predicción comunica incertidumbre.
- La interfaz funciona conceptualmente con lector de pantalla y texto grande.
- El mapa permanece legible.
- Los reportes protegen privacidad y seguridad.
- El dashboard urbano no invade la experiencia del pasajero.
- Las capacidades tecnológicas se presentan como concepto, no como infraestructura confirmada.
