
from __future__ import annotations

import os
import pytest

STATE_PATH = os.path.join(os.path.dirname(__file__), "state.json")
BASE_URL = "http://localhost:93"


@pytest.fixture(scope="session")
def storage_state(browser):
    """
    Create storage_state once per test session and save it to state.json.    
    """
    if not os.path.exists(STATE_PATH):
        context = browser.new_context()
        page = context.new_page()       
        page.goto("http://localhost:93")
       
        context.storage_state(path=STATE_PATH)
        context.close()

    return STATE_PATH


@pytest.fixture()
def context(browser, storage_state):
    """
    New isolated context per test, but preloaded with storage_state.
    """
    ctx = browser.new_context(storage_state=storage_state)
    yield ctx
    ctx.close()


@pytest.fixture()
def page(context):
    p = context.new_page()
    yield p
    p.close()


@pytest.fixture(scope="module")
def shared_context(browser, storage_state):
    """
    Shared context for tests that need to maintain browser state across tests.
    """
    ctx = browser.new_context(storage_state=storage_state)
    yield ctx
    ctx.close()


@pytest.fixture(scope="module")
def shared_page(shared_context):
    """
    Shared page for tests that need to maintain browser state across tests.
    This page persists across tests in the same module.
    """
    p = shared_context.new_page()
    # Always start from a known state
    page.goto(BASE_URL, wait_until="domcontentloaded")
    yield p
    p.close()

