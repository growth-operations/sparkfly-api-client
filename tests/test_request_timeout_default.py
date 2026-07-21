# coding: utf-8
"""Regression tests for the bounded default request timeout.

Context (incident PD Q2H3F5WK564P5F, hubspot-sparkfly prod, 2026-07-21):
Every HTTP call defaulted to a 5-minute timeout (``rest.py``:
``_request_timeout or 5 * 60``) with no client-level override. When Sparkfly was
slow/unresponsive for one account's event storm, each caller (a Cloud Run async
handler) blocked ~300s on the Sparkfly call, holding a container-concurrency
slot for the full request timeout. Slots exhausted and instances wedged into
sustained 504s. These tests pin the bounded, configurable default so a slow
Sparkfly call fails fast and frees the slot.
"""

from sparkfly.configuration import Configuration
from sparkfly.rest import RESTClientObject


def _resolve(rest_client, per_call):
    """Mirror the timeout-resolution rule in RESTClientObject.request()."""
    return per_call if per_call is not None else rest_client.request_timeout


def test_configuration_default_timeout_is_bounded():
    cfg = Configuration()
    assert cfg.request_timeout is not None, "default must be bounded, not unbounded"
    assert cfg.request_timeout <= 60, "default should fail fast (<= 60s)"


def test_rest_client_reads_configured_timeout():
    cfg = Configuration(request_timeout=17.5)
    rc = RESTClientObject(cfg)
    assert rc.request_timeout == 17.5


def test_explicit_per_call_timeout_wins():
    rc = RESTClientObject(Configuration())
    # An explicit per-call value always overrides the default.
    assert _resolve(rc, 5) == 5
    # No per-call value falls back to the bounded client default.
    assert _resolve(rc, None) == rc.request_timeout
    assert _resolve(rc, None) <= 60


def test_opt_out_restores_unbounded():
    # None explicitly restores the historical unbounded behavior for callers
    # that knowingly need a long-running request.
    rc = RESTClientObject(Configuration(request_timeout=None))
    assert rc.request_timeout is None
