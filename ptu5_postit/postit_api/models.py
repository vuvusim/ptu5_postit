from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Post(models.Model):
    title = models.CharField(_('title'), max_length=50)
    body = models.TextField(_('body'))
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="posts"
    )
    creatade_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self) -> str:
        return _("{title} by {user} posted at {created_at}").format(
            title=self.title,
            user=self.user,
            created_at=self.creatade_at,
        )