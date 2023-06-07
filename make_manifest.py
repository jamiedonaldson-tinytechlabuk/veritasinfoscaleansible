import json
import os

from ansible.galaxy.collection import _build_files_manifest
from ansible.galaxy.collection import _build_manifest
from ansible.galaxy.collection import _get_galaxy_yml
from ansible.module_utils._text import to_bytes


galaxy = _get_galaxy_yml('galaxy.yml')
b_here = to_bytes(os.path.abspath('.'))

with open('MANIFEST.json', 'w+') as f:
    json.dump(
        _build_manifest(**galaxy),
        f,
        indent=2,
        sort_keys=True,
    )

with open('FILES.json', 'w+') as f:
    json.dump(
        _build_files_manifest(
            b_here,
            galaxy['namespace'],
            galaxy['name'],
            #galaxy['build_ignore'],
        ),
        f,
        indent=2,
        sort_keys=True,
    )
