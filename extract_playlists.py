# This is a simple Python script to extract each playlist in a PLIF file to a separate CSV file.
#
# Note: You'll need to install the package "pathvalidate" to run this project

import argparse
import json
import csv
from pathvalidate import sanitize_filename

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    plif_file = open(args.filename)
    json_data = json.load(plif_file)
    playlists = json_data["playlists"]

    for playlist in playlists:

        caption = playlist["caption"]
        description = playlist["description"]
        curator = playlist["curator"] or ""

        by = " by %s" % curator if curator else ""
        tail = ". %s" % description if description else ""

        filename = sanitize_filename(caption + ".csv")
        with open(filename, "w+") as p:

            # First write the title row:
            p.write("%s%s%s\n" % (caption, by, tail))

            # Now the csv data:
            writer = csv.writer(p)

            # Starting with a header row:
            writer.writerow(["name", "artist", "album", "isrc", "catalog_id"])

            # Data:
            for row in playlist["rows"]:
                name = row["name"]
                artist = row["artist"]
                album = row["album"]
                ids = row["identifiers"]
                isrc = ids.get("isrc", "")
                catalog_id = ids.get("apple_music_catalog_id", "")
                writer.writerow([name, artist, album, isrc, catalog_id])
            p.close()