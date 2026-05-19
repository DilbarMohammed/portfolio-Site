from collections import defaultdict

from django.views.generic import ListView, TemplateView

from contacts.forms import ContactForm

from .models import Experience, Project, Skill


def meta(title: str, description: str) -> dict[str, str]:
    return {
        "page_title": title,
        "meta_description": description,
    }


def grouped_skills(queryset):
    groups = defaultdict(list)
    for skill in queryset:
        groups[skill.get_category_display()].append(skill)
    return dict(groups)


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        skills = Skill.objects.filter(is_featured=True)
        return {
            **super().get_context_data(**kwargs),
            **meta(
                "Your Name | Full Stack Developer Portfolio",
                "A modern full stack developer portfolio featuring projects, skills, experience, and contact information.",
            ),
            "skills_by_category": grouped_skills(skills),
            "projects": Project.objects.filter(featured=True)[:4],
            "experience": Experience.objects.all()[:6],
            "contact_form": ContactForm(),
        }


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **meta(
                "About | Your Name",
                "Learn more about my background, approach, skills, education, and professional experience.",
            ),
            "skills_by_category": grouped_skills(Skill.objects.filter(is_featured=True)),
            "experience": Experience.objects.all(),
        }


class ProjectListView(ListView):
    model = Project
    template_name = "pages/projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = Project.objects.all()
        self.selected_tech = self.request.GET.get("tech", "").strip()
        if self.selected_tech:
            queryset = queryset.filter(tech_stack__icontains=self.selected_tech)
        return queryset

    def get_context_data(self, **kwargs):
        projects = Project.objects.all()
        technologies = sorted({tech for project in projects for tech in project.tech_list})
        return {
            **super().get_context_data(**kwargs),
            **meta(
                "Projects | Your Name",
                "Explore selected full stack development projects with live demos, GitHub links, and technology stacks.",
            ),
            "technologies": technologies,
            "selected_tech": self.selected_tech,
        }
