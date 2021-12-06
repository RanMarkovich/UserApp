from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="env: local or remote"
    )


@fixture
def env(request):
    return request.config.getoption("--env")
