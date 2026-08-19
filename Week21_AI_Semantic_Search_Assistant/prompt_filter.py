"""Backward-compatible import for older notebooks and scripts."""

from src.security import check_output, filter_prompt, normalize_prompt

__all__ = ["check_output", "filter_prompt", "normalize_prompt"]
