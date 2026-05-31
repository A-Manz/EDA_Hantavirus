# EDA_Hantavirus

Este repositorio contiene un análisis exploratorio y estadístico de casos clínicos de enfermedades causadas por hantavirus a escala global. En él se estudian las variables físicas, epidemiológicas y geográficas y su influencia en la evolución clínica de los pacientes.

El análisis se desarrolla en Python a partir de la base de datos *Hantavirus (Andes Virus) — Global Epidemiology*, publicada en Kaggle por Shahzad y Aammar (2026), concretamente mediante la tabla `hantavirus_clinical`, que contiene 8000 registros de casos clínicos.

## Hipótesis del trabajo

Se han planteado 3 hipótesis iniciales para su análisis:

1. **Los distintos síndromes causados por hantavirus tienen efectos diferenciales en la salud del individuo.**  
   Se analiza si el síndrome pulmonar por hantavirus (**HPS**) y la fiebre hemorrágica con síndrome renal (**HFRS**) influyen en variables como la gravedad, la supervivencia y la duración del ingreso hospitalario.

2. **Los pacientes con condiciones médicas adicionales presentan mayores complicaciones durante la enfermedad y una recuperación condicionada.**  
   Se evalúa si la variable `comorbidity` influye de alguna manera en la supervivencia, la gravedad o la duración de la estancia en el hospital.

3. **La distribución geográfica de los casos está relacionada con las variantes de hantavirus conocidas.**  
   Se contrasta si los patrones observados por país reflejan la separación epidemiológica entre HFRS y HPS.

## Herramientas y librerías utilizadas

Este proyecto hace uso de JupyterNotebooks como entorno principal y Python como lenguaje de programación. Adicionalmente, se han utilizado las siguientes librerías: 

**Pandas**: para la carga, limpieza y manipulación de los datos.
```bash
pip install pandas
```

**Numpy**:  para determinadas operaciones numéricas.
```bash
pip install numpy
```

**Matplotlib**: para la creación y visualización de figuras y gráficas
```bash
pip install matplotlib
```

**Seaborn**: para la creación de figuras y gráficas estadísticas
```bash
pip install seaborn
```

**Scipy**: para la realización de tests de contraste estadístico
```bash
pip install scipy
```

## Estructura del repositorio

La estructura de este repositorio es la siguiente:

```text
.
├── main.ipynb
├── README.md
├── Memoria.pdf
├── Presentacion.pdf
└── src
    ├── data
    │   └── hantavirus_clinical.csv
    ├── img
    │   └── figuras de las gráficas guardadas en formato png
    └── utils
        ├── funciones.py
        └── variables_info.ipynb
```

**`main.ipynb`**: contiene el análisis completo del estudio: carga de datos, selección de variables, análisis descriptivo univariante, análisis bivariante, visualización de los datos y contrastes estadísticos.

**`Memoria.pdf`**: recoge la explicación formal del estudio, las hipótesis, la interpretación de resultados y las conclusiones extraídas de los mismos.

**`src/data/hantavirus_clinical.csv`**: contiene la base de datos utilizada para el análisis.

**`src/utils/funciones.py`**: agrupa las funciones auxiliares de visualización utilizadas durante el análisis (diagramas de barras, histogramas por categorías, diagramas de dispersión y comparaciones entre variables cualitativas).


## Conclusiones del estudio

Se observa una relación clara entre el **síndrome presentado**, la **gravedad de la enfermedad**, la **comorbilidad**, la **supervivencia** y la **duración del ingreso hospitalario** en días. Los contrastes estadísticos indican que el tipo de síndrome causado por el hantavirus está asociado a diferencias clínicas relevantes, pero es necesaria la realización de un estudio multivariante con interacción para evaluar la influencia conjunta que estas variables tienen entre sí y en la salud del individuo.

El análisis no encuentra evidencia estadística suficiente para afirmar que la **comorbilidad** influya de forma significativa en la supervivencia, la gravedad o la duración del ingreso hospitalario de los pacientes. Por tanto, la segunda hipótesis del estudio no queda respaldada por los datos analizados.

La distribución geográfica de los casos confirma los resultados epidemiológicos conocidos: los casos de **HFRS** aparecen vinculados al continente euroasiático, mientras que los casos de **HPS** se concentran en el continente americano. Esta separación respalda la hipótesis de que la distribución geográfica está relacionada con las variantes de hantavirus conocidas, pero es necesaria la consideración de otras variables geográficas y administrativas para determinar otras posibles relaciones entre las distintas cepas de hantavirus y factores como la capacidad del sistema sanitario en cada país y su influencia en el desarrollo de la enfermedad en pacientes.

## Autoría

**Ana Manzanares Muñoz**  

- [GitHub](https://github.com/A-Manz)
- [LinkedIn](https://www.linkedin.com/in/ana-manzanares-4a8733263)