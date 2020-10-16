# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import legal


def test_deliver_document():
    contact = legal.contact()
    assert 'Kontakt' in contact
    assert 'Version' in contact

    assert legal.impressum()
    assert legal.agb()
    assert legal.privacy()
