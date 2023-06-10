# TanBionIApp
## Aplicación Web a partir de conjunto de datos de Desastres Naturales de la historia del mundo.

## Descripción
El proyecto se realizó a partir del conjunto de datos: https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis. Consisten en datos sobre los desastres naturales que han sido registrados en la historia de la humanidad, con datos como fecha, lugar y gravedad basada en fatalidades y daños económicos.  


## Objetivos
Proporcionar un portal de información y reporte sobre desastres climáticos históricos.
Permitir realizar consultas personalizadas y análisis de datos a nivel de país y tipo de desastre.
Busca predecir catástrofes naturales basándose en eventos pasados para una mejor gestión del riesgo climático.

## Implementación
Se realizó mediante Flask, que integra el código HTML del mapa y el código HTML de distintas aplicaciones de Power BI para visualización de datos. 

## La aplicación
Consta de cuatro aptitudes:
- Mapa: cada país se pinta de un color dentro de una escala acorde a la cantidad de daño producido en cada uno de ellos. Fue desarrollado en Python, con implementación de la herramienta ChatGPT para encontrar las bibliotecas adecuadas y desarrollar el código correspondiente para la visualización que se pretendía lograr.
- Resumen: aplicación Power BI que permite un mapa interactivo con filtros de fecha y tipo de desastre. Ayudado en la herramienta ChatGPT.
- Países: aplicación Power BI que permite obtener un resumen por países, continentes o regiones.
- Predicciones: ayudados con la herramienta GitHub Copilot, se realizaron predicciones de fatalidades por catástrofes naturales, obteniendo una tendencia para las próximas décadas. Se realizó mediante modelos de autoregresión con media móvil (ARIMA).

## Conclusiones
Se cumplieron los objetivos propuestos de visualización de datos.
Utilizando modelos de ML se pudo predecir la tendencia de los daños en las próximas tres décadas.
Gracias a la ayuda de las herramientas de IA se pudo realizar una tarea compleja y completa con muy pocos conocimientos en programación full stack.



