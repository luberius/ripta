from django.shortcuts import redirect


def ripta_middleware(get_response):
    def middleware(req):
        response = get_response(req)

        if req.path == '/login':
            return response

        if req.user.is_authenticated:
            return response

        return redirect('/login')

    return middleware
