# -*- coding: utf-8 -*-
# Написано по мотивам https://github.com/klen/django-gitrevision

from git import Repo, InvalidGitRepositoryError

from django.conf import settings


GIT_PATH = getattr(settings, "GIT_PATH", settings.PROJECT_ROOT)


class GitRevisionMiddleware(object):
    def process_request(self, request):
        try:
            revision = Repo(GIT_PATH).head.commit.hexsha
        except InvalidGitRepositoryError:
            revision = 'unknown'
        request.vcs_revision = revision
