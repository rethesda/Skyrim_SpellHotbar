from pathlib import Path
import cv2


# this removes all png comment from images

def copy_and_clean_image(path_in: Path, path_out: Path):
    if not path_out.parent.exists():
        path_out.parent.mkdir(parents=True)
    img_in = cv2.imread(str(path_in), cv2.IMREAD_UNCHANGED)
    cv2.imwrite(str(path_out), img_in)


def cleanse_images(input_dir: str, output_dir: str, subdirs: bool = True):
    path = Path(input_dir)
    out = Path(output_dir)
    for p in path.glob("*/*.png" if subdirs else "*.png"):
        rel_path = p.relative_to(path)
        copy_and_clean_image(p, out / rel_path)


if __name__ == "__main__":
    input_dir_root = r"F:\Skyrim Dev\Python_projects\SpellHotbar"
    output_dir_root = r"F:\Skyrim Dev\Skyrim_SpellHotbar\python_scripts"

    #cleanse_images(f"{input_dir_root}/ai_spell_icons", f"{output_dir_root}/vanilla_spell_icons")
    #cleanse_images(f"{input_dir_root}/modded_spell_icons", f"{output_dir_root}/modded_spell_icons")
    #cleanse_images(f"{input_dir_root}/icons", f"{output_dir_root}/icons", subdirs=False)
    #cleanse_images(f"{input_dir_root}/icons", f"{output_dir_root}/icons", subdirs=True)



