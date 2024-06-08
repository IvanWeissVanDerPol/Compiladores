# This file makes the 'post_processing' directory a Python package.
# It can be used to import functions from the module files easily.

from .manual_adjustments import apply_manual_adjustments
from .update_patterns import update_dialogue_patterns

__all__ = [
    'apply_manual_adjustments',
    'update_dialogue_patterns'
]
