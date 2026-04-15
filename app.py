import streamlit as st
import base64
import urllib.parse



img_logo = 'img/logo1.png'
img_imagen = 'img/img_logo1.png'
img_logo_negro = 'img/logo_negro.png'



st.logo(img_logo_negro, size='large', link='http://localhost:8501/')
# Crear navegación con columnas (alternativa más simple)



if "page" not in st.session_state:
    st.session_state.page = "Inicio"

page = st.session_state.page

# permite que el sidebar quede en color oscuro azul



with st.sidebar:
    st.title("Menú")
    with st.container(border=True):
        if st.button("Inicio", use_container_width=True):
            st.session_state.page = "Inicio"
            st.rerun()
        if st.button("Soluciones", use_container_width=True):
            st.session_state.page = "Soluciones"
            st.rerun()
        if st.button("Proyecto", use_container_width=True):
            st.session_state.page = "Nosotros"
            st.rerun()
        if st.button("Contacto", use_container_width=True):
            st.session_state.page = "Contacto"
            st.rerun()




#muestra los iconos de fontawesome
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# Mostrar contenido según la página
if st.session_state.page == "Inicio":
    img_path = 'img/inicio03.png'
    def get_image_base64(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    #css nav_bar
    st.markdown(f"""
    <style>

        .caja_transparente {{
            background-color: rgba(255, 255, 255, 0.5);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 30px;
            border-radius: 12px;
            width: 85%;
            color: black;
            backdrop-filter: blur(2px);
            font-size: clamp(14px, 1.2vw, 18px);
            text-align: center;
            max-width: 90%;
            margin: 0 auto;
        }}

        .imagen-container {{
            position: relative;
            width: 100%;
            height: 600px;
            overflow: hidden;
            border-radius: 12px;
        }}

        .icons-container {{
            display: flex;
            gap: 30px;
            justify-content: center;
            margin-bottom: 15px;
            font-size: clamp(14px, 1.2vw, 18px);
            color: black;
            text-transform: none;
        }}

    }}
    </style>

    <div class="imagen-container">
        <img src="data:image/png;base64,{get_image_base64(img_path)}"
            style="width:100%; height:100%; object-fit:cover; border-radius:12px">
        </img>
        <div class="caja_transparente">
            <div class="icons-container">
                <i class="fa-solid fa-microchip"> IoT</i>
                <i class="fa-solid fa-brain"> AI</i>
                <i class="fa-solid fa-cloud"> SaaS</i>
            </div>
            <h3>TRANSFORMA DATOS EN VENTAS</h3>
            <p>No sigas tomando decisiones por intuición y empieza a vender tus proyecto inmobiliarios con datos en tiempo real.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('')


    with st.container():
             st.title('Deja de perder ventas sin saber por qué')
             st.markdown('##### Estás invirtiendo millones en pilotos, diseño y equipos de venta… pero no sabes qué está haciendo que un cliente compre o se vaya.')
             st.markdown('**:red[Peor aún] : estás tomando desiciones basadas en intuición, no en datos.**')

    with st.container():
        col1, = st.columns(1, gap="large")
        with col1:
            if st.button("Revisa nuestras soluciones", use_container_width=True):
                st.session_state.page = "Soluciones"
                st.rerun()

    st.divider()

    with st.container():

            st.title("El problema")
            st.markdown('##### Cada persona que entra a tu piloto es una oportunidad de venta. Pero hoy, estás a ciegas:')
            st.markdown('**- No sabes qué espacios generan más interés.**')
            st.markdown('**- No sabes en qué momento el cliente pierde intención.**')
            st.markdown('**-No sabes si el problema viene de marketing o de estrategia comercial.**')

    st.markdown('**:red[Mientras tanto] ...**')
    st.markdown('**Pierdes conversiones todos los días sin darte cuenta, hasta que ya es demasiado tarde para actuar.**'.upper())

    with st.container():
        col1, = st.columns(1, gap="large")
        with col1:
            if st.button("Agenda una asesoría personalizada", use_container_width=True):
                st.session_state.page = "Contacto"
                st.rerun()

    st.divider()

# funcion para tener imagen en el slider
    def img_as_data_uri(path):
        ext = path.split(".")[-1]
        data = base64.b64encode(open(path, "rb").read()).decode("utf-8")
        return f"data:image/{ext};base64,{data}"

    img_uri = img_as_data_uri("img/inicio07.png")
    img_uri2 = img_as_data_uri("img/solucion05.png")
    img_uri3 = img_as_data_uri("img/inicio06.png")

    #silder
    st.markdown(f"""
    <style>
    .slider {{
        position: relative;
        width: 100%;
        height: 225px;
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
        padding: 20px;
        box-sizing: border-box;
        color: white;
    }}

    /* Fondo */
    .slide:nth-child(1) {{ background: #202020; animation-delay: 0s;}}
    .slide:nth-child(2) {{ background: #202020; animation-delay: 5s;}}
    .slide:nth-child(3) {{ background: #202020; animation-delay: 10s;}}

    /* Contenido */
    .text {{ width: 50%; }}
    .text h2 {{ font-size: 36px; }}
    .text p {{ font-size: 18px; opacity: 0.8; }}

    .image {{ width: 40%; }}
    .image img {{
     width: 100%;
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
            <img src={img_uri2}>
        </div>
    </div>

    <div class="slide">
        <div class="text">
            <h2>Plataforma SaaS</h2>
            <p>Visualiza toda tu operación en una sola interfaz.</p>
        </div>
        <div class="image">
            <img src={img_uri3}>
        </div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    with st.container():
        col1, col2 = st.columns(2, gap="large")
    with col1:
        st.title("Nuestras soluciones")
        st.markdown('##### Transformamos el comportamiento real de tus clientes en datos concretos.')
    with col2:
        st.markdown("Implementamos **sensores de alta precisión en casas piloto y obra** para capturar datos del comportamiento de los espacios. Nuestra plataforma procesa esta información en tiempo real y la convierte en insights accionables que permiten optimizar estrategias comerciales, mejorar la operación y tomar decisiones basadas en evidencia.", text_alignment="justify")
    st.divider()
    with st.container():
        col1, col2, col3 = st.columns(3, gap="large", border=True)
    with col1:
        st.subheader("Benchmark online")
        st.caption('Ve más allá de tu proyecto, analiza el mercado y acúa a tiempo ')
        with st.popover("Mas información"):
            st.subheader("Benchmark online", text_alignment="justify")
            st.write("El benchmark online es una herramienta que permite comparar el desempeño de tu proyecto inmobiliario con otros proyectos similares en el mercado. A través de datos en tiempo real, puedes analizar tendencias, identificar oportunidades y tomar decisiones informadas para optimizar tus ventas y operaciones.")
            st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="benchmark")
    with col2:
        st.subheader("Gestión de conversión", text_alignment="left")
        st.caption('Encuentra oportunidades para aumentar las  utilidades de tu proyecto')
        with st.popover("Mas información"):
            st.subheader("Gestión de conversión", text_alignment="justify")
            st.write("La gestión de conversión es un proceso que se enfoca en optimizar cada etapa del embudo de ventas para convertir más prospectos en clientes. Utilizando datos en tiempo real, puedes identificar puntos de fricción, mejorar la experiencia del cliente y aumentar las tasas de conversión, lo que se traduce en mayores utilidades para tu proyecto inmobiliario.")
            st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="conversion")
    with col3:
        st.subheader("In-project Tracking")
        st.caption('Convierte cada interacción en una oportunidad de venta o eficiencia operativa')
        with st.popover("Mas información"):
            st.subheader("In-project Tracking", text_alignment="justify")
            st.write("El In-project Tracking es una solución que permite monitorear en tiempo real el comportamiento de los usuarios dentro de tu proyecto inmobiliario. A través de sensores y dispositivos inteligentes, puedes capturar datos sobre cómo los prospectos interactúan con los espacios, lo que te brinda insights valiosos para mejorar la experiencia del cliente, optimizar operaciones y aumentar las oportunidades de venta.")
            st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="tracking")

    st.button("Ver todas las soluciones", use_container_width=True, on_click=lambda: st.session_state.update(page="Soluciones"), key="asesoria")
    st.divider()


elif st.session_state.page == "Soluciones":

    img_path = 'img/soluciones_img.png'
    def get_image_base64(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
    <style>

        .caja_transparente {{
            background-color: rgba(255, 255, 255, 0.5);
            position: absolute;
            top: 65%;
            left: 38%;
            transform: translate(-50%, -50%);
            padding: 20px;
            border-radius: 12px;
            width: 70%;
            color: black;
            backdrop-filter: blur(3px);
            font-size: clamp(14px, 1.2vw, 18px);
            max-width: 70%;
             margin: 0 auto;
        }}

        .imagen-container {{
            position: relative;
            width: 100%;
            height: 300px;
            overflow: hidden;
            border-radius: 12px;
        }}

    }}
    </style>

    <div class="imagen-container">
        <img src="data:image/png;base64,{get_image_base64(img_path)}"
            style="width:100%; height:100%; object-fit:cover; border-radius:12px">
        </img>
        <div class="caja_transparente">
            <h3>Inteligencia de datos para proyectos inmobiliarios</h3>
            <p>Toma decisiones con información real y actualizada</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Nuestras soluciones")
    st.markdown('##### Transformamos el comportamiento real de tus clientes en datos concretos.')
    with st.container(border=True):
        st.markdown('Desde la captación de oportunidades hasta la evaluación de proyectos, nuestra plataforma centraliza y analiza información clave del mercado en tiempo real. Esto te permite **reducir la incertidumbre, detectar oportunidades y optimizar cada decisión**.', text_alignment="justify")

    with st.container():
        col1, col2, col3 = st.columns(3, gap="large", border=True)
        with col1:
            st.subheader("Benchmark online", text_alignment="justify")
            st.caption('Ve más allá de tu proyecto, analiza el mercado y acúa a tiempo ')
            with st.popover("Mas información"):
                st.subheader("Benchmark online", text_alignment="justify")
                st.write("El benchmark online es una herramienta que permite comparar el desempeño de tu proyecto inmobiliario con otros proyectos similares en el mercado. A través de datos en tiempo real, puedes analizar tendencias, identificar oportunidades y tomar decisiones informadas para optimizar tus ventas y operaciones.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="benchmark2")
        with col2:
            st.subheader("Gestión de conversión", text_alignment="left")
            st.caption('Encuentra oportunidades para aumentar las  utilidades de tu proyecto')
            with st.popover("Mas información"):
                st.subheader("Gestión de conversión", text_alignment="justify")
                st.write("La gestión de conversión es un proceso que se enfoca en optimizar cada etapa del embudo de ventas para convertir más prospectos en clientes. Utilizando datos en tiempo real, puedes identificar puntos de fricción, mejorar la experiencia del cliente y aumentar las tasas de conversión, lo que se traduce en mayores utilidades para tu proyecto inmobiliario.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="conversion2")
        with col3:
            st.subheader("In-project Tracking", text_alignment="justify")
            st.caption('Convierte cada interacción en una oportunidad de venta o eficiencia operativa')
            with st.popover("Mas información"):
                st.subheader("In-project Tracking", text_alignment="justify")
                st.write("El In-project Tracking es una solución que permite monitorear en tiempo real el comportamiento de los usuarios dentro de tu proyecto inmobiliario. A través de sensores y dispositivos inteligentes, puedes capturar datos sobre cómo los prospectos interactúan con los espacios, lo que te brinda insights valiosos para mejorar la experiencia del cliente, optimizar operaciones y aumentar las oportunidades de venta.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="tracking2")
    with st.container():
        col1, col2, col3 = st.columns(3, gap="large", border=True)
        with col1:
            st.subheader("Conteo de personas")
            st.caption('Monitorea el flujo de personas en tu proyecto, en tiempo real')
            with st.popover("Mas información"):
                st.subheader("Conteo de personas", text_alignment="justify")
                st.write("El conteo de personas es una solución que permite monitorear en tiempo real el flujo de personas dentro de tu proyecto inmobiliario. A través de sensores inteligentes, puedes obtener datos precisos sobre la cantidad de visitantes, su comportamiento y patrones de movimiento, lo que te brinda insights valiosos para optimizar la experiencia del cliente, mejorar la seguridad y aumentar las oportunidades de venta.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="conteo")
        with col2:
            st.subheader('Forecasting de datos')
            st.caption('Optimiza la eficiencia de tu proyecto inmobiliario con predicciones de datos')
            with st.popover("Mas información"):
                st.subheader('Predicciónes de datos (forecasting)', text_alignment="justify")
                st.write("La predicción de datos, o forecasting, es una solución que utiliza modelos analíticos avanzados para anticipar tendencias del mercado, evaluar escenarios futuros y tomar decisiones con mayor certeza. Al analizar datos históricos y en tiempo real, puedes identificar patrones y predecir comportamientos futuros, lo que te permite optimizar la eficiencia de tu proyecto inmobiliario y mantener una ventaja competitiva.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="equipos")
        with col3:
            st.subheader('Gestión de zonas')
            st.caption('Controla y optimiza el uso de espacios en tu proyecto inmobiliario')
            with st.popover("Mas información"):
                st.subheader('Gestión de zonas', text_alignment="justify")
                st.write("La gestión de zonas es una solución que permite controlar y optimizar el uso de espacios en tu proyecto inmobiliario. A través de sensores y dispositivos inteligentes, puedes monitorear el uso de áreas específicas, identificar patrones de comportamiento y tomar decisiones informadas para mejorar la experiencia del cliente y maximizar el valor del proyecto.")
                st.button("Agenda una asesoría", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="zonas")
    st.divider()

    with st.container():
        st.title('Consultoría personalizada')
        st.markdown('##### Te ayudamos a convertir datos en decisiones inteligentes')
        col1, col2 = st.columns(2, gap="large", border=True)
        with col1:
            st.image("img/solucion01.png", width='content')
            st.subheader('Tecnología IoT de alta precisión')
            st.write('Garantizamos datos confiables con un 98% de precisión, gracias a una tecnología robusta, calibrada y monitoreada 24/7')
        with col2:
            st.image("img/solucion03.png", width='content')
            st.subheader('Data accionable en tiempo real')
            st.write('La información está disponible en tiempo real a través de nuestra plataforma, permitiéndote tomar decisiones informadas y oportunas que impactan directamente en tus resultados.')
    with st.container():
        col1, col2 = st.columns(2, gap="large", border=True)
        with col1:
            st.image("img/solucion04.png", width='content')
            st.subheader('Acompañamiento y monitoreo continuo')
            st.write('Nuestros especialistas están dispuestos a atender solicitudes y acompañar al cliente a transformar los datos en planes de acción concretos.')
        with col2:
            st.image("img/solucion02.png", width='content')
            st.subheader('Inteligencia predictiva y toma de decisiones')
            st.write('Anticipa tendencias del mercado, evalúa escenarios y toma decisiones con mayor certeza utilizando modelos analíticos avanzados.')

    with st.container():
        st.button("Agenda una asesoría personalizada", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="asesoria2")

elif st.session_state.page == "Nosotros":
    img_path = 'img/inicio01.png'
    def get_image_base64(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")



    st.markdown(f"""
    <style>

        .caja_transparente {{
            background-color: rgba(255, 255, 255, 0.5);
            position: absolute;
            top: 65%;
            left: 38%;
            transform: translate(-50%, -50%);
            padding: 20px;
            border-radius: 12px;
            width: 70%;
            color: black;
            backdrop-filter: blur(3px);
            font-size: clamp(14px, 1.2vw, 18px;)
        }}

        .imagen-container {{
            position: relative;
            width: 100%;
            height: 300px;
            overflow: hidden;
            border-radius: 12px;
        }}

    }}
    </style>

    <div class="imagen-container">
        <img src="data:image/png;base64,{get_image_base64(img_path)}"
            style="width:100%; height:100%; object-fit:cover; border-radius:12px">
        </img>
        <div class="caja_transparente">
            <h3>El futuro del monitoreo inmobiliario</h3>
            <p>Tecnología que transorma datos en decisiones reales</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Proyecto")
    st.markdown('##### Construyendo la nueva forma de entender el avance y comportamiento inmobiliario')
    with st.container():
        col1, = st.columns(1, gap="large", border=True)
        with col1:
            st.markdown("""
                        Este proyecto está siendo construido desde cero con un enfoque claro: llevar inteligencia, automatización y datos en tiempo real a una industria que históricamente ha operado con incertidumbre.

                        Habilitamos una plataforma que combina IoT y AI para monitorear tanto el avance de obras como el comportamiento en casas piloto, transformando estos datos en información clara, medible y accionable.

                        El objetivo no es solo digitalizar procesos, sino redefinir cómo se toman decisiones en el desarrollo inmobiliario — desde la ejecución de proyectos hasta la comprensión real de cómo se habitan y utilizan los espacios."""
                        )
            st.button("Contáctanos", use_container_width=True, on_click=lambda: st.session_state.update(page="Contacto"), key="asesoria3")

    st.divider()


    st.title('Cómo lo hacemos')
    with st.container(border=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image("img/texto9.png", width='content')
        with col2:
            st.markdown("""
                        ##### Captura de datos en terreno

                        Implementamos sensores IoT para obtener información directa desde obras y casas piloto, sin depender de reportes manuales.
                        """)

    with st.container(border=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image("img/proyecto01.png", width='content')
        with col2:
            st.markdown("""
                        ##### Procesamiento inteligente

                        Aplicamos modelos de inteligencia artificial para analizar los datos y detectar patrones, desviaciones y oportunidades.
                        """)
    with st.container(border=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image("img/texto10.png", width='content')
        with col2:
            st.markdown("""
                        ##### plataforma SaaS

                        Centralizamos toda la información en una plataforma fácil de usar, que entrega insights claros para la toma de decisiones.
                        """)

    st.button("Mas información", use_container_width=True, on_click=lambda: st.session_state.update(page="Soluciones"), key="asesoria4")

elif st.session_state.page == "Contacto":
    img_path2 = 'img/contacto02.png'
    def get_image_base64(img_path2):
        with open(img_path2, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")



    st.markdown(f"""
    <style>

        .caja_transparente2 {{
            background-color: rgba(255, 255, 255, 0.5);
            position: absolute;
            top: 65%;
            left: 38%;
            transform: translate(-50%, -50%);
            padding: 20px;
            border-radius: 12px;
            width: 70%;
            color: black;
            backdrop-filter: blur(3px);
            font-size: clamp(14px, 1.2vw, 18px);
            }}


        .imagen-container2 {{
            position: relative;
            width: 100%;
            height: 300px;
            overflow: hidden;
            border-radius: 12px;
        }}
    </style>
    <div class="imagen-container2">
        <img src="data:image/png;base64,{get_image_base64(img_path2)}"
            style="width:100%; height:100%; object-fit:cover; border-radius:12px">
        </img>
        <div class="caja_transparente2">
            <h3>Convierte información en ventaja competitiva</h3>
            <p>Da el siguiente paso hacia decisiones basadas en datos</p>
        </div>

    </div>
    """, unsafe_allow_html=True)


    st.title("Contacto")
    st.divider()
    with st.container():
        st.markdown('##### Agenda una conversación y empieza a utilizar datos reales para mejorar tus resultados')

    with st.form("contacto", clear_on_submit=True):
        nombre = st.text_input("Nombre", placeholder="Escribe tu nombre")
        correo = st.text_input("Correo", placeholder="Escribe tu correo")
        mensaje = st.text_area("Mensaje", placeholder="Escribe tu mensaje")
        enviar = st.form_submit_button("Enviar", use_container_width=True)

    if enviar:
        if not nombre or not correo or not mensaje:
            st.error("Por favor, completa todos los campos.")
        else:
            texto = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"

            texto_encode = urllib.parse.quote(texto)
            numero = '56984003382'

            url = f"https://api.whatsapp.com/send?phone={numero}&text={texto_encode}"
            st.success("Redirigiendo a WhatsApp...")
            st.link_button("WhatsApp", url=url, use_container_width=True)

st.divider()
# termina el contenido de la pagina, se puede agregar más contenido a cada sección según sea necesario
with st.container(border=True, horizontal=True, horizontal_alignment="center"):
        st.image("img/logo4.png")
        st.markdown("Data en vivo para decisiones inmobiliarias", text_alignment="center")
st.markdown("""
    <div style="display:flex; justify-content:center; margin-top:20px;">
            <a href="https://wa.me/+56984003382" target="_blank">
                <button style="background-color:#ffffff; color:black; border:none; padding:2px 10px; border-radius:8px; cursor:pointer; font-size:25px; margin-right:20px;"><i class="fa-solid fa-phone"> </i></button>
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=joaquin.antunezuribe@gmail.com" target="_blank">
                <button style="background-color:#ffffff; color:black; border:none; padding:2px 10px; border-radius:8px; cursor:pointer; font-size:25px; margin-right:20px;"><i class="fa-solid fa-envelope"> </i></button>
            </a>
    </div>
                """, unsafe_allow_html=True, text_alignment="center")

st.divider()
st.caption("© 2026 Web TI. Todos los derechos reservados.", text_alignment="center")
