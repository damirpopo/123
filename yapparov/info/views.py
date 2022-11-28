from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    user_ip = request.META["REMOTE_ADDR"]

    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>user_ip: {user_ip}</p>
    <p>User_agent: {user_agent}</p>
    <a href="error">error</a>
    <a href="user">user</a>
    """)
def error(request):
    return HttpResponse(f"Произошла ошибка", status=400, reason="Error")


def user(request, login="Undefined", name="Undefined" ,num=0):
    return HttpResponse(f"<h2>login: {login} name: {name} num: {num}</h2>")