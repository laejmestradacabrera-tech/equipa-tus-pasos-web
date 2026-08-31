import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

# ============================================================
# EQUIPA TUS PASOS | PORTAL B2B
# VERSIÓN 1.0 — CAPTACIÓN COMERCIAL
# ============================================================

st.set_page_config(
    page_title="Equipa Tus Pasos | B2B",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CONFIGURACIÓN
# ============================================================

ARCHIVO_SOLICITUDES = Path("solicitudes_b2b.csv")

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }

    .hero {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border-radius: 24px;
        padding: 58px 35px;
        text-align: center;
        color: white;
        box-shadow: 0 12px 30px rgba(0,0,0,.14);
        margin-bottom: 35px;
    }

    .hero-title {
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 900;
        line-height: 1.08;
        letter-spacing: -1.5px;
        margin-bottom: 18px;
    }

    .hero-highlight {
        color: #fbbf24;
    }

    .hero-subtitle {
        max-width: 850px;
        margin: auto;
        color: #cbd5e1;
        font-size: 1.08rem;
        line-height: 1.65;
    }

    .section-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 900;
        color: #111827;
        margin: 15px 0 28px 0;
    }

    .catalog-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 30px;
        min-height: 370px;
        box-shadow: 0 5px 15px rgba(15,23,42,.07);
        transition: all .25s ease;
    }

    .catalog-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(15,23,42,.11);
    }

    .industrial {
        border-top: 5px solid #111827;
    }

    .clinical {
        border-top: 5px solid #38bdf8;
    }

    .card-icon {
        font-size: 3rem;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 1.45rem;
        font-weight: 900;
        color: #111827;
        margin-bottom: 12px;
    }

    .card-text {
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 18px;
    }

    .benefit {
        color: #475569;
        margin: 7px 0;
        font-size: .95rem;
    }

    .benefit span {
        color: #16a34a;
        font-weight: 900;
        margin-right: 7px;
    }

    .form-box {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 28px;
        box-shadow: 0 6px 18px rgba(15,23,42,.06);
        margin-top: 10px;
    }

    .form-title {
        font-size: 1.65rem;
        font-weight: 900;
        color: #111827;
        margin-bottom: 4px;
    }

    .form-subtitle {
        color: #64748b;
        margin-bottom: 20px;
    }

    .summary {
        background: #f8fafc;
        border-left: 4px solid #fbbf24;
        padding: 18px;
        border-radius: 12px;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: .85rem;
        padding: 30px 0 10px 0;
    }

    div.stButton > button {
        border-radius: 11px;
        font-weight: 800;
        min-height: 46px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# FUNCIONES
# ============================================================

def guardar_solicitud(datos):
    nuevo = pd.DataFrame([datos])

    if ARCHIVO_SOLICITUDES.exists():
        try:
            anterior = pd.read_csv(ARCHIVO_SOLICITUDES)
            nuevo = pd.concat([anterior, nuevo], ignore_index=True)
        except Exception:
            pass

    nuevo.to_csv(ARCHIVO_SOLICITUDES, index=False, encoding="utf-8-sig")


def seleccionar_linea(linea):
    st.session_state["linea"] = linea
    st.session_state["mostrar_formulario"] = True


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        Equipamos a tu empresa
        <span class="hero-highlight">paso a paso</span>
    </div>
    <div class="hero-subtitle">
        Distribución mayorista especializada en calzado industrial y de servicio.
        Atención corporativa, cobertura en Zona Occidente y soluciones de calzado
        para las necesidades de tu empresa.
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LÍNEAS DE ESPECIALIDAD
# ============================================================

st.markdown(
    '<div class="section-title">Nuestras Líneas de Especialidad</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="catalog-card industrial">
        <div class="card-title">Línea Industrial y Seguridad</div>
        <div class="card-text">
            Calzado diseñado para ambientes de trabajo exigentes,
            con enfoque en protección, durabilidad y confort.
        </div>
        <div class="benefit"><span>✓</span> Opciones con protección en puntera.</div>
        <div class="benefit"><span>✓</span> Suelas antiderrapantes.</div>
        <div class="benefit"><span>✓</span> Opciones resistentes a diferentes ambientes de trabajo.</div>
        <div class="benefit"><span>✓</span> Modelos para jornadas prolongadas.</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Solicitar Catálogo Industrial",
        key="btn_industrial",
        use_container_width=True,
        type="primary"
    ):
        seleccionar_linea("Industrial y Seguridad")

with col2:
    st.markdown("""
    <div class="catalog-card clinical">
        <div class="card-title">Línea Clínica y de Servicio</div>
        <div class="card-text">
            Soluciones de calzado enfocadas en comodidad, ligereza
            y funcionalidad para profesionales en constante movimiento.
        </div>
        <div class="benefit"><span>✓</span> Diseños ligeros y anatómicos.</div>
        <div class="benefit"><span>✓</span> Materiales de fácil limpieza en modelos seleccionados.</div>
        <div class="benefit"><span>✓</span> Opciones con absorción de impacto.</div>
        <div class="benefit"><span>✓</span> Confort para jornadas prolongadas.</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Solicitar Catálogo Clínico",
        key="btn_clinical",
        use_container_width=True
    ):
        seleccionar_linea("Clínica y de Servicio")

# ============================================================
# FORMULARIO Y CATÁLOGO DINÁMICO
# ============================================================

if st.session_state.get("mostrar_formulario", False):

    st.markdown("---")

    linea = st.session_state.get("linea", "No seleccionada")

    # Inyección de Catálogo Industrial
    if linea == "Industrial y Seguridad":
        st.markdown("## Ingeniería y Protección Total para tu Plantilla")
        st.markdown("""
        *Cumplimiento estricto con **NOM-113-STPS-2009** y **NOM-017-STPS-2024**.*
        * **Protección Dieléctrica:** Aislante especializado de alta fiabilidad.
        * **Casco Policarbonato+ABS:** 200 Joules de resistencia, ligero y anticorrosivo.
        * **Tecnología Anti-slip & BIOFORM:** Tracción extrema y ergonomía para reducir fatiga.
        """)
        
        st.markdown("### Modelos de Entrega Inmediata")
        
        cat1, cat2, cat3, cat4 = st.columns(4)
        
        with cat1:
            st.image("Industrial 1.png", use_container_width=True)
            st.markdown("**Mod. 142002 | Dama**")
            st.caption("PROT: PP+D")
            
        with cat2:
            st.image("Industrial 2.png", use_container_width=True)
            st.markdown("**Mod. 141902 | Dama**")
            st.caption("PROT: PP+D")
            
        with cat3:
            st.image("Industrial 3.png", use_container_width=True)
            st.markdown("**Mod. 424703 | Caballero**")
            st.caption("PROT: PP+D")
            
        with cat4:
            st.image("Industrial 4.png", use_container_width=True)
            st.markdown("**Mod. 424902 | Caballero**")
            st.caption("PROT: PP+D")
        
        st.markdown("---")

    st.markdown(
        f"""
        <div class="form-box">
            <div class="form-title">Solicita información comercial</div>
            <div class="form-subtitle">
                Línea seleccionada: <strong>{linea}</strong>
                <br>
                Completa tus datos y nuestro equipo podrá dar seguimiento a tu requerimiento.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("formulario_b2b", clear_on_submit=False):

        st.markdown("### 1. Datos de la empresa")

        c1, c2 = st.columns(2)

        with c1:
            empresa = st.text_input(
                "Empresa *",
                placeholder="Nombre de la empresa"
            )
            contacto = st.text_input(
                "Nombre del contacto *",
                placeholder="Nombre completo"
            )
            puesto = st.text_input(
                "Puesto",
                placeholder="Compras, RH, Seguridad, etc."
            )

        with c2:
            telefono = st.text_input(
                "Teléfono / WhatsApp *",
                placeholder="10 dígitos"
            )
            correo = st.text_input(
                "Correo electrónico *",
                placeholder="nombre@empresa.com"
            )
            ciudad = st.text_input(
                "Ciudad / ubicación",
                placeholder="Ej. Guadalajara, Jal."
            )

        st.markdown("### 2. Necesidad")

        c3, c4 = st.columns(2)

        with c3:
            volumen = st.selectbox(
                "Volumen aproximado",
                [
                    "Seleccionar",
                    "1–20 pares",
                    "21–50 pares",
                    "51–100 pares",
                    "101–500 pares",
                    "Más de 500 pares",
                    "Compra recurrente"
                ]
            )

        with c4:
            necesidad = st.selectbox(
                "¿Qué necesitas?",
                [
                    "Seleccionar",
                    "Catálogo",
                    "Cotización",
                    "Muestra",
                    "Compra inicial",
                    "Abastecimiento recurrente",
                    "Información general"
                ]
            )

        tallas = st.text_input(
            "Tallas requeridas",
            placeholder="Ej. 24 a 29 / surtido mixto"
        )

        comentario = st.text_area(
            "Cuéntanos qué necesitas",
            placeholder="Describe brevemente tu requerimiento..."
        )

        acepto = st.checkbox(
            "Confirmo que los datos proporcionados son correctos."
        )

        enviar = st.form_submit_button(
            "ENVIAR SOLICITUD",
            use_container_width=True,
            type="primary"
        )

    if enviar:
        errores = []

        if not empresa.strip():
            errores.append("Ingresa el nombre de la empresa.")

        if not contacto.strip():
            errores.append("Ingresa el nombre del contacto.")

        if not telefono.strip():
            errores.append("Ingresa un teléfono o WhatsApp.")

        if not correo.strip():
            errores.append("Ingresa un correo electrónico.")

        if volumen == "Seleccionar":
            errores.append("Selecciona un volumen aproximado.")

        if necesidad == "Seleccionar":
            errores.append("Selecciona el tipo de requerimiento.")

        if not acepto:
            errores.append("Confirma que los datos son correctos.")

        if errores:
            for error in errores:
                st.error(error)
        else:
            datos = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "linea": linea,
                "empresa": empresa.strip(),
                "contacto": contacto.strip(),
                "puesto": puesto.strip(),
                "telefono": telefono.strip(),
                "correo": correo.strip(),
                "ciudad": ciudad.strip(),
                "volumen": volumen,
                "necesidad": necesidad,
                "tallas": tallas.strip(),
                "comentario": comentario.strip(),
            }

            try:
                guardar_solicitud(datos)

                st.session_state["solicitud_enviada"] = True
                st.session_state["ultima_solicitud"] = datos

            except Exception as e:
                st.error(f"No fue posible registrar la solicitud: {e}")

# ============================================================
# CONFIRMACIÓN
# ============================================================

if st.session_state.get("solicitud_enviada", False):

    datos = st.session_state["ultima_solicitud"]

    st.success(
        "Solicitud registrada correctamente. Gracias por contactar a Equipa Tus Pasos."
    )

    st.markdown(
        f"""
        <div class="summary">
            <strong>Resumen de tu solicitud</strong><br><br>
            <b>Empresa:</b> {datos["empresa"]}<br>
            <b>Contacto:</b> {datos["contacto"]}<br>
            <b>Línea:</b> {datos["linea"]}<br>
            <b>Necesidad:</b> {datos["necesidad"]}<br>
            <b>Volumen:</b> {datos["volumen"]}<br>
            <b>Ubicación:</b> {datos["ciudad"] or "No indicada"}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "Realizar otra solicitud",
        use_container_width=True
    ):
        st.session_state["solicitud_enviada"] = False
        st.session_state["mostrar_formulario"] = False
        st.rerun()

# ============================================================
# PIE
# ============================================================

st.markdown("""
<div class="footer">
    Equipa Tus Pasos · Soluciones B2B de calzado · Zona Occidente
</div>
""", unsafe_allow_html=True)
