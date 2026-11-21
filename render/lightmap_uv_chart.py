"""Lightmap UV chart helpers.

Rectangles are expressed as ``(x, y, width, height)`` unless stated
otherwise.  The functions here cover the small, independent pieces of the
lightmap baking pipeline: chart dilation, overlap detection, seam stitching,
texel density, atlas packing, HDR storage, static validation, UV clamping and
rebaking.
"""

import math


def dilate(rect, pixels):
    """Expand a chart rectangle by ``pixels`` on every side.

    Dilation grows the island outwards so bilinear filtering at the island
    border does not pull in neighbouring charts' lighting.
    """
    x, y, width, height = rect
    if pixels < 0:
        raise ValueError("dilation must be non-negative")
    return (x - pixels, y - pixels, width + 2 * pixels, height + 2 * pixels)


def overlap(a, b):
    """Return whether two ``(x, y, width, height)`` rectangles overlap.

    Rectangles that merely share an edge are not considered overlapping, so
    dilated charts can be packed flush against each other.  A rectangle with
    a non-positive extent is empty and never overlaps anything.
    """
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    if aw <= 0 or ah <= 0 or bw <= 0 or bh <= 0:
        return False
    return ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah


def stitch_weight(a, b):
    """Blend weight for a texel shared by two charts across a seam.

    The stitched texel uses the average of the two sides so a wall split into
    two charts does not show a brightness step along the seam.
    """
    return (a + b) / 2.0


def texel_density(texels, area):
    """Texels per unit of surface area for a chart."""
    if area <= 0:
        raise ValueError("chart area must be positive")
    return texels / area


def rotate_pack(rect, quarter):
    """Rotate a chart rectangle by a number of quarter turns for packing.

    Odd quarter turns swap width and height; even turns leave the rectangle
    unchanged.  The origin is kept so the caller controls placement.
    """
    x, y, width, height = rect
    if quarter % 2:
        width, height = height, width
    return (x, y, width, height)


def hdr_bits(bits):
    """Return the storage precision to use for an HDR lightmap.

    HDR lightmaps need enough precision to keep highlights from clipping, so
    anything below 16 bits is promoted to 16-bit float.
    """
    return max(int(bits), 16)


def static_only(is_static):
    """Validate that a baked object is marked static.

    Only objects explicitly flagged static may be baked into the lightmap; an
    unflagged object would be baked and then keep moving at runtime.
    """
    return is_static is True


def clamp_uv(uv):
    """Clamp a UV coordinate into the [0, 1] atlas range.

    Clamping prevents edge sampling from falling outside the atlas and
    returning the clear colour at distant walls.
    """
    return tuple(0.0 if value < 0.0 else 1.0 if value > 1.0 else value for value in uv)


def rebake(direct, indirect):
    """Return both baked components for a rebake.

    A rebake must update direct and indirect lighting together; carrying the
    previous indirect result forward leaves stale bounce light.
    """
    return (direct, indirect)


def chart_area(width, height):
    """Surface area covered by a chart."""
    if width < 0 or height < 0:
        raise ValueError("chart dimensions must be non-negative")
    return width * height


def padding_px(resolution, pad):
    """Total edge padding in pixels for an atlas of ``resolution`` texels."""
    if resolution < 0 or pad < 0:
        raise ValueError("resolution and padding must be non-negative")
    return resolution * pad


def seam_key(chart, edge):
    """Stable identifier for one edge of a chart's seam."""
    return f"{chart}:{edge}"


def total_texels(charts):
    """Sum the texel counts of a collection of charts."""
    return sum(charts)


def is_lightmap_uv(index):
    """Whether a UV channel index refers to the lightmap UV set.

    The lightmap uses the second UV set, which is index 1 in zero-based
    channel numbering.
    """
    return index == 1


def lightmap_id(seed, index):
    """Deterministic identifier for a lightmap entry."""
    return f"{seed}:{index}"
