from django.shortcuts import redirect


class LoginRequierdUser:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("acount:login")

        return super(LoginRequierdUser, self).dispatch(request, *args, **kwargs)
