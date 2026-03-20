import streamlit as st
import base64



img_logo = 'img/logo4.png'
img_imagen = 'img/logo_front.png'

# Crear navegación con columnas (alternativa más simple)

st.logo(img_logo, size='large', link='http://localhost:8501/')

page = None
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        #st.logo(img_logo, size='small', link='http://localhost:8501/')
        st.image(img_imagen, width=100)

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


with open("video/video2.mp4", "rb") as f:
    video_bytes = f.read()

video_base64 = base64.b64encode(video_bytes).decode()

#css nav_bar
st.markdown(f"""
<style>

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

# funcion para tener imagen en el slider
def img_as_data_uri(path):
    ext = path.split(".")[-1]
    data = base64.b64encode(open(path, "rb").read()).decode("utf-8")
    return f"data:image/{ext};base64,{data}"

img_uri = img_as_data_uri("img/imagen1.png")

#silder
st.markdown(f"""
<style>
.slider {{
  position: relative;
  width: 100%;
  height: 250px;
  overflow: hidden;
  border-radius: 16px;
}}

/* Slides */
.slide {{
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  animation: fade 15s infinite;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 60px;
  box-sizing: border-box;
  color: black;
}}

/* Fondo */
.slide:nth-child(1) {{ background: #fffdfa; animation-delay: 0s;}}
.slide:nth-child(2) {{ background: #fffdfa; animation-delay: 5s;}}
.slide:nth-child(3) {{ background: #fffdfa; animation-delay: 10s;}}

/* Contenido */
.text {{ width: 50%; }}
.text h2 {{ font-size: 36px; }}
.text p {{ font-size: 18px; opacity: 0.8; }}

.image {{ width: 40%; }}
.image img {{
  width: 100%;ß
  border-radius: 12px;
}}

/* Animación fade */
@keyframes fade {{
  0% {{ opacity: 0; }}
  5% {{ opacity: 1; }}
  30% {{ opacity: 1; }}
  35% {{ opacity: 0; }}
  100% {{ opacity: 0; }}
}}
</style>

<div class="slider">

  <div class="slide">
    <div class="text">
      <h2>IoT en terreno</h2>
      <p>Captura en tiempo real lo que ocurre en casas piloto y obra.</p>
    </div>
    <div class="image">
      <img src= {img_uri}>
    </div>
  </div>

  <div class="slide">
    <div class="text">
      <h2>AI que analiza</h2>
      <p>Transforma comportamiento en decisiones inteligentes.</p>
    </div>
    <div class="image">
      <img src="img/imagen1.png">
    </div>
  </div>

  <div class="slide">
    <div class="text">
      <h2>Plataforma SaaS</h2>
      <p>Visualiza toda tu operación en una sola interfaz.</p>
    </div>
    <div class="image">
      <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71">
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
