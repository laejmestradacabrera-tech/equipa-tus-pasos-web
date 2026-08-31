import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import base64

# ============================================================
# EQUIPA TUS PASOS | PORTAL B2B
# VERSIÓN 2.0 — SEO Y CATÁLOGO INTEGRADO
# ============================================================

# Optimización SEO #1: Título de página con palabras clave de alto impacto
st.set_page_config(
    page_title="Calzado Industrial Flexi PRO | Equipa Tus Pasos B2B",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# INYECCIÓN SEO (Invisible para el usuario, visible para Google)
# ============================================================
st.markdown("""
<div style="display: none;" aria-hidden="true">
    <h1>Distribuidor Mayorista Calzado Industrial Flexi PRO en Guadalajara y Jalisco</h1>
    <p>Equipa Tus Pasos es el proveedor líder B2B de botas de seguridad industrial, calzado clínico y zapatos de trabajo Flexi PRO en la Zona Occidente, Tlaquepaque y Guadalajara. Cumplimiento estricto con NOM-113-STPS-2009 y NOM-017-STPS-2024. Calzado dieléctrico, suela anti-slip, casco de policarbonato y tecnología BIOFORM. Venta por volumen para empresas. Modelos 142002, 141902, 424703 y 424902 disponibles para entrega inmediata. Cotizaciones B2B.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CONFIGURACIÓN
# ============================================================

ARCHIVO_SOLICITUDES = Path("solicitudes_b2b.csv")

# ============================================================
# CSS CORPORATIVO (Sin emojis, tonos institucionales)
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
        background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
        border-radius: 24px;
        padding: 58px 35px 40px 35px;
        text-align: center;
        color: white;
        box-shadow: 0 12px 30px rgba(0,0,0,.14);
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 900;
        line-height: 1.08;
        letter-spacing: -1.5px;
        margin-bottom: 18px;
    }

    .hero-highlight {
        color: #b91c1c; /* Tono guinda Flexi PRO */
    }

    .hero-subtitle {
        max-width: 850px;
        margin: auto;
        color: #cbd5e1;
        font-size: 1.08rem;
        line-height: 1.65;
    }
    
    .brand-banner {
        background-color: #f1f5f9;
        color: #475569;
        text-align: center;
        padding: 12px;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 35px;
        font-size: 0.9rem;
        text-transform: uppercase;
        border: 1px solid #e2e8f0;
    }
    
    .brand-banner span {
        color: #b91c1c;
        font-weight: 900;
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
        border-top: 5px solid #b91c1c;
    }

    .clinical {
        border-top: 5px solid #0369a1;
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
        border-left: 4px solid #b91c1c;
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
# HERO Y BRANDING FLEXI
# ============================================================

col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    try:
        st.image("logo_flexi.png", use_container_width=True)
    except Exception:
        st.markdown("<h2 style='text-align: center; color: #b91c1c; font-weight: 900; font-style: italic; letter-spacing: 2px; margin-bottom: 20px;'>FLEXI PRO</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">
        Equipamos a tu empresa
        <span class="hero-highlight">paso a paso</span>
    </div>
    <div class="hero-subtitle">
        Lleva la reconocida comodidad y tecnología de Flexi a tu entorno laboral. 
        Distribución mayorista especializada en calzado corporativo para la Zona Occidente, 
        asegurando protección certificada y confort absoluto para tu plantilla.
    </div>
</div>
<div class="brand-banner">
    Distribuidor de soluciones corporativas con el respaldo de <span>FLEXI PRO</span><br>
    <span style="font-size: 0.85rem; font-weight: 500; text-transform: none; margin-top: 8px; display: inline-block; color: #111827;">
        Capacidad de surtimiento garantizada para cualquier modelo de la <b>Colección Otoño-Invierno</b> en los volúmenes que tu empresa requiera.
    </span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CONSULTA DE CATÁLOGO COMPLETO (Visor PDF incrustado)
# ============================================================

with st.expander("CONSULTAR CATÁLOGO COMPLETO OI", expanded=False):
    try:
        with open("catalogo_flexi.pdf", "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception:
        st.info("El catálogo virtual se está actualizando. Solicítalo directamente vía WhatsApp o en el formulario inferior.")

st.markdown("<br>", unsafe_allow_html=True)

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
        <div class="card-title">Línea Flexi PRO Industrial</div>
        <div class="card-text">
            La comodidad superior de Flexi, blindada para entornos exigentes. 
            Calzado certificado que tu personal realmente querrá utilizar durante toda su jornada.
        </div>
        <div class="benefit"><span>✓</span> Tecnología ergonómica BIOFORM de Flexi.</div>
        <div class="benefit"><span>✓</span> Cumplimiento estricto de la NOM-113-STPS.</div>
        <div class="benefit"><span>✓</span> Casco de Policarbonato ultraligero y dieléctrico.</div>
        <div class="benefit"><span>✓</span> Suelas Anti-slip de máxima tracción.</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Ver Catálogo Flexi PRO Industrial",
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
            Soluciones de calzado enfocadas en comodidad térmica, ligereza
            y funcionalidad para profesionales de la salud en constante movimiento.
        </div>
        <div class="benefit"><span>✓</span> Soporte anatómico característico de Flexi.</div>
        <div class="benefit"><span>✓</span> Materiales premium de fácil limpieza.</div>
        <div class="benefit"><span>✓</span> Absorción de impacto en cada paso.</div>
        <div class="benefit"><span>✓</span> Diseñado para guardias y jornadas prolongadas.</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Ver Catálogo Clínico",
        key="btn_clinical",
        use_container_width=True
    ):
        seleccionar_linea("Clínica y de Servicio")

# ============================================================
# CATÁLOGO DINÁMICO Y FORMULARIO
# ============================================================

if st.session_state.get("mostrar_formulario", False):

    st.markdown("---")

    linea = st.session_state.get("linea", "No seleccionada")

    # Inyección de Catálogo Flexi PRO Industrial
    if linea == "Industrial y Seguridad":
        st.markdown("## Ingeniería Flexi PRO para tu Plantilla")
        st.markdown("""
        *El aliado estratégico para la seguridad industrial. Fabricado con materiales de calidad superior.*
        * **Cumplimiento Legal:** Certificación oficial **NOM-113-STPS-2009** y **NOM-017-STPS-2024**.
        * **Protección Dieléctrica (PP+D):** Aislante especializado de alta fiabilidad en entornos de riesgo.
        * **Casco Policarbonato+ABS:** 200 Joules de resistencia, ligero, anticorrosivo y libre de sustancias tóxicas.
        * **Tecnología BIOFORM y Anti-slip:** Suela moldeada anatómicamente y patín que reduce drásticamente el riesgo de derrape.
        """)
        
        st.markdown("### Modelos de Entrega Inmediata")
        
        cat1, cat2, cat3, cat4 = st.columns(4)
        
        with cat1:
            try:
                st.image("Industrial 1.png", use_container_width=True)
            except Exception:
                st.info("Imagen no disponible")
            st.markdown("**Mod. 142002 | Dama**")
            st.caption("PROT: PP+D | Flexi PRO")
            
        with cat2:
            try:
                st.image("Industrial 2.png", use_container_width=True)
            except Exception:
                st.info("Imagen no disponible")
            st.markdown("**Mod. 141902 | Dama**")
            st.caption("PROT: PP+D | Flexi PRO")
            
        with cat3:
            try:
                st.image("Industrial 3.png", use_container_width=True)
            except Exception:
                st.info("Imagen no disponible")
            st.markdown("**Mod. 424703 | Caballero**")
            st.caption("PROT: PP+D | Flexi PRO")
            
        with cat4:
            try:
                st.image("Industrial 4.png", use_container_width=True)
            except Exception:
                st.info("Imagen no disponible")
            st.markdown("**Mod. 424902 | Caballero**")
            st.caption("PROT: PP+D | Flexi PRO")
        
        st.markdown("---")

    # Botón de Contacto Rápido (WhatsApp)
    st.markdown(
        """
        <div style="background: white; border: 1px solid #e5e7eb; border-radius: 16px; padding: 25px; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 style="color: #111827; margin-bottom: 10px;">¿Prefieres atención inmediata y directa?</h3>
            <p style="color: #64748b; margin-bottom: 20px;">Si deseas omitir el formulario, envíanos un mensaje y un especialista corporativo te atenderá en este momento.</p>
            <a href="https://wa.me/4773949916" target="_blank" style="background-color: #25d366; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 900; display: inline-block;">
                CONTACTAR POR WHATSAPP
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="form-box">
            <div class="form-title">Solicita información comercial</div>
            <div class="form-subtitle">
                Línea seleccionada: <strong>{linea}</strong>
                <br>
                Completa tus datos y un especialista corporativo te contactará a la brevedad.
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

        st.markdown("### 2. Necesidad del proyecto")

        c3, c4 = st.columns(2)

        with c3:
            volumen = st.selectbox(
                "Volumen aproximado",
                [
                    "Seleccionar",
                    "1 a 20 pares",
                    "21 a 50 pares",
                    "51 a 100 pares",
                    "101 a 500 pares",
                    "Más de 500 pares",
                    "Abastecimiento recurrente"
                ]
            )

        with c4:
            necesidad = st.selectbox(
                "¿Qué requieres en este momento?",
                [
                    "Seleccionar",
                    "Cotización formal",
                    "Catálogo completo",
                    "Muestra física",
                    "Información general"
                ]
            )

        tallas = st.text_input(
            "Curva de tallas (Opcional)",
            placeholder="Ej. 24 a 29 / Surtido mixto"
        )

        comentario = st.text_area(
            "Detalles adicionales",
            placeholder="Describe brevemente las necesidades de tu planta o personal..."
        )

        acepto = st.checkbox(
            "Confirmo que los datos proporcionados son correctos."
        )

        enviar = st.form_submit_button(
            "ENVIAR SOLICITUD CORPORATIVA",
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
        "Solicitud registrada correctamente. Un especialista de Equipa Tus Pasos te contactará a la brevedad."
    )

    st.markdown(
        f"""
        <div class="summary">
            <strong>Resumen de tu solicitud corporativa</strong><br><br>
            <b>Empresa:</b> {datos["empresa"]}<br>
            <b>Contacto:</b> {datos["contacto"]}<br>
            <b>Línea de Interés:</b> {datos["linea"]}<br>
            <b>Requerimiento:</b> {datos["necesidad"]}<br>
            <b>Volumen Estimado:</b> {datos["volumen"]}<br>
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
# PIE DE PÁGINA
# ============================================================

st.markdown("""
<div class="footer">
    Equipa Tus Pasos · Soluciones B2B de calzado corporativo · Zona Occidente
</div>
""", unsafe_allow_html=True)
