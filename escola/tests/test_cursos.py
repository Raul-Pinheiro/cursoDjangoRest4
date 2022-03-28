from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
                codigo_curso = 'CTF',
                descricao = 'Curso Teste First',
                nivel = 'A'
        )
        self.curso_1 = Curso.objects.create(
                codigo_curso = 'CTS',
                descricao = 'Curso Teste Second',
                nivel = 'A'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """ Testa se o metodo GET está listando corretamente os cursos """

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)



    def test_requisicao_post_para_criar_cursos(self):
        """ Testa se o metodo POST está criando corretamente os cursos """

        data = {
            "codigo_curso": 'CTS',
            "descricao": 'Curso Teste Second',
            "nivel":'B'
        }

        response = self.client.post(self.list_url, data = data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_requisicao_delete_para_deletar_cursos(self):
        """ Testa se o metodo DELETE está proibindo o curso de ser deletado """

        response = self.client.delete('/cursos/1/')

        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



    def test_requisicao_put_para_atualizar_cursos(self):
        """ Testa se o metodo PUT está atualizando corretamente os cursos """

        data = {
            "codigo_curso": 'CPP',
            "descricao": 'Curso Pra Profissa',
            "nivel":'B'
        }

        response = self.client.put('/cursos/1/', data = data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)