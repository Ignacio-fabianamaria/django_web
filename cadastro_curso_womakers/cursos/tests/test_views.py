from pytest_django.asserts import assertTemplateUsed


def test_curso_view_must_return_template(client):
    response = client.get('/curso/criar_curso')
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_curso.html')
