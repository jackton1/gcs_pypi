import sys

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

import pytest

from gcspypi2.__main__ import main as gcspypi

# TODO (Fix me)


@pytest.mark.skip("Fix with mock data")
def test_main_create_and_upload_package(project_dir, gcs_bucket):
    with patch("google.cloud.storage.Client"):
        with project_dir("hello-world"):
            gcspypi("--bucket", gcs_bucket.name)

        assert gcs_bucket.get_blob("hello-world/index.html")
        assert gcs_bucket.get_blob("hello-world/hello-world-0.1.0.tar.gz")
        assert gcs_bucket.get_blob(
            "hello-world/hello_world-0.1.0-py{}-none-any.whl".format(
                sys.version_info.major
            )
        )


@pytest.mark.skip("Fix with mock data")
def test_main_upload_sdist_package_from_custom_dist_path(project_dir, gcs_bucket):
    with patch("google.cloud.storage.Client"):
        with project_dir("custom-dist-path"):
            gcspypi("--dist-path", "my-dist", "--bucket", gcs_bucket.name)

        assert gcs_bucket.get_blob("foo/index.html")
        assert gcs_bucket.ge_blob("foo/foo-0.1.0.tar.gz")


@pytest.mark.skip("Fix with mock data")
def test_main_upload_wheel_package_from_custom_dist_path(project_dir, gcs_bucket):
    with patch("google.cloud.storage.Client"):
        with project_dir("custom-dist-path"):
            gcspypi("--dist-path", "helloworld-dist", "--bucket", gcs_bucket.name)

        assert gcs_bucket.get_blob("hello-world/index.html")
        assert gcs_bucket.get_blob("hello-world/hello_world-0.1.0-py3-none-any.whl")
