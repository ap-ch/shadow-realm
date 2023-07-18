from PIL import Image, ImageDraw, ImageFont

def jimbofy(text: str) -> Image:
    """Generates an image with a caption sending "text" to the Shadow Realm

    Args:
        text: The thing you want to send to the Shadow Realm

    Returns:
        An Image depicting your text being sent to the Shadow Realm

    """
    img = Image.open("./static/images/jimbo.png")
    img_draw = ImageDraw.Draw(img)
    arial = ImageFont.truetype("./static/fonts/arial.ttf", 42)
    img_draw.text((144, 520), f"Looks like you're going to the Shadow Realm,\n{text}.", font=arial, fill=(255, 255, 0))
    return img
