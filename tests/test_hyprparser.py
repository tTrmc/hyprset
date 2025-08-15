"""Tests for the custom hyprparser module."""

import pytest
import tempfile
import os
from app.modules.hyprparser import Setting, Color, Bezier, HyprData
from app.modules.hyprparser.parser import HyprlandConfigParser


class TestColor:
    def test_color_creation(self):
        color = Color('FF', '00', 'AA', 'EE')
        assert color.r == 255
        assert color.g == 0
        assert color.b == 170
        assert color.a == 238
        assert color.hex == 'FF00AAEE'

    def test_color_from_hex(self):
        color = Color.from_hex('#FF00AAEE')
        assert color.hex == 'FF00AAEE'
        
        # Test without # prefix
        color2 = Color.from_hex('FF00AAEE')
        assert color2.hex == 'FF00AAEE'

    def test_color_from_rgba_string(self):
        color = Color.from_rgba_string('rgba(255,0,170,0.93)')
        assert color.r == 255
        assert color.g == 0
        assert color.b == 170
        assert color.a == 237  # 0.93 * 255


class TestBezier:
    def test_bezier_creation(self):
        bezier = Bezier('test', (0.25, 0.1, 0.75, 0.9))
        assert bezier.name == 'test'
        assert bezier.points == (0.25, 0.1, 0.75, 0.9)
        assert bezier.x0 == 0.25
        assert bezier.y1 == 0.9

    def test_bezier_config_string(self):
        bezier = Bezier('myBezier', (0.05, 0.9, 0.1, 1.05))
        config_str = bezier.to_config_string()
        expected = "bezier = myBezier, 0.05, 0.9, 0.1, 1.05"
        assert config_str == expected


class TestSetting:
    def test_setting_creation(self):
        setting = Setting('general:gaps_in', 10)
        assert setting.section == 'general:gaps_in'
        assert setting.value == 10


class TestHyprlandConfigParser:
    def test_config_parsing(self):
        config_content = """
        # Test config
        general {
            gaps_in = 5
            gaps_out = 10
            border_size = 2
            col.active_border = rgba(33ccffee)
        }
        
        bezier = myBezier, 0.05, 0.9, 0.1, 1.05
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
            f.write(config_content)
            f.flush()
            
            parser = HyprlandConfigParser(f.name)
            parser.load()
            
            # Test settings parsing
            assert 'general:gaps_in' in parser.settings
            assert parser.settings['general:gaps_in'].value == 5
            
            # Test bezier parsing
            assert 'myBezier' in parser.beziers
            bezier = parser.beziers['myBezier']
            assert bezier.points == (0.05, 0.9, 0.1, 1.05)
            
        os.unlink(f.name)

    def test_color_value_parsing(self):
        parser = HyprlandConfigParser()
        
        # Test rgba parsing
        color = parser._parse_value('rgba(255,128,64,0.8)')
        assert isinstance(color, Color)
        assert color.r == 255
        assert color.g == 128
        
        # Test hex parsing
        color2 = parser._parse_value('#FF8040CC')
        assert isinstance(color2, Color)
        assert color2.hex == 'FF8040CC'

    def test_number_parsing(self):
        parser = HyprlandConfigParser()
        
        assert parser._parse_value('42') == 42
        assert parser._parse_value('3.14') == 3.14
        assert parser._parse_value('true') is True
        assert parser._parse_value('false') is False


if __name__ == '__main__':
    pytest.main([__file__])