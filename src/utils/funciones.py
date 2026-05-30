
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def diagramas_barras (df, columnas, etiquetas=False, relativo=False, guardar=False):
    n = len(columnas)
    fig, axes = plt.subplots(nrows=int(np.ceil(n/3)), ncols=3, figsize=(15, 1.5*n))

    if n == 1:
        axes = [axes]

    for i, columna in enumerate(columnas):
        fila = i // 3
        columna_grafico = i % 3
        ax = axes[fila][columna_grafico]

        if df[columna].dtype == bool:
            frecuencias_abs = (df[columna].map({False:"False", True:"True"})).value_counts()
        else:
            frecuencias_abs = df[columna].value_counts()

        if relativo:
            frecuencias = frecuencias_abs / frecuencias_abs.sum() * 100
            ax.set_ylabel("Frecuencia relativa (%)")
        else:
            frecuencias = frecuencias_abs
            ax.set_ylabel("Frecuencia absoluta")

        colores = plt.cm.BuGn(np.linspace(0.35, 0.85, len(frecuencias)))
        barras = ax.bar(frecuencias.index, frecuencias.values, color = colores,  edgecolor = "black")

        ax.set_title(f"Diagrama de barras de '{columna}'")
        ax.set_xlabel(columna)
        ax.grid(axis="y", alpha=0.3)

        if etiquetas:
            for barra, frec in zip(barras, frecuencias.values):
                x = barra.get_x() + barra.get_width() / 3
                y = barra.get_height()

                if relativo:
                    texto = f"{frec:.2f}%"
                else:
                    texto = f"{frec}"

                ax.text(x, y, texto, ha="center", va="bottom", fontsize=9)
        plt.setp(ax.get_xticklabels(), rotation=60, ha="right")

    plt.tight_layout()

    if guardar: plt.savefig(f"./src/img/diagrama_barras_{"_".join(columnas)}.png", dpi=300, bbox_inches="tight") 
    plt.show()
    return


def boxplot_histograma(df, columna, relleno="#89D2A2", color_linea = "green", guardar=False):
    # Cuartiles para el boxplot
    q1 = np.percentile(df[columna], 25)
    q2 = np.percentile(df[columna], 50)
    q3 = np.percentile(df[columna], 75)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    # BOXPLOT
    sns.boxplot(y=df[columna], ax=axes[0], color=relleno, width=0.25)

    axes[0].set_title(f"Diagrama de caja de {columna}")
    axes[0].set_ylabel(columna)

    axes[0].text(0.15, q1, f"Q1 = {q1:.2f}", va="center")
    axes[0].text(0.15, q2, f"Q2 = {q2:.2f}", va="center")
    axes[0].text(0.15, q3, f"Q3 = {q3:.2f}", va="center")

    # HISTOGRAMA Y FUNCION DE DENSIDAD
    sns.histplot(df[columna], bins="auto", ax=axes[1], color=relleno, edgecolor="black")

    media = np.mean(df[columna])
    axes[1].axvline(media, color="red", linestyle="--", linewidth=1, label=f"Media = {media:.2f}")
    axes[1].legend()

    sns.kdeplot(df[columna], ax=axes[1].twinx(), color=color_linea, linewidth=2)

    axes[1].set_title(f"Histograma de {columna}")
    axes[1].set_xlabel(columna)
    axes[1].set_ylabel("Frecuencia")

    plt.tight_layout()
    if guardar: plt.savefig(f"./src/img/boxpot_histograma_{columna}.png", dpi=300, bbox_inches="tight") 
    plt.show()
    return


def histograma_por_categorias(df, var_cuantitativa, var_cualitativa, bins=20, max_cat_por_grafico = 3,  estadistico = "count", guardar=False):
    categorias = df[var_cualitativa].unique()
    grupos = [categorias[i:i + max_cat_por_grafico] for i in range(0, len(categorias), max_cat_por_grafico)]
    
    fig, axes = plt.subplots(nrows=(int(np.ceil(len(grupos)/2))), ncols=min(2, len(grupos)), figsize=(7*min(2, len(grupos)), 3 * len(grupos)))
    axes = np.array(axes).reshape(-1)   # Para recorrer con un for 

    for ax, grupo in zip(axes, grupos):

        sns.histplot(
            data=df,
            x=var_cuantitativa,
            hue=var_cualitativa,
            hue_order = grupo,  # Limitar a las variables en el grupo actual
            bins=bins,
            kde=True,
            stat=estadistico,   # "density" para valores relativos
            common_norm=True,  # Si se usa density, normaliza respecto del dataset completo
            alpha=0.4,
            ax=ax
        )
        ax.set_title(f"{var_cuantitativa} según {var_cualitativa}: "f"{', '.join(map(str, grupo))}")    # map convierte elems de lista
        ax.set_xlabel(var_cuantitativa)

    if guardar: plt.savefig(f"./src/img/histograma_{var_cuantitativa}_{var_cualitativa}.png", dpi=300, bbox_inches="tight") 
    plt.show()
    return


def comparar_cualitativas(df, var_principal, *vars_comparacion, ncols = 2, relativo=False, apilado=False, etiquetas=True, paleta="mako", guardar=False):
    n = len(vars_comparacion)
    nrows = int(np.ceil(n / ncols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(7*min(2, nrows), 6*nrows))
    axes = np.array(axes).reshape(-1)

    for i, var in enumerate(vars_comparacion):
        ax = axes[i]
        tabla = pd.crosstab(df[var], df[var_principal]) # Tabla de contingencia

        if relativo:
            tabla = tabla.div(tabla.sum(axis=1), axis=0) * 100
            ylabel = "Frecuencia relativa (%)"
        else:
            ylabel = "Frecuencia absoluta"

        if apilado:
            colores = sns.color_palette(paleta, n_colors=tabla.shape[1])
            tabla.plot( kind="bar", stacked=True, ax=ax, color=colores)

            if etiquetas:
                for contenedor in ax.containers:
                    ax.bar_label(contenedor,fmt="%.1f" if relativo else "%.0f", label_type="center")

        else:
            tabla_larga = tabla.reset_index().melt(id_vars=var, var_name=var_principal, value_name="frecuencia")    # Transformar a formato columnas

            sns.barplot(data=tabla_larga, x=var, y="frecuencia", hue=var_principal, ax=ax, palette=paleta)

            if etiquetas:
                for contenedor in ax.containers:
                    ax.bar_label(contenedor, fmt="%.1f" if relativo else "%.0f", padding=2)

        ax.set_title(f"{var_principal} según {var}")
        ax.set_xlabel(var)
        ax.set_ylabel(ylabel)
        ax.tick_params(axis="x", rotation=45)
        ax.legend(title=var_principal)

    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()

    if guardar: plt.savefig(f"./src/img/diagrama_barras_{var_principal}_{"_".join(vars_comparacion)}.png", dpi=300, bbox_inches="tight") 
    plt.show()
    return


def diagrama_dispersion(df, variable_x, variable_y, guardar=False):
    correlacion = df[variable_x].corr(df[variable_y])

    plt.figure(figsize=(8, 6))

    sns.scatterplot(data=df, x=variable_x, y=variable_y)

    plt.title(f"Diagrama de dispersión: {variable_x} vs {variable_y}\n"
        f"Coeficiente de correlación: {correlacion:.4f}")

    plt.xlabel(variable_x)
    plt.ylabel(variable_y)
    plt.grid(True, alpha=0.3)

    if guardar: plt.savefig(f"./src/img/diag_dispersion_{variable_x}_{variable_y}.png", dpi=300, bbox_inches="tight")
    plt.show()
    return