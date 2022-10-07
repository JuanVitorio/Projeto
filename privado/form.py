from django.forms import ModelForm
from privado.models import Time, Conflito, Arbitro, Cidade, DeclaracaoArbitro, VidapubliArbitro,  DenunciaArbitro, DocumentoArbitro, Partida

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ["codigo", "nome", "cidade"]

class ConflitoForm(ModelForm):
    class Meta:
        model = Conflito
        fields = ["codigo", "arbitro", "partida", "time", "descricao", "errotecnico"]

class ArbitroForm(ModelForm):
    class Meta:
        model = Arbitro
        fields = ["nome", "datanasc", "cidade", "formafisica"]

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nome"]

class PartidaForm(ModelForm):
    class Meta:
        model = Partida
        fields = ["usuario", "data", "arbitro", "local", "visitante"]

class PolemicaForm(ModelForm):
    class Meta:
        model = DeclaracaoArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class PolemicaVPForm(ModelForm):
    class Meta:
        model = VidapubliArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class DenunciasForm(ModelForm):
    class Meta:
        model = DenunciaArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class PapeladaForm(ModelForm):
    class Meta:
        model = DocumentoArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

