"""
Test module
"""

from lifen_test.core.app import App

test = {
    "pages": [
        {
            "words": [
                {
                    "text": "hanche",
                    "bbox": {"x_min": 0.75, "x_max": 0.81, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "JACQUES",
                    "bbox": {
                        "x_min": 0.74,
                        "x_max": 0.83,
                        "y_min": 0.16,
                        "y_max": 0.17,
                    },
                },
                {
                    "text": "pour",
                    "bbox": {"x_min": 0.57, "x_max": 0.61, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "la",
                    "bbox": {"x_min": 0.73, "x_max": 0.75, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "en",
                    "bbox": {"x_min": 0.23, "x_max": 0.26, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "bien",
                    "bbox": {"x_min": 0.15, "x_max": 0.19, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "consultation",
                    "bbox": {"x_min": 0.26, "x_max": 0.36, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "Monsieur",
                    "bbox": {"x_min": 0.36, "x_max": 0.44, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "Jean",
                    "bbox": {"x_min": 0.44, "x_max": 0.48, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "à",
                    "bbox": {"x_min": 0.72, "x_max": 0.73, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "droite.",
                    "bbox": {"x_min": 0.82, "x_max": 0.87, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "revu",
                    "bbox": {"x_min": 0.19, "x_max": 0.23, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "DUPONT",
                    "bbox": {"x_min": 0.49, "x_max": 0.57, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "douleur",
                    "bbox": {"x_min": 0.65, "x_max": 0.71, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "J’ai",
                    "bbox": {"x_min": 0.12, "x_max": 0.15, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "une",
                    "bbox": {"x_min": 0.61, "x_max": 0.65, "y_min": 0.09, "y_max": 0.1},
                },
                {
                    "text": "Nicolas",
                    "bbox": {
                        "x_min": 0.67,
                        "x_max": 0.73,
                        "y_min": 0.16,
                        "y_max": 0.17,
                    },
                },
                {
                    "text": "Docteur",
                    "bbox": {"x_min": 0.6, "x_max": 0.67, "y_min": 0.16, "y_max": 0.17},
                },
            ]
        }
    ],
    "original_page_count": 1,
    "needs_ocr_case": "no_ocr",
}


def test_app_sort_words():
    """
    Test sort_words method
    """
    app = App()
    app.sort_words(test["pages"][0])

    assert test["pages"][0]["words"][0]["text"] == "J’ai"
    assert test["pages"][0]["words"][-1]["text"] == "JACQUES"
    assert test["pages"][0]["words"][-1]["bbox"] == {
        "x_min": 0.74,
        "x_max": 0.83,
        "y_min": 0.16,
        "y_max": 0.17,
    }
    assert test["pages"][0]["words"][0]["bbox"] == {
        "x_min": 0.12,
        "x_max": 0.15,
        "y_min": 0.09,
        "y_max": 0.1,
    }


def test_app_extract_names():
    """
    Test extract_names method
    """
    app = App()
    app.docs = test
    app.sort_words(app.docs["pages"][0])
    app.extract_names(app.docs)

    assert app.extracted_names[0] == {
        "page_number": 0,
        "names": [
            {"first_name": "Jean", "last_name": "DUPONT"},
            {"first_name": "Nicolas", "last_name": "JACQUES"},
        ],
    }

    test_one_name = {
        "pages": [
            {
                "words": [
                    {
                        "text": "hanche",
                        "bbox": {
                            "x_min": 0.75,
                            "x_max": 0.81,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "pour",
                        "bbox": {
                            "x_min": 0.57,
                            "x_max": 0.61,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "la",
                        "bbox": {
                            "x_min": 0.73,
                            "x_max": 0.75,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "en",
                        "bbox": {
                            "x_min": 0.23,
                            "x_max": 0.26,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "bien",
                        "bbox": {
                            "x_min": 0.15,
                            "x_max": 0.19,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "consultation",
                        "bbox": {
                            "x_min": 0.26,
                            "x_max": 0.36,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Monsieur",
                        "bbox": {
                            "x_min": 0.36,
                            "x_max": 0.44,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Jean",
                        "bbox": {
                            "x_min": 0.44,
                            "x_max": 0.48,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "à",
                        "bbox": {
                            "x_min": 0.72,
                            "x_max": 0.73,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "droite.",
                        "bbox": {
                            "x_min": 0.82,
                            "x_max": 0.87,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "revu",
                        "bbox": {
                            "x_min": 0.19,
                            "x_max": 0.23,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "DUPONT",
                        "bbox": {
                            "x_min": 0.49,
                            "x_max": 0.57,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "douleur",
                        "bbox": {
                            "x_min": 0.65,
                            "x_max": 0.71,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "J’ai",
                        "bbox": {
                            "x_min": 0.12,
                            "x_max": 0.15,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "une",
                        "bbox": {
                            "x_min": 0.61,
                            "x_max": 0.65,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Nicolas",
                        "bbox": {
                            "x_min": 0.67,
                            "x_max": 0.73,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                    {
                        "text": "Docteur",
                        "bbox": {
                            "x_min": 0.6,
                            "x_max": 0.67,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                ]
            }
        ],
        "original_page_count": 1,
        "needs_ocr_case": "no_ocr",
    }
    app.docs = test_one_name
    app.sort_words(app.docs["pages"][0])
    app.extract_names(app.docs)

    assert app.extracted_names[0] == {
        "page_number": 0,
        "names": [{"first_name": "Jean", "last_name": "DUPONT"}],
    }

    test_one_name = {
        "pages": [
            {
                "words": [
                    {
                        "text": "hanche",
                        "bbox": {
                            "x_min": 0.75,
                            "x_max": 0.81,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "pour",
                        "bbox": {
                            "x_min": 0.57,
                            "x_max": 0.61,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "la",
                        "bbox": {
                            "x_min": 0.73,
                            "x_max": 0.75,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "en",
                        "bbox": {
                            "x_min": 0.23,
                            "x_max": 0.26,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "bien",
                        "bbox": {
                            "x_min": 0.15,
                            "x_max": 0.19,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "consultation",
                        "bbox": {
                            "x_min": 0.26,
                            "x_max": 0.36,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Monsieur",
                        "bbox": {
                            "x_min": 0.36,
                            "x_max": 0.44,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Jean",
                        "bbox": {
                            "x_min": 0.44,
                            "x_max": 0.48,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "à",
                        "bbox": {
                            "x_min": 0.72,
                            "x_max": 0.73,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "droite.",
                        "bbox": {
                            "x_min": 0.82,
                            "x_max": 0.87,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "revu",
                        "bbox": {
                            "x_min": 0.19,
                            "x_max": 0.23,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "DUPONT",
                        "bbox": {
                            "x_min": 0.49,
                            "x_max": 0.57,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "douleur",
                        "bbox": {
                            "x_min": 0.65,
                            "x_max": 0.71,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "J’ai",
                        "bbox": {
                            "x_min": 0.12,
                            "x_max": 0.15,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "une",
                        "bbox": {
                            "x_min": 0.61,
                            "x_max": 0.65,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Nicolas",
                        "bbox": {
                            "x_min": 0.67,
                            "x_max": 0.73,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                    {
                        "text": "Docteur",
                        "bbox": {
                            "x_min": 0.6,
                            "x_max": 0.67,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                ]
            },
            {
                "words": [
                    {
                        "text": "hanche",
                        "bbox": {
                            "x_min": 0.75,
                            "x_max": 0.81,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "pour",
                        "bbox": {
                            "x_min": 0.57,
                            "x_max": 0.61,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "la",
                        "bbox": {
                            "x_min": 0.73,
                            "x_max": 0.75,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "en",
                        "bbox": {
                            "x_min": 0.23,
                            "x_max": 0.26,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "bien",
                        "bbox": {
                            "x_min": 0.15,
                            "x_max": 0.19,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "consultation",
                        "bbox": {
                            "x_min": 0.26,
                            "x_max": 0.36,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Monsieur",
                        "bbox": {
                            "x_min": 0.36,
                            "x_max": 0.44,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Jean",
                        "bbox": {
                            "x_min": 0.44,
                            "x_max": 0.48,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "à",
                        "bbox": {
                            "x_min": 0.72,
                            "x_max": 0.73,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "droite.",
                        "bbox": {
                            "x_min": 0.82,
                            "x_max": 0.87,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "revu",
                        "bbox": {
                            "x_min": 0.19,
                            "x_max": 0.23,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "douleur",
                        "bbox": {
                            "x_min": 0.65,
                            "x_max": 0.71,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "J’ai",
                        "bbox": {
                            "x_min": 0.12,
                            "x_max": 0.15,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "une",
                        "bbox": {
                            "x_min": 0.61,
                            "x_max": 0.65,
                            "y_min": 0.09,
                            "y_max": 0.1,
                        },
                    },
                    {
                        "text": "Nicolas",
                        "bbox": {
                            "x_min": 0.67,
                            "x_max": 0.73,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                    {
                        "text": "Docteur",
                        "bbox": {
                            "x_min": 0.6,
                            "x_max": 0.67,
                            "y_min": 0.16,
                            "y_max": 0.17,
                        },
                    },
                ]
            },
        ],
        "original_page_count": 1,
        "needs_ocr_case": "no_ocr",
    }
    app.docs = test_one_name
    app.sort_words(app.docs["pages"][0])
    app.extract_names(app.docs)

    assert app.extracted_names == [
        {
            "page_number": 0,
            "names": [{"first_name": "Jean", "last_name": "DUPONT"}],
        },
        {"page_number": 1, "names": []},
    ]
