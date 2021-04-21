import uuid

from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Curso(Base):
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    }
    curso = models.CharField('Curso', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    link = models.CharField('Link', max_length=100)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.curso

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Pessoa(Base):
    nome = models.CharField('nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    github = models.CharField('Github', max_length=100, default='#')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome

class Tecnologia(Base):
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
        ('lni-laptop-phone', 'Responsivo'),
        ('lni-rocket', 'Foguete'),
        ('lni-github', 'Github'),
    }
    tecnologia = models.CharField('Tecnologia', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'

    def __str__(self):
        return self.tecnologia


class Expectativa(Base):

    ICONE_CHOICES = {
        ('lni-cog', 'Backend'),
        ('lni-layers', 'Frontend'),
        ('lni-mobile', 'Mobile'),
        ('lni-laptop-phone', 'Responsivo'),
    }

    MODALIDADE_CHOICES = {
        ('CLT', 'Clt'),
        ('PJ', 'Pessoa_juridica'),
        ('Estagio', 'estagio'),
    }

    AREA_CHOICES = {
        ('Front-end', 'Frontend'),
        ('Back-end', 'Backend'),
        ('Full-stack', 'Fullstack'),
        ('Mobile', 'Mobile'),
    }
    modalidade = models.CharField('Modalidade', max_length=50, choices=MODALIDADE_CHOICES)
    horario = models.CharField('Horario', max_length=20)
    area = models.CharField('Area', max_length=50, choices=AREA_CHOICES)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Expectativa'
        verbose_name_plural = 'Expectativas'

    def __str__(self):
        return self.horario


class Experiencia(Base):

    MODALIDADE_CHOICES = {
        ('CLT', 'Clt'),
        ('PJ', 'Pessoa juridica'),
        ('Estagio', 'estagio'),
        ('Analista de Redes', 'Analista_cop'),

    }

    empresa = models.CharField('Empresa', max_length=20)
    modalidade = models.CharField('Modalidade', max_length=20, choices=MODALIDADE_CHOICES)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    periodoi = models.DateField('Período inicial')
    periodof = models.DateField('Período final', null=True, blank=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 210, 'height': 210, 'crop':True}})
    atividades = models.TextField('Atividades realizadas', max_length=200)
    site = models.CharField('Facebook', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return self.empresa
