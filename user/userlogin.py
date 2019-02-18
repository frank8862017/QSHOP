from django.shortcuts import HttpResponseRedirect, reverse


def verify_login1(func):
    def warpper(request, *args, **kwargs):
        print(request)
        print('判断没有登录')
        if request.session.get('U_userid'):
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('user:login'))

    return warpper
