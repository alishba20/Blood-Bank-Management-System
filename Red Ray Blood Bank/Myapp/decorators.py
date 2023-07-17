from django.shortcuts import redirect

def nurse_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('role') == 'nurse':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper

def shift_incharge_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('role') == 'shiftIncharge':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper
