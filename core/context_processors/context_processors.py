from core.models import Setting


def my_setting_func(request):
    setting_data=Setting.objects.last()
    return{
        'setting_data': setting_data
    }