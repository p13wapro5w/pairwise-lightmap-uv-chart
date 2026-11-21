import math

def dilate(rect, pixels):
    """岛外扩。"""
    raise NotImplementedError("TODO: dilate")

def overlap(a, b):
    """重叠检测。"""
    raise NotImplementedError("TODO: overlap")

def stitch_weight(a, b):
    """接缝权重。"""
    raise NotImplementedError("TODO: stitch_weight")

def texel_density(texels, area):
    """纹素密度。"""
    raise NotImplementedError("TODO: texel_density")

def rotate_pack(rect, quarter):
    """旋转打包。"""
    raise NotImplementedError("TODO: rotate_pack")

def hdr_bits(bits):
    """HDR 位数。"""
    raise NotImplementedError("TODO: hdr_bits")

def static_only(is_static):
    """静态校验。"""
    raise NotImplementedError("TODO: static_only")

def clamp_uv(uv):
    """UV 钳制。"""
    raise NotImplementedError("TODO: clamp_uv")

def rebake(direct, indirect):
    """重烘。"""
    raise NotImplementedError("TODO: rebake")

def chart_area(width, height):
    """岛面积。"""
    raise NotImplementedError("TODO: chart_area")

def padding_px(resolution, pad):
    """边缘像素。"""
    raise NotImplementedError("TODO: padding_px")

def seam_key(chart, edge):
    """接缝键。"""
    raise NotImplementedError("TODO: seam_key")

def total_texels(charts):
    """纹素总量。"""
    raise NotImplementedError("TODO: total_texels")

def is_lightmap_uv(index):
    """UV 通道判定。"""
    raise NotImplementedError("TODO: is_lightmap_uv")

def lightmap_id(seed, index):
    """光照贴图 id。"""
    raise NotImplementedError("TODO: lightmap_id")
