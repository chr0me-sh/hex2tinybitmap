from PIL import Image, ImageOps
import io


def make_bitmap(px_data: bytes, fg: str, bg: str) -> Image:
    img = Image.frombytes('1', (8, 8), data=px_data)
    img = img.convert('L')
    img = img.resize((256, 256), resample=Image.NEAREST) 
    img_col = ImageOps.colorize(img, bg, fg)
    return img_col


def generate(img_data: str, fg: str, bg: str) -> io.BytesIO:
    img_bytes = bytes.fromhex(img_data)
    buf = io.BytesIO()
    img = make_bitmap(img_bytes, fg, bg)
    img.save(buf, format="PNG")
    return buf.getvalue()