from itertools import chain
import random
from django.shortcuts import render, redirect
from privado.models import Time, Conflito, Arbitro, Usuario, Cidade, VidapubliArbitro, DeclaracaoArbitro, DenunciaArbitro, DocumentoArbitro, Partida
from privado.form import *
from django.db.models.aggregates import Count
from django.db.models import Max

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
    formPartida = PartidaForm(request.POST, request.FILES)
    pacote = {}
    arbt = Arbitro.objects.all()
    resultado = []
    ganhador = []
    ganhador.append(0)
    lista_notas_juizes = []
    for i in arbt:
        pontos = 0

        ContDe= DeclaracaoArbitro.objects.filter(arbitro = i).count()
        ContDenun= DenunciaArbitro.objects.filter(arbitro = i).count()
        ContVp= VidapubliArbitro.objects.filter(arbitro = i).count()
        ContDoc= DocumentoArbitro.objects.filter(arbitro = i).count()

        if (i.formafisica == False):
            pontos = pontos+1
            
        if(ContDe > 0):
            pontos = pontos + (ContDe*2)
        
        if (ContDenun > 0):
            pontos = pontos + (ContDenun*3)

        if (ContVp > 0):
            pontos = pontos + (ContVp*4)
        
        if (ContDoc > 0):
            pontos = pontos + (ContDoc*5)
        

        tupla_juiz_nota= (i, pontos)
        lista_notas_juizes.append(tupla_juiz_nota)
    
    lista_notas_juizes_ordenada = sorted(lista_notas_juizes, key=lambda tup: tup[1])
    if(len(lista_notas_juizes_ordenada) == 0):
        resultado_final=[]
    else:
        tupla_primeiro_juiz = lista_notas_juizes_ordenada[0] 
        menor_nota = tupla_primeiro_juiz[1]
        resultado_final = []

        for juiz_tupla in lista_notas_juizes_ordenada:
            if juiz_tupla[1] == menor_nota:
                resultado_final.append(juiz_tupla[0])

    if request.method == "POST":
        if formPartida.is_valid():
            if(len(resultado_final) != 0):
                list_arbitros = []
                arbitro_ganhador =' '

                obj_visitante = formPartida.cleaned_data.get("visitante")
                cid_visitante = obj_visitante.cidade

                Part_visitante_visitante = Partida.objects.filter(visitante = obj_visitante).order_by('-data').first()
                Part_visitante_local = Partida.objects.filter(local = obj_visitante).order_by('-data').first()
                Conflito_visitante = Conflito.objects.filter(time = obj_visitante).order_by('-partida').first()           
                if (Conflito_visitante == None):
                    arb_Part_conflito_visitante = ' '
                else: 
                    cod_Part_conflito_visitante = Conflito_visitante.partida
                    arb_Part_conflito_visitante = cod_Part_conflito_visitante.arbitro

                obj_local = formPartida.cleaned_data.get("local")
                cid_local = obj_local.cidade

                Part_local_visitante = Partida.objects.filter(visitante = obj_local).order_by('-data').first()
                Part_local_local = Partida.objects.filter(local = obj_local).order_by('-data').first()
                Conflito_local = Conflito.objects.filter(time = obj_local).order_by('-partida').first()
                if (Conflito_local == None):
                    arb_Part_conflito_local = ' '
                else: 
                    cod_Part_conflito_local = Conflito_local.partida
                    arb_Part_conflito_local = cod_Part_conflito_local.arbitro

                for i in resultado_final:
                    Part_arb = Partida.objects.filter(arbitro = i).order_by('-data').first()
                    cid_arb = Cidade.objects.filter(nome = i.cidade)
                    codarb = i.codigo
                    if (cid_arb != cid_visitante) and (cid_arb != cid_local):
                        if(Part_arb != Part_visitante_visitante) and (Part_arb != Part_visitante_local) and (Part_arb != Part_local_visitante) and (Part_arb != Part_local_local):
                            if(i != arb_Part_conflito_visitante) and (i != arb_Part_conflito_local):
                                list_arbitros.append(i)  
                if (len(resultado_final) == 1):
                    arbitro_ganhador = resultado_final[0]
            
                if(len(list_arbitros) > 1):
                    arbitro_ganhador = random.choice(list_arbitros)

                obj = Partida.objects.create(
                    usuario = Usuario.objects.get(codigo = 1),
                    arbitro = Arbitro.objects.get(codigo = arbitro_ganhador.codigo),
                    visitante = formPartida.cleaned_data.get("visitante"),
                    local = formPartida.cleaned_data.get("local"),
                    data = formPartida.cleaned_data.get("data"),
                    )
                obj.save()
                return redirect("/")       

    pacote = {"FormPartida": formPartida, "ganhador": resultado_final}
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



   
