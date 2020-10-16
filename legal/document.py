# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import legal


def agb():
    return load_file('agb')


def impressum():
    return load_file('impressum')


def contact():
    return load_file('contact')


def privacy():
    return load_file('privacy')


def load_file(name: str) -> str:
    """Load file and append current version number."""
    path = os.path.join(legal.ROOT, f'legal/text/{name}')
    content = utila.file_read(path)
    result = version_append(content)
    return result


TEMPLATE = """\
{text}

______________
Version: {version}
"""


def version_append(text: str) -> str:
    result = TEMPLATE.format(
        text=text,
        version=legal.__version__,
    )
    return result
