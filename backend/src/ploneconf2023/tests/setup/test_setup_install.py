from ploneconf2023 import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if ploneconf2023 is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IPloneconf2023Layer is registered."""
        from ploneconf2023.interfaces import IPloneconf2023Layer

        assert IPloneconf2023Layer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240603001"
