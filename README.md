# extract_playlists
A simple Python script to extract playlist CSV files from a PLIF (PlayList Interchange Format) file

Syntax: `extract_playlists.py <filename.plif>`

Note: You'll need to install the package "pathvalidate" to run this project.

### Example:

To extract the 3 playlists in the 'example.plif' file to 3 seperate CSV files, type the following at a macOS command prompt:

`% python3 extract_playlists.py example.plif`

This 'example.plif' file was created by backing-up three Apple Music playlists using the Playlisty app. Playlisty uses PLIF format for all playlist backups.
