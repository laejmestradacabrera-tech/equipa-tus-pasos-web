import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser siempre la primera línea de Streamlit
st.set_page_config(
    page_title="Equipa Tus Pasos | B2B",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PERSONALIZADOS ---
# Aquí le damos el look corporativo, limpio y moderno
st.markdown("""
    <style>
    /* Ocultar el menú superior y el footer por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Espaciado del contenedor principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Estilos del Encabezado (Hero Section) */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 60px 40px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    .hero-title {
        font-family: 'Arial Black', sans-serif;
        font-size: 3rem;
        margin-bottom: 10px;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #94a3b8;
        max-width: 800px;
        margin: 0 auto 20px auto;
    }
    .hero-highlight {
        color: #eab308; /* Color amarillo oro/industrial */
    }
    
    /* Estilos de las Tarjetas de la Vitrina */
    .catalog-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    .catalog-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    .card-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #0f172a;
        margin-bottom: 15px;
    }
    .card-text {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    /* Títulos de sección */
    .section-title {
        text-align: center;
        color: #0f172a;
        font-weight: 800;
        margin-bottom: 30px;
        font-size: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# --- 1. ENCABEZADO (HERO SECTION) ---
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Equipamos a tu empresa <span class="hero-highlight">paso a paso</span></div>
        <div class="hero-subtitle">Distribución mayorista especializada en calzado industrial y de servicio. Atención corporativa con cobertura inmediata y entregas estratégicas en toda la Zona Occidente.</div>
    </div>
""", unsafe_allow_html=True)


# --- 2. VITRINA DUAL (CATÁLOGOS) ---
st.markdown('<div class="section-title">Nuestras Líneas de Especialidad</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="catalog-card">
            <div class="card-icon">👷‍♂️</div>
            <div class="card-title">Línea Industrial y Seguridad</div>
            <div class="card-text">
                Calzado robusto diseñado para soportar las jornadas más exigentes en fábricas, almacenes y construcción. 
                <br><br>
                <b>Beneficios Clave:</b><br>
                ✓ Casquillo de protección normado.<br>
                ✓ Suelas antiderrapantes y resistentes a aceites.<br>
                ✓ Materiales dieléctricos (modelos seleccionados).<br>
                ✓ Alta durabilidad y confort para jornadas de 8+ horas.
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Botón nativo de Streamlit
    if st.button("Solicitar Catálogo Industrial", use_container_width=True, type="primary"):
        st.success("¡Excelente! Desplázate al formulario inferior para cotizar tu calzado industrial.")

with col2:
    st.markdown("""
        <div class="catalog-card" style="border-top: 4px solid #38bdf8;">
            <div class="card-icon">👩‍⚕️</div>
            <div class="card-title">Línea Clínica y de Servicio</div>
            <div class="card-text">
                Ergonomía superior para profesionales de la salud, laboratorios, clínicas y personal de servicio en constante movimiento.
                <br><br>
                <b>Beneficios Clave:</b><br>
                ✓ Diseño ultra ligero y anatómico.<br>
                ✓ Pieles suaves y de fácil limpieza (Modelos blancos).<br>
                ✓ Sistema de absorción de impacto en talón.<br>
                ✓ Confort extremo para evitar fatiga en jornadas de guardia.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Solicitar Catálogo Clínico", use_container_width=True, type="secondary"):
        st.info("¡Excelente! Desplázate al formulario inferior para cotizar tu calzado de servicio.")

# --- 3. SECCIÓN EN CONSTRUCCIÓN (Para el siguiente paso) ---
st.markdown("---")
st.markdown("<div style='text-align:center; color:#94a3b8;'>Formulario de Captación B2B y Lógica Logística (Próximamente)</div>", unsafe_allow_html=True)
