#!/usr/bin/python3
from plugins import bestanime, trollvideo
from subprocess import call, Popen, PIPE, STDOUT

try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


def main():
    animeName = input("Type an anime name: ")
    animeName = bestanime.searchable_string(animeName)
    episodes = bestanime.get_episodes(bestanime.search_page(animeName))
    episodeUrls = bestanime.get_episode_url(bestanime.search_page(animeName))
    selector = 0
    for episode in episodes:
        print ("([{}] {})".format(selector, episode))
        selector = selector + 1
    """
    selector = 0
    for episode in episodeUrls:
        print ("([{}] {})".format(selector, episode))
        selector = selector + 1
    """
    episodeChoice = input("Choose an episode to view: ")
    print ("Viewing ", episodes[int(episodeChoice)])

    mirrors = bestanime.getMirrors(episodeUrls[int(episodeChoice)])
    print ("Available Mirrors")
    print (mirrors)

    host = bestanime.getHostingSite(mirrors[0])
    print (host)

    content = trollvideo.trollvideo(host)
    print (content)

    call(['vlc', content], stdout=DEVNULL, stderr=STDOUT)

    print ("Video has finished watch another?")


if __name__ == "__main__":
    main()
