from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layaut = """
        <hr>
            <ul>
                <li><a href="/inicio"> Inicio </a></li>
                <li><a href="/primos"> Mostrar números [a, b] </a></li>
                <li><a href="/examen"> Mensaje de saludo </a></li>
            </ul>
        </hr>
        """

def inicio(request):
    cursos = ['LP3',
              'legislacion',
              'micro',
              'procesos',
              'investigacion',
              'algortimos',
              'dinamica']

    return render(request, 'inicio.html',
    {
        'titulo':'Inicio',
        'cursos' : cursos
    })

    
def primos(request):
    # Aquí colocaremos la lógica para encontrar los números primos
    prime_numbers = []
    count = 0
    number = 2

    while count < 10:  # Cambia este número si deseas imprimir más números primos
        is_prime = True

        # Verificar si el número es primo
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(number)
            count += 1

        number += 1

    return HttpResponse(layaut + prime_numbers )
def examen(request):

    return render(request, 'examen.html')