from PIL import Image

def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    
    width_divisible = image_size[0] % tile_size[0] == 0 
    height_divisible = image_size[1] % tile_size[1] == 0

    tile = tile_size[0]*tile_size[1]
    image = image_size[0]*image_size[1]
    if width_divisible and height_divisible:
        tiles = {i for i in range(int(image/tile)) }
        if set(ordering) == tiles:
            return True
    return False
    


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    image = Image.open(image_path)
    if not valid_input(image.size,tile_size,ordering):
        return False
    
    tiles = (image.size[0]/tile_size[0], image.size[1]/tile_size[1])

    output_img = Image.new("RGBA",image.size)
    sub_imgs = []
    for i in ordering:
        region = (i*tile_size[0],
                  i*tile_size[1],
                  tile_size[0]*(i+1),
                  tile_size[1]*(i+1))
        sub_imgs.append(image.crop(region))

    positions = zip(range(tiles[0]),range(tiles[1]))    
    for i in range(tiles[0]*tiles[1]):
        output_img.paste(sub_imgs[i],positions[i])
    return output_img

    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
rearrange_tiles("/qualifier/images/pydis_logo_scrambled.png",(128,128),[0,3,1,2],"image.png")
