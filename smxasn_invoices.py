#!/usr/bin/python
import pyodbc
from meritor_pdf import smx_pdf
from ntlm.smtp import ntlm_authenticate
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import json

class invoices(object):

	"""
		Obtiene las facturas del cliente para enviarlo por correo
		Orlando Hdz
		09-May-2014
	"""

	def __init(self):
		self.path_pdfs = ""
		self.dsn = ""
		self.user = ""
		self.password = ""
		self.database = ""
		self.clientes = "0"
		self.address_book = []
		self.sender = ""
		self.smtp_host = ""
		self.smtp_usuario = ""
		self.smtp_password =""



	def envia_mail(self, archivo):
		print "enviando mail"

		subject = "New Commercial Invoice"
		body = "Sisamex, has generated a new commercial invoice \n Attached file"
		

		msg = MIMEMultipart()    
		msg['From'] = self.sender
		msg['To'] = ','.join(self.address_book)
		msg['Subject'] = subject
		msg.attach(MIMEText(body, 'plain'))
		part = MIMEApplication(open(self.path_pdfs + "/" + archivo,"rb").read())
		part.add_header('Content-Disposition', 'attachment', filename=archivo)
		msg.attach(part)
		text=msg.as_string()

		connection = smtplib.SMTP(self.smtp_host, 25)
		connection.ehlo()
		ntlm_authenticate(connection, self.smtp_usuario, self.smtp_password)
		connection.sendmail(self.sender,self.address_book, text)
		connection.quit()		


	def run(self):
		con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (self.dsn, self.user, self.password, self.database)
		cnxn = pyodbc.connect(con_string)
		cursor_mst = cnxn.cursor()

		#obtiene las facturas que tengan registro de vigilancia 
		#tambien que no se hallan enviado anteriormente
		print self.clientes
		cursor_mst.execute("""
						select 
						    factura, cliente  
						from 
						    asn_embarque_enca as a 
						where 
						    a.cliente in (""" + self.clientes + """) 
						    and a.cancelada = 'F' 
						    and a.vigilancia_tiempo is not null 
						    and not exists 
						        ( select * 
						          from asn_facturas_enviadas as b 
						          where a.factura = b.factura)	""")
		rows_mst = cursor_mst.fetchall()
		for row_mst in rows_mst:
			#obtiene los encabezados
			if row_mst.factura > 0:
					cursor = cnxn.cursor()
					print 'creando factura %d' % row_mst.factura
					cursor.execute("""
							select
								convert(varchar,fecha,103) as fecha,
							    isnull(nombre,'') as slodto_r1,
							    isnull(dat1,'') as slodto_r2,
							    isnull(dat2,'') as slodto_r3,
							    isnull(dat3,'') as slodto_r4,
							    isnull(dat4,'') as slodto_r5,
							    isnull(embarcadoa,'') as shipto_r1,
							    isnull(emb_dir1,'') as shipto_r2,
							    isnull(emb_dir2,'') as shipto_r3,
							    isnull(emb_dir3,'') as shipto_r4,
							    isnull(emb_dir4,'') as shipto_r5,
							    isnull(dat1_mex,'') as aduana_r1,
							    isnull(dat2_mex,'') as aduana_r2,
							    isnull(dat3_mex,'') as aduana_r3,
							    isnull(dat4_mex,'') as aduana_r4,
							    isnull(dat5_mex,'') as aduana_r5,
							    isnull(dat1_usa,'') as broker_r1,
							    isnull(dat2_usa,'') as broker_r2,
							    isnull(dat3_usa,'') as broker_r3,
							    isnull(dat4_usa,'') as broker_r4,
							    isnull(dat5_usa,'') as broker_r5,
							    isnull(embarque_ref,'') as shipping_order,
							    convert(varchar,fecha,103) as shipping_date,
							    isnull(transporte,'') as carrier,
							    isnull(numero_camion,'') as bl_number,
							    isnull(terminos_vta,'') as commercial_terms,
							    isnull(pedimento,'') as clave_pedimento,
							    isnull(peso_um,'') as peso_um,
							    isnull(moneda,'') as moneda
						 	from 
						    	v_factura_reporte
						 	where 
						    	seq=1 
						    	and factura=? """, row_mst.factura)

					row = cursor.fetchone()
					pdf = smx_pdf()
					if row:
						pdf.ruta_destino = self.path_pdfs
						pdf.factura = str(row_mst.factura)
						pdf.fecha = row.fecha
						pdf.sold_to_r1 = row.slodto_r1
						pdf.sold_to_r2 = row.slodto_r2
						pdf.sold_to_r3 = row.slodto_r3
						pdf.sold_to_r4 = row.slodto_r4
						pdf.sold_to_r5 = row.slodto_r5
						if len(row.shipto_r3) > 40:
							row.shipto_r4 = row.shipto_r1[40:len(row.shipto_r3)]
							row.shipto_r3 = row.shipto_r1[0:39]
						pdf.ship_to_r1 = row.shipto_r1
						pdf.ship_to_r2 = row.shipto_r2
						pdf.ship_to_r3 = row.shipto_r3
						pdf.ship_to_r4 = row.shipto_r4
						pdf.ship_to_r5 = row.shipto_r5
						pdf.agente_aduanal_r1 = row.aduana_r1
						pdf.agente_aduanal_r2 = row.aduana_r2
						pdf.agente_aduanal_r3 = row.aduana_r3
						pdf.agente_aduanal_r4 = row.aduana_r4
						pdf.agente_aduanal_r5 = row.aduana_r5
						pdf.us_broker_r1 = row.broker_r1
						pdf.us_broker_r2 = row.broker_r2
						pdf.us_broker_r3 = row.broker_r3
						pdf.us_broker_r4 = row.broker_r4
						pdf.us_broker_r5 = row.broker_r5
						pdf.shipping_order = str(row.shipping_order)
						pdf.shipping_date = row.shipping_date
						pdf.carrier = row.carrier
						pdf.bl_number = str(row.bl_number)
						pdf.comercial_terms = row.commercial_terms
						pdf.clave_pedimento = row.clave_pedimento
						pdf.peso_um = row.peso_um
						pdf.moneda = row.moneda


					#obtiene las partidas
					cursor.close()
					cursor = cnxn.cursor()
					cursor.execute("""
	            					select
	            						seq,
									    isnull(parte_cliente,'') as parte_no,
									    isnull(descripcion,'') as descripcion,
									    isnull(descripcion_usa,'') as descripcion2,
									    isnull(pais_origen,'') as pais_origen,
									    isnull(cant,0) as cantidad,
									    isnull(peso,0) as peso,
									    isnull(precio,0) as precio,
									    isnull(total,0) as total,
									    isnull(orden_compra,'') as orden_compra
									 from 
									    v_factura_reporte
									 where 
									    factura=?
									 order by seq
										""",row_mst.factura)
					rows = cursor.fetchall()
					partidas = {}
					if rows:
						for row in rows:
							detalle = []
							if row.seq != 99:
								detalle.append(row.seq)
								detalle.append(row.parte_no)
								detalle.append(row.descripcion)
								detalle.append(row.descripcion2 + ' PO: ' + row.orden_compra)
								detalle.append(row.pais_origen)
								detalle.append(str(row.cantidad))
								detalle.append(str(row.peso))
								detalle.append(str(row.precio))
								detalle.append(str(row.total))
							else:
								detalle.append(row.seq+1)
								detalle.append('')
								detalle.append(row.descripcion)
								detalle.append('')
								detalle.append('')
								detalle.append('')
								detalle.append('')
								detalle.append('')
								detalle.append('')

							partidas[row.parte_no] = detalle



						cursor.close()

						pdf.partidas = partidas

						#esto se va implementar para engranes donde para los empaques
						#obtener el peso total
						#print 'obtiene el peso total'
						#cursor = cnxn.cursor()
						#cursor.execute("exec pg_gn_peso_total ?,0,0",factura)
						#row = cursor.fetchone()
						#if row:
						#	pdf.peso_total = str(row[0])
						#cursor.close()

						pdf.build_pdf()

	 
						#registrar la factura 
						cursor = cnxn.cursor()
						cursor.execute("""
		            						insert into asn_facturas_enviadas 
		            					(compania, cliente_mapics, factura, fecha_enviada)  	
		            					values (?,?,?, getdate())
		            					""",72,row_mst.cliente,row_mst.factura)
						cursor.commit()
						cursor.close()

						#envia el mail
						#invoices.saludo(self)
						invoices.envia_mail(self,pdf.archivo_salida)

		cursor_mst.close()





if __name__ == "__main__":

	#Carga los parametros
	with open('/home/administrator/app/SmxAsn//parametros_smx.json') as data_file:
		data = json.load(data_file)

	#Instanciando factura
	oInvoices = invoices()
	oInvoices.dsn = data["parametros"]["dsn"]
	oInvoices.user = data["parametros"]["user"]
	oInvoices.password = data["parametros"]["password"]
	oInvoices.database = data["parametros"]["database"]
	oInvoices.clientes = data["parametros"]["clientes"]
	oInvoices.path_pdfs = data["parametros"]["path_pdfs"]
	oInvoices.address_book = data["parametros"]["address_book"]
	oInvoices.sender = data["parametros"]["smtp_sender"]
	oInvoices.smtp_host = data["parametros"]["smtp_host"]
	oInvoices.smtp_usuario = data["parametros"]["smtp_usuario"]
	oInvoices.smtp_password = data["parametros"]["smtp_password"]

	oInvoices.run()


