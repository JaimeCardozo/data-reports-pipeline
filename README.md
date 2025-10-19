# 🧠 Comunidad — Automatización de Reportes con Python & GitHub Actions

Proyecto de **automatización de generación y envío de reportes Excel**, desarrollado en **Python** y desplegado con **GitHub Actions**.

---

## 🚀 Descripción general

Este proyecto crea automáticamente un archivo **Excel con grupos de personas**, lo **guarda localmente** y posteriormente lo **envía por correo electrónico**, todo de forma automatizada desde **GitHub Actions**.

La idea principal es demostrar un flujo **end-to-end** de ciencia de datos y automatización:

1. **Generar datos** (lista de grupos de hermanos en `createList.py`).
2. **Guardar los resultados en Excel** (`pandas + openpyxl`).
3. **Automatizar la ejecución en la nube** (workflow de GitHub Actions).
4. **Enviar el Excel generado por correo** (`send_mail.py` usando SMTP seguro).
5. **Subir el resultado como artifact o release.**

---

## ⚙️ Estructura del proyecto
Comunidad/
├── .github/
│ └── workflows/
│ └── generar_excel.yml # Workflow de automatización
│
├── .gitignore # Ignora entornos y archivos generados
├── createList.py # Script principal: genera los grupos y el Excel
├── send_mail.py # Envía el Excel por correo (SMTP)
├── Lista_hermanos.py # Datos base para la creación de grupos
├── printDates.py # Utilidades adicionales
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo
---

## 🧰 Tecnologías utilizadas

- 🐍 **Python 3.11**
- 📊 **pandas** — manipulación y exportación de datos
- 📗 **openpyxl** — manejo avanzado de archivos Excel
- 📬 **smtplib / email.message** — envío de correos
- ☁️ **GitHub Actions** — CI/CD y automatización en la nube

---

## 🧩 Instalación local

Si deseas probar el proyecto en tu equipo:

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/JaimeCardozo/Comunidad.git
cd Comunidad

# 2️⃣ Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate    # En Windows: .venv\Scripts\activate

# 3️⃣ Instala las dependencias
pip install -r requirements.txt

# 4️⃣ Ejecuta el script principal
python createList.py
````
El archivo Grupos_Hermanos.xlsx se generará automáticamente en la raíz del proyecto.

⚙️ Automatización con GitHub Actions

Cada vez que realizas un push o ejecutas manualmente el workflow:

Instala Python y dependencias.

Ejecuta createList.py → genera el Excel.

Ejecuta send_mail.py → envía el archivo al correo configurado.

Sube el Excel como artifact descargable.

📁 Workflow:
.github/workflows/generar_excel.yml

🔒 Variables Secretas (GitHub Secrets)

El envío de correos usa credenciales seguras definidas como Secrets en GitHub:

Nombre	Descripción
SMTP_USERNAME	Dirección de correo (por ejemplo, Gmail)
SMTP_PASSWORD	Contraseña de aplicación (App Password)
EMAIL_TO	Destinatarios del correo

🛡️ Todos los secretos están cifrados y no se exponen en el código.

Resultado del correo

El correo se envía con un asunto dinámico que incluye la fecha y hora de ejecución:
📊 Grupos Hermanos – 2025-10-18 21:37
Y adjunta automáticamente el archivo Excel generado.

🧠 Autor

Jaime Cardozo
Científico de Datos | Automatización & CI/CD | Python Enthusiast
📧 Contacto: https://www.linkedin.com/in/jaime-enrique-cardozo-beltr%C3%A1n-898923229/

⭐ Cómo contribuir

Si deseas mejorar el flujo o agregar nuevas funcionalidades:

Haz un fork del proyecto

Crea una nueva rama:

git checkout -b feature/nueva-funcionalidad


Envía tu pull request

📜 Licencia

Este proyecto se distribuye bajo la licencia MIT — úsalo, modifícalo y compártelo libremente.

