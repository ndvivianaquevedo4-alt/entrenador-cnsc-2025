import streamlit as st

# --- Tarea N° 3: Conexión del Formulario y Tarea N° 4: Sidebar ---
def display_main_interface():
    # Estilos CSS directamente insertados (St.markdown permite CSS/HTML)
    st.markdown("""
        <style>
        .sidebar-content { padding: 20px; }
        .main-header { background-color: #00796b; color: white; padding: 15px; text-align: center; }
        .form-section { border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
        .stButton>button { background-color: #00796b; color: white; border: none; }
        </style>
        <div class="main-header"><h1>Plataforma de Preparación CNSC</h1></div>
    """, unsafe_allow_html=True)
    
    # --- Asistente CNSC AI (Sidebar - Tarea N° 4) ---
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.header("🤖 Asistente CNSC AI")
        st.write("Pregunta sobre la Ley 909, tu cargo o el temario.")
        
        # Campo de entrada de usuario para el chat
        user_input = st.text_input("Escribe tu pregunta...", key="ai_input")
        if st.button("Enviar", key="ai_send"):
            # Lógica básica para confirmar la entrada
            st.write(f"Pregunta recibida: {user_input}") 
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- Contenido Principal ---
    st.title("🔍 Selecciona la Convocatoria")

    # Formulario (TAREA N° 3: Conexión del Formulario)
    with st.form(key='selection_form'):
        convocatoria = st.text_input("Convocatoria (Ej: Nación 6)", key="convocatoria")
        
        tipo = st.selectbox("Tipo de Empleo (Ej: Nivel Profesional)", 
                            options=["", "Profesional", "Técnico", "Asistencial"],
                            key="tipo")
        
        position = st.text_input("Cargo Específico", 
                                 placeholder="Ej: Abogado Asesor", 
                                 key="position")
        
        submit_button = st.form_submit_button(label='Buscar Material y Cuestionarios')

    # Lógica de procesamiento del formulario
    if submit_button:
        if convocatoria and tipo and position:
            st.success(f"¡Búsqueda recibida! Convocatoria: **{convocatoria}**, Tipo: **{tipo}**, Cargo: **{position}**.")
            
            # TAREA N° 5: Cargar Material de Estudio
            st.header("📚 Material de Estudio y Preguntas")
            st.write(f"Cargando material para **{position}**...")
            st.info("Aquí cargaremos las leyes y preguntas específicas en la siguiente tarea.")
        else:
            st.warning("Por favor, completa todos los campos del formulario.")

    # TAREA N° 2: Botón de Verificación de Enlaces
    st.markdown("---")
    if st.button("Verificar Enlaces de las Leyes", key="verify_links"):
        st.info("¡Función de verificación de enlaces iniciada! (Lógica a implementar en Tarea 2)")

# Ejecuta la interfaz principal
if __name__ == '__main__':
    display_main_interface()