from flask import Flask
from flask import render_template
import os
import pathlib
import re
import json

app = Flask(__name__)

IMAGE_DIR = pathlib.Path(os.environ["IMAGE_DIR"])
STRIP_RE = re.compile("(_.+$)")


def get_title_from_file_name(fn):
    """
    Extract the caption from the filename. This is everything before any underscore that might be in the name.
    :param fn:
    :return:
    """
    p = pathlib.Path(fn)
    return re.sub(STRIP_RE, "", p.stem).replace("_", " ")


def get_sort_from_file_name(fn):
    """
    Gets the sortable caption. See comments in gallery() below on sorting.
    :param fn:
    :return:
    """
    p = pathlib.Path(fn)
    stem = p.stem
    if "_" in stem:
        return stem[stem.index("_") + 1:].lower() + stem.lower()
    if " " in stem:
        return stem[stem.index(" ") + 1:].lower() + stem.lower()
    else:
        return stem


@app.route('/gh')
def gallery():
    """
    Render the gallery of images from the IMAGE_DIR. First we read the configuration file from the
    IMAGE_DIR (create it if doesn't exist). Then read all the files in the directory, extract the caption
    from the filename and the sort order.

    Filenames will be used as the captions for the pictures with the following twists:
        If the filename contains an underscore, then the underscore and everything after it is not displayed.
        If the filename contains an underscore, then the sort string for that image will start with whatever is
            after the underscore.
        If there is no underscore, then the sort string will be last name, first name where the names are presumed
            to be separated by the first space in the filename.
        All names are forced to lowercase for purposes of sorting.

        Examples:

            Joe Smith.JPG -> Displays "Joe Smith", sorts as "smithjoe"
            Joe Smith_Rodgers -> Displays as "Joe Smith", sorts as "rogersjoe smith"
    :return:
    """
    config_path = IMAGE_DIR.joinpath("config.json")
    if not config_path.exists():
        config = {
            "cellWidth": 240,
            "cellHeight": 240,
            "captionHeight": 20,
            "captionFont": "Arial, serif",
            "backgroundColor": "#3c3f41",
            "captionFontColor": "gainsboro",
            "refreshInterval": 60
        }
        with open(config_path, "w+") as fd:
            json.dump(config, fd, indent=4)

    with open(config_path, "r") as fd:
        config = json.load(fd)

    config['imageDir'] = IMAGE_DIR

    file_list = os.listdir(IMAGE_DIR)
    file_list = [{"title": get_title_from_file_name(fn),
                  "sort": get_sort_from_file_name(fn),
                  "file": fn} for fn in file_list if fn != "config.json"]
    file_list = sorted(file_list, key=lambda f: f["sort"])
    return render_template('gallery.html', file_list=file_list, config=config)
