# toursapp1.0
Aplicacion hecha en flask sql alchemy hecha por QUINTEROS / PALMA / VAZQUES / OSTAIZA / VALENZUELA



<!-- from ironpdf import *

@app.route('/generate_pdf/<int:user_id>')
def generate_pdf(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    # Renderizar la plantilla Jinja con los datos del usuario
    rendered_html = render_template('formulario.html', user=user)

    # Crear un objeto renderer
    renderer = ChromePdfRenderer()
    renderer.RenderingOptions.CreatePdfFormsFromHtml = True

    # Generar el archivo PDF
    pdf = renderer.RenderHtmlAsPdf(rendered_html)

    # Guardar el archivo PDF
    pdf.SaveAs(f"user_{user_id}_formulario.pdf")

    return f"PDF generated for user {user_id}"


 -->

Instala todas las librerias del proyecto con pip install -r requirements.txt