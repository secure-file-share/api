from django.http import JsonResponse
# from alpha.models import AppKeys


class VerifyAPIKeyMiddleware:
    """Authenticate APIs with API Key."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request.path.startswith("/api/auth/") or request.path.startswith("/admin/"):
        #     return None

        # api_key = request.META.get("HTTP_API_KEY")

        # if not api_key:
        #     return JsonResponse({
        #         "status": False,
        #         "message": "'api_key' is missing from request headers."
        #     }, status=400)

        # app_name, app_key = api_key.split(" ")
        # auth = AppKeys.check_key(app_key, app_name)

        # if not auth:
        #     return JsonResponse({
        #         "message": "Unauthorized"
        #     }, status=401)

        return None
