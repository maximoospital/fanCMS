from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from server.routes.herramientas import router as HerramientaRouter
from server.routes.comentarios import router as ComentarioRouter
import os
import asyncio
import aiomysql
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from jinja2 import Template

with open("./static/vencida.html", "r") as file:
    template_vencido = Template(file.read())

with open("./static/vencimiento.html", "r") as file:
    template_xvencer = Template(file.read())

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

def herramientas_formatted(herramientas) -> list[dict]:
    if(herramientas == None):
        return []
    else:
        return [herramienta_helper(herramienta) for herramienta in herramientas]

def checkear_x_vencer(fecha):
    fechavenc = datetime.datetime.strptime(fecha.split("T")[0], "%Y-%m-%d").date()
    hoy = datetime.date.today();
    return (fechavenc - hoy).days == 15

def checkear_vencido(fecha):
    fechavenc = datetime.datetime.strptime(fecha.split("T")[0], "%Y-%m-%d").date()
    hoy = datetime.date.today();
    return (fechavenc - hoy).days == 0

async def si_vencio(herramienta):
    print("si_vencio: recibido")
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await cur.execute("UPDATE herramients SET activo = 0 WHERE id = %s", (herramienta["id"], ))
    await conn.commit()
    await cur.close()
    conn.close()
    if(enable_email == "enable"):
        print("si_vencio: DB actualizada, app desactivada")
        # Send an email to the admin, saying that the tool is expired.
        print("si_vencio: registrando smtp")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        print("si_vencio: loggeando")
        server.login(smtp_username, smtp_password)
        print("si_vencio: loggeado al mail")

        email_data = {
            "titulo": f"Notificacion: {herramienta['nombre']} vencio. - "+app_title,
            "servicionombre": herramienta['nombre'],
            "servicio": herramienta["id"],
            "administrador": herramienta["administrador"],
            "serviciocliente": herramienta["cliente"],
            "id": herramienta["id"],
            "sender_name": app_title,
            "cmsurl": cmsurl
        }
        email_content = template_vencido.render(email_data)
        print("si_vencio: mail renderizado")

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = herramienta["administrador"]
        msg["Subject"] = email_data["titulo"]
        msg.attach(msgImage1)
        msg.attach(msgImage2)
        
        print("si_vencio: mail creado")

        # Attach the HTML content to the email
        msg.attach(MIMEText(email_content, "html"))

        # Print and send the email
        print(f"Sending email to {herramienta['administrador']}")
        
        server.sendmail(sender_email, herramienta["administrador"], msg.as_string())
        server.quit()
        print("mail enviado")
    return "Herramienta vencida. Admin notificado."

async def si_x_vencer(herramienta):
    print("si_x_vencer: recibido")
    if(enable_email == "enable"):
        # Send an email to the admin, saying that the tool is expired.
        print("si_x_vencer: registrando smtp")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        print("si_x_vencer: loggeando")
        server.login(smtp_username, smtp_password)
        print("si_x_vencer: loggeado al mail")

        email_data = {
            "titulo": f"Notificacion: {herramienta['nombre']} esta por vencer. - "+app_title,
            "servicionombre": herramienta['nombre'],
            "servicio": herramienta["id"],
            "administrador": herramienta["administrador"],
            "serviciocliente": herramienta["cliente"],
            "id": herramienta["id"],
            "sender_name": app_title,
            "cmsurl": cmsurl
        }
        email_content = template_xvencer.render(email_data)
        print("si_x_vencer: mail renderizado")

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = herramienta["administrador"]
        msg["Subject"] = email_data["titulo"]
        msg.attach(msgImage1)
        msg.attach(msgImage2)
        

        print("si_x_vencer: mail creado")

        # Attach the HTML content to the email
        msg.attach(MIMEText(email_content, "html"))

        # Print and send the email
        print(f"Sending email to {herramienta['administrador']}")
        
        server.sendmail(sender_email, herramienta["administrador"], msg.as_string())
        server.quit()
        print("mail enviado")
    return "Herramienta x vencer. Admin notificado."


async def extender_fechas(herramienta):
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await cur.execute("UPDATE herramientas SET vencimiento = DATE_ADD(vencimiento, INTERVAL 1 MONTH) WHERE id = %s AND renovacion = 1 AND plan = mensual", (herramienta["id"],))
    await cur.execute("UPDATE herramientas SET vencimiento = DATE_ADD(vencimiento, INTERVAL 1 YEAR) WHERE id = %s AND renovacion = 1 AND plan = anual", (herramienta["id"],))
    await conn.commit()
    await cur.close()
    conn.close()
    return "Fecha de renovacion extendida."

description = """
API, para CRUD de informacion de herrramientas.
"""

app = FastAPI(
    title=app_title,
    description=description,
    version="1.0",
    contact={
        "name": "Maximo Ospital",
        "url": "http://maximoospital.github.io",
        "email": "maximo.ospital@avatarla.com",
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(HerramientaRouter, tags=["Herramienta"], prefix='/herramienta')
app.include_router(ComentarioRouter, tags=["Comentario"], prefix='/comentario')

@app.on_event("startup")
@repeat_every(seconds=86400)
async def asignar_y_filtrar():
    conn = await aiomysql.connect(host=os.environ.get('MYSQL_HOST'), port=3306,
                                user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                db=os.environ.get('MYSQL_DATABASE'), loop=asyncio.get_event_loop())
    cur = await conn.cursor()
    await cur.execute("SELECT * FROM herramients")
    herramientas = await cur.fetchall()
    await cur.close()
    conn.close()
    print("-----------------------------NUEVO LOOP-----------------------------")
    print("Herramientas Activas:")
    herramientas_activas = [herramienta for herramienta in herramientas if herramienta[8]]
    print(herramientas_activas)
    print("Herramientas Sin Renovacion:")
    herramientas_renovacion = [herramienta for herramienta in herramientas_activas if not herramienta[9]]
    print(herramientas_renovacion)
    print("Herramientas Con Renovacion:")
    herramientas_conrenovacion = [herramienta for herramienta in herramientas_activas if herramienta[9]]
    print(herramientas_conrenovacion)
    for herramienta in herramientas_conrenovacion:
        if(checkear_vencido(herramienta[4])):
            print("Vence, renovando.")
            print(await extender_fechas(herramienta_helper(herramienta)))
            break
        else:
            print("No se vence.")
            break
    print("Herramientas Vencidas Activas:")
    herramientas_vencidas = [herramienta for herramienta in herramientas_renovacion if checkear_vencido(herramienta[4])]
    print(herramientas_vencidas)    
    for herramienta in herramientas_vencidas:
        print("Vencida, notificando.")
        print(await si_vencio(herramienta_helper(herramienta)))
        break
    print("Herramientas Activas X Vencer:")
    herramientas_15_dias = [herramienta for herramienta in herramientas_renovacion if checkear_x_vencer(herramienta[4])]
    print(herramientas_15_dias)      
    for herramienta in herramientas_15_dias:
        print("Vencida, notificando.")
        print(await si_x_vencer(herramienta_helper(herramienta)))
        break

@app.get("/", tags=['root'])
async def read_root():
    return {"message": "API para CRUD de informacion de herrramientas."}