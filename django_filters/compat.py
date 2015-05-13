from django.conf import settings


_mod_name = getattr(settings, 'FILTER_FORM_MODULE', 'django.forms')

if '.' in _mod_name:
    _mod_name = _mod_name.rsplit('.', 1)
    forms = getattr(
        __import__(_mod_name[0], globals(), locals(), [_mod_name[1]], 0),
        _mod_name[1])
else:
    forms = __import__(_mod_name, globals(), locals(), [], 0)
