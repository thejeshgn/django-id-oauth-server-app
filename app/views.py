import json
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.models import User

class UserAPI(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user_dict = {}
        user_dict["username"] = user.username
        user_dict["email"] = user.email
        user_dict["id"] = user.id
        user_dict["first_name"] = user.first_name
        user_dict["last_name"] = user.last_name
        user_dict["is_active"] = user.is_active
        data = json.dumps(user_dict)
        return HttpResponse(data, content_type="application/json")