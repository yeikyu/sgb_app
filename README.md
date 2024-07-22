# toursapp1.0
Aplicacion hecha en flask sql alchemy hecha por QUINTEROS / PALMA / VAZQUES / OSTAIZA / VALENZUELA



<!-- from ironpdf import *

# Crear un formulario PDF a partir de una cadena HTML
Form_Data = """ 
<html> 
    <body> 
        <table> 
            <tr> 
                <td>Name</td> 
                <td><input name="name" type="text"/></td></td> 
            </tr> 
            <tr> 
                <td>Age</td> 
                <td><input name="age" type="text"/></td></td> 
            </tr> 
            <tr> 
                <td>Gender</td> 
            </tr> 
            <tr> 
                <td><input name="Gender" type="radio">Male</input></td> 
                <td><input name="Gender" type="radio">Female</input></td> 
            </tr> 
        </table> 
    </body> 
</html>"""

# Crear un objeto renderer
renderer = ChromePdfRenderer()
renderer.RenderingOptions.CreatePdfFormsFromHtml = True

# Generar el archivo PDF
pdf = renderer.RenderHtmlAsPdf(Form_Data)

# Guardar el archivo PDF
pdf.SaveAs("formulario.pdf")



 -->


En este ejemplo, estamos creando un formulario PDF a partir de una cadena HTML utilizando ironpdf. Luego, estamos generando el archivo PDF utilizando el objeto renderer y guardándolo en un archivo llamado formulario.pdf.

Ten en cuenta que para utilizar ironpdf, debes instalar el paquete ironpdf en tu entorno de desarrollo. Puedes hacerlo utilizando el comando pip install ironpdf.