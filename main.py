"""Application entry point for the AI Study API."""

import logging

# Show INFO logs (extraction, chunking, retries, completion) in the server console,
# so you can see exactly where a long document is at.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

from documind.app import app  # noqa: E402

__all__ = ["app"]
