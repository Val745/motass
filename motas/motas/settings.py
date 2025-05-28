
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPEND_SLASH = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8l5^x(e07*z##5z5=ctj)68td$1c0lo2b*vw6^vij#9lo-qu1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_app',  
]


JAZZMIN_SETTINGS = {
    "site_title": "Administración",
    "site_header": "Veterinaria Motas",
    "site_brand": "Motas Admin",

    "welcome_sign": "Bienvenid@ al panel de administración de Motas",
    "translate_solid": True,

    "show_sidebar": True,
    "navigation_expanded": True,

    "custom_css": "CSS/custom_admin.css",  # asegúrate de que el archivo exista
    "custom_js": ["js/custom_admin.js"],

    "changeform_format": "horizontal_tabs",

    "order_with_respect_to": ["auth", "myapp"],

    "icons": {
        "auth": "fas fa-users",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
    },

    "theme": "darkly",  # Puede ser cualquier, porque lo vamos a sobrescribir
}


JAZZMIN_UI_TWEAKS = {
    # Tema base (puedes probar "flatly", "cosmo", "minty" para fondos claros)
    "theme": "flatly",
    
    # Paleta de colores principal
    "primary": "pink",
    "secondary": "pink",
    "accent": "pink",
    
    # Barra superior
    "navbar": "navbar-pink navbar-dark",  # También prueba navbar-light si prefieres texto oscuro
    "brand_colour": "navbar-pink",
    
    # Sidebar
    "sidebar": "sidebar-dark-pink",  # Para fondo rosa oscuro
    # "sidebar": "sidebar-light-pink",  # Para fondo rosa claro
    
    # Botones
    "button_classes": {
        "warning": "btn-warning",
        "success": "btn-success",
        "primary": "btn-light-pink",  # Save
        "secondary": "btn-lavender",  # Continue
        "danger": "btn-hot-pink",     # Delete
        "info": "btn-light-blue",     # Add another
        "success": "btn-mint",        # History
    },
    
    # Varios
    "body_small_text": False,
    "brand_small_text": False,
    "no_navbar_border": False,
    "navbar_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    
    # Estilo del menú
    "nav_accordion": True,
    "actions_sticky_top": True,
    
    # Colores alternativos (puedes personalizar)
    "dark_mode_theme": "darkly",
    
    # Clases CSS para elementos específicos
    "related_modal_active": True,
    "custom_css": None,  # Ya lo defines en JAZZMIN_SETTINGS
    "custom_js": None,   # Ya lo defines en JAZZMIN_SETTINGS
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mi_app.middleware.AutoRedirectResetDone',

]

ROOT_URLCONF = 'motas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mi_app', 'templates')],  # Ajusta la ruta
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'motas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

AUTH_USER_MODEL = 'mi_app.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'  # Código de idioma para español
TIME_ZONE = 'America/Mexico_City'  # Ajusta según tu zona horaria
USE_I18N = True  # Habilitar internacionalización
USE_L10N = True  # Habilitar localización
USE_TZ = True  # Usar zona horaria


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Al final del archivo o cerca de STATIC_URL
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'no-reply@motas.com'


