# This file makes the 'utils' directory a Python package.
# It can be used to import functions from the module files easily.

from .co_reference_resolution import resolve_co_references
from .error_handling import log_error, handle_error
from .fallback import fallback_response

__all__ = [
    'resolve_co_references',
    'log_error',
    'handle_error',
    'fallback_response'
]
