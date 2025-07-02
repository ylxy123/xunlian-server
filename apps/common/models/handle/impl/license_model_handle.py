from common.cache.file_cache import FileCache
from common.models.handle.base_handle import IBaseModelHandle
import os
from smartdoc.const import PROJECT_DIR


class LicenseModelHandle(IBaseModelHandle):
    def get_model_dict(self):
        cache_dir = os.path.join(PROJECT_DIR, 'data', 'cache', 'xpack_cache')
        cache = FileCache(cache_dir, {})
        return {'xpack_cache': cache}

