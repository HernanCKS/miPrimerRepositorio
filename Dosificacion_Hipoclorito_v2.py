def calcular_dosificacion(
    produccion_agua,  # L/h
    volumen_tanque,   # L
    cloro_residual,   # mg/L
    concentracion_hipoclorito,  # % (p.ej., 10 para hipoclorito al 10%)
    volumen_tanque_solucion,    # L
    dosificacion_bomba          # L/h
):
    # Convertir concentración de hipoclorito a g/L
    concentracion_hipoclorito_gL = concentracion_hipoclorito * 10

    # Cloro requerido en el tanque de almacenamiento
    cloro_requerido = volumen_tanque * cloro_residual  # en mg
    hipoclorito_requerido_tanque = cloro_requerido / concentracion_hipoclorito_gL  # en L

    # Cloro requerido por hora en el flujo de agua
    cloro_requerido_hora = produccion_agua * cloro_residual  # en mg/h
    cloro_requerido_hora_g = cloro_requerido_hora / 1000  # Convertir a g/h

    # Concentración requerida en la solución
    concentracion_solucion_gL = cloro_requerido_hora_g / dosificacion_bomba  # en g/L
    hipoclorito_requerido_solucion = (
        concentracion_solucion_gL * volumen_tanque_solucion / concentracion_hipoclorito_gL
    )  # en L

    # Resultados
    return {
        "hipoclorito_tanque_almacenamiento": hipoclorito_requerido_tanque * 1000,  # en mL
        "hipoclorito_tanque_solucion": hipoclorito_requerido_solucion * 1000,  # en mL
        "concentracion_solucion": concentracion_solucion_gL,  # g/L
    }


# Parámetros configurables
produccion_agua = 300  # L/h
volumen_tanque = 4000  # L
cloro_residual = 2  # mg/L
concentracion_hipoclorito = 10  # %
volumen_tanque_solucion = 100  # L
dosificacion_bomba = 2  # L/h

# Llamar a la función
resultados = calcular_dosificacion(
    produccion_agua,
    volumen_tanque,
    cloro_residual,
    concentracion_hipoclorito,
    volumen_tanque_solucion,
    dosificacion_bomba,
)

# Mostrar resultados
print("Resultados:")
print(f"Volumen de hipoclorito requerido en el tanque de almacenamiento: {resultados['hipoclorito_tanque_almacenamiento']} mL")
print(f"Volumen de hipoclorito para preparar solución: {resultados['hipoclorito_tanque_solucion']} mL")
print(f"Concentración de la solución: {resultados['concentracion_solucion']:.3f} g/L")
