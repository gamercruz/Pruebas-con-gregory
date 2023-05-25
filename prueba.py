import requests
import base64


# Lee la imagen en forma de bytes
with open('imagen.png', 'rb') as archivo:
    imagen_bytes = archivo.read()

# Codifica la imagen en base64
imagen_codificada = base64.b64encode(imagen_bytes).decode('utf-8')
imagen_base64 = f'data:image/jpeg;base64,{imagen_codificada}'

# Realiza la solicitud a la API de OCR.space
url = 'https://api.ocr.space/parse/image'
payload = {
    'apikey': '966e9dc7a988957', 
    'base64Image': imagen_base64,
    'language': 'spa',
}
respuesta = requests.post(url, data=payload)
resultado = respuesta.json()

# Extrae el texto del resultado
# texto = resultado['ParsedResults']

# # Imprime el texto extraído

texto = resultado['ParsedResults'][0]['ParsedText']

print(texto)

# # Verifica si la solicitud fue exitosa
# if resultado['IsErroredOnProcessing']:
#     print('Error al procesar la imagen. ' , resultado['IsErroredOnProcessing'])
# else:
#     # Extrae el texto del resultado
#     texto = resultado['ParsedText']

#     # Imprime el texto extraído
#     print(texto)