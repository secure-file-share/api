JAZZMIN_SETTINGS = {
    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "custom/img/logo-sm.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": "custom/img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Secure File Share",

    # Copyright on the footer
    "copyright": "SecureFileShare",

    #############
    # Side Menu #
    #############

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [
        "auth.group",
    ],

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "client.user": "fas fa-users",
        "fileshare.files": "far fa-file-alt",
        "fileshare.fileshare": "fas fa-share-square",
        "organization.organization": "far fa-building"
    },

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    # "related_modal_active": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    # "theme": "sketchy",
    # "dark_mode_theme": "darkly",
}
