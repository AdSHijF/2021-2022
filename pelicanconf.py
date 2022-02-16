AUTHOR = "AdSHijF"
SITENAME = "AdSHijF/2021-2022"
SITEURL = ""

ARTICLE_PATHS = ["posts"]
PAGE_PATHS = ["pages"]

TIMEZONE = "Africa/Abidjan"

DEFAULT_LANG = "de"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DISPLAY_CATEGORIES_ON_MENU = False

TYPOGRIFY = True

ARTICLE_ORDER_BY = "reversed-date"

ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DIRECT_TEMPLATES = ["index"]
USE_FOLDER_AS_CATEGORY = False

CATEGORY_SAVE_AS = ""
AUTHOR_SAVE_AS = ""

MENUITEMS = [("Home", SITEURL + "/")]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "mdx_linkify.mdx_linkify": {},
    },
    "output_format": "html5",
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME_STATIC_DIR = "static"

THEME = "pelican-themes/pelican-bootstrap3/"

BOOTSTRAP_THEME = "readable"
BOOTSTRAP_FLUID = False

STATIC_PATHS = ["static", "audio", "image", "video"]
THEME_STATIC_PATHS = []

EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
    "static/favicon.png": {"path": "favicon.png"},
    "static/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

FAVICON = "favicon.png"
TOUCHICON = "apple-touch-icon.png"

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
USE_PAGER = True
HIDE_SITENAME = False
HIDE_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
CC_LICENSE = "by-nc-sa"
USE_OPEN_GRAPH = False

BANNER = "---override---"
THEME_TEMPLATES_OVERRIDES = ["templates"]

CUSTOM_CSS = THEME_STATIC_DIR + "/css/ekko-lightbox.css"
CUSTOM_JS = THEME_STATIC_DIR + "/js/ekko-lightbox.min.init.js"

MAPBOX = True

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["i18n_subsites"]

I18N_TEMPLATES_LANG = "de"

# Blogroll
LINKS = ()
# Social widget
SOCIAL = ()

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
