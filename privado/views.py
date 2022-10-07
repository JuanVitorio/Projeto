import os
from re import A
from django.shortcuts import render, redirect
from privado.models import Time, Conflito, Arbitro, Cidade, VidapubliArbitro, DeclaracaoArbitro, DenunciaArbitro, DocumentoArbitro, Partida
from privado.form import *
from django.db.models.aggregates import Count

def login(request):
    return render(request, "SAAB/login.html")

def times(request):
    time = Time.objects.all()
    parametros = {"time": time}  
    return render(request, "SAAB/times.html", parametros)

def formTime(request):
    formTime = TimeForm(request.POST or None)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formTime.html", pacote)

def updateTime(request, id):
    aval = Time.objects.get(pk=id)
    formTime = TimeForm(request.POST or None, instance=aval)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formTime.html", pacote)

def deleteTime(request, id):
    aval = Time.objects.get(pk=id)
    aval.delete()
    return redirect("/times")

def conflitos(request):
    conflito = Conflito.objects.all()
    parametros = {"conflito": conflito}
    return render(request, "SAAB/conflitos.html", parametros)

def formConflito(request):
    formConflito = ConflitoForm(request.POST or None)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}
    return render(request, "SAAB/formconflito.html", pacote)

def updateConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    formConflito = ConflitoForm(request.POST or None, instance=aval)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}
    return render(request, "SAAB/formConflito.html", pacote)

def deleteConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    aval.delete()
    return redirect("/conflitos")

def arbitros(request):
    arbt = Arbitro.objects.all()
    pacote = {"arbitros": arbt, "editArbitro": 123}
    return render(request, "SAAB/arbitros.html", pacote)

def cidades(request):
    cidd = Cidade.objects.all()
    pacote = {"cidades": cidd, "editCidade": 123}
    return render(request, "SAAB/cidades.html", pacote)

def formCidade(request):
    formCidade = CidadeForm(request.POST or None)
    if formCidade.is_valid() :
        formCidade.save()
        return redirect("/cidades")
    pacote = {"formCidade": formCidade}
    return render(request, "SAAB/formCidade.html", pacote)

def updateCidade(request, id):
    cida = Cidade.objects.get(pk=id)
    formCidade = CidadeForm(request.POST or None, instance=cida)
    if formCidade.is_valid() :
        formCidade.save()
        return redirect("/cidades")
    pacote = {"formCidade": formCidade}
    return render(request, "SAAB/formCidade.html", pacote)

def deleteCidade(request, id):
    cida = Cidade.objects.get(pk=id)
    cida.delete()
    return redirect("/cidades")

def formArbitro(request):
    formArbitro = ArbitroForm(request.POST or None)
    if formArbitro.is_valid() :
        formArbitro.save()
        return redirect("/arbitros")

    pacote = {"formArbitro": formArbitro}
    return render(request, "SAAB/formArbitro.html", pacote)

def updateArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    formArbitro = ArbitroForm(request.POST or None, instance=arbi)
    if formArbitro.is_valid() :
        formArbitro.save()
        return redirect("/arbitros")

    pacote = {"formArbitro": formArbitro}
    return render(request, "SAAB/formArbitro.html", pacote)

def deleteArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    arbi.delete()
    return redirect("/arbitros")

def detalhamentoArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    ContDe= DeclaracaoArbitro.objects.filter(arbitro = id). aggregate(decla_count= Count ('*'))
    ContDenun= DenunciaArbitro.objects.filter(arbitro = id). aggregate(denun_count=Count ('*'))
    ContVp= VidapubliArbitro.objects.filter(arbitro = id). aggregate(vp_count=Count ('*'))
    ContDoc= DocumentoArbitro.objects.filter(arbitro = id). aggregate(doc_count=Count ('*'))
    context = {
        'arbitro': arbi,
        'ContDe': ContDe,
        'ContDenun': ContDenun,
        'ContVp': ContVp,
        'ContDoc': ContDoc
    }

    return render(request, "SAAB/detalhamentoArbitro.html", context)

def InfoAdicionais (request, id):
    arbi = Arbitro.objects.get(pk=id)
    Decla = DeclaracaoArbitro.objects.filter(arbitro=id)
    Denun = DenunciaArbitro.objects.filter(arbitro=id)
    VidaPub = VidapubliArbitro.objects.filter(arbitro=id)
    Doc = DocumentoArbitro.objects.filter(arbitro=id)
    context = {
        'arbitro': arbi,
        'Decla': Decla,
        'Denun': Denun,
        'VidaPub': VidaPub,
        'Doc': Doc
    }
    return render(request, "SAAB/InfoAdicionais.html", context)

def formPolemica(request, id):
    formPolemica = PolemicaForm(request.POST or None)
    if formPolemica.is_valid() :
        formPolemica.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPolemica": formPolemica}
    return render(request, "SAAB/formPolemica.html", pacote)

def updatePolemica(request, ida, id):
    pole = DeclaracaoArbitro.objects.get(pk=id)
    formPolemica = PolemicaForm(request.POST or None, instance=pole)
    if formPolemica.is_valid():
        formPolemica.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPolemica": formPolemica}
    return render(request, "SAAB/formPolemica.html", pacote)

def deletePolemica(request, ida, id):
    pole = DeclaracaoArbitro.objects.get(pk=id)
    pole.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def formPolemicaVP(request, id):
    formPolemicaVP = PolemicaVPForm(request.POST or None)
    if formPolemicaVP.is_valid() :
        formPolemicaVP.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPolemicaVP": formPolemicaVP}
    return render(request, "SAAB/formPolemicaVP.html", pacote)

def updatePolemicaVP(request, ida, id):
    polevp = VidapubliArbitro.objects.get(pk=id)
    formPolemicaVP = PolemicaVPForm(request.POST or None, instance=polevp)
    if formPolemicaVP.is_valid() :
        formPolemicaVP.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPolemicaVP": formPolemicaVP}
    return render(request, "SAAB/formPolemicaVP.html", pacote)

def deletePolemicaVP(request, ida, id):
    polevp = VidapubliArbitro.objects.get(pk=id)
    polevp.delete()
    return redirect("/InfoAdicionais/"+str(ida))
    
def formDenuncias(request, id):
    formDenuncias = DenunciasForm(request.POST or None)
    if formDenuncias.is_valid() :
        formDenuncias.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formDenuncias": formDenuncias}
    return render(request, "SAAB/formDenuncias.html", pacote)

def updateDenuncias(request, ida, id):
    denuncia = DenunciaArbitro.objects.get(pk=id)
    formDenuncias = DenunciasForm(request.POST or None, instance=denuncia)
    if formDenuncias.is_valid() :
        formDenuncias.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formDenuncias": formDenuncias}
    return render(request, "SAAB/formDenuncias.html", pacote)

def deleteDenuncias(request, ida, id):
    denuncia = DenunciaArbitro.objects.get(pk=id)
    denuncia.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def formPapelada(request, id):
    formPapelada = PapeladaForm(request.POST or None)
    if formPapelada.is_valid() :
        formPapelada.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPapelada": formPapelada}
    return render(request, "SAAB/formPapelada.html", pacote)

def updatePapelada(request, ida, id):
    papelada = DocumentoArbitro.objects.get(pk=id)
    formPapelada = PapeladaForm(request.POST or None, instance=papelada)
    if formPapelada.is_valid() :
        formPapelada.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPapelada": formPapelada}
    return render(request, "SAAB/formPapelada.html", pacote)

def deletePapelada(request, ida, id):
    papelada = DocumentoArbitro.objects.get(pk=id)
    papelada.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def cbf(request, arb):

    info = []
    Conflitos = Conflito.objects.filter(arbitro = arb). aggregate(Count ('*'))
    ContDe= DeclaracaoArbitro.objects.filter(arbitro = arb). aggregate(decla_count=Count ('*'))
    ContDenun= DenunciaArbitro.objects.filter(arbitro = arb). aggregate(denun_count=Count ('*'))
    ContVp= VidapubliArbitro.objects.filter(arbitro = arb). aggregate(vp_count=Count ('*'))
    ContDoc= DocumentoArbitro.objects.filter(arbitro = arb). aggregate(doc_count=Count ('*'))
    context = {
        'Conflitos': Conflitos,
        'ContDe': ContDe,
        'ContDenun': ContDenun,
        'ContVp': ContVp,
        'ContDoc': ContDoc
    }  
    return render(request, "SAAB/sorteio.html", context)

def sorteio(request):
    arbt = Arbitro.objects.all()
    #guarda todos os objetos arbitros do banco 
    pontos = 0
    #guarda a pontuação de um arbitro
    resultado = []
    #guardar a pontuação de cada arbitro
    aux = -1 
    #axilia o array resultados a guardar a pontuação de cada arbitro
    #servira como paramito de lugar par ao array resultado [aux]
    aux2 = 0 
    #auilia no for de cmparação dos resultados 
    ganhador = ' '
    #String que armazena o arbitro sorteado

    #o FOR ira passar por todos os arbitros pela variavel 'arbt' 
    #ate agora, esse for ira apenas fazer o apanhado de abitros apitos conforme as regras
    #da cbf e não das estabelecidas por nos. 
    for i in arbt:
        #todos os conflitos que envolvem o arbitro i 
        Conflitos = Conflito.objects.filter(arbitro = i).count()
        #todos as declarações polemicas que envolvem o arbitro i 
        ContDe= DeclaracaoArbitro.objects.filter(arbitro = i).count()
        #todos as denuncias que envolvem o arbitro i 
        ContDenun= DenunciaArbitro.objects.filter(arbitro = i).count()
        #todos os acontecimentos polemicos da vida publica que envolvem o arbitro i 
        ContVp= VidapubliArbitro.objects.filter(arbitro = i).count()
        #todos os registros de documentos mal feitos ou incompletos que envolvem o arbitro i 
        ContDoc= DocumentoArbitro.objects.filter(arbitro = i).count()
        
        #apartir daqui tera uma sequencia de ifs e elses para que o arbitro i possa passar por todos os ifs
        #mesmo que no anterior ele não tenha passado

        #regra de uma boa forma fisica
        #se sim, somasse os pontos com o peso do if que no momento é 1. indo para os proximos ifs quem contem as outras regras
        #e mesmo sendo não, ele ira se deparar com o else mais embaixo que fara ele passar pelos outros ifs
        #e assim sucessivamente. Por isso o codigo ficou tão extenso 
        if (i.formafisica == True):
            pontos = pontos+1
            if(ContDe > 0):
                pontos = pontos + (ContDe*2)
                if (ContDenun > 0):
                    pontos = pontos + (ContDenun*3)
                    if (ContVp > 0):
                        pontos = pontos + (ContVp*4)
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                #apos ter passado por todos os ifs o aux ira icar somandosse sempre 1
                                #por exemplo, inicialmente ele é = -1 e no primeiro i ele passa a ser = 0
                                aux = aux +1
                                aux2 = aux
                                #fiz isso para que nesse momento do codigo o array comece na posição 0 e va se incrementando com os pontos de cada arbitro em posições diferentes do array
                                resultado [aux] = pontos
                                #esse for servira para comparar os pontos de i com os dos outros que ja se passaram
                                #no caso se aux for = 0 o for não ira funcionar ja que não tem outro arbitro para comparar
                                for a in range(aux):
                                    #aqui entra o aux2 que eu defini como sendo o mesmo valor de aux 
                                    #na segunda volta do for, que é quando ele ira funcionar
                                    #aux ira ser = 1 e aux2 tambem 
                                    #dessa forma, nesse if ele ira fazer a comparação de qual dos pontos é menor, o da posição 1 ou 0 
                                    if (resultado[aux] < resultado[aux2-1]):
                                        #se for o da posição 1, i ira ser o ganhador por enquanto 
                                        ganhador = i 
                                        #no caso de ter outras voltas essa operação é importante para que os pontos de i seja comparado com os outros e assim o for não ficar comparando empre as mesmas posições
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        #se eles tiverem com os mesmo pontos a variavel ganhador passar a ser um array
                                        #PONTO A SER QUESTIONADO--------acho que pode ser isso que ta dando errado, de eu mudar o tipo da variavel. mas tipo se fosse a sintaxe mesmo que estivesse errada tava dando erro na tela de sorteio mas não aparece nenhum erro ------
                                        ganhador =[]
                                        #esse sera o array de ganhadores que estara na posição aux que na proxima rodada do for se incrementarar com +1
                                        ganhador[aux] = i
                                        return ganhador
                            #o restante do codigo é so uma enterna repetição do  que eu ja comentei 
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                    else:
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                resultado [aux] = pontos
                                aux2 = aux
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado.append(pontos)
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                else:
                    if (ContVp > 0):
                        pontos = pontos + (ContVp*4)
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                    else:
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
            else:
                if (ContDenun >0):
                    pontos = pontos + (ContDenun*3)
                    if (ContVp > 0):
                        pontos = pontos + (ContVp*4)
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                    else:
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
        else:
            if(ContDe > 0):
                pontos = pontos + (ContDe*2)
                if (ContDenun >0):
                    pontos = pontos + (ContDenun*3)
                    if (ContVp > 0):
                        pontos = pontos + (ContVp*4)
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                    else:
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                else:
                    if (ContVp > 0):
                        pontos = pontos + (ContVp*4)
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                    else:
                        if (ContDoc > 0):
                            pontos = pontos + (ContVp*5)
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                        else:
                            if (Conflitos > 0):
                                pontos = pontos + (ContVp*6)
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
                            else:
                                aux = aux +1
                                aux2 = aux
                                resultado [aux] = pontos
                                for a in range(aux):
                                    if (resultado[aux] < resultado[aux2-1]):
                                        ganhador = i 
                                        aux2 = aux2 -1
                                        return ganhador
                                    elif (resultado[aux] == resultado[aux2-1]):
                                        ganhador =[]
                                        ganhador[aux] = i
                                        return ganhador
 
    formPartida = PartidaForm(request.POST or None)
    if formPartida.is_valid():
        formPartida.save()
        return redirect("")
    pacote = {"formPartida": formPartida, "arbitros": arbt, "ganhador": ganhador}
    return render(request, "SAAB/sorteio.html", pacote)





def inicioAdmin(request):
    part = Partida.objects.all()
    parametros = {"partidas": part}  
    return render(request, "SAAB/partidas.html", parametros)

def updatePartida(request, id):
    partida = Partida.objects.get(pk=id)
    formPartida = PartidaForm(request.POST or None, instance=partida)

    if formPartida.is_valid():
        formPartida.save()
        return redirect('url_partida')

    pacote = {"formPartida": formPartida}
    return render(request, "SAAB/formPartida.html", pacote)

def deletePartida(request, id):
    partida = Partida.objects.get(pk=id)
    partida.delete()
    return redirect("/partidas")

def detalhamentoPartida(request, id):
    conflitos = Conflito.objects.all()
    partida = Partida.objects.filter(pk=id)
    time = Time.objects.filter(pk=id)
    detalhes = {"detalhes":partida, "conflitos":conflitos, "time":time}
    return render(request, "SAAB/detalhamentoPartida.html", detalhes)



   
