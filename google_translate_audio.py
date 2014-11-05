#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description='A Python script that use google translate to generate audio files from text')
parser.add_argument('-w', '--word', type=str, help='word or phrase')
parser.add_argument('-l', '--language', type=str, default='en-us', help='voice language, default: en-us')
parser.add_argument('-o', '--output', type=str, default='audio.mp3', help='output file, default: audio.mp3')
args = parser.parse_args()

if not args.word:
    parser.print_help()
    sys.exit(1)

def get_audio(phrase, filename=args.output, language=args.language):
    url = "http://translate.google.com/translate_tts"
    params = { 'q': phrase, 'tl': language }

    try:
        response = requests.get(url, params=params)
        if response.headers['content-type'] == 'audio/mpeg':
            with open(filename, 'wb') as f:
                for content in response.iter_content():
                    f.write(content)
            print "The file %s has been created" % filename
    except Exception, e:
        raise("Error: %s" % e)

get_audio(args.word)
