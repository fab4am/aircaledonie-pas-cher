#!/usr/bin/python3
#
# Author : Amandine Aupetit
# http://amandine.aupetit.info
# https://github.com/fab4am
#

from htmldom import htmldom
import requests
import re
import datetime

delaidepart = 15 # en jours, dans combien de jours souhaitez-vous partir au plus tôt
departauplustard = 40 # en jours,  dans combien de jours souhaitez-vous partir au plus tard
dureesejourmin = 3 # durée minimale du séjour en jours (exemple 3 = 2 jours, 2 nuits)
dureesejourmax = 7 # surée maximale du séjour en jours
prixmax = 16000 # prix maximum pour 1 personne aller-retour
destination = "LIF" # code destination, liste ci-dessous

"""
Destination : code aéroport // tarif minimal aller (Tarif superloisir avril 2016)
Belep : BMY // 9850F
Ile des Pins : ILP // 5950F
Kone : KNQ // 7850F
Koumac : KOC // 8650F
Lifou : LIF // 7850F
Mare : MEE // 7850F
Ouvea : UVE // 7850F
Tiga : TGJ // 7850F
Touho : TOU // 7850F
"""

go = True
datealler = datetime.datetime.now() + datetime.timedelta(days=delaidepart)
dateretour = datealler + datetime.timedelta(days=dureesejourmin)


while(go):

	if (datealler - datetime.datetime.now()).days > departauplustard:
		go = False
		break

	base_url = 'http://www.aircal.nc/WebService/B2cService.asmx/GetAvailability'
	my_params = {"origin":"GEA","destination":destination,"dateFrom": datealler.strftime("%Y%m%d"),"dateTo":dateretour.strftime("%Y%m%d"),"iOneWay":False,"iFlightOnly":"0","iAdult":1,"iChild":0,"iInfant":0,"BoardingClass":"","CurrencyCode":"","strPromoCode":"","SearchType":"FARE","iOther":0,"otherType":"","strIpAddress":""}
	response = requests.get(base_url, params = my_params)

	data = response.text.replace("&gt;", ">").replace("&lt;", "<") #.replace('<?xml version="1.0" encoding="utf-8"?>', '').replace('<string xmlns="http://tempuri.org/">', '')

	dom = htmldom.HtmlDom()
	dom = dom.createDom(data)
	p = dom.find( "#ctl00_dvOutwardResult .BodyCOL5 span" )

	aller = list()
	retour = list()

	for el in p:
		
		try:
			m = re.search("\d*,?\d\d\d\.00", el.html())
			prix = m.group()
			aller.append(int(prix.replace(',', '').replace('.00', '')))
		except:
			pass

	if len(aller) == 0:
		datealler = datealler + datetime.timedelta(days=1)
		dateretour = datealler + datetime.timedelta(days=dureesejourmin)
	else:
		dom = htmldom.HtmlDom()
		dom = dom.createDom(data)
		p = dom.find( "#ctl00_dvReturnResult .BodyCOL5 span" )

		for el in p:
			
			try:
				m = re.search("\d*,?\d\d\d\.\d\d", el.html())
				prix = m.group()
				retour.append(int(prix.replace(',', '').replace('.00', '')))
			except:
				pass

		if len(retour) > 0 and min(aller)+min(retour) <= prixmax:
			print("%s F : Séjour de %s jours du %s au %s (%s F + %s F)" % (min(aller)+min(retour), (dateretour - datealler).days, datealler.strftime("%Y-%m-%d"), dateretour.strftime("%Y-%m-%d"), min(aller), min(retour)))

		if (dateretour - datealler).days < dureesejourmax:
			dateretour = dateretour + datetime.timedelta(days=1)
		else:
			datealler = datealler + datetime.timedelta(days=1)
			dateretour = datealler + datetime.timedelta(days=dureesejourmin)
