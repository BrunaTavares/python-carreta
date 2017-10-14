# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import requests 
import json
import time
from random import randint


def generateLocalEstado(situacao):
    
    # Patio Carregada
    if situacao == 1:
        destino=randint(1,2)
        if destino==1:
            local="Transito"
            estado="Carregada"
        else:
            local="Doca"
            estado="Carregada"
        return(local,estado)
        
    # Patio Descarregada
    elif situacao == 2:
        destino=randint(1,2)
        if destino==1:
            local="Transito"
            estado="Descarregada"
        else:
            local="Doca"
            estado="Descarregada"
        return(local,estado)

    # Doca Carregada
    elif situacao==3:
        destino=randint(1,4)
        
        if destino==1:
            local="Transito"
            estado="Carregada"
            return(local,estado)
            
        elif destino==2:
            local="Patio"
            estado="Carregada"
            return(local,estado)
            
        elif destino==3:
            local="Doca"
            estado="Carregando"
            return(local,estado)
        elif destino==4:
            local="Doca"
            estado="Descarregando"
            return(local,estado)
        
    #Doca Descarregada
    elif situacao==4:
        destino=randint(1,3)
        
        if destino==1:
            local="Transito"
            estado="Descarregada"
            return(local,estado)
            
        elif destino==2:
            local="Patio"
            estado="Descarregada"
            return(local,estado)
            
        elif destino==3:
            local="Doca"
            estado="Carregando"
            return(local,estado)
            
    # Doca Carregando
    elif situacao==5:
        destino=randint(1,2)
        if destino==1:
            local="Doca"
            estado="Carregada"
        else:
            local="Doca"
            estado="Pausada"
        return(local,estado)
        
    # Doca Descarregando
    elif situacao==6:
        destino=randint(1,2)
        if destino==1:
            local="Doca"
            estado="Descarregada"
        else:
            local="Doca"
            estado="Pausada"
        return(local,estado)
        
    # Doca Pausada
    elif situacao==7:
        destino=randint(1,2)
        if destino==1:
            local="Doca"
            estado="Carregando"
        else:
            local="Doca"
            estado="Descarregando"
        return(local,estado)
        
   # Transito Carregada
    elif situacao==8:
        destino=randint(1,2)
        if destino==1:
            local="Patio"
            estado="Carregada"
        else:
            local="Doca"
            estado="Carregada"
        return(local,estado)
        
    #Transito Descarregada
    elif situacao==9:
        destino=randint(1,2)
        if destino==1:
            local="Patio"
            estado="Descarregada"
        else:
            local="Doca"
            estado="Descarregada"
        return(local,estado)
    else:
        local="Erro"
        estado="Erro"
        return(local,estado)
def generateParam(carreta):
        
    switcher = {
        "Patio":{"Carregada":1,"Descarregada":2,} ,
        "Doca": {"Carregada":3,"Descarregada":4,"Carregando":5,"Descarregando":6,"Pausada":7,},
        "Transito": {"Carregada":8,"Descarregada":9},
    }
    
    
    
    codigoCarreta=carreta["codigoCarreta"]
    estadoAtual=carreta["estadoAtual"]
    localAtual=carreta["localAtual"]
    palletsLivresInicioEstadoAtual=carreta["palletsLivresInicioEstadoAtual"]
    switcher2=switcher.get(localAtual, "Erro")
    
    if switcher2=="Erro":
        estadoAtual="Erro"
        return "Erro"
    else:
        situacao=switcher2.get(estadoAtual, "Erro")
        
    if situacao=="Erro":
        return "Erro"
    else:
        localAtual,estadoAtual=generateLocalEstado(situacao)
    update={"codigoCarreta":codigoCarreta,"estadoAtual":estadoAtual,"localAtual":localAtual,"palletsLivresInicioEstadoAtual":palletsLivresInicioEstadoAtual}
    
    body=json.dumps(update)
    
    return body


    
if __name__ == "__main__":
    while True:
        filial=randint(1, 3) 
        body= json.dumps({"userlevel":1,"filial":filial})
        r = requests.post('https://carreta.000webhostapp.com/api/listacarretas.php', body)
        filial=json.loads(r.text)
        
        if filial["success"] == 0:
            print("erro")
        else:     
            position=randint(0,len(filial["info"]["carretas"])-1)
            carreta=filial["info"]["carretas"][position]
            body=generateParam(carreta)
            r = requests.post('https://carreta.000webhostapp.com/api/updatecarreta.php', body)
            print(r.text)
            time.sleep(60*15)  
        
        
    