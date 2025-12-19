from __future__ import annotations


def validate_non_empty_string(value: str | None, field_name: str) -> str:
    """Validate that a string value is non-empty.

    Args:
        value: The string to validate
        field_name: Name of the field for error messages

    Returns:
        The validated string value

    Raises:
        ValueError: If value is None or empty
    """
    if not value:
        raise ValueError(f"{field_name} cannot be empty")
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    stripped = value.strip()
    if not stripped:
        raise ValueError(f"{field_name} cannot be whitespace-only")
    return stripped


def validate_model_name(model: str | None) -> str:
    """Validate GenAI model name format.

    Args:
        model: The model name to validate

    Returns:
        The validated model name

    Raises:
        ValueError: If model name is invalid
    """
    validated = validate_non_empty_string(model, "model")
    if "/" not in validated:
        raise ValueError("model must follow 'provider/name' format")
    return validated
