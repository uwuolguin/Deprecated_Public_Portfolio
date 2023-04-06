#ANTES DE EJECUTAR ELIMINAR EL ARCHIVO token.json
#modificar la lista SCOPES con lo que necesites de https://developers.google.com/gmail/api/auth/scopes?hl=es-419
from __future__ import print_function
import base64
import os.path
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.compose','https://www.googleapis.com/auth/gmail.send','https://mail.google.com/']

import tableauserverclient as TSC
import pandas as pd

tableau_auth = TSC.PersonalAccessTokenAuth('uwu96', 'Z7ip8aXtTkOOsW1x6hK3VQ==:pDzK0qHrO4m7PfJ36C7olcvJoYjIOhP0', 'bulls')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)
#Cliente Activo 4W
workbook = server.workbooks.get_by_id('6993baa9-6eaf-4734-afbf-a6557d9b61d1')
server.workbooks.populate_views(workbook)
view = server.views.get_by_id('7e155859-dd4b-439b-a38b-fae7eace13c7') #Cliente activo resumen
view2 = server.views.get_by_id('2171a2ed-577d-4591-9278-36f7bac59ad1') # Cliente Activo Detalle



pdf_req_option = TSC.PDFRequestOptions(page_type=TSC.PDFRequestOptions.PageType.Tabloid,
				       orientation=TSC.PDFRequestOptions.Orientation.Portrait,maxage=1
				       )
csv_req_option = TSC.CSVRequestOptions(maxage=1)

ListaConcesionarios=[


		['acos2014600836@gmail.com','DERCO','John Smith'],
		['acos2014600836@gmail.com','SUZUVAL','Andres Morales'],	]


for i in ListaConcesionarios:
	

    print("entre")
    pdf_req_option.vf('concesionario',i[1] )    
    server.views.populate_pdf(view,pdf_req_option)
    with open('./Cliente_Activo_'+i[1]+'.pdf', 'wb') as f:
        f.write(view.pdf)


    csv_req_option.vf('concesionario', i[1])
    csv_req_option.vf('Es_Activo', 'no')
    server.views.populate_excel(view2,csv_req_option)
    with open('./Cliente_No_Activo_'+i[1]+'.xlsx', 'wb') as f:
        f.write(b''.join(view2.excel))

###################################################GMAIL###############################################

    def gmail_send_message():

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('gmail', 'v1', credentials=creds)
            message = EmailMessage()

            message.set_content('Dear'+ i[2]+' We are attaching the active client \nRegards\nTI Department')

            message['To'] = i[0]
            message['From'] = i[0]
            message['Subject'] = 'Cliente Activo'

            attachment_filename = 'Cliente_Activo_'+i[1]+'.pdf'
            type_subtype, _ = mimetypes.guess_type(attachment_filename)
            maintype, subtype = type_subtype.split('/')

            with open(attachment_filename, 'rb') as fp:
                attachment_data = fp.read()
            message.add_attachment(attachment_data, maintype, subtype)
            
            attachment_filename2 = 'Cliente_No_Activo_'+i[1]+'.xlsx'
            type_subtype, _ = mimetypes.guess_type(attachment_filename2)
            maintype, subtype = type_subtype.split('/')

            with open(attachment_filename2, 'rb') as fp:
                attachment_data = fp.read()
            message.add_attachment(attachment_data, maintype, subtype)

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }

            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
        return send_message

    gmail_send_message()

