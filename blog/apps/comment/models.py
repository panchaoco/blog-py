from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


from article.models import BlogArticle
# Create your models here.

User = get_user_model()


class Comment(models.Model):
    """
    评论
    """
    COMMENT_TYPE = (
        (1, "一级评论"),
        (2, "二级评论"),
    )
    content = models.TextField(null=True, blank=True, verbose_name="评论内容", help_text="评论内容")
    comment_type = models.IntegerField(choices=COMMENT_TYPE, verbose_name="评论级别", help_text="评论级别")
    article_id = models.ForeignKey(BlogArticle, null=True, blank=True, on_delete=models.CASCADE, verbose_name="文章ID", help_text="文章ID")
    thumbs_up_count = models.IntegerField(null=True, default=10, blank=True, verbose_name="点赞次数", help_text="点赞次数")
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE, blank=True, related_name="children", verbose_name="父评论ID", help_text="父评论ID")
    comment_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间", help_text="评论时间")
    reply_user = models.CharField(null=True, blank=True, max_length=60, verbose_name="被回复的用户", help_text="被回复的用户")
    email = models.EmailField(null=True, blank=True, verbose_name="邮箱", help_text="邮箱")
    nickname = models.CharField(null=True, blank=True, max_length=60, verbose_name="昵称", help_text="昵称")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
