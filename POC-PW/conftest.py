
from __future__ import annotations

import os
import pytest
from datetime import datetime

STATE_PATH = os.path.join(os.path.dirname(__file__), "state.json")
BASE_URL = "http://localhost:93"
SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


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
    p.goto(BASE_URL, wait_until="domcontentloaded")
    yield p
    p.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshots on test failure.
    This hook is executed after each test phase (setup, call, teardown).
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Only capture screenshot if test failed during the 'call' phase
    if rep.when == "call" and rep.failed:
        # Create screenshots directory if it doesn't exist
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

        # Try to get the page fixture from the test
        page = None
        if "page" in item.funcargs:
            page = item.funcargs["page"]
        elif "shared_page" in item.funcargs:
            page = item.funcargs["shared_page"]
        elif "context" in item.funcargs:
            # If context is available, try to get pages from it
            try:
                context = item.funcargs["context"]
                pages = context.pages
                if pages:
                    page = pages[0]
            except (AttributeError, IndexError):
                pass
        elif "browser" in item.funcargs:
            # If browser is available, try to get pages from active contexts
            try:
                browser = item.funcargs["browser"]
                contexts = browser.contexts
                if contexts:
                    pages = contexts[0].pages
                    if pages:
                        page = pages[0]
            except (AttributeError, IndexError):
                pass

        if page:
            # Generate a unique screenshot filename with timestamp (including microseconds)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)

            try:
                page.screenshot(path=screenshot_path)
                print(f"\n📸 Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\n⚠️ Failed to capture screenshot: {str(e)}")


