import pytest


def test_import():
    import project  # noqa: F401


@pytest.mark.llm
def test_llm_roundtrip():
    from project.llm import complete

    assert complete("Reply with the single word: ok").strip().lower().startswith("ok")
