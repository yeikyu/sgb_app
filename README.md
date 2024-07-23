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


En este ejemplo, estamos creando un formulario PDF a partir de una cadena HTML utilizando ironpdf. Luego, estamos generando el archivo PDF utilizando el objeto renderer y guardándolo en un archivo llamado formulario.pdf.

Ten en cuenta que para utilizar ironpdf, debes instalar el paquete ironpdf en tu entorno de desarrollo. Puedes hacerlo utilizando el comando pip install ironpdf.