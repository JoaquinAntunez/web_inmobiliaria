import streamlit as st
import base64



img_logo = 'img/logo4.png'

# Crear navegación con columnas (alternativa más simple)



page = None
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        #st.logo(img_logo, size='large', link='http://localhost:8501/')
        st.image(img_logo, width=150)

    with col2:
        if st.button("Inicio", use_container_width=True):
            page = "Inicio"
            st.session_state.page = "Inicio"

    with col3:
        if st.button("Soluciones", use_container_width=True):
            page = "Soluciones"
            st.session_state.page = "Soluciones"

    with col4:
        if st.button("Nosotros", use_container_width=True):
            page = "Nosotros"
            st.session_state.page = "Nosotros"

    with col5:
        if st.button("Contacto", use_container_width=True):
            page = "Contacto"
            st.session_state.page = "Contacto"

pages_dict = {
    "Inicio": col2,
    "Soluciones": col3,
    "Nosotros": col4,
    "Contacto": col5,
}

# Obtener página del estado o default
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

page = st.session_state.page

st.markdown("---")

# Mostrar contenido según la página
# (funciones cuando se aprete el boton, tener en concideración)
#if page == "Inicio":
#    st.title("🏠 Inicio")
#    st.write("Bienvenido a la página de inicio")
#elif page == "Soluciones":
#    st.title("📚 Soluciones")
#    st.write("Contenido de las soluciones")
#elif page == "Nosotros":
#    st.title("💡 Nosotros")
#    st.write("Información sobre nosotros")
#elif page == "Contacto":
#    st.title("⚙️ Contacto")
#    st.write("Información de contacto")


with open("video/video.mp4", "rb") as f:
    video_bytes = f.read()

video_base64 = base64.b64encode(video_bytes).decode()

#css nav_bar
st.markdown(f"""
<style>
"[![]{img_logo}](http://localhost:8501/)"

.video-container {{
    position: relative;
    width: 100%;
}}

.video-container video {{
    width: 100%;
    opacity: 0.5;
    border-radius: 10px;
}}

.top_text {{
    display: flex;
    gap: 40px;
    letter-spacing: 1px;
    position: absolute;
    top: 25%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 24px;
    text-align: center;
    font-weight: bold;
}}

.overlay-text {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    width: 80%;

}}

.subtitle {{
    font-size: 1.5vw;
    font-weight: 300;
    opacity: 0.9;
    position: absolute;
    top: 75%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 20px;
    text-align: center;
    width: 80%;
}}

</style>

<div class="video-container">
    <video autoplay loop muted>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <div class="top_text">
        <span><i class='fas fa-microchip'></i> IoT</span>
        <span><i class='fas fa-brain'></i> AI</span>
        <span><i class='fas fa-cloud'></i> SaaS</span>
    </div>
    <div class="overlay-text">
        DATA EN VIVO PARA DECISIONES INMOBILIARIAS
    </div>
    <div class="subtitle">
        Monitorea casas piloto y obra con tecnología que convierte lo que pasa en terreno en insights accionables.
    </div>

</div>
""", unsafe_allow_html=True)


with st.container():
    col1, = st.columns(1, gap="large")
    with col1:
        if st.button("Revisa nuestras soluciones", use_container_width=True):
            st.session_state.page = "Contacto"
            st.rerun()


with st.container():
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.header("¿Qué hacemos?")
        st.write("Capturamos el comportamiento en espacios físicos (casa piloto y obra) a través de dispositivos inteligentes de alta precisión, entregando datos accionables en tiempo real que permiten optimizar ventas, eficientizar operaciones y mejorar la experiencia de compra y avance en obra.")
    with col2:
        st.image("img/Terreno.png")
