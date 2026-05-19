from datetime import date

from django.conf import settings


def site_context(request):
    return {
        "current_year": date.today().year,
        "site_name": settings.SITE_NAME,
        "site_tagline": settings.SITE_TAGLINE,
        "portfolio_intro": settings.PORTFOLIO_INTRO,
        "portfolio_email": settings.PORTFOLIO_EMAIL,
        "portfolio_phone": settings.PORTFOLIO_PHONE,
        "portfolio_location": settings.PORTFOLIO_LOCATION,
        "portfolio_github": settings.PORTFOLIO_GITHUB,
        "portfolio_linkedin": settings.PORTFOLIO_LINKEDIN,
        "portfolio_x": settings.PORTFOLIO_X,
    }
