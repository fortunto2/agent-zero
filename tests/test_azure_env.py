import os


def get_api_key(service):
    service_upper = service.upper()
    candidates = [
        f"API_KEY_{service_upper}",
        f"{service_upper}_API_KEY",
        f"{service_upper}_API_TOKEN",
    ]
    if "_" in service_upper:
        parts = service_upper.split("_")
        reversed_service = "_".join(reversed(parts))
        candidates.extend([
            f"API_KEY_{reversed_service}",
            f"{reversed_service}_API_KEY",
            f"{reversed_service}_API_TOKEN",
        ])
    for key in candidates:
        value = os.getenv(key)
        if value:
            return value
    return "None"


def build_config(api_key=None, azure_endpoint=None, api_version=None):
    if not api_key:
        api_key = get_api_key("openai_azure")
    if not azure_endpoint:
        azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT") or os.getenv("AZURE_OPENAI_ENDPOINT")
    if not api_version:
        api_version = (
            os.getenv("OPENAI_API_VERSION")
            or os.getenv("AZURE_OPENAI_API_VERSION")
            or os.getenv("OPENAI_AZURE_API_VERSION")
        )
    return {
        "api_key": api_key,
        "azure_endpoint": azure_endpoint,
        "openai_api_version": api_version,
    }


def test_get_api_key_reversed(monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "val")
    assert get_api_key("openai_azure") == "val"


def test_env_variants(monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://example")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "123")
    cfg = build_config()
    assert cfg["azure_endpoint"] == "https://example"
    assert cfg["openai_api_version"] == "123"
