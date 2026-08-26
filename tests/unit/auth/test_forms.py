# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from io import BytesIO
from typing import final

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from server.apps.auth.forms import UploadAvatarForm
from server.apps.auth.models import User


def _make_image(name: str = 'avatar.png') -> SimpleUploadedFile:
    image = Image.new('RGB', (100, 100), color='red')
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return SimpleUploadedFile(name, buffer.read(), content_type='image/png')


@final
class TestUploadAvatarForm(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            email='test@example.com',
            password='pass123',
        )
        self.user = User.objects.get(email='test@example.com')

    def test_valid_image_upload(self) -> None:
        form = UploadAvatarForm(
            data={},
            files={'avatar': _make_image()},
            instance=self.user,
        )
        assert form.is_valid(), form.errors
        form.save()
        self.user.refresh_from_db()
        assert self.user.avatar

    def test_no_file_returns_invalid(self) -> None:
        form = UploadAvatarForm(
            data={},
            files={},
            instance=self.user,
        )
        assert not form.is_valid()
        assert 'avatar' in form.errors

    def test_invalid_file_type_returns_invalid(self) -> None:
        bad_file = SimpleUploadedFile(
            'file.txt',
            b'not an image',
            content_type='text/plain',
        )
        form = UploadAvatarForm(
            data={},
            files={'avatar': bad_file},
            instance=self.user,
        )
        assert not form.is_valid()
        assert 'avatar' in form.errors
