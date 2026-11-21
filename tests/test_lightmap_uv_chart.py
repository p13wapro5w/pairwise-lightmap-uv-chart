import pytest
import math
from render import lightmap_uv_chart as mod

CASES = [
    ("dilate", 'm.dilate((1, 2, 3, 4), 1) == (0, 1, 5, 6)'),
    ("overlap", 'm.overlap((0, 0, 2, 2), (1, 1, 3, 3)) is True'),
    ("stitch", 'm.stitch_weight(1, 3) == approx(2.0)'),
    ("density", 'm.texel_density(4, 2) == approx(2.0)'),
    ("rotate", 'm.rotate_pack((0, 0, 2, 4), 1) == (0, 0, 4, 2)'),
    ("hdr", 'm.hdr_bits(16) == 16'),
    ("static", 'm.static_only(True) is True'),
    ("clamp", 'm.clamp_uv((-0.2, 1.2)) == (0.0, 1.0)'),
    ("rebake", 'm.rebake(1, 2) == (1, 2)'),
    ("area", 'm.chart_area(3, 4) == 12'),
    ("padding", 'm.padding_px(256, 4) == 1024'),
    ("seam", 'm.seam_key("c1", 2) == "c1:2"'),
    ("texels", 'm.total_texels([4, 8]) == 12'),
    ("uv", 'm.is_lightmap_uv(1) is True'),
    ("id", 'm.lightmap_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
