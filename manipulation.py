import asyncio
import functools
import textwrap
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "./data/fonts"
IMAGE_PATH = "./data/layouts"


def executor(func):
    """Wraps a sync function into an async function.

    This provides us non-blocking wrapped functions.
    """

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        """Sync function wrapper."""
        loop = asyncio.get_event_loop()
        partial_function = functools.partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, partial_function)

    return wrapper


class Manipulation:
    """A set of static methods used in the Image extension."""

    @staticmethod
    @executor
    def typeracer(txt: str):
        font = ImageFont.truetype(f"{FONT_PATH}/monoid.ttf", size=30)
        w, h = font.getsize_multiline(txt)

        with Image.new("RGB", (w + 10, h + 10)) as base:
            canvas = ImageDraw.Draw(base)
            canvas.multiline_text((5, 5), txt, font=font)
            buffer = BytesIO()
            base.save(buffer, "png", optimize=True)

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def welcome(top_text: str, bottom_text: str, member_avatar: BytesIO):
        font = ImageFont.truetype(f"{FONT_PATH}/arial_bold.ttf", size=20)
        join_w, member_w = font.getsize(bottom_text)[0], font.getsize(top_text)[0]

        with Image.new("RGB", (600, 400)) as card:
            card.paste(Image.open(member_avatar).resize((263, 263)), (170, 32))
            draw = ImageDraw.Draw(card)
            draw.text(
                ((600 - join_w) / 2, 309), bottom_text, (255, 255, 255), font=font
            )
            draw.text(((600 - member_w) / 2, 1), top_text, (169, 169, 169), font=font)
            buffer = BytesIO()
            card.save(buffer, "png", optimize=True)

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def pixelate(image: BytesIO):
        with Image.open(image) as im:
            small = im.resize((32, 32), resample=Image.BILINEAR)
            result = small.resize(im.size, Image.NEAREST)
            buffer = BytesIO()
            result.save(buffer, "png")

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def whyareyougay(author: BytesIO, member: BytesIO):
        author = Image.open(author)
        member = Image.open(member)

        with Image.open(f"{IMAGE_PATH}/wayg.jpg") as img:
            img.paste(author.resize((128, 128)), (507, 103))
            img.paste(member.resize((128, 128)), (77, 120))
            buffer = BytesIO()
            img.save(buffer, "png", optimize=True)

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def fiveguysonegirl(author: BytesIO, member: BytesIO):
        author = Image.open(author)
        member = Image.open(member)

        with Image.open(f"{IMAGE_PATH}/5g1g.png") as img:
            img.paste(member.resize((128, 128)), (500, 275))

            for i in [(31, 120), (243, 53), (438, 85), (637, 90), (815, 20)]:
                img.paste(author.resize((128, 128)), i)

            buffer = BytesIO()
            img.save(buffer, "png", optimize=True)

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def wanted(image: BytesIO):
        image = Image.open(image).resize((189, 205))

        with Image.open(f"{IMAGE_PATH}/wanted.png") as img:
            img.paste(image, (73, 185))
            buffer = BytesIO()
            img.save(buffer, "png")

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor  # 395, 206 - knocked out; 236, 50 - winner
    def fight(winner: BytesIO, knocked_out: BytesIO):
        winner = Image.open(winner).resize((40, 40))
        knocked_out = Image.open(knocked_out).resize((60, 60))

        with Image.open(f"{IMAGE_PATH}/fight.jpg") as img:
            img.paste(winner, (236, 50))
            img.paste(knocked_out.rotate(-90), (395, 206))
            buffer = BytesIO()
            img.save(buffer, "png")

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def clyde(txt: str):
        font = ImageFont.truetype(f"{FONT_PATH}/whitneybook.otf", 18)

        with Image.open(f"{IMAGE_PATH}/clyde.png") as img:
            draw = ImageDraw.Draw(img)
            draw.text((72, 33), txt, (255, 255, 255), font=font)
            buffer = BytesIO()
            img.save(buffer, "png")

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def drake(no: str, yes: str):
        no_wrapped = textwrap.wrap(text=no, width=13)
        yes_wrapped = textwrap.wrap(text=yes, width=13)
        font = ImageFont.truetype(f"{FONT_PATH}/arial_bold.ttf", size=28)

        with Image.open(f"{IMAGE_PATH}/drake.jpg") as img:
            draw = ImageDraw.Draw(img)
            draw.text((270, 10), "\n".join(no_wrapped), (0, 0, 0), font=font)
            draw.text((270, 267), "\n".join(yes_wrapped), (0, 0, 0), font=font)
            buffer = BytesIO()
            img.save(buffer, "png")

        buffer.seek(0)
        return buffer

    @staticmethod
    @executor
    def achievement(title: str, caption: str, colour=(255, 255, 0, 255)):
        front = Image.open(f"{IMAGE_PATH}/achievement/achievement.png")
        txt = Image.new("RGBA", (len(caption) * 15, 64))
        fnt = ImageFont.truetype(f"{FONT_PATH}/minecraft.ttf", 16)
        d = ImageDraw.Draw(txt)

        w, h = d.textsize(caption, font=fnt)
        w = max(320, w)

        mid = Image.new("RGBA", (w + 20, 64), (255, 255, 255, 0))

        midd = Image.open(f"{IMAGE_PATH}/achievement/mid.png")
        end = Image.open(f"{IMAGE_PATH}/achievement/end.png")

        for i in range(0, w):
            mid.paste(midd, (i, 0))
        mid.paste(end, (w, 0))

        txt = Image.new("RGBA", (w + 20, 64), (255, 255, 255, 0))

        d = ImageDraw.Draw(txt)
        d.text((0, 9), title, font=fnt, fill=colour)
        d.text((0, 29), caption, font=fnt, fill=(255, 255, 255, 255))

        mid = Image.alpha_composite(mid, txt)

        im = Image.new("RGBA", (w + 80, 64))

        im.paste(front, (0, 0))
        im.paste(mid, (60, 0))

        buffer = BytesIO()
        im.save(buffer, "PNG")
        buffer.seek(0)
        return buffer
