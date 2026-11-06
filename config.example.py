"""
Конфигурация тулкита. Скопируйте в config.py и заполните.

    cp config.example.py config.py
"""

# --- Цель -------------------------------------------------------------------
# Базовый URL инстанса без завершающего слэша, напр. "https://hcm.corp.local"
BASE_URL = "https://hcm.example.local"

# --- Аутентификация ---------------------------------------------------------
# Basic-аутентификация: приложение ждёт заголовок
#   Authorization: Basic base64(login:password)
# Логин и пароль задаются здесь в открытом виде, base64 считается автоматически.
BASIC_LOGIN = "PASTE_LOGIN"
BASIC_PASSWORD = "PASTE_PASSWORD"

# Плюс к Basic приложение требует session-cookie:
#   Cookie: SessionID=<uuid>
COOKIE_NAME = "SessionID"
SESSION_ID = "PASTE_SESSION_UUID"

# Если удобнее задать готовый заголовок Authorization целиком (напр. уже
# закодированный Basic) — впишите сюда, тогда BASIC_LOGIN/PASSWORD игнорируются.
BASIC_RAW = ""   # напр. "Basic dXNlcjpwYXNz"

# Дополнительные заголовки/cookie, если нужны.
# Доп. cookie можно добавить строкой в EXTRA_COOKIES: {"CSRF": "..."}.
EXTRA_HEADERS = {
    # "X-Requested-With": "XMLHttpRequest",
}
EXTRA_COOKIES = {
    # "CSRF-Token": "...",
}

# --- Scope ------------------------------------------------------------------
# Хосты, по которым разрешено ходить. Коллектор не выйдет за их пределы.
# По умолчанию — только хост из BASE_URL (заполняется автоматически, если пусто).
ALLOWED_HOSTS = []          # напр. ["hcm.example.local"]

# Префиксы путей, которые нужно ИСКЛЮЧИТЬ (logout, деструктивные действия и т.п.).
# Пути, содержащие любую из этих подстрок, не обходятся и не фаззятся.
DENY_SUBSTRINGS = [
    "logout", "logoff", "signout", "exit",
    "delete", "remove", "drop", "purge", "destroy",
    "/_ad/",            # административные действия WebTutor лучше трогать точечно
]

# --- Сетевое поведение ------------------------------------------------------
# Прокси для реплея/верификации через Burp или ZAP. None — напрямую.
PROXY = None                # напр. "http://127.0.0.1:8080"

# Проверять TLS. Для стенда с самоподписанным сертом поставьте False.
VERIFY_TLS = True

# Пауза между запросами, сек (глобальный троттлинг, щадит стенд и SOC).
REQUEST_DELAY = 0.3

# Таймаут запроса, сек.
TIMEOUT = 20

# Одновременные потоки для фаззера (коллектор ходит в один поток).
CONCURRENCY = 4

# User-Agent. Явно помечаем себя как инструмент тестирования — так находку
# проще отличить в логах от реальной атаки.
USER_AGENT = "websoft-hcm-pentest/1.0 (authorized security testing)"

# --- Коллектор --------------------------------------------------------------
# Глубина обхода HTML-страниц.
CRAWL_MAX_DEPTH = 3
# Предел числа страниц, чтобы не уйти в бесконечность.
CRAWL_MAX_PAGES = 800

# --- Пути к артефактам (между шагами) --------------------------------------
ENDPOINTS_FILE = "endpoints.json"
TARGETS_FILE = "targets.json"
FINDINGS_FILE = "findings.json"
SQLMAP_TARGETS_FILE = "sqlmap_targets.txt"
