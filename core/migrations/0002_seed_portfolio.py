from django.db import migrations


def seed_portfolio(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")
    Project = apps.get_model("core", "Project")
    Experience = apps.get_model("core", "Experience")

    skills = [
        ("HTML", "frontend", 92, "bi-filetype-html", 1),
        ("CSS", "frontend", 90, "bi-filetype-css", 2),
        ("JavaScript", "frontend", 84, "bi-filetype-js", 3),
        ("Bootstrap", "frontend", 88, "bi-bootstrap", 4),
        ("Python", "backend", 90, "bi-filetype-py", 1),
        ("Django", "backend", 92, "bi-server", 2),
        ("SQLite", "backend", 82, "bi-database", 3),
        ("Django Admin", "backend", 88, "bi-shield-check", 4),
        ("Git", "tools", 86, "bi-git", 1),
        ("GitHub", "tools", 85, "bi-github", 2),
        ("VS Code", "tools", 88, "bi-code-square", 3),
        ("Deployment", "tools", 78, "bi-cloud-arrow-up", 4),
    ]
    for name, category, proficiency, icon_class, order in skills:
        Skill.objects.get_or_create(
            name=name,
            defaults={
                "category": category,
                "proficiency": proficiency,
                "icon_class": icon_class,
                "order": order,
            },
        )

    projects = [
        {
            "title": "Portfolio Platform",
            "slug": "portfolio-platform",
            "summary": "A polished Django portfolio with theme switching, admin-managed content, and responsive sections.",
            "description": "A production-ready personal site with reusable templates, SEO metadata, contact storage, and a refined UI system.",
            "image": "img/projects/portfolio-platform.svg",
            "tech_stack": "Django, Bootstrap, JavaScript, SQLite",
            "github_url": "https://github.com/",
            "live_url": "https://example.com/",
            "order": 1,
        },
        {
            "title": "Commerce Analytics Dashboard",
            "slug": "commerce-analytics-dashboard",
            "summary": "A responsive dashboard concept for tracking revenue, customers, and product performance.",
            "description": "Designed for operators who need quick scanning, clean metrics, and practical business insights.",
            "image": "img/projects/commerce-dashboard.svg",
            "tech_stack": "Python, Django, Charts, Bootstrap",
            "github_url": "https://github.com/",
            "live_url": "https://example.com/",
            "order": 2,
        },
        {
            "title": "API Workflow Suite",
            "slug": "api-workflow-suite",
            "summary": "A backend-first project focused on clean models, forms, routing, and integration-ready architecture.",
            "description": "Built around maintainable Django patterns for data capture, admin workflows, and service boundaries.",
            "image": "img/projects/api-suite.svg",
            "tech_stack": "Django, REST, SQLite, Git",
            "github_url": "https://github.com/",
            "live_url": "https://example.com/",
            "order": 3,
        },
        {
            "title": "Design System Starter",
            "slug": "design-system-starter",
            "summary": "A component library concept with cards, buttons, forms, badges, and responsive layout primitives.",
            "description": "A practical frontend foundation for building consistent product interfaces with accessible components.",
            "image": "img/projects/design-system.svg",
            "tech_stack": "HTML, CSS, Bootstrap, JavaScript",
            "github_url": "https://github.com/",
            "live_url": "https://example.com/",
            "order": 4,
        },
    ]
    for project in projects:
        Project.objects.get_or_create(slug=project["slug"], defaults=project)

    experience = [
        {
            "type": "work",
            "title": "Full Stack Developer",
            "organization": "Independent Projects",
            "location": "Remote",
            "period": "2025 - Present",
            "description": "Building Django applications with clean templates, database-backed features, and responsive user interfaces.",
            "order": 1,
            "is_current": True,
        },
        {
            "type": "education",
            "title": "Computer Science Foundations",
            "organization": "Academic and self-directed learning",
            "location": "",
            "period": "2024 - 2026",
            "description": "Studied programming, databases, web architecture, and practical software engineering workflows.",
            "order": 2,
            "is_current": True,
        },
        {
            "type": "certification",
            "title": "Django Web Development",
            "organization": "Professional learning track",
            "location": "Online",
            "period": "2026",
            "description": "Focused on Django project structure, models, forms, admin customization, and deployment-ready settings.",
            "order": 3,
            "is_current": False,
        },
    ]
    for item in experience:
        Experience.objects.get_or_create(
            title=item["title"],
            organization=item["organization"],
            defaults=item,
        )


def remove_seed_portfolio(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")
    Project = apps.get_model("core", "Project")
    Experience = apps.get_model("core", "Experience")

    Skill.objects.filter(
        name__in=[
            "HTML",
            "CSS",
            "JavaScript",
            "Bootstrap",
            "Python",
            "Django",
            "SQLite",
            "Django Admin",
            "Git",
            "GitHub",
            "VS Code",
            "Deployment",
        ]
    ).delete()
    Project.objects.filter(
        slug__in=[
            "portfolio-platform",
            "commerce-analytics-dashboard",
            "api-workflow-suite",
            "design-system-starter",
        ]
    ).delete()
    Experience.objects.filter(
        title__in=[
            "Full Stack Developer",
            "Computer Science Foundations",
            "Django Web Development",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_portfolio, remove_seed_portfolio),
    ]
