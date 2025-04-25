import numpy as np


def clip_histogram(hist, clip_limit):
    excess = np.maximum(hist - clip_limit, 0)
    clipped = np.minimum(hist, clip_limit)
    redistribute = excess.sum() // len(hist)
    return clipped + redistribute


def compute_tile_mapping(tile: np.ndarray, clip_limit: float) -> np.ndarray:
    hist = np.histogram(tile, bins=256, range=(0, 256))[0]
    clipped_hist = clip_histogram(hist, clip_limit=clip_limit)

    # count usual hist for tile
    cdf = clipped_hist.cumsum()
    cdf = cdf * 255 / cdf[-1]
    cdf = cdf.astype(np.uint8)

    return cdf


def clahe_np(img: np.ndarray, clip_limit: float = 40., tile_size: tuple[int, int] = (8, 8)) -> np.ndarray:
    height, width = img.shape
    tile_height, tile_width = tile_size

    n_tiles_y = (height + tile_height - 1) // tile_height
    n_tiles_x = (width + tile_width - 1) // tile_width

    mappings = np.empty((n_tiles_y, n_tiles_x, 256), dtype=np.uint8)

    for ty in range(n_tiles_y):
        for tx in range(n_tiles_x):
            y_begin = ty * tile_height
            y_end = min(height, (ty + 1) * tile_height)
            x_begin = tx * tile_width
            x_end = min(width, (tx + 1) * tile_width)

            tile = img[y_begin:y_end, x_begin:x_end]

            mappings[ty, tx] = compute_tile_mapping(tile, clip_limit=clip_limit)

    out = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            ty = y / tile_height - 0.5
            tx = x / tile_width - 0.5

            ty0 = int(np.floor(ty))
            tx0 = int(np.floor(tx))

            dy = ty - ty0
            dx = tx - tx0

            def safe_idx(val, max_val):
                return min(
                    max(val, 0),
                    max_val - 1
                )
            ty0 = safe_idx(ty0, n_tiles_y)
            ty1 = safe_idx(ty0 + 1, n_tiles_y)
            tx0 = safe_idx(tx0, n_tiles_x)
            tx1 = safe_idx(tx0 + 1, n_tiles_x)

            pixel = img[y, x]

            Q00 = mappings[ty0, tx0][pixel]
            Q01 = mappings[ty0, tx1][pixel]
            Q10 = mappings[ty1, tx0][pixel]
            Q11 = mappings[ty1, tx1][pixel]

            top = (1. - dx) * Q00 + dx * Q01
            # was dx * Q10 + dx * Q11
            bottom = (1. - dx) * Q10 + dx * Q11
            value = (1. - dy) * top + dy * bottom

            out[y, x] = np.clip(value, 0, 255)

    return out


if __name__ == '__main__':
    import cv2
    import matplotlib.pyplot as plt

    img = cv2.imread("data/l9_0.jpg", cv2.IMREAD_GRAYSCALE)
    clahe_img = clahe_np(img, tile_size=(32, 32), clip_limit=40)

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("CLAHE Interpolated")
    plt.imshow(clahe_img, cmap='gray')
    plt.show()
