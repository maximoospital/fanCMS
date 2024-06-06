import os
import asyncio
import aiomysql
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


logoimg = open('./static/logo2.png', 'rb')
msgImage1 = MIMEImage(logoimg.read())
msgImage1.add_header('Content-ID', '<image1>')
logoimg.close()

botonimg = open('./static/boton.png', 'rb')
msgImage2 = MIMEImage(botonimg.read())
msgImage2.add_header('Content-ID', '<image2>')
botonimg.close()

smtp_server = os.getenv('smtp_server')
smtp_port = os.getenv('smtp_port')
smtp_username = os.getenv('smtp_username')
smtp_password = os.getenv('smtp_password')
sender_email = os.getenv('sender_email')
cmsurl = os.getenv('cmsurl')
enable_email = os.getenv('enable_email')
app_title = os.getenv('app_title')

with open("./static/registro.html", "r") as file:
    template_registro = Template(file.read())

# Connect to database and create the herramientas table if it doesn't exist
async def create_herramientas_table():
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await cur.execute("CREATE TABLE IF NOT EXISTS herramients (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), descripcion VARCHAR(255), plan VARCHAR(255), vencimiento VARCHAR(255), cliente VARCHAR(255), sitio VARCHAR(255), administrador VARCHAR(255), activo BOOLEAN, renovacion BOOLEAN )")
    await cur.execute("CREATE TABLE IF NOT EXISTS comnts (commentid INT AUTO_INCREMENT PRIMARY KEY, herramienta_id INT, texto VARCHAR(255) )")
    await cur.close()
    conn.close()

# Connect to database, retrieve the herramienta table and it's collection of herramientas, and assign it to the herramienta model
async def retrieve_herramientas():
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("SELECT * FROM herramients")
    herramientas = await cur.fetchall()
    await cur.close()
    conn.close()
    return herramientas_formatted(herramientas)

async def retrieve_comnts(herramienta_id: str):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("SELECT * FROM comnts WHERE herramienta_id = %s", (herramienta_id))
    comnts = await cur.fetchall()
    await cur.close()
    conn.close()
    return comnts_formatted(comnts)

async def retrieve_all_comnts():
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("SELECT * FROM comnts")
    comnts = await cur.fetchall()
    await cur.close()
    conn.close()
    return comnts_formatted(comnts)

def herramienta_helper(herramienta) -> dict:
    if(herramienta != None):
        return {
            "id": str(herramienta[0]),
            "nombre": herramienta[1],
            "descripcion": herramienta[2],
            "plan": herramienta[3],
            "vencimiento": str(herramienta[4]),
            "cliente": herramienta[5],
            "sitio": herramienta[6],
            "administrador": herramienta[7],
            "activo": herramienta[8],
            "renovacion": herramienta[9]
        }
    else:
        print("No se encontro")

def comentario_helper(comentario) -> dict:
    if(comentario != None):
        return {
            "commentid": str(comentario[0]),
            "herramienta_id": str(comentario[1]),
            "texto": comentario[2]
        }
    else:
        print("No se encontro")

# Retrieve all herramientas present in the database and return according to the herramienta_helper dict
def herramientas_formatted(herramientas) -> list[dict]:
    return [herramienta_helper(herramienta) for herramienta in herramientas]

def comnts_formatted(comnts) -> list[dict]:
    return [comentario_helper(comentario) for comentario in comnts]


# Adds a single herramienta to the database, gives it a unique id, and returns the new herramienta from the database using the herramienta_helper dict
async def add_herramienta(herramienta_data: dict) -> dict:
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    print("Adding herramienta")
    print(herramienta_data)
    print("Adding herramienta nombre")
    print(herramienta_data['nombre'])
    await cur.execute("INSERT INTO herramients (nombre, descripcion, plan, vencimiento, cliente, sitio, administrador, activo, renovacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (herramienta_data['nombre'], herramienta_data['descripcion'], herramienta_data['plan'], herramienta_data['vencimiento'], herramienta_data['cliente'], herramienta_data['sitio'], herramienta_data['administrador'], herramienta_data['activo'], herramienta_data['renovacion']))
    await conn.commit()
    await cur.execute("SELECT * FROM herramients WHERE id = %s", (cur.lastrowid,))
    herramienta = await cur.fetchone()
    print("Added herramienta")
    print(herramienta)
    await cur.close()
    conn.close()
    if(enable_email=="enable"):
        # Send an email to the admin, saying that the tool is registrada.
        print("registro: registrando smtp")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        print("registro: loggeando")
        server.login(smtp_username, smtp_password)
        print("registro: loggeado al mail")

        email_data = {
            "titulo": f"Notificacion: Se registro {herramienta_data['nombre']}. - "+app_title,
            "servicionombre": herramienta_data['nombre'],
            "servicio": await retrieve_latest_id(herramienta_data["nombre"]),
            "administrador": herramienta_data["administrador"],
            "serviciocliente": herramienta_data["cliente"],
            "id": await retrieve_latest_id(herramienta_data["nombre"]),
            "sender_name": app_title,
            "cmsurl": cmsurl
        }
        email_content = template_registro.render(email_data)
        print("registro: mail renderizado")

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = herramienta_data["administrador"]
        msg["Subject"] = email_data["titulo"]
        msg.attach(msgImage1)
        msg.attach(msgImage2)
        

        print("registro: mail creado")

        # Attach the HTML content to the email
        msg.attach(MIMEText(email_content, "html"))

        # Print and send the email
        print(f"Sending email to {herramienta_data['administrador']}")
        
        server.sendmail(sender_email, herramienta_data["administrador"], msg.as_string())
        server.quit()
        print("mail enviado")
    return herramienta_helper(herramienta)

async def add_comentario(data: dict) -> dict:
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("INSERT INTO comnts (herramienta_id, texto) VALUES (%s, %s)", (data['herramienta_id'], data['texto']))
    await conn.commit()
    await cur.execute("SELECT * FROM comnts WHERE commentid = %s", (cur.lastrowid,))
    comentario = await cur.fetchone()
    await cur.close()
    conn.close()
    return comentario_helper(comentario)

# Retrieve a single herramienta from the database using it's id
async def retrieve_herramienta(id: str):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("SELECT * FROM herramients WHERE id = %s", (id,))
    herramienta = await cur.fetchone()
    await cur.close()
    conn.close()
    return herramienta_helper(herramienta)

# Update a single herramienta in the database using it's id
async def update_herramienta(id: str, data: dict):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    query = "UPDATE herramients SET nombre = %s, descripcion = %s, plan = %s, vencimiento = %s, cliente = %s, sitio = %s, administrador = %s, activo = %s, renovacion = %s WHERE id = %s"
    await cur.execute(query, (data["nombre"], data["descripcion"], data["plan"], data["vencimiento"], data["cliente"], data["sitio"], data["administrador"], data["activo"], data["renovacion"],  id))
    await conn.commit()
    await cur.close()
    conn.close()
    return True 

# Delete a single herramienta from the database using it's id
async def delete_herramienta(id: str):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("DELETE FROM herramients WHERE id = %s", (id,))
    await cur.execute("DELETE FROM comnts WHERE herramienta_id = %s", (id, ))
    await conn.commit()
    await cur.close()
    conn.close()
    return True 

# Delete a single comentario from the database using it's id
async def delete_comentario(commentid: str):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("DELETE FROM comnts WHERE commentid = %s", (commentid, ))
    await conn.commit()
    await cur.close()
    conn.close()
    return True

# Delete multiple herramientas from the database using their ids
async def delete_herramientas(ids: list[str]):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("DELETE FROM herramients WHERE id IN %s", (tuple(ids),))
    await cur.execute("DELETE FROM comnts WHERE herramienta_id IN %s", (tuple(ids), ))
    await conn.commit()
    await cur.close()
    conn.close()
    return True 

# Delete all herramientas from the database
async def delete_all():
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("DELETE FROM herramients")
    await cur.execute("DELETE FROM comnts")
    await conn.commit()
    await cur.close()
    conn.close()
    return True 


# Retrieve the latest id from the herramientas table using it's name
async def retrieve_latest_id(name: str):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                  user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await create_herramientas_table()
    await cur.execute("SELECT id FROM herramients WHERE nombre = %s ORDER BY id DESC LIMIT 1", (name,))
    id = await cur.fetchone()
    await cur.close()
    conn.close()
    return id