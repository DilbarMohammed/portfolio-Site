from django.db import models


class Skill(models.Model):
    class Category(models.TextChoices):
        FRONTEND = "frontend", "Frontend"
        BACKEND = "backend", "Backend"
        TOOLS = "tools", "Tools"

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=Category.choices)
    proficiency = models.PositiveSmallIntegerField(default=85)
    icon_class = models.CharField(max_length=80, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=220)
    description = models.TextField()
    image = models.CharField(
        max_length=255,
        default="img/projects/portfolio-platform.svg",
        help_text="Static asset path, for example img/projects/portfolio-platform.svg",
    )
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(",") if tech.strip()]


class Experience(models.Model):
    class Type(models.TextChoices):
        WORK = "work", "Work"
        EDUCATION = "education", "Education"
        CERTIFICATION = "certification", "Certification"

    type = models.CharField(max_length=20, choices=Type.choices)
    title = models.CharField(max_length=140)
    organization = models.CharField(max_length=140)
    location = models.CharField(max_length=120, blank=True)
    period = models.CharField(max_length=80)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title} at {self.organization}"
