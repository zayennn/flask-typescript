from flask import Blueprint, request, jsonify, redirect, url_for, make_response
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


def generate_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Selamat pagi, dunia!"
    elif 12 <= hour < 18:
        return "Selamat siang, dunia!"
    elif 18 <= hour < 22:
        return "Selamat malam, dunia!"
    else:
        return "Sudah waktunya istirahat, dunia!"

def get_status(value):
    if value >= 90:
        return "Sangat memuaskan"
    elif 75 <= value < 90:
        return "lulus"
    elif 60 <= value < 75:
        return "perlu perbaikan"
    else:
        return "tidak lulus"

def get_color(status):
    if status == "Sangat memuaskan":
        return "green"
    elif status == "lulus":
        return "blue"
    elif status == "perlu perbaikan":
        return "orange"
    else:
        return "red"

@dashboard_bp.route("/")
def index():
    greeting = generate_greeting()
    response_text = f"""
    <html>
        <head>
            <title>Dashboard - Index</title>
        </head>
        <body>
            <h1>{greeting}</h1>
            <p>Selamat datang di halaman dashboard utama!</p>
            <ul>
                <li><a href="{url_for('dashboard.showProfile')}">Profile (default)</a></li>
                <li><a href="{url_for('dashboard.showProfile', username='Budi', age=23, value=82)}">Profile Budi</a></li>
                <li><a href="{url_for('dashboard.showProfile', username='Ani', age=19, value=55)}">Profile Ani</a></li>
            </ul>
        </body>
    </html>
    """
    response = make_response(response_text)
    response.headers['X-Dashboard-Custom'] = 'IndexAccess'
    return response


@dashboard_bp.route(
    "/profile", defaults={"_route": "profile", "username": "", "age": 0, "value": 0}
)
@dashboard_bp.route(
    "/profile/<string:username>/<int:age>/<int:value>",
    defaults={"_route": "show-profile"},
)
def showProfile(_route, username, age, value):
    logs = []
    logs.append(f"Akses profile pada {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if _route == "profile":
        logs.append("Akses profile default tanpa parameter.")
        info = """
            <html>
                <head>
                   <title>Profile - Default</title>
                </head>
                <body>
                   <h2>Selamat datang di halaman profile!</h2>
                   <p>Silakan tambahkan parameter username, age, dan value pada URL untuk melihat detail profile.</p>
                   <p>Contoh: <code>/dashboard/profile/Budi/23/82</code></p>
                </body>
            </html>
        """
        response = make_response(info)
        response.headers['X-Profile-Type'] = 'Default'
        response.headers['X-Profile-Log'] = " | ".join(logs)
        return response
    elif _route == "show-profile":
        logs.append(f"Menampilkan profile untuk username: {username}, age: {age}, value: {value}")
        status = get_status(value)
        color = get_color(status)
        timestamp = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        html = f"""
            <html>
                <head>
                    <title>Profile {username}</title>
                </head>
                <body>
                    <div style="border:1px solid #ccc; padding:16px; width:350px;">
                        <h1>Nama Kamu: <span style="color:navy;">{username}</span></h1>
                        <h2>Umur Kamu: {age} tahun</h2>
                        <h2>Nilai Kamu: {value}</h2>
                        <h2>Status Kamu: <span style="color:{color};">{status}</span></h2>
                        <small><em>Diperiksa pada {timestamp}</em></small>
                    </div>
                    <hr>
                    <a href="{url_for('dashboard.index')}">Kembali ke Dashboard</a>
                </body>
            </html>
        """
        response = make_response(html)
        response.headers['X-Profile-Type'] = 'Custom'
        response.headers['X-Profile-Log'] = " | ".join(logs)
        return response
