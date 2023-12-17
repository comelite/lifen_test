"""
App module
"""
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional, Sequence


class App:
    """
    App class
    """

    def __init__(self) -> None:
        """
        Init app
        Args:
            None

        Returns:
            None
        """
        self.path_detect_word = Path("lifen_test/data/utils/detect_word.txt")
        with open(self.path_detect_word, encoding="utf-8") as file:
            self.list_detect_word = file.read().splitlines()
        self.extracted_names: Sequence[dict[str, object] | None]
        self.docs: dict[str, Any] = {}

    def sort_words(self, words: dict[str, Any]) -> None:
        """
        Sort words by their y_min and x_min coordinates
        Args:
            words (dict[str, any]): Words

        Returns:
            dict[str, any]: Sorted words
        """
        words["words"] = sorted(
            words["words"],
            key=lambda word: (word["bbox"]["y_min"], word["bbox"]["x_min"]),
        )

    def check_if_name(
        self, next_word_index: int, page: dict[str, Any], word: dict[str, Any]
    ) -> Optional[dict[str, Any]]:
        """
        Check if the two next words are names
        Args:
            next_word_index (int): Index of the next word
            page (dict[str, any]): Page
            word (dict[str, any]): Word

        Returns:
            dict[str, any]: Names
        """
        first_name = ""
        last_name = ""

        next_word_index = page["words"].index(word) + 1
        if next_word_index < len(page["words"]):
            first_name = page["words"][next_word_index]["text"]
            next_word_index += 1
            if next_word_index < len(page["words"]):
                text = page["words"][next_word_index]["text"]
                if text.isupper() and re.match(r"^[A-Z]+$", text) and first_name != "":
                    last_name = text
                else:
                    first_name = ""
            else:
                first_name = ""

        if first_name != "" and last_name != "":
            return {"first_name": first_name, "last_name": last_name}

        return None

    def extract_names(self, document: dict[str, Any]) -> None:
        """
        Extract names from document
        Args:
            document (dict[str, any]): Document

        Returns:
            None
        """
        name_in_page = []
        names = []

        for i, page in enumerate(document["pages"]):
            for word in page["words"]:
                text = word["text"]
                if text.lower() in self.list_detect_word:
                    name = self.check_if_name(page["words"].index(word), page, word)
                    if name is not None:
                        names.append(name)
            dict_names = {"page_number": i, "names": names.copy()}
            name_in_page.append(dict_names.copy())
            names.clear()
        self.extracted_names = name_in_page.copy()

    def load(self, path: Path) -> None:
        """
        Load json file
        Args:
            path (Path): Path to json file

        Returns:
            None
        """
        try:
            with open(path, encoding="utf-8") as json_file:
                try:
                    self.docs = json.load(json_file)
                except json.decoder.JSONDecodeError as err:
                    print(
                        "Error: file is not a valid json file: ",
                        err,
                    )
                    sys.exit()
        except FileNotFoundError:
            print("Error: file not found:", path)
            sys.exit()

    def save(self, path: Path) -> None:
        """
        Save json file
        Args:
            path (Path): Path to json file

        Returns:
            None
        """
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(self.extracted_names, json_file)

    def run(self, path_load: Path, path_save: Path) -> None:
        """
        Run the app
        Args:
            path_load (Path): Path to json file
            path_save (Path): Path to json file

        Returns:
            None
        """
        self.load(path_load)
        for page in self.docs["pages"]:
            self.sort_words(page)
        self.extract_names(self.docs)
        self.save(path_save)
