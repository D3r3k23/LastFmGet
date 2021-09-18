import lastfmget

import json
from dataclasses import dataclass, field
from typing import Callable

USER = 'D3r3k523'

@dataclass
class DUMP:
    name: str
    meth: Callable
    args: dict = field(default_factory=dict)

def main():
    lastfmget.init('test/cfg/api_cfg_with_cache.yaml')
    dumps = [
        DUMP(name=meth.__name__, meth=meth) for meth in [
            lastfmget.user_info,
            lastfmget.user_now_playing,
            lastfmget.user_recent_tracks,
            lastfmget.user_top_artists,
            lastfmget.user_top_albums,
            lastfmget.user_top_tracks,
            lastfmget.user_weekly_chart_list,
            lastfmget.user_weekly_artist_chart,
            lastfmget.user_weekly_album_chart,
            lastfmget.user_weekly_track_chart
        ]
    ] + [
        DUMP(name='user_recent_tracks_large',
             meth=lastfmget.user_recent_tracks,
             args={'count': 500}
        ),
        DUMP(name='user_top_artists_large',
             meth=lastfmget.user_top_artists,
             args={'count': 1000}
        ),
        DUMP(name='user_top_artists_7day',
             meth=lastfmget.user_top_artists,
             args={'count': 20, 'period': '7day'}
        ),
        DUMP(name='user_top_artists_1month',
             meth=lastfmget.user_top_artists,
             args={'count': 50, 'period': '1month'}
        ),
        DUMP(name='user_top_artists_12month',
             meth=lastfmget.user_top_artists,
             args={'count': 100, 'period': '12month'}
        )
    ]
    for d in dumps:
        dump(d)

def dump(d):
    fn   = f'data/dump/{d.name}.json'
    data = d.meth(USER, **d.args)
    with open(fn, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
