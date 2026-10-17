from django.db import models
from django.utils.text import slugify
class Project(models.Model):
    CATEGORY_CHOICES = [("networking","Networking"),("security","Network Security"),("automation","Automation"),("infrastructure","IT Infrastructure"),("other","Other")]
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="networking")
    short_description = models.CharField(max_length=240)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True, help_text="Separate technologies with commas.")
    image = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    attachment = models.FileField(upload_to="projects/files/", blank=True, null=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-featured", "-created_at"]
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "project"
            slug, n = base, 2
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug, n = f"{base}-{n}", n+1
            self.slug = slug
        super().save(*args, **kwargs)
    @property
    def technology_list(self):
        return [x.strip() for x in self.technologies.split(",") if x.strip()]
    def __str__(self):
        return self.title
