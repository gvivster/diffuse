
from diffuse.widgets import FileDiffViewerBase
from diffuse.preferences import Preferences


def test_calculate_wrapped_segments_no_wrap():
    """Short lines should return single segment."""
    prefs = Preferences('test')
    viewer = FileDiffViewerBase(2, prefs)
    
    text = "Short line"
    segments = viewer._calculate_wrapped_segments(text, wrap_width=1000, char_width=10)
    
    assert len(segments) == 1
    assert segments[0] == (0, len(text), 0)  # (start, end, row)


def test_calculate_wrapped_segments_simple_wrap():
    """Long line should wrap at word boundary."""
    prefs = Preferences('test')
    viewer = FileDiffViewerBase(2, prefs)
    
    text = "This is a very long line that needs wrapping"
    # Assume char_width=10, wrap_width=200 = 20 chars per line
    segments = viewer._calculate_wrapped_segments(text, wrap_width=200, char_width=10)
    
    # Should break at word boundaries
    assert len(segments) >= 2
    assert segments[0][2] == 0  # First segment on row 0
    assert segments[1][2] == 1  # Second segment on row 1


def test_calculate_wrapped_segments_no_spaces():
    """Line with no spaces should hard-wrap at character boundary."""
    prefs = Preferences('test')
    viewer = FileDiffViewerBase(2, prefs)
    
    text = "A" * 50  # 50 character line with no spaces
    segments = viewer._calculate_wrapped_segments(text, wrap_width=200, char_width=10)
    
    # Should hard-wrap at 20 chars
    assert len(segments) >= 2
    assert segments[0] == (0, 20, 0)
    assert segments[1] == (20, 40, 1)
