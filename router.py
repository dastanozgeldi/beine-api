from io import BytesIO

from fastapi import APIRouter, Response

from manipulation import Manipulation
from utils import make_image

router = APIRouter()


@router.get("/typeracer/", description="Typeracer game, find who types the fastest!")
async def typeracer(txt: str):
    bts = await Manipulation.typeracer(txt)
    return Response(content=bts.read(), media_type="image/png")


@router.get("/welcome/", description="Get welcoming image for your server.")
async def welcome(top_text: str, bottom_text: str, url: str):
    member_avatar = make_image(url)
    bts = await Manipulation.welcome(top_text, bottom_text, BytesIO(member_avatar))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/pixelate/", description="Blur image down to pixels")
async def pixelate(url: str):
    image = make_image(url)
    bts = await Manipulation.pixelate(BytesIO(image))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/wanted/", description="WANTED: $500 image")
async def wanted(url: str):
    image = make_image(url)
    bts = await Manipulation.wanted(BytesIO(image))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/fight/", description="Boxing ring amongst 2 people, 2 image urls")
async def fight(url1: str, url2: str):
    image1 = make_image(url1)
    image2 = make_image(url2)
    bts = await Manipulation.fight(BytesIO(image1), BytesIO(image2))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/whyareyougay/", description="Legendary wHy ArE yOu GaE? meme")
async def whyareyougay(url1: str, url2: str):
    image1 = make_image(url1)
    image2 = make_image(url2)
    bts = await Manipulation.whyareyougay(BytesIO(image1), BytesIO(image2))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/clyde/", description="Say things as Discord's Clyde bot!")
async def clyde(txt: str):
    bts = await Manipulation.clyde(txt)
    return Response(content=bts.read(), media_type="image/png")


@router.get("/5g1g/", description="Legendary 5 guys 1 girl meme")
async def fiveguysonegirl(url1: str, url2: str):
    image1 = make_image(url1)
    image2 = make_image(url2)
    bts = await Manipulation.fiveguysonegirl(BytesIO(image1), BytesIO(image2))
    return Response(content=bts.read(), media_type="image/png")


@router.get("/drake/", description="Drake's no/yes meme")
async def drake(no: str, yes: str):
    bts = await Manipulation.drake(no, yes)
    return Response(content=bts.read(), media_type="image/png")


@router.get("/achievement/", description="Drake's no/yes meme")
async def achievement(title: str, caption: str):
    bts = await Manipulation.achievement(title, caption)
    return Response(content=bts.read(), media_type="image/png")
