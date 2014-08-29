from flask import Blueprint, render_template, current_app
import os
import logging

from .util import init_cache, update_cache, get_images_list


dashboard = Blueprint('dashboard', __name__, url_prefix='/')
cache_dir = 'image_cache'
first_run = True
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


@dashboard.route('/')
def index():
    global first_run
    log.info('index called')
    images_list = []
    media_path = current_app.config.get('media_path')
    carousel_interval = current_app.config.get('carousel_interval')
    root_path = current_app.root_path
    cache_path = os.path.join(root_path, 'static', cache_dir)
    if first_run:
        log.info('first run')
        init_cache(cache_path)
        first_run = False
    update_cache(cache_path, media_path)
    images_list = get_images_list(cache_path)
    return render_template('index.html',
                           carousel_interval=carousel_interval,
                           images_list=images_list,
                           sep=os.path.sep,
                           cache_dir=cache_dir)



