#!/usr/bin/env python3
"""Create a static snapshot of the tested Django API for GitHub Pages."""
import html
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.urls import NoReverseMatch, reverse
from rest_framework.test import APIClient
from booking.models import Room


def main():
    room, _ = Room.objects.get_or_create(
        name="Library Study Room A",
        defaults={
            "building": "Campus Library",
            "capacity": 4,
            "is_available": True,
        },
    )
    client = APIClient()
    paths = [
        ("List study rooms", reverse("room-list")),
        ("Room availability details", reverse("room-detail", args=[room.pk])),
    ]
    # When the recording's feature change is merged, its endpoint appears
    # automatically in the deployed Pages snapshot.
    try:
        paths.append(("API status", reverse("api-status")))
    except NoReverseMatch:
        pass

    cards = []
    for label, path in paths:
        response = client.get(path)
        if response.status_code != 200:
            raise RuntimeError(f"Unexpected response for {path}: {response.status_code}")
        pretty_json = json.dumps(response.data, indent=2, sort_keys=True)
        cards.append(
            '<article class="example"><div class="example-header">'
            f'<span class="method">GET</span><strong>{html.escape(label)}</strong>'
            f'<span class="url">{html.escape(path)}</span>'
            f'<span class="status">{response.status_code} OK</span>'
            '</div><pre aria-label="Generated JSON response"><code>'
            f'{html.escape(pretty_json)}</code></pre></article>'
        )

    template = (ROOT / "pages" / "index.template.html").read_text(encoding="utf-8")
    output = (
        template
        .replace("__GENERATED_ENDPOINTS__", "\n".join(cards))
        .replace("__COMMIT__", html.escape(os.environ.get("GITHUB_SHA", "local")[:8]))
        .replace("__GENERATED_AT__", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    )

    site = ROOT / "_site"
    site.mkdir(exist_ok=True)
    (site / "index.html").write_text(output, encoding="utf-8")
    shutil.copy2(ROOT / "pages" / "style.css", site / "style.css")
    (site / ".nojekyll").touch()
    print(f"Built GitHub Pages snapshot: {len(cards)} API examples in {site}")


if __name__ == "__main__":
    main()
