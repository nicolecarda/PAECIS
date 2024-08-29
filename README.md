
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://github.com/nicolecarda/PAECIS/blob/main/archivos/imagen_hospital.jpeg" alt="Hospital Icon" width="150px" alt="">
</a></p>

  <h3 align="center">README - Movimiento de Internación en hospitales públicos de la Ciudad Autónoma de Buenos Aires (CABA)</h3>

  <p align="center">
    Guía para recorrer los elementos del Trabajo de Investigación Final (TIF) del PAECIS. 
    <br />
  </p>
</div>

<!-- CONTENIDOS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#tecnologias">Tecnologías</a></li>
      </ul>
      <ul>
        <li><a href="#datasets">Datasets</a></li>
      </ul>
    </li>
    <li>
      <a href="#ejecucion">Ejecución</a>
      <ul>
        <li><a href="#requisitos">Requisitos</a></li>
      </ul>
    </li>
    <li><a href="#mapa-del-proyecto">Mapa del proyecto</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

<!-- SOBRE EL PROYECTO -->
## Sobre el proyecto

Este documento sintetiza aspectos técnicos del proyecto. 
La presentación y fundamentación del tema se encuentran en el <a href="https://docs.google.com/document/d/1zQXEgrDECZ2bzF5gXRDDmGZykQ0alNtXb8YtfD2Ifi0/edit#heading=h.2wdyy08e7xgr">Informe Técnico</a>.

### Tecnologías 

Aquí listamos las tecnologías utilizadas para el desarrollo del proyecto:  

* <a href="https://www.python.org/">Python</a>
* <a href="https://jupyter.org/">Jupyter Notebook</a>

### Datasets utilizados 

Los datasets utilizados están disponibles en el repositorio de Github. 

Los insumos para desarrollarlos fueron obtenidos de los siguientes sitios web: 

* <a href="https://data.buenosaires.gob.ar/dataset/movimiento-hospitalario">Buenos Aires Data: Movimiento Hospitalario</a>
* <a href="https://www.estadisticaciudad.gob.ar/eyc/?cat=335">IndecBA: Egresos e Indicadores de Internación</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- EJECUCIÓN -->
## Ejecución de los modelos y tableros

Este proyecto contiene un modelo predictivo sobre las variables que determinan la permanencia hospitalaria.
Para ejecutar el modelo que está en el archivo 'main.py', hay que indicar en la terminal la siguiente sentencia: 
$ python main.py --path "archivos" --modelo "DecisionTree" --persistir

Donde
* path: ruta donde se va a guardar el modelo.
* modelo: se puede elegir entre Decision Tree o Linear Regression.
* persistir: este comando es opcional, dependiendo si el/la usuario/a desea guardar el modelo. 

Para obtener los Dashboards, es necesario que el/la usuario/a ejecute la celda en la Jupyter Notebook. 

### Requisitos

Es necesario instalar las siguientes librerías: 
* blinker==1.8.2
* certifi==2024.2.2
* charset-normalizer==3.3.2
* click==8.1.7
* colorama==0.4.6
* dash==2.17.0
* dash-core-components==2.0.0
* dash-html-components==2.0.0
* dash-table==5.0.0
* Flask==3.0.3
* idna==3.7
* importlib_metadata==7.1.0
* itsdangerous==2.2.0
* Jinja2==3.1.4
* MarkupSafe==2.1.5
* nest-asyncio==1.6.0
* numpy==1.26.4
* packaging==24.0
* pandas==2.2.2
* plotly==5.22.0
* python-dateutil==2.9.0.post0
* pytz==2024.1
* requests==2.32.1
* retrying==1.3.4
* setuptools==69.5.1
* six==1.16.0
* tenacity==8.3.0
* typing_extensions==4.11.0
* tzdata==2024.1
* urllib3==2.2.1
* Werkzeug==3.0.3
* zipp==3.18.2

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MAPA DEL PROYECTO -->
## Mapa del Proyecto 

Sugerimos el siguiente orden de acceso a los archivos: 
1. Informe Técnico. Permite conocer la presentación del tema, la fundamentación y los objetivos.
2. Jupyter Notebooks:

        a. Unificación BDEyC: aquí se encuentran los Dashboards.

        b. Random Forest BA Data: aquí se encuentra el modelo predictivo.

        c. main.py: aquí se encuentra el desarrollo de funciones.

3. PPT PAECIS. Síntesis del proyecto y resultados. <a href="https://docs.google.com/presentation/d/1opykfX-L8uuJpe1Q3ObpWN_2meXtnJCt-mNduD6P9xo/edit#slide=id.g2e1f670a6dd_1_75">Disponible aquí</a>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACTO -->
## Contacto

* Nicole Carda - ncarda96@gmail.com
* Cecilia Palermo - cecipalermo@gmail.com
  
Link del proyecto: https://github.com/nicolecarda/PAECIS/tree/main

<p align="right">(<a href="#readme-top">back to top</a>)</p>

