from django.shortcuts import render

# funciones auxiliares de validación
def es_nombre_valido(nombre: str) -> bool:
    return bool(nombre.strip())

def es_correo_valido(correo: str) -> bool:
    if " " in correo or correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if not usuario or not dominio or "." not in dominio:
        return False
    if correo.startswith(".") or correo.endswith("."):
        return False
    return True

def es_telefono_valido(telefono: str) -> bool:
    if not telefono.startswith("+"):
        return False
    partes = telefono[1:]
    if not partes.isdigit():
        return False
    if len(partes) < 8 or len(partes) > 15:
        return False
    return True

# vista que renderiza el formulario y valida
def index(request):
    errores = {}
    mensaje = ""

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        correo = request.POST.get("correo", "").strip()
        telefono = request.POST.get("telefono", "").strip()

        # Validaciones
        if not es_nombre_valido(nombre):
            errores["nombre"] = "El nombre no puede estar vacío"
        if not es_correo_valido(correo):
            errores["correo"] = "Correo inválido"
        if not es_telefono_valido(telefono):
            errores["telefono"] = "Teléfono inválido"

        if not errores:
            mensaje = "Todos los datos son válidos ✅"

    return render(request, "index.html", {"errores": errores, "mensaje": mensaje})
