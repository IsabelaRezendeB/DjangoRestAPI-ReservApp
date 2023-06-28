# ReservAPP

Back-end desenvolvido em Django Rest Framework para o aplicativo [ReservApp](https://github.com/GualterMM/ReservApp)

## Requisitos
1. Instalar o [Django Rest Framework](https://www.django-rest-framework.org/) e suas devidas dependências expecificadas.
2. Utilizei o [Visual Studio Code](https://code.visualstudio.com/) mas também é possível utilizar outro editor de sua preferência.
3. Para ver a funcionalidade da aplicação, recomendo utilizar o [Postman](https://www.postman.com/downloads/), a URL /swagger ou qualquer plataforma de sua preferência que execute teste de API. 

## Execução
1. Primeiramente, digite no terminal para clonar o repositório:
    ```
    git clone https://github.com/IsabelaRezendeB/DjangoRestAPI-ReservApp.git
    ```

2. Após instalar o projeto, digite no terminal o seguinte comando para criar uma máquina virtual
    ```
    python -m venv ./venv
    ```
3. Para iniciá-la:
    ```
    venv\Scripts\activate.bat
    ```
4. Para instalar as dependências:
    ```
    pip install -r requirements.txt
    ```
5. Para fazer as migrations do Model:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
6. Para executar o projeto:
    ```
    python manage.py runserver
    ```
7. Para executar os testes:
    ```
    python manage.py test
    ```

## Endpoints
É possível visualizar todos os endpoints quando você roda o servidor e entra na URL /swagger/
### **Usuarios**: 
`GET` /usuarios/\
`POST` /usuarios/\
`GET` /usuarios/{id}/\
`PUT` /usuarios/{id}/\
`PATCH` /usuarios/{id}/\
`DELETE` /usuarios/{id}/\
`GET` /usuarios/?q={email}
### **Restaurantes**: 
`GET` /restaurantes/\
`POST` /restaurantes/\
`GET` /restaurantes/{id}/\
`PUT` /restaurantes/{id}/\
`PATCH` /restaurantes/{id}/\
`DELETE` /restaurantes/{id}/\
`GET` /restaurantes/?q={categoria}
### **Restaurantes filtrados por nome**: 
`GET` /restaurante/{nome}/\
### **Reservas**: 
`GET` /reserva/\
`POST` /reserva/\
`GET` /reserva/{id}/\
`PUT` /reserva/{id}/\
`PATCH` /reserva/{id}/\
`DELETE` /reserva/{id}/\
`GET` /reserva/?q={usuario_id}
### **Restaurantes Favoritos**: 
`GET` /restaurantefavorito/\
`POST` /restaurantefavorito/\
`GET` /restaurantefavorito/{id}/\
`PUT` /restaurantefavorito/{id}/\
`PATCH` /restaurantefavorito/{id}/\
`DELETE` /restaurantefavorito/{id}/\
`GET` /restaurantefavorito/?q={usuario_id}
### **Itens do Cardapio**: 
`GET` /itemcardapio/\
`POST` /itemcardapio/\
`GET` /itemcardapio/{id}/\
`PUT` /itemcardapio/{id}/\
`PATCH` /itemcardapio/{id}/\
`DELETE` /itemcardapio/{id}/\
`GET` /itemcardapio/?q={restaurante_id}
### **Itens filtrados por tipo e restaurante**: 
`GET` /itens/{restaurante_id}/{tipo_item}/\
### **Itens por restaurante**: 
`GET` /itensrestaurante/{restaurante_id}/itens/\

## Equipe de Desenvolvimento


<table>
  <tr>
    <td align="center">
      <a href="https://github.com/GualterMM">
        <img src="https://avatars.githubusercontent.com/u/35864822?v=4" width="100px;" alt="Foto do Gualter Machado no GitHub"/><br>
        <sub>
          <b>Gualter Machado</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/IsabelaRezendeB">
        <img src="https://avatars.githubusercontent.com/u/49520751?v=4" width="100px;" alt="Foto da Isabela Rezende no GitHub"/><br>
        <sub>
          <b>Isabela Rezende</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VictoriaRBrito">
        <img src="https://avatars.githubusercontent.com/u/82007104?v=4" width="100px;" alt="Foto da Victoria Brito no GitHub"/><br>
        <sub>
          <b>Victoria Brito</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
