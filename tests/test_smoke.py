import pytest


def test_import():
    import project  # noqa: F401


def test_llm_module_imports(monkeypatch: pytest.MonkeyPatch) -> None:
    """Import project.llm with no credentials set.

    Catches import-time breakage (moved SDK symbols, bad module paths) in CI
    without calling any API. Does not need the `llm` marker: nothing here
    touches the network.
    """
    for var in (
        "ANTHROPIC_API_KEY",
        "OPENROUTER_API_KEY",
        "LANGFUSE_PUBLIC_KEY",
        "LANGFUSE_SECRET_KEY",
        "LANGFUSE_HOST",
        "HF_TOKEN",
    ):
        monkeypatch.delenv(var, raising=False)

    from project.llm import complete

    assert callable(complete)


@pytest.mark.llm
def test_llm_roundtrip():
    from project.llm import complete

    assert complete("Reply with the single word: ok").strip().lower().startswith("ok")
