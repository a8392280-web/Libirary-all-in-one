# media_controller.py
import random
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from app.windows.show import ShowMediaWindow


# ---------------------------------------------
# RANDOM PICK
# ---------------------------------------------
def pick_random_item(self, list_widget, media_type: str):
    count = list_widget.count()
    if count == 0:
        QMessageBox.information(self, f"No {media_type.title()}", "This list is empty!")
        return

    random_index = random.randint(0, count - 1)
    item = list_widget.item(random_index)

    list_widget.scrollToItem(item)
    item.setSelected(True)

    model = item.data(Qt.UserRole)
    if model and hasattr(model, 'title'):
        QMessageBox.information(self, "Random Pick", f"🎬 Your random {media_type} is:\n\n{model.title}")
    else:
        QMessageBox.information(self, "Random Pick", "Unknown")


# ---------------------------------------------
# FILTER LIST (search)
# ---------------------------------------------
def media_filter_list(text, list_widget):
    text = text.strip().lower()

    if text == "":
        for i in range(list_widget.count()):
            list_widget.item(i).setHidden(False)
        return

    for i in range(list_widget.count()):
        item = list_widget.item(i)
        model = item.data(Qt.UserRole)

        if model:
            name = str(model.title or "").lower()
            year = str(model.year or "").lower()
            search_text = f"{name} {year}"
            item.setHidden(text not in search_text)
        else:
            item.setHidden(True)


# ---------------------------------------------
# SORT CHANGED
# ---------------------------------------------
def media_on_sort_changed(main_widget, section, media_type: str, sort_by):
    # Determine sort key + direction
    if sort_by == "Name (A-Z)":
        sort_key, reverse = "title", False
    elif sort_by == "Name (Z-A)":
        sort_key, reverse = "title", True
    elif sort_by == "Year (Newest-Oldest)":
        sort_key, reverse = "year", True
    elif sort_by == "Year (Oldest-Newest)":
        sort_key, reverse = "year", False
    elif sort_by == "IMDB Rating (High-Low)":
        sort_key, reverse = "imdb_rating", True
    elif sort_by == "IMDB Rating (Low-High)":
        sort_key, reverse = "imdb_rating", False
    elif sort_by == "User Rating (High-Low)":
        sort_key, reverse = "user_rating", True
    elif sort_by == "User Rating (Low-High)":
        sort_key, reverse = "user_rating", False
    else:
        return

    # Save settings dynamically
    main_widget.settings.setValue(f"{media_type}_{section}_sort_by_text", sort_by)
    main_widget.settings.setValue(f"{media_type}_{section}_sort_by", sort_key)
    main_widget.settings.setValue(f"{media_type}_{section}_sort_by_reverse", reverse)

    print(f"{media_type} sort change")

    # Refresh correct section
    section_dict = getattr(main_widget, f"{media_type}_sections")
    main_widget.refresh_one_section(section, media_type, section_dict[section]["list"])


# ---------------------------------------------
# ITEM CLICKED
# ---------------------------------------------
def media_on_item_clicked(self, item, section, media_type):
    model = item.data(Qt.UserRole)
    if model and hasattr(model, "id"):
        self.selected_id = model.id

        win = ShowMediaWindow(
            section=section,
            item_id=self.selected_id,
            media_type=media_type
        )

        win.item_deleted.connect(lambda *_: self.refresh_all_sections(media_type))
        win.item_moved.connect(lambda *_: self.refresh_all_sections(media_type))

        win.exec()
