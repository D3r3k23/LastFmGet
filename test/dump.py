import lastfmget

import json

def main():
    lastfmget.init('cfg/api_cfg_with_cache.yaml')

    USER = 'D3r3k523'
    methods = [
        ( lastfmget.user_info,                USER ),
        ( lastfmget.user_now_playing,         USER ),
        ( lastfmget.user_recent_tracks,       USER ),
        ( lastfmget.user_top_artists,         USER ),
        ( lastfmget.user_top_albums,          USER ),
        ( lastfmget.user_top_tracks,          USER ),
        ( lastfmget.user_weekly_chart_list,   USER ),
        ( lastfmget.user_weekly_artist_chart, USER ),
        ( lastfmget.user_weekly_album_chart,  USER ),
        ( lastfmget.user_weekly_track_chart,  USER )
    ]

    for method, *args in methods:
        dump(method, *args)

def dump(method, *args):
    data = method(*args)

    with open(f'dump/{method.__name__}.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
