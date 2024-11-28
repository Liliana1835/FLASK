from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'  # Clave secreta para mostrar mensajes

# Configuración de Flask-Mail para Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sanchezllamocaliliana@gmail.com'  # Tu correo de Gmail
app.config['MAIL_PASSWORD'] = 'wdaj szou wrjf ynhp'  # La contraseña de tu correo
app.config['MAIL_DEFAULT_SENDER'] = 'sanchezllamocaliliana@gmail.com'

# Inicializa la extensión Flask-Mail
mail = Mail(app)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página "about"
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para el formulario de contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Crear el mensaje de correo
        msg = Message(
            subject=f"Nuevo mensaje de {nombre}",
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Nombre: {nombre}\nCorreo: {email}\nMensaje:\n{mensaje}"
        )

        try:
            mail.send(msg)
            flash("Mensaje enviado exitosamente. ¡Gracias por contactarnos!", "success")
        except Exception as e:
            flash(f"No se pudo enviar el mensaje. Error: {e}", "danger")

        return redirect('/contact')

    return render_template('contact.html')

# Ejecución de la aplicación en modo debug
if __name__ == '__main__':
    app.run(debug=True)
