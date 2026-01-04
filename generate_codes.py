import secrets
import string
import os

def generate_secure_codes(num_codes=500, length=6):
    """Genera una lista de códigos únicos y seguros."""
    # Usamos letras mayúsculas, minúsculas y números para máxima seguridad
    characters = string.ascii_letters + string.digits
    codes = set()
    
    print(f"Generando {num_codes} códigos...")
    while len(codes) < num_codes:
        # secrets.choice garantiza una generación criptográficamente segura
        code = ''.join(secrets.choice(characters) for _ in range(length))
        codes.add(code)
    return list(codes)

if __name__ == '__main__':
    # 1. Genera los códigos
    generated_codes = generate_secure_codes()
    
    # 2. Guarda los códigos en el archivo
    file_path = 'access_codes.txt'
    with open(file_path, 'w') as f:
        for code in generated_codes:
            f.write(f"{code}\n")
            
    # 3. Muestra el resultado
    print(f"✅ Generados {len(generated_codes)} códigos únicos.")
    print(f"Se han guardado en el archivo: {file_path}")
    print("\n--- ¡IMPORTANTE! ---")
    print("El archivo 'access_codes.txt' contiene tus 500 códigos. Es lo que venderás.")