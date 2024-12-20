# Generated by Django 5.1.2 on 2024-11-02 20:37

import base.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('professor_id', models.AutoField(primary_key=True, serialize=False)),
                ('professor_situacao', models.CharField(choices=[('0', 'Concursado'), ('1', 'CLT'), ('2', 'Temporário'), ('3', 'Substituto'), ('4', 'Estagiário'), ('5', 'Terceirizado'), ('6', 'Curriculo'), ('7', 'Atestado'), ('8', 'Demitido')], max_length=1, verbose_name='Situação do professor(a)')),
                ('professor_inep', models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[base.validators.validate_professor_inep, base.validators.validate_digits], verbose_name='Inep')),
                ('professor_cpf', models.CharField(blank=True, max_length=14, null=True, unique=True, validators=[base.validators.validate_cpf], verbose_name='Cpf')),
                ('professor_rg', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='RG')),
                ('professor_nome', models.CharField(max_length=100, validators=[base.validators.validate_no_digits], verbose_name='Nome completo')),
                ('professor_data_nascimento', models.CharField(max_length=10, validators=[base.validators.validate_data], verbose_name='Data de nascimento')),
                ('professor_sexo', models.CharField(choices=[('1', 'Masculino'), ('2', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('professor_cor', models.CharField(choices=[('0', 'Não declarada'), ('1', 'Branca'), ('2', 'Preta'), ('3', 'Parda'), ('4', 'Amarela'), ('5', 'Indígena')], default='0', max_length=1, verbose_name='Cor / Raça')),
                ('professor_nacionalidade', models.CharField(choices=[('1', 'Brasileira'), ('2', 'Brasileira - Naturalizado(a)'), ('3', 'Estrangeira')], default='1', max_length=1, verbose_name='Nacionalidade')),
                ('professor_estado_nascimento', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('professor_municipio_nascimento', models.CharField(blank=True, max_length=100, verbose_name='Municipio nascimento')),
                ('professor_logradouro_residencia', models.CharField(max_length=100, verbose_name='Logradoro')),
                ('professor_numero_residencia', models.CharField(max_length=10, verbose_name='Número')),
                ('professor_complemento_residencia', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('professor_zona_residencia', models.CharField(choices=[('1', 'Urbana'), ('2', 'Rural')], default='1', max_length=1, verbose_name='Localização')),
                ('professor_localizacao_residencia', models.CharField(choices=[('1', 'Área de assentamento'), ('2', 'Terra indígena'), ('3', 'Área quilombola'), ('7', 'Não está em uma localização diferenciada')], default='7', max_length=1, verbose_name='Localização diferenciada')),
                ('professor_bairro_residencia', models.CharField(blank=True, max_length=50, verbose_name='Bairro')),
                ('professor_cep_residencia', models.CharField(max_length=9, validators=[base.validators.validate_cep], verbose_name='CEP')),
                ('professor_estado_residencia', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='PA', max_length=2, verbose_name='Estado')),
                ('professor_municipio_residencia', models.CharField(max_length=100, verbose_name='Municipio residência')),
                ('professor_ddd', models.CharField(blank=True, max_length=2, validators=[base.validators.validate_ddd, base.validators.validate_digits], verbose_name='professor - DDD Telefone')),
                ('professor_telefone', models.CharField(blank=True, max_length=9, validators=[base.validators.validate_phone, base.validators.validate_digits], verbose_name='professor - Telefone')),
                ('professor_email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='Email')),
                ('professor_filiacao', models.CharField(choices=[('0', 'Não declarado/Ignorado'), ('1', 'Filiação 1 e/ou Filiação 2')], max_length=1, verbose_name='Filiação')),
                ('professor_filiacao1_nome', models.CharField(blank=True, max_length=100, validators=[base.validators.validate_no_digits], verbose_name='Filiação 1 - Nome')),
                ('professor_filiacao2_nome', models.CharField(blank=True, max_length=100, validators=[base.validators.validate_no_digits], verbose_name='Filiação 2 - Nome')),
                ('professor_ensino_outro_lugar', models.CharField(blank=True, choices=[('1', 'Não'), ('2', 'Hospital'), ('3', 'Domicílio'), ('4', 'Instalações exteriores')], default='1', max_length=1, verbose_name='Ensino em outro lugar')),
                ('professor_nivel_escolaridade', models.CharField(choices=[('1', 'Não concluiu o ensino fundamental'), ('2', 'Ensino fundamental'), ('7', 'Ensino médio'), ('6', 'Ensino superior')], max_length=1, verbose_name='Maior nível de escolaridade')),
                ('professor_tipo_ensino_medio', models.CharField(blank=True, choices=[('1', 'Formação geral'), ('2', 'Modalidade normal (magistério)'), ('3', 'Curso técnico'), ('4', 'Magistério indígena, modalidade normal')], max_length=1, verbose_name='Tipo de ensino médio cursado')),
                ('professor_curso_conclusao1', models.CharField(blank=True, max_length=4, validators=[base.validators.validate_year, base.validators.validate_digits], verbose_name='Ano de conclusão')),
                ('professor_curso_publica1', models.CharField(blank=True, max_length=1, verbose_name='Pública')),
                ('professor_curso_privada1', models.CharField(blank=True, max_length=1, verbose_name='Privada')),
                ('professor_curso_instituicao1', models.CharField(blank=True, max_length=100, verbose_name='Instituição de Educação Superior')),
                ('professor_curso_conclusao2', models.CharField(blank=True, max_length=4, validators=[base.validators.validate_year, base.validators.validate_digits], verbose_name='Ano de conclusão')),
                ('professor_curso_publica2', models.CharField(blank=True, max_length=1, verbose_name='Pública')),
                ('professor_curso_privada2', models.CharField(blank=True, max_length=1, verbose_name='Privada')),
                ('professor_curso_instituicao2', models.CharField(blank=True, max_length=100, verbose_name='Instituição de Educação Superior')),
                ('professor_curso_conclusao3', models.CharField(blank=True, max_length=4, validators=[base.validators.validate_year, base.validators.validate_digits], verbose_name='Ano de conclusão')),
                ('professor_curso_publica3', models.CharField(blank=True, max_length=1, verbose_name='Pública')),
                ('professor_curso_privada3', models.CharField(blank=True, max_length=1, verbose_name='Privada')),
                ('professor_curso_instituicao3', models.CharField(blank=True, max_length=100, verbose_name='Instituição de Educação Superior')),
                ('professor_pos_graduacao_concluida', models.CharField(choices=[('0', 'Não'), ('1', 'Sim')], max_length=1, verbose_name='Tem pós graduação concluida')),
                ('professor_especializacao', models.CharField(blank=True, max_length=1, verbose_name='Especialização')),
                ('professor_mestrado', models.CharField(blank=True, max_length=1, verbose_name='Mestrado')),
                ('professor_doutorado', models.CharField(blank=True, max_length=1, verbose_name='Doutorado')),
                ('professor_outros_cursos', models.CharField(choices=[('0', 'Não'), ('1', 'Sim')], max_length=1, verbose_name='Outros cursos específicos')),
                ('professor_curso_creche', models.CharField(blank=True, max_length=1, verbose_name='Creche')),
                ('professor_curso_pre_escola', models.CharField(blank=True, max_length=1, verbose_name='Pré-escola')),
                ('professor_curso_fundamental1', models.CharField(blank=True, max_length=1, verbose_name='Anos iniciais do ensino fundamental')),
                ('professor_curso_fundamental2', models.CharField(blank=True, max_length=1, verbose_name='Anos finais do ensino fundamental')),
                ('professor_curso_ensino_medio', models.CharField(blank=True, max_length=1, verbose_name='Ensino médio')),
                ('professor_curso_educacao_especial', models.CharField(blank=True, max_length=1, verbose_name='Educação especial')),
                ('professor_curso_jovens_adultos', models.CharField(blank=True, max_length=1, verbose_name='Educação de jovens e adultos')),
                ('professor_curso_educacao_indigena', models.CharField(blank=True, max_length=1, verbose_name='Educação indígena')),
                ('professor_curso_educacao_campo', models.CharField(blank=True, max_length=1, verbose_name='Educação do campo')),
                ('professor_curso_educacao_ambiental', models.CharField(blank=True, max_length=1, verbose_name='Educação ambiental')),
                ('professor_curso_direitos_humanos', models.CharField(blank=True, max_length=1, verbose_name='Educação em direitos humanos')),
                ('professor_curso_diversidade_sexual', models.CharField(blank=True, max_length=1, verbose_name='Gênero e diversidade sexual')),
                ('professor_curso_direitos_crianca', models.CharField(blank=True, max_length=1, verbose_name='Direitos de crianças e adolescentes')),
                ('professor_curso_relacoes_etnicas', models.CharField(blank=True, max_length=1, verbose_name='Educação para as relações étnico-raciais')),
                ('professor_curso_gestao_escolar', models.CharField(blank=True, max_length=1, verbose_name='Gestão escolar')),
                ('professor_curso_outros', models.CharField(blank=True, max_length=1, verbose_name='Outros cursos')),
                ('professor_justificativa_documentos', models.CharField(blank=True, choices=[('1', 'O aluno(a) não possui os documentos solicitados'), ('2', 'A escola não recebeu os documentos solicitados')], max_length=1, verbose_name='Justificativa da falta de documentos')),
                ('professor_deficiencia', models.CharField(choices=[('0', 'Não'), ('1', 'Sim')], max_length=1, verbose_name='Tem Deficiência Física')),
                ('professor_cegueira', models.CharField(blank=True, max_length=1, verbose_name='Cegueira')),
                ('professor_baixa_visao', models.CharField(blank=True, max_length=1, verbose_name='Baixa visão')),
                ('professor_surdez', models.CharField(blank=True, max_length=1, verbose_name='Surdez')),
                ('professor_deficiencia_auditiva', models.CharField(blank=True, max_length=1, verbose_name='Deficiência auditiva')),
                ('professor_surdocegueira', models.CharField(blank=True, max_length=1, verbose_name='Surdocegueira')),
                ('professor_deficiencia_fisica', models.CharField(blank=True, max_length=1, verbose_name='Deficiência física')),
                ('professor_deficiencia_intelectual', models.CharField(blank=True, max_length=1, verbose_name='Deficiência intelectual')),
                ('professor_deficiencia_multipla', models.CharField(blank=True, max_length=1, verbose_name='Deficiência múltipla')),
                ('professor_autismo', models.CharField(blank=True, max_length=1, verbose_name='Autismo')),
                ('professor_altas_habilidades', models.CharField(blank=True, max_length=1, verbose_name='Altas habilidades')),
                ('professor_urgencia_nome', models.CharField(blank=True, max_length=100, verbose_name='Urgência - Nome')),
                ('professor_urgencia_ddd', models.CharField(blank=True, max_length=2, validators=[base.validators.validate_ddd, base.validators.validate_digits], verbose_name='Urgência - DDD')),
                ('professor_urgencia_telefone', models.CharField(blank=True, max_length=9, validators=[base.validators.validate_phone, base.validators.validate_digits], verbose_name='Urgência - Telefone')),
                ('professor_urgencia_parentesco', models.CharField(blank=True, max_length=50, verbose_name='Urgência - Parentesco')),
                ('professor_urgencia_procedimentos', models.TextField(blank=True, verbose_name='Procedimentos em caso de urgência')),
                ('professor_alergia', models.CharField(blank=True, max_length=1, verbose_name='alergia')),
                ('professor_alergia_tipo', models.TextField(blank=True, max_length=1000, verbose_name='Tipo de alergia(s) e cuidados')),
                ('professor_cuidados_diferenciados', models.TextField(blank=True, max_length=1000, verbose_name='Cuidados diferenciados')),
                ('professor_plano_saude', models.CharField(blank=True, max_length=1, verbose_name='Plano de Saúde')),
                ('professor_plano_saude_nome', models.CharField(blank=True, max_length=50, verbose_name='Nome do Plano de Saúde')),
                ('professor_plano_saude_ddd', models.CharField(blank=True, max_length=2, validators=[base.validators.validate_ddd, base.validators.validate_digits], verbose_name='DDD')),
                ('professor_plano_saude_telefone', models.CharField(blank=True, max_length=9, validators=[base.validators.validate_phone, base.validators.validate_digits], verbose_name='Telefone')),
                ('professor_plano_saude_email', models.EmailField(blank=True, max_length=250, verbose_name='Email')),
                ('professor_convenio', models.CharField(blank=True, max_length=1, verbose_name='Convênio')),
                ('professor_convenio_nome', models.CharField(blank=True, max_length=50, verbose_name='Nome do convênio')),
                ('professor_convenio_ddd', models.CharField(blank=True, max_length=2, validators=[base.validators.validate_ddd, base.validators.validate_digits], verbose_name='DDD')),
                ('professor_convenio_telefone', models.CharField(blank=True, max_length=9, validators=[base.validators.validate_phone, base.validators.validate_digits], verbose_name='Telefone')),
                ('professor_convenio_email', models.EmailField(blank=True, max_length=250, verbose_name='Email')),
                ('professor_programa_social', models.CharField(blank=True, max_length=1, verbose_name='Convênio')),
                ('professor_programa_social_nome', models.CharField(blank=True, max_length=50, verbose_name='Nome do convênio')),
                ('professor_programa_social_ddd', models.CharField(blank=True, max_length=2, validators=[base.validators.validate_ddd, base.validators.validate_digits], verbose_name='DDD')),
                ('professor_programa_social_telefone', models.CharField(blank=True, max_length=9, validators=[base.validators.validate_phone, base.validators.validate_digits], verbose_name='Telefone')),
                ('professor_programa_social_email', models.EmailField(blank=True, max_length=250, verbose_name='Email')),
                ('professor_estagio', models.CharField(blank=True, max_length=1, verbose_name='Estagio')),
                ('professor_estagio_instituicao', models.CharField(blank=True, max_length=100, verbose_name='Instituição')),
                ('professor_estagio_tempo', models.CharField(blank=True, max_length=100, verbose_name='Tempo')),
                ('professor_estagio_observacoes', models.TextField(blank=True, max_length=1000, verbose_name='Observações sobre o estágio')),
                ('professor_observacoes', models.TextField(blank=True, max_length=1000, verbose_name='Observações')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data da Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Data da alteração')),
                ('professor_area_conhecimento1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorareaconhecimento1', to='base.areaconhecimento', verbose_name='Componenete curricular')),
                ('professor_area_conhecimento2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorareaconhecimento2', to='base.areaconhecimento', verbose_name='Componenete curricular')),
                ('professor_area_conhecimento3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorareaconhecimento3', to='base.areaconhecimento', verbose_name='Componenete curricular')),
                ('professor_curso1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorcurso1', to='base.cursofs', verbose_name='Curso Formação Superior')),
                ('professor_curso2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorcurso2', to='base.cursofs', verbose_name='Curso Formação Superior')),
                ('professor_curso3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorcurso3', to='base.cursofs', verbose_name='Curso Formação Superior')),
                ('professor_pais_nascimento', models.ForeignKey(default='Brasil', on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorpaisnascimento', to='base.pais', verbose_name='País de nascimento')),
                ('professor_pais_residencia', models.ForeignKey(default='Brasil', on_delete=django.db.models.deletion.DO_NOTHING, related_name='professorpaisresidencia', to='base.pais', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'ordering': ['professor_nome'],
            },
        ),
    ]
