from django.shortcuts import redirect
from django.urls import resolve

class AutoRedirectResetDone:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Verifica si la URL es /reset/done/ y si es una solicitud POST
        if resolve(request.path_info).url_name == 'password_reset_complete' and request.method == 'POST':
            return redirect('signin')  # Usa el nombre de tu URL de signin
        
        return response