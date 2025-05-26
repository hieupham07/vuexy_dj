from django.http import JsonResponse
from django.conf import settings
import json
import os
from pathlib import Path

from web_project.template_helpers.theme import TemplateHelper


# menu_file_path =  settings.BASE_DIR / "templates" / "layout" / "partials" / "menu" / "vertical" / "json" / "vertical_menu.json"
menu_file_path = Path(settings.BASE_DIR) / "templates" / "layout" / "partials" / "menu" / "vertical" / "json" / "vertical_menu.json"

# json_path = os.path.join(pth_path)
# with open(json_path, encoding='utf-8') as f:
#     menu_file_path = json.load(f)
"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in web_project/__init__.py
"""


class TemplateBootstrapLayoutVertical:

    @staticmethod
    def init(context):
        context.update(
            {
                "layout": "vertical",
                "content_navbar": True,
                "is_navbar": True,
                "is_menu": True,
                "is_footer": True,
                "navbar_detached": True,
            }
        )

        # map_context according to updated context values
        TemplateHelper.map_context(context)

        TemplateBootstrapLayoutVertical.init_menu_data(context)

        return context

    @staticmethod
    def init_menu_data(context):
        menu_data = []
        if menu_file_path.exists():
            with menu_file_path.open(encoding='utf-8') as f:
                try:
                    menu_data = json.load(f)
                except json.JSONDecodeError as e:
                    # Log hoặc xử lý lỗi nếu cần
                    print(f"Lỗi đọc JSON: {e}")

        context.update({"menu_data": menu_data})
        # # Load the menu data from the JSON file
        # menu_data = json.load(menu_file_path.open()) if menu_file_path.exists() else []

        # # Updated context with menu_data
        # context.update({"menu_data": menu_data})
