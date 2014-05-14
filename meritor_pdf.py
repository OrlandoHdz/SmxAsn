from fpdf import FPDF
import locale

class smx_pdf(FPDF):
	"""
		Crea el PDF fisico para que despues sea enviado por mail
		Orlando Hdz
		09-May-2014
	"""        
        def __init__(self):
                super(smx_pdf,self).__init__()
                self.factura = ""
                self.fecha = ""
                self.sold_to_r1 = ""
                self.sold_to_r2 = ""
                self.sold_to_r3 = ""
                self.sold_to_r4 = ""
                self.sold_to_r5 = ""
                self.ship_to_r1 = ""
                self.ship_to_r2 = ""
                self.ship_to_r3 = ""
                self.ship_to_r4 = ""
                self.ship_to_r5 = ""
                self.agente_aduanal_r1 = ""
                self.agente_aduanal_r2 = ""
                self.agente_aduanal_r3 = ""
                self.agente_aduanal_r4 = ""
                self.agente_aduanal_r5 = ""
                self.us_broker_r1 = ""
                self.us_broker_r2 = ""
                self.us_broker_r3 = ""
                self.us_broker_r4 = ""
                self.us_broker_r5 = ""
                self.shipping_order = ""
                self.shipping_date = ""
                self.carrier = ""
                self.bl_number = ""
                self.comercial_terms = ""
                self.clave_pedimento = ""
                self.origin = ""
                self.purchase_order = ""
                self.partidas = {}
                self.ruta_destino = "."
                self.prefijo_archivo = "mer"
                self.peso_um = "LBS"
                self.moneda = "USD"
                self.peso_total = "0"
                self.archivo_salida = ""
                

        def header(this):
                this.set_font('Arial','',8)
                this.set_xy(10,13)
                this.cell(w=40,h=3,txt='Meritor Mexicana SA de CV',border=0,ln=1,align="L")
                this.cell(w=40,h=3,txt='Blvd Nexxus ADN 2505',border=0,ln=1,align="L")
                this.cell(w=40,h=3,txt='Parque Ind. Nexxus ADN',border=0,ln=1,align="L")
                this.cell(w=40,h=3,txt='Cienega de Flores Mexico    65550',border=0,ln=1,align="L")
                this.cell(w=40,h=3,txt='RFC.- MME-971205-KXA ',border=0,ln=0,align="L")

                
                this.set_font('Arial','',15)
                this.set_xy(165,10)
                this.cell(0,0,'Commercial Invoice',0,align="R")

                this.set_font('Arial','',10)
                this.set_xy(150,14)	
                this.set_fill_color(211,211,211)
                this.cell(w=25,h=5,txt='DATE',border=1,fill=1,ln=0,align='C')
                this.cell(w=25,h=5,txt='INVOICE',border=1,fill=1,ln=0,align='C')
                this.set_xy(150,19)	
                this.cell(w=25,h=5,txt=this.fecha,border=1,fill=0,ln=0,align='C')
                this.cell(w=25,h=5,txt=this.factura,border=1,fill=0,ln=0,align='C')

                #sold to
                this.set_xy(10,30)	
                this.set_fill_color(211,211,211)
                this.cell(w=92,h=5,txt='SOLD TO',border=1,fill=1,align='L')
                this.rect(x=10,y=35,w=92,h=25)
                this.set_font('Arial','',10)
                this.set_xy(10,35)
                this.cell(w=92,h=5,txt=this.sold_to_r1,border=0,fill=0,align='L')
                this.set_xy(10,39)
                this.cell(w=92,h=5,txt=this.sold_to_r2,border=0,fill=0,align='L')
                this.set_xy(10,43)
                this.cell(w=92,h=5,txt=this.sold_to_r3,border=0,fill=0,align='L')
                this.set_xy(10,47)
                this.cell(w=92,h=5,txt=this.sold_to_r4,border=0,fill=0,align='L')
                this.set_xy(10,51)
                this.cell(w=92,h=5,txt=this.sold_to_r5,border=0,fill=0,align='L')

                #ship to
                this.set_xy(108,30)	
                this.set_fill_color(211,211,211)
                this.cell(w=92,h=5,txt='SHIP TO',border=1,fill=1,align='L')
                this.rect(x=108,y=35,w=92,h=25)
                this.set_font('Arial','',10)
                this.set_xy(108,35)
                this.cell(w=92,h=5,txt=this.ship_to_r1,border=0,fill=0,align='L')
                this.set_xy(108,39)
                this.cell(w=92,h=5,txt=this.ship_to_r2,border=0,fill=0,align='L')
                this.set_xy(108,43)
                this.cell(w=92,h=5,txt=this.ship_to_r3,border=0,fill=0,align='L')
                this.set_xy(108,47)
                this.cell(w=92,h=5,txt=this.ship_to_r4,border=0,fill=0,align='L')
                this.set_xy(108,51)
                this.cell(w=92,h=5,txt=this.ship_to_r5,border=0,fill=0,align='L')


                #Agente Aduanal Mexicano
                this.set_xy(10,62)	
                this.set_fill_color(211,211,211)
                this.cell(w=92,h=5,txt='Agente Aduanal Mexicano',border=1,fill=1,align='L')
                
                this.rect(x=10,y=67,w=92,h=25)
                this.set_font('Arial','',10)
                this.set_xy(10,67)
                this.cell(w=92,h=5,txt=this.agente_aduanal_r1,border=0,fill=0,align='L')
                this.set_xy(10,71)
                this.cell(w=92,h=5,txt=this.agente_aduanal_r2,border=0,fill=0,align='L')
                this.set_xy(10,75)
                this.cell(w=92,h=5,txt=this.agente_aduanal_r3,border=0,fill=0,align='L')
                this.set_xy(10,79)
                this.cell(w=92,h=5,txt=this.agente_aduanal_r4,border=0,fill=0,align='L')
                this.set_xy(10,83)
                this.cell(w=92,h=5,txt=this.agente_aduanal_r5,border=0,fill=0,align='L')
                
                #U.S. Broker
                this.set_xy(108,62)	
                this.set_fill_color(211,211,211)
                this.cell(w=92,h=5,txt='U.S. Broker',border=1,fill=1,align='L')
                
                this.rect(x=108,y=67,w=92,h=25)
                this.set_font('Arial','',10)
                this.set_xy(108,67)
                this.cell(w=92,h=5,txt=this.us_broker_r1,border=0,fill=0,align='L')
                this.set_xy(108,71)
                this.cell(w=92,h=5,txt=this.us_broker_r2,border=0,fill=0,align='L')
                this.set_xy(108,75)
                this.cell(w=92,h=5,txt=this.us_broker_r3,border=0,fill=0,align='L')
                this.set_xy(108,79)
                this.cell(w=92,h=5,txt=this.us_broker_r4,border=0,fill=0,align='L')
                this.set_xy(108,83)
                this.cell(w=92,h=5,txt=this.us_broker_r5,border=0,fill=0,align='L')

                #datos generales 1 enca
                this.set_font('Arial','',8)
                this.set_xy(10,94)
                this.cell(w=47,h=5,txt='Shipping Order',border=1,fill=1,align='C')
                #this.set_xy(57,94)
                this.cell(w=47,h=5,txt='Shipping Date',border=1,fill=1,align='C')
                #this.set_xy(104,94)
                this.cell(w=47,h=5,txt='Carrier',border=1,fill=1,align='C')
                #this.set_xy(151,94)
                this.cell(w=49,h=5,txt='BL Number',border=1,fill=1,align='C')

                #datos generales 1 
                this.set_xy(10,99)
                this.cell(w=47,h=5,txt=this.shipping_order,border=1,fill=0,align='C')
                this.cell(w=47,h=5,txt=this.shipping_date,border=1,fill=0,align='C')
                if len(this.carrier) > 25:
                        this.carrier = this.carrier[0:25]
                this.cell(w=47,h=5,txt=this.carrier,border=1,fill=0,align='C')
                this.cell(w=49,h=5,txt=this.bl_number,border=1,fill=0,align='C')

                #datos generales 2 enca
                this.set_xy(10,104)
                this.cell(w=47,h=5,txt='Comercial Terms.',border=1,fill=1,align='C')
                this.cell(w=47,h=5,txt='Clave Pedimento',border=1,fill=1,align='C')
                this.cell(w=47,h=5,txt='Origin',border=1,fill=1,align='C')
                this.cell(w=49,h=5,txt='Purchase Order',border=1,fill=1,align='C')
                
                #datos generales 2 
                this.set_xy(10,109)
                this.cell(w=47,h=5,txt=this.comercial_terms,border=1,fill=0,ln=0,align='C')
                this.cell(w=47,h=5,txt=this.clave_pedimento,border=1,fill=0,ln=0,align='C')
                this.cell(w=47,h=5,txt=this.origin,border=1,fill=0,ln=0,align='C')
                this.cell(w=49,h=5,txt=this.purchase_order,border=1,ln=0,fill=0,align='C')

                #encabezado del detalle	
                this.set_xy(10,117)
                this.cell(w=35,h=5,txt='Part No.',border=1,fill=1,ln=0,align='L')
                this.cell(w=66,h=5,txt='Description',border=1,fill=1,ln=0,align='L')
                this.cell(w=10,h=5,txt='Origin',border=1,fill=1,ln=0,align='L')
                this.cell(w=17,h=5,txt='Qty',border=1,fill=1,ln=0,align='C')
                this.cell(w=17,h=5,txt='Weight',border=1,fill=1,ln=0,align='C')
                this.cell(w=21,h=5,txt='Unit Price',border=1,fill=1,ln=0,align='C')
                this.cell(w=25,h=5,txt='Total',border=1,fill=1,ln=0,align='C')

                this.rect(x=10,y=122,w=191,h=160)

                this.ln(5)


        # footer
        def footer(this):
                # Position at 1.5 cm from bottom
                this.set_y(-15)
                # Arial italic 8
                this.set_font('Arial','',8)
                # Page number
                this.cell(0,10,'*** THIS COMERCIAL INVOICES IS ONLY FOR CUSTOM PURPOSE ***',0,0,'C')

        def build_pdf(this):    
                this.alias_nb_pages()
                this.add_page()
                this.set_font('Arial','',6)

                total_importe = 0
                total_peso = 0
                locale.setlocale( locale.LC_ALL, '' )

                #las partidas

                for p,v in sorted(this.partidas.items(),key=lambda x:x[1]):
                        if len(v[1]) > 30:
                                v[1] = v[1][0:30]

                        if len(v[2]) > 70:
                                v[2] = v[2][0:70]

                        if len(v[3]) > 100:
                                v[3] = v[3][0:100]

                        if float(v[0]) >= 100:
                                this.cell(w=35,h=5,txt='' ,border=0,fill=0,ln=0,align='L')  #maximo 30 caracteres (parte)
                                this.cell(w=66,h=5,txt=v[2] ,border=0,fill=0,ln=0,align='L') #maximo 70 caracteres (descrpcion)
                                this.cell(w=10,h=5,txt='' ,border=0,fill=0,ln=0,align='C') #maximo 3 caracteres (origen)
                                this.cell(w=17,h=5,txt='' ,border=0,fill=0,ln=0,align='C') #maximo 15 caracteres (cantidad)
                                this.cell(w=17,h=5,txt='' ,border=0,fill=0,ln=0,align='R') #maximo 10 caracteres (peso)
                                this.cell(w=21,h=5,txt='' ,border=0,fill=0,ln=0,align='R') #maximo 15 caracteres (precio)
                                this.cell(w=25,h=5,txt='' ,border=0,fill=0,ln=1,align='R') #maximo 20 caracteres (importe)
                                #descriocion en ingles
                                this.cell(w=35,h=5,txt='',border=0,fill=0,ln=0,align='L')  #maximo 23 caracteres
                                this.cell(w=66,h=5,txt='' ,border=0,fill=0,ln=1,align='L') #maximo 100 caracteres (descripcion en ingles)
                        else:
                                this.cell(w=35,h=5,txt=v[1] ,border=0,fill=0,ln=0,align='L')  #maximo 30 caracteres (parte)
                                this.cell(w=66,h=5,txt=v[2] ,border=0,fill=0,ln=0,align='L') #maximo 70 caracteres (descrpcion)
                                this.cell(w=10,h=5,txt=v[4] ,border=0,fill=0,ln=0,align='C') #maximo 3 caracteres (origen)
                                this.cell(w=17,h=5,txt='{:,.0f}'.format(float(v[5]))  ,border=0,fill=0,ln=0,align='C') #maximo 15 caracteres (cantidad)
                                this.cell(w=17,h=5,txt='{:,.2f}'.format(float(v[6])) ,border=0,fill=0,ln=0,align='R') #maximo 10 caracteres (peso)
                                this.cell(w=21,h=5,txt=locale.currency(float(v[7]),grouping=True) ,border=0,fill=0,ln=0,align='R') #maximo 15 caracteres (precio)
                                this.cell(w=25,h=5,txt=locale.currency(float(v[8]),grouping=True) ,border=0,fill=0,ln=1,align='R') #maximo 20 caracteres (importe)
                                #descriocion en ingles
                                this.cell(w=35,h=5,txt='',border=0,fill=0,ln=0,align='L')  #maximo 23 caracteres
                                this.cell(w=66,h=5,txt=v[3] ,border=0,fill=0,ln=1,align='L') #maximo 100 caracteres (descripcion en ingles)
                                
                                total_importe += float(v[8])
                                total_peso += float(v[6])


                #totales
                this.ln(4)
                this.set_font('Arial','B',10)
                this.set_x(80)
                this.cell(w=100,h=5,txt='Total ' + this.peso_um + '  {:,.2f}'.format(total_peso) + '   ' + this.moneda + ' ' + locale.currency(total_importe,grouping=True) ,border=0,fill=0,ln=1,align='R') 
                this.archivo_salida = this.prefijo_archivo + this.factura + '.pdf'
                this.output(this.ruta_destino + '/' + this.archivo_salida,'F')



