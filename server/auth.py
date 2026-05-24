"""Fly builder — authentication middleware.

Validates Bearer token from Authorization header against BUILDER_TOKEN secret.
"""
from __future__ import annotations

import os
from http import HTTPStatus


def verify_token(auth_header: str | None) -> bool:
    """Return True if auth_header carries a valid Bearer token."""
    expected = os.environ.get("BUILDER_TOKEN", "").strip()
    if not expected:
        return False
    if not auth_header or not auth_header.startswith("Bearer "):
        return False
    return auth_header[len("Bearer "):].strip() == expected


class AuthError(Exception):
    status_code: int = HTTPStatus.UNAUTHORIZED

    def __init__(self, message: str = "Unauthorized") -> None:
        super().__init__(message)
        self.message = message
