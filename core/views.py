from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
import io
from django.http import FileResponse
from django.views.generic import View

from reportlab.pdfgen import canvas

from core.models import Curso, Pessoa, Tecnologia, Expectativa, Experiencia
from .forms import ContatoForm


class IndexView(FormView, View):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?').all()
        context['pessoas'] = Pessoa.objects.order_by('?').all()
        context['tecnologias'] = Tecnologia.objects.order_by('?').all()
        context['expectativas'] = Expectativa.objects.order_by('?').all()
        context['experiencias'] = Experiencia.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs ):
        messages.success(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

class Pdf(View):
    def get(self, request, *args, **kwargs):

        #cria um arquivo para receber os dados e gerar o pdf
        buffer = io.BytesIO()

        # cria o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere 'informações no pdf'
        pdf.drawString(100, 100, )

        # Quando finaliza de inserir
        pdf.showPage()
        pdf.save()

        # por sim retornamos o buffer para o inicio do arquivo
        buffer.seek(0)

        # Fazer o dowload
        # return FileResponse(buffer, as_attachment=True, filename='Henirque.pdf')

        # Abre direto no navegador
        return FileResponse(buffer, filename='Henirque.pdf')