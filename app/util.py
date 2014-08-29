import logging
import os
from shutil import rmtree, copy

log = logging.getLogger(__name__)

def init_cache(cache_path):
    log.info('init cache: initializing cache path: {0}'.format(cache_path))
    if os.path.exists(cache_path):
        log.info('init cache: cache path exists, removing.')
        rmtree(cache_path)
    log.info('init cache: creating cache path.')
    os.mkdir(cache_path)
    log.info('init cache: done initializing cache path')

def update_cache(cache_path, media_path):
    log.info('update cache: updating cache')
    existing_files = os.listdir(cache_path)
    media_files = os.listdir(media_path)
    new_files = list(set(media_files) - set(existing_files))
    log.info('update cache: new files found this update: {0}'.format(new_files))
    for new_file in new_files:
        log.info('update cache: copying new file: {0}'.format(new_file))
        try:
            copy(os.path.join(media_path, new_file), os.path.join(cache_path, new_file))
        except BaseException as ex:
            log.warn('update cache: dropping file {0} due to {1}'.format(new_file, ex))

def get_images_list(cache_path):
    images_list = []
    log.info('get images list: reading images in cache path: {0}'.format(cache_path))
    all_images_list = os.listdir(cache_path)
    for image in all_images_list:
        if image.startswith('.'):
            log.warn('get images list: dropping dot file {0}'.format(image))
            continue
        log.info('get images list: adding {0}'.format(image))
        images_list.append(image)
    return images_list